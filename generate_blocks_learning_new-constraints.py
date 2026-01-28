"""
Learning trial generation for TSRlearn experiment 
"""

import random
import json
import pandas as pd
from collections import deque, Counter
from typing import Dict, List, Tuple

from balanced_sequence_generation import (
    generate_all_sequences_A_balanced,
    generate_sequence_B_with_constraints,
    validate_sequences
)
# ============================================================================
# SETTINGS
# ============================================================================

# middle 10 are the concepts that always represent the middle 10 images from the sequence
# they are included in the localizer task
# buffer_pool includes remaining concepts that should be added as buffers (2 in the beginning, 2 at the end)

buffer_pool = [
  "bed",
  "bird",
  "car",
  "cat",
  "fish",
  "guitar",
  "key",
  "lamp",
  "phone",
  "train",
  "tree"
]

MIDDLE_10_FIXED = [
    "ball",
    "bicycle",
    "bread",
    "chair",
    "dog",
    "flower",
    "hammer",
    "hand",
    "house",
    "jacket",
]

SEED = 42 # randomize properly!!

N_EXEMPLARS_PER_CONCEPT = 40
MAX_SIM_ATTEMPTS = 1000000

n_participants = 20

# map keys to positions on the screen 
POSITION_KEYS = {"left": "left", "center": "center", "right": "right"}

SEQUENCE_RUNS = {"A": 12, "B": 6}  # used to compute position targets
stim_per_seq = 14

# constraints
MAX_SAME_POSITION_STREAK = 2
MIN_DISTANCE_DIS_CUR_FORWARD = 2   # Distractor comes after current
MIN_DISTANCE_DIS_CUR_BACKWARD = 3  # Distractor comes before current

YES_KEY = 'left'   # YES response on left
NO_KEY  = 'right'  # NO response on right

# Type3 (distance report) mapping for distances 0..4
DIST_KEY_MAP_0_TO_4 = {0: "1", 1: "2", 2: "3", 3: "4", 4: "5"}


# ============================================================================
# function to map trigger numbers to each concept name 
# ============================================================================

def _build_concept_to_trigger_map():
    """Create mapping of all concepts to trigger numbers."""
    mapping = {}
    
    # MIDDLE_10_FIXED: 1-10
    for idx, concept in enumerate(MIDDLE_10_FIXED):
        mapping[concept] = idx + 1
    
    # Buffer concepts: 11+
    for idx, concept in enumerate(buffer_pool):
        mapping[concept] = 11 + idx
    
    return mapping

CONCEPT_TO_TRIGGER = _build_concept_to_trigger_map()



def _add_learn_trig_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Add trigger number columns using the pre-built CONCEPT_TO_TRIGGER map."""
    df = df.copy()
    
    df["promptTrigNumber"]  = df["promptConcept"].apply(lambda c: CONCEPT_TO_TRIGGER.get(c, 0))
    df["correctTrigNumber"] = df["correctConcept"].apply(lambda c: CONCEPT_TO_TRIGGER.get(c, 0))
    df["dist01TrigNumber"]  = df["dist01Concept"].apply(lambda c: CONCEPT_TO_TRIGGER.get(c, 0))
    df["dist02TrigNumber"]  = df["dist02Concept"].apply(lambda c: CONCEPT_TO_TRIGGER.get(c, 0))
    
    return df


# ============================================================================
# functions to monitor position distribution, distractor distances etc. across
# all participants (just for monitoring, not as a constraint)
# ============================================================================

def initialize_global_counters():
    """Initialize global counters for monitoring distributions"""
    return {
        'position_assignments': Counter(),      # {('correct', 'left'): count, ...}
        'distractor_distances': Counter(),       # {distance: count}
        'distance_between_distractors': Counter() # {diff: count}
    }

def update_global_counters(counters, df_learning, seqA, seqB):
    
    """Update global counters from a participant's learning trials"""
    # Create sequence lookups
    seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
    seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}
    
    for _, row in df_learning.iterrows():
        
        # Position assignments
        counters['position_assignments'][('correct', row['correct_pos'])] += 1
        counters['position_assignments'][('dist01', row['dist01_pos'])] += 1
        counters['position_assignments'][('dist02', row['dist02_pos'])] += 1
        
        # Distractor distances and difference
        seq_name = row['learningSeq']
        seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup
        
        prompt_idx = seq_lookup[row['promptConcept']]
        dist01_idx = seq_lookup[row['dist01Concept']]
        dist02_idx = seq_lookup[row['dist02Concept']]
        
        dist01_dist = abs(dist01_idx - prompt_idx)
        dist02_dist = abs(dist02_idx - prompt_idx)
        
        counters['distractor_distances'][dist01_dist] += 1
        counters['distractor_distances'][dist02_dist] += 1
        
        # Track difference between distractors
        diff = dist02_dist - dist01_dist
        counters['distance_between_distractors'][diff] += 1
    
    return counters

def save_global_counters(filepath, counters):
    """Save global counters to JSON file"""
    # Convert tuple keys to strings for JSON
    position_str = {str(k): v for k, v in counters['position_assignments'].items()}
    
    with open(filepath, 'w') as f:
        json.dump({
            'position_assignments': position_str,
            'distractor_distances': dict(counters['distractor_distances']),
            'distance_between_distractors': dict(counters['distance_between_distractors'])
        }, f, indent=2)

def print_global_report(counters, n_participants):
    """Print final global distribution report"""
    print("GLOBAL MONITORING REPORT")
    
    print(f"\nParticipants monitored: {n_participants}")
    
    print("\nPosition Assignments (for monitoring):")
    for item_type in ['correct', 'dist01', 'dist02']:
        print(f"  {item_type}:")
        for pos in ['left', 'center', 'right']:
            count = counters['position_assignments'].get((item_type, pos), 0)
            print(f"    {pos:8s}: {count:6d}")
    
    print("\nDistractor Distances from current image (for monitoring):")
    for dist in sorted(counters['distractor_distances'].keys()):
        count = counters['distractor_distances'][dist]
        print(f"  Distance {dist:2d}: {count:6d}")
    
    print("\nDifference between dist02 and dist01 (for monitoring):")
    for diff in sorted(counters['distance_between_distractors'].keys()):
        count = counters['distance_between_distractors'][diff]
        print(f"  Difference {diff:2d}: {count:6d}")
    


# ============================================================================
# helper functions for learning trials generation 
# ============================================================================

def generate_exemplar_assignments_all_participants(
    n_participants: int,
    all_concepts: List[str],
    n_exemplars: int = N_EXEMPLARS_PER_CONCEPT,
    seed: int = SEED
) -> Dict[str, Dict[int, Tuple[int, int]]]:
    """
    Pre-assign exemplars to all participants for all concepts.
    Ensures each exemplar (1-40) is assigned to exactly one participant.
    """
    rng = random.Random(seed)
    concept_to_participant_pairs = {}
    
    for concept in all_concepts:
        exemplars = list(range(1, n_exemplars + 1))
        rng.shuffle(exemplars)
        
        pairs = {}
        for p in range(n_participants):
            exA = exemplars[p * 2]
            exB = exemplars[p * 2 + 1]
            pairs[p] = (exA, exB)
        
        concept_to_participant_pairs[concept] = pairs
    
    return concept_to_participant_pairs


def _pick_exemplars_for_AB_with_assignments(
    concepts_in_both: List[str],
    participant_idx: int,
    exemplar_assignments: Dict[str, Dict[int, Tuple[int, int]]]
) -> Tuple[Dict[str, int], Dict[str, int]]:
    """just return individual exemplars from tuples stored before"""
    exA, exB = {}, {}
    
    for c in concepts_in_both:
        if c in exemplar_assignments and participant_idx in exemplar_assignments[c]:
            a, b = exemplar_assignments[c][participant_idx]
            exA[c] = a
            exB[c] = b
        else:
            raise KeyError(
                f"Concept '{c}' or participant {participant_idx} not in exemplar assignments. "
                f"Make sure exemplar_assignments includes all possible concepts."
            )
    
    return exA, exB

def _concept_from_path(path: str) -> str:
    """Extract concept name from file path like 'stimuli/bird/bird_01.jpg'"""
    if not path:
        return ""
    parts = path.split("/")
    if len(parts) >= 2:
        return parts[-2]
    return ""

def _index_in_seq(seq: List[str], concept: str) -> int:
    return seq.index(concept)

def _middle_concepts_for_seq(seq: List[str]) -> set:
    """Get middle 10 concepts (positions 2-11 in 14-concept sequence)"""
    idxs = _middle10_indices_for_len14()
    return {seq[i] for i in idxs}

def _middle10_indices_for_len14():
    """Return middle 10 indices (exclude first 2 and last 2)"""
    return list(range(2, 12))  # 10 indices

def _trial_gap_from_concepts(seq: List[str], c1: str, c2: str) -> int:
    i, j = sorted([_index_in_seq(seq, c1), _index_in_seq(seq, c2)])
    return (j - i) - 1

def _distance(i, j):
    """Distance = (j - i) - 1 for sorted indices"""
    i, j = sorted([i, j])
    return (j - i) - 1

def _file(concept: str, exemplar_id: int) -> str:
    return f"stimuli/{concept}/{concept}_{exemplar_id:02d}.jpg"

def _exemplar_from_file(path: str):
    """Extract exemplar number from file path"""
    if not path:
        return ""
    base = path.split("/")[-1]
    num = base.split("_")[-1].split(".")[0]
    try:
        return int(num)
    except Exception:
        return ""


# ============================================================================
# functions for validating constraints
# ============================================================================

def print_participant_distance_distribution(df_learning: pd.DataFrame, seqA: List[str], seqB: List[str], ppt_id: str) -> None:
    """
    Print the distribution of distance differences for a participant.
    Shows how many times each distance difference (dist02 - dist01) occurs.
    """
    seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
    seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}
    
    distance_diffs = Counter()
    dist01_distances = Counter()
    dist02_distances = Counter()
    
    for _, row in df_learning.iterrows():
        seq_name = row['learningSeq']
        seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup
        
        prompt_idx = seq_lookup[row['promptConcept']]
        dist01_idx = seq_lookup[row['dist01Concept']]
        dist02_idx = seq_lookup[row['dist02Concept']]
        
        dist01_distance = abs(dist01_idx - prompt_idx)
        dist02_distance = abs(dist02_idx - prompt_idx)
        
        # Track difference
        diff = dist02_distance - dist01_distance
        distance_diffs[diff] += 1
        
        # Track individual distances
        dist01_distances[dist01_distance] += 1
        dist02_distances[dist02_distance] += 1
    
    print(f"\nDistance Distribution for Participant {ppt_id}")
    print(f"Total trials: {len(df_learning)}")
    
    print(" dist01 (near distractor) distances:")
    for dist in sorted(dist01_distances.keys()):
        count = dist01_distances[dist]
        pct = (count / len(df_learning)) * 100
        bar = "█" * (count // 6)
        print(f"Distance {dist:2d}: {count:3d} ({pct:5.1f}%) {bar}")
    
    print("dist02 (far distractor) distances:")
    for dist in sorted(dist02_distances.keys()):
        count = dist02_distances[dist]
        pct = (count / len(df_learning)) * 100
        bar = "█" * (count // 6)
        print(f"Distance {dist:2d}: {count:3d} ({pct:5.1f}%) {bar}")
    
    print("Difference between dist02 and dist01:")
    for diff in sorted(distance_diffs.keys()):
        count = distance_diffs[diff]
        pct = (count / len(df_learning)) * 100
        bar = "█" * (count // 6)
        print(f" Diff {diff:2d}: {count:3d} ({pct:5.1f}%) {bar}")


def validate_learning_distractor_distances(df_learning: pd.DataFrame, seqA: List[str], seqB: List[str], *, verbose=False) -> None:
    """
    Validates that for EVERY learning trial, dist01_distance < dist02_distance.
    
    """
    seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
    seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}
    
    violations = []
    
    for trial_idx, (_, row) in enumerate(df_learning.iterrows()):
        seq_name = row['learningSeq']
        seq = seqA if seq_name == 'A' else seqB
        seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup
        
        prompt_idx = seq_lookup[row['promptConcept']]
        dist01_idx = seq_lookup[row['dist01Concept']]
        dist02_idx = seq_lookup[row['dist02Concept']]
        
        dist01_distance = abs(dist01_idx - prompt_idx)
        dist02_distance = abs(dist02_idx - prompt_idx)
        
        # dist01 should always be closer (smaller distance) than dist02
        if dist01_distance >= dist02_distance:
            violations.append({
                'trial': trial_idx,
                'seq': seq_name,
                'prompt': row['promptConcept'],
                'dist01': row['dist01Concept'],
                'dist02': row['dist02Concept'],
                'dist01_distance': dist01_distance,
                'dist02_distance': dist02_distance,
            })
    
    if violations:
        print(f"Selection of distractors does not make sense")
        print(f"Found {len(violations)} trials where dist01_distance >= dist02_distance:")
        print(f"(This violates the constraint: dist01 should ALWAYS be closer than dist02)\n")
        
        for v in violations[:10]:  # Show first 10
            print(f"  Trial {v['trial']:3d} (Seq {v['seq']}): prompt={v['prompt']:10s}, "
                  f"dist01={v['dist01']:10s} ({v['dist01_distance']}) vs "
                  f"dist02={v['dist02']:10s} ({v['dist02_distance']})")
        
            print(f"  number of violations: {len(violations)}")
                
        raise AssertionError(
            f"Distractor distance constraint violated in {len(violations)} trials. "
            f"dist01_distance must always be < dist02_distance."
        )
    



def print_participant_distance_histogram(df_learning: pd.DataFrame, seqA: List[str], seqB: List[str], ppt_id: str) -> Dict[int, int]:
    """
    Print histogram of distractor distances for a participant.
    Shows counts for each distance value (0-12).
    
    Returns: Dict mapping distance -> count
    """
    seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
    seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}
    
    distance_counts = Counter()
    
    for _, row in df_learning.iterrows():
        seq_name = row['learningSeq']
        seq = seqA if seq_name == 'A' else seqB
        seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup
        
        prompt_idx = seq_lookup[row['promptConcept']]
        dist01_idx = seq_lookup[row['dist01Concept']]
        dist02_idx = seq_lookup[row['dist02Concept']]
        
        dist01_distance = abs(dist01_idx - prompt_idx)
        dist02_distance = abs(dist02_idx - prompt_idx)
        
        distance_counts[dist01_distance] += 1
        distance_counts[dist02_distance] += 1
    
    # Print histogram
    print(f"\n  Distance histogram for participant {ppt_id}:")
    print(f"  Distance: Count")
    for dist in sorted(distance_counts.keys()):
        count = distance_counts[dist]
        bar = "█" * (count // 5)  # Visual bar (each █ = 5 trials)
        print(f"       {dist:2d} : {count:3d}  {bar}")
    
    return dict(distance_counts)
    


# ============================================================================
# functions for selecting distractor stimuli on each trial 
# ============================================================================


def _select_two_distractors_balanced(
    seq: List[str],
    current_idx: int,
    rng: random.Random,
    exclude_indices: set = None,
    min_gap: int = 1,
    distance_difference_usage: Counter = None,
    debug: bool = False
) -> Tuple[int, int] | None:
    """
    Select two distractors (dist01, dist02) with independent probabilistic weighting such that:
    1. dist01 is closer to current than dist02 (dist01_distance < dist02_distance)
    2. dist02 - dist01 >= min_gap (depends on if they came before or after current in sequence)
       - Forward (after current): distance >= 2
       - Backward (before current): distance >= 3
    3. PROBABILISTIC WEIGHTING applied independently to both:
       - Forward distractors: uniform probability
       - Backward distractors: weighted by distance (further back = higher probability)
    4. BALANCES distance DIFFERENCES between dist01 and dist02 (prefer less-used differences)
    
    Logic:
    - Create weighted pool for dist01 (backward weighted by distance)
    - For each dist01 option, create weighted pool for dist02 with constraint dist02 > dist01
    - Apply same probabilistic weighting to dist02 (backward weighted by distance)
    - Select pair that best balances the difference
    
    Args:
        distance_difference_usage: Counter tracking (dist02_distance - dist01_distance) for balancing
                                   Goal: make all differences occur equally often
    
    Returns:
        (dist01_idx, dist02_idx) or None if selection fails
    """
    
    if exclude_indices is None:
        exclude_indices = set()
    if distance_difference_usage is None:
        distance_difference_usage = Counter()
    
    max_attempts = 10000 # could be increased
    
    for attempt in range(max_attempts):
        # Step 1: Get all valid candidates for each position
        all_candidates = []
        
        for j in range(len(seq)):
            if j in exclude_indices or j == current_idx:
                continue
            
            # Determine if forward or backward
            if j > current_idx:
                # Forward: distance >= 2
                dist = j - current_idx
                if dist >= MIN_DISTANCE_DIS_CUR_FORWARD:
                    all_candidates.append((j, dist, "forward"))
            else:
                # Backward: distance >= 3
                dist = current_idx - j
                if dist >= MIN_DISTANCE_DIS_CUR_BACKWARD:
                    all_candidates.append((j, dist, "backward"))
        
        if len(all_candidates) < 2:
            if debug and attempt == 0:
                print(f"    WARNING: Only {len(all_candidates)} candidates available at pos {current_idx}")
            return None
        
        # Step 2: Separate forward and backward for probabilistic weighting
        forward_candidates = [(j, d) for j, d, direction in all_candidates if direction == "forward"]
        backward_candidates = [(j, d) for j, d, direction in all_candidates if direction == "backward"]
        
        # Helper function to calculate custom weight
        def get_backward_weight(distance):
            """Custom weighting for backward candidates."""
            # could do more elaborate weights here?
            if distance == 3:
                return 0.3 # simple, just lower prob for distances of 3
            else:  # distance >= 3
                return 1.0
        
        # Step 3: Create weighted pools for DIST01 (with probabilistic selection)
        weighted_dist01 = []
        for j, d in forward_candidates:
            weighted_dist01.extend([(j, d, "forward")] * 1)
        for j, d in backward_candidates:
            weight = get_backward_weight(d)
            # Convert float weight to integer repetitions (multiply by 4 and round)
            weight_int = max(1, int(round(weight * 4)))
            weighted_dist01.extend([(j, d, "backward")] * weight_int)
        
        # Step 4: For each possible dist01, create weighted pool for DIST02
        # and find the best pair (dist01 < dist02, with difference balancing)
        best_pair = None
        best_score = float('inf')
        
        # Shuffle dist01 pool for randomness
        rng.shuffle(weighted_dist01)
        
        # Try different dist01 options
        for idx1_idx, (idx1, dist1, dir1) in enumerate(weighted_dist01):
            # Create weighted pool for dist02 with constraint: dist02_distance > dist01_distance
            weighted_dist02 = []
            
            for j, d in forward_candidates:
                if d > dist1:  # Constraint: dist02 > dist01
                    weighted_dist02.extend([(j, d, "forward")] * 1)
            
            for j, d in backward_candidates:
                if d > dist1:  # Constraint: dist02 > dist01
                    weight = get_backward_weight(d)
                    weight_int = max(1, int(round(weight * 4)))
                    weighted_dist02.extend([(j, d, "backward")] * weight_int)
            
            if not weighted_dist02:
                continue  # No valid dist02 for this dist01, try next dist01
            
            # Shuffle dist02 pool
            rng.shuffle(weighted_dist02)
            
            # Find best dist02 that balances the difference
            for idx2_idx, (idx2, dist2, dir2) in enumerate(weighted_dist02):
                if idx2 != idx1 and (dist2 - dist1) >= min_gap:
                    # Score by how often THIS DIFFERENCE has been used
                    diff = dist2 - dist1
                    usage_score = distance_difference_usage[diff]
                    if usage_score < best_score:
                        best_score = usage_score
                        best_pair = (idx1, idx2)
        
        if best_pair is not None:
            return best_pair
    
    
    return None


# ============================================================================
# functions to assign three choice options (correct, dist01, dist02 to positions on the screen)
# ============================================================================

def _sample_positions(
    rng: random.Random,
    last_pos: Dict[str, deque],
    pos_tally: Dict[str, Dict[str, int]],
    pos_targets: Dict[str, Dict[str, int]],
    prev_trial_images: Dict[str, Tuple[str, str]] | None = None,
    current_trial_images: Dict[str, str] | None = None,
) -> Tuple[str, str, str] | None:
    """
    Sample position assignments for (correct, dist01, dist02).
    
    Constraints:
    1. No more than MAX_SAME_POSITION_STREAK consecutive same position
    2. Don't exceed local position targets
    3. Image repetition constraint: If an image repeats from previous trial,
       it must appear in a DIFFERENT POSITION than it did before
    
    Inputs:
        prev_trial_images: Dict mapping role -> (image_path, prev_position)
                          e.g. {"correct": (path, "left"), "dist01": (path, "center"), ...}
        current_trial_images: Dict mapping role -> image_path (CURRENT trial)
                             e.g. {"correct": "stimuli/cat/cat_01.jpg", ...}
    """
    if prev_trial_images is None:
        prev_trial_images = {}
    if current_trial_images is None:
        current_trial_images = {}
    
    perms = [
        ("left", "center", "right"), ("left", "right", "center"),
        ("center", "left", "right"), ("center", "right", "left"),
        ("right", "left", "center"), ("right", "center", "left"),
    ]
    
    rng.shuffle(perms)
    
    for cpos, d1pos, d2pos in perms:
        
        
        ok = True
        
        # Check streak and target constraints
        for cond, pos in [("correct", cpos), ("dist01", d1pos), ("dist02", d2pos)]:
            # Check streak constraint
            streak = 0
            for p in reversed(last_pos[cond]):
                if p == pos:
                    streak += 1
                else:
                    break
            if streak + 1 > MAX_SAME_POSITION_STREAK:
                ok = False
                break
            
            # Check local target for having this stimulus type in this position
            if pos_tally[cond][pos] >= pos_targets[cond][pos] + 1:
                ok = False
                break
        
        if not ok:
            continue
        
        # If an image appeared ANYWHERE in the previous trial (any role),
        # it must be in a DIFFERENT POSITION in the current trial (any role)
        if current_trial_images and prev_trial_images:
            # Build a map of all images from previous trial and their positions
            image_to_prev_pos = {}
            for role, (prev_image, prev_pos) in prev_trial_images.items():
                if prev_image:
                    image_to_prev_pos[prev_image] = prev_pos
            
            # map for current trial positions
            roles_and_positions = {
                "correct": (cpos, current_trial_images.get("correct")),
                "dist01": (d1pos, current_trial_images.get("dist01")),
                "dist02": (d2pos, current_trial_images.get("dist02")),
            }
            
            image_repetition_ok = True
            for role, (curr_pos, curr_image) in roles_and_positions.items():
                if curr_image is None:
                    continue
                
                # If this image appeared in the previous trial (any role),
                # it must NOT be in the same position
                if curr_image in image_to_prev_pos:
                    prev_pos = image_to_prev_pos[curr_image]
                    if curr_pos == prev_pos:
                        image_repetition_ok = False
                        break
            
            if not image_repetition_ok:
                continue
        
        return cpos, d1pos, d2pos
    
    return None




# ============================================================================
# main function to build the learning trials
# ============================================================================

def build_trials_with_fixed_middle(
    seed: int = SEED,
    global_counters: dict | None = None,
    exemplar_assignments: Dict[str, Dict[int, Tuple[int, int]]] = None,
    participant_idx: int = 0,
    debug: bool = True,
    precomputed_sequences_A: List[Tuple[List[str], List[str]]] | None = None,
    middle_10_fixed: List[str] = None  # NEW: needed for Seq B generation
) -> Tuple[pd.DataFrame, List[str], List[str], Dict[str, int], Dict[str, int]]:
    """Build learning trials with fixed middle 10 concepts."""
    
    if middle_10_fixed is None:
        middle_10_fixed = MIDDLE_10_FIXED
    
    rng = random.Random(seed)
    
    # Use precomputed balanced sequence A (group-level balancing, so it already set for each ppt)
    if precomputed_sequences_A is not None and participant_idx < len(precomputed_sequences_A):
        seqA, buffers_A = precomputed_sequences_A[participant_idx]
    else:
        print(f" participant: {participant_idx}, eror generating balanced sequence A, check if ther eis an error with ppt id")
    
    # generate permuted sequence B 
    seqB = generate_sequence_B_with_constraints(
        seqA=seqA,
        buffers_A=buffers_A,
        middle_10_fixed=middle_10_fixed,
        rng=rng,
        max_tries=1000000,
        verbose=debug
    )
    
    # validate the two sequences
    is_valid = validate_sequences(seqA, seqB)
    print(f"VALID: {is_valid}")
    
    
    # Pick exemplars for all concepts in both sequences
    all_unique_concepts = list(set(seqA + seqB))
    
    if exemplar_assignments is not None:
        # Use pre-assigned exemplars
        exA, exB = _pick_exemplars_for_AB_with_assignments(
            all_unique_concepts,
            participant_idx=participant_idx,
            exemplar_assignments=exemplar_assignments
        )
    else:
        print("examplar assignment did not work, please check the exemplar names")
    
    # Position balancing targets
    total_trials = sum(SEQUENCE_RUNS.values()) * (stim_per_seq - 1)
    appearances_per_pos = total_trials // 3
    pos_targets = {
        "correct": {"left": appearances_per_pos, "center": appearances_per_pos, "right": total_trials - 2 * appearances_per_pos},
        "dist01":  {"left": appearances_per_pos, "center": appearances_per_pos, "right": total_trials - 2 * appearances_per_pos},
        "dist02":  {"left": appearances_per_pos, "center": appearances_per_pos, "right": total_trials - 2 * appearances_per_pos},
    }

    # Failure tracking
    failure_counts = {
        "distractor_selection": 0,
        "position_sampling": 0,
        "position_target_exceeded": 0,
        "position_streak": 0,
        "image_repetition_pos_change": 0,
        "other": 0
    }

    # Distance DIFFERENCE usage tracking (for balancing all diffs equally within participant)
    participant_distance_difference_usage = Counter()

    for attempt in range(1, MAX_SIM_ATTEMPTS + 1):
        rng_attempt = random.Random(seed + attempt)
        
        if attempt == 1:
            print("  Generating learning trials...")
        elif attempt % 10000 == 0:
            print(f" attempt {attempt}/{MAX_SIM_ATTEMPTS}")
        
        rows: list[dict] = []

        last_positions = {
            "correct": deque(maxlen=MAX_SAME_POSITION_STREAK),
            "dist01":  deque(maxlen=MAX_SAME_POSITION_STREAK),
            "dist02":  deque(maxlen=MAX_SAME_POSITION_STREAK),
        }
        pos_tally = {
            "correct": {"left": 0, "center": 0, "right": 0},
            "dist01":  {"left": 0, "center": 0, "right": 0},
            "dist02":  {"left": 0, "center": 0, "right": 0},
        }

        prev_trial_info = None  # Will store (correct_img, dist01_img, dist02_img, cpos, d1pos, d2pos)

        attempt_failed = False
        failure_reason = None
        failure_location = None

        def _add_one_route(
            seq_label: str,
            seq: List[str],
            ex_this: Dict[str, int],
            seq_other: List[str],
            ex_other: Dict[str, int],
            run_index: int,
            block_label: str
        ) -> bool:
            nonlocal rows, last_positions, pos_tally
            nonlocal prev_trial_info
            nonlocal attempt_failed, failure_reason, failure_location
            nonlocal participant_distance_difference_usage

            for i in range(len(seq) - 1):
                curr, nxt = seq[i], seq[i + 1]

                # Select two distractors with distance DIFFERENCE balancing
                try:
                    result = _select_two_distractors_balanced(
                        seq, i, rng_attempt,
                        exclude_indices={i, i+1},
                        min_gap=1,
                        distance_difference_usage=participant_distance_difference_usage  # ← Balance differences
                    )
                    if result is None:
                        dist01_idx, dist02_idx = None, None
                    else:
                        dist01_idx, dist02_idx = result
                except Exception as e:
                    if debug and attempt < 10:
                        print(f"  Exception in distractor selection at seq={seq_label}, i={i}: {e}")
                    failure_counts["distractor_selection"] += 1
                    attempt_failed = True
                    failure_reason = "distractor_selection_exception"
                    failure_location = f"seq={seq_label}, pos={i}"
                    return False


                if dist01_idx is None or dist02_idx is None:
                    if debug and attempt < 5:
                        print(f"  No valid distractors found at seq={seq_label}, pos={i} (curr={curr}, nxt={nxt})")
                    failure_counts["distractor_selection"] += 1
                    attempt_failed = True
                    failure_reason = "no_valid_distractors"
                    failure_location = f"seq={seq_label}, pos={i}"
                    return False
                
                dist01 = seq[dist01_idx]
                dist02 = seq[dist02_idx]
                
                # Update distance difference usage for balancing future selections
                dist01_distance = abs(dist01_idx - i)
                dist02_distance = abs(dist02_idx - i)
                distance_diff = dist02_distance - dist01_distance
                participant_distance_difference_usage[distance_diff] += 1

                # Build image file paths for CURRENT trial (needed for image repetition check)
                prompt_file = _file(curr, ex_this[curr])
                correct_file = _file(nxt, ex_this[nxt])
                dist01_file = _file(dist01, ex_this[dist01])
                dist02_file = _file(dist02, ex_this[dist02])
                
                current_trial_images = {
                    "correct": correct_file,
                    "dist01": dist01_file,
                    "dist02": dist02_file,
                }

                # Sample positions with image repetition constraint
                prev_images = None
                if prev_trial_info is not None:
                    prev_correct_img, prev_dist01_img, prev_dist02_img, prev_cpos, prev_d1pos, prev_d2pos = prev_trial_info
                    prev_images = {
                        "correct": (prev_correct_img, prev_cpos),
                        "dist01": (prev_dist01_img, prev_d1pos),
                        "dist02": (prev_dist02_img, prev_d2pos),
                    }

                pos = _sample_positions(
                    rng_attempt, last_positions, pos_tally, pos_targets,
                    prev_trial_images=prev_images,
                    current_trial_images=current_trial_images  
                )
                if pos is None:
                    if debug and attempt < 5:
                        print(f"  No valid position found at seq={seq_label}, pos={i} (curr={curr}, nxt={nxt})")
                        print(f"    Current tallies: correct={pos_tally['correct']}, dist01={pos_tally['dist01']}, dist02={pos_tally['dist02']}")
                    failure_counts["position_sampling"] += 1
                    attempt_failed = True
                    failure_reason = "position_sampling"
                    failure_location = f"seq={seq_label}, pos={i}"
                    return False
                cpos, d1pos, d2pos = pos


                last_positions["correct"].append(cpos)
                pos_tally["correct"][cpos] += 1
                last_positions["dist01"].append(d1pos)
                pos_tally["dist01"][d1pos] += 1
                last_positions["dist02"].append(d2pos)
                pos_tally["dist02"][d2pos] += 1


                rows.append({
                    "block": block_label,
                    "learningSeq": seq_label,
                    "runIndexWithinSeq": run_index,
                    "currPosInSeq": i + 1,

                    "promptFile":  prompt_file,
                    "correctFile": correct_file,
                    "dist_01File": dist01_file,
                    "dist_02File": dist02_file,

                    "promptConcept":  curr,
                    "correctConcept": nxt,
                    "dist01Concept":  dist01,
                    "dist02Concept":  dist02,

                    "correct_pos": cpos,
                    "dist01_pos":  d1pos,
                    "dist02_pos":  d2pos,
                    "correct_ans": POSITION_KEYS[cpos],
                    "pairTargetPosInSeq": i + 2,
                })
                
                # Store for next iteration
                prev_trial_info = (correct_file, dist01_file, dist02_file, cpos, d1pos, d2pos)
            
            return True

        def _add_routes_interleaved_B_then_A(seqA, exA, seqB, exB, reps_per_seq: int, block_label: str) -> bool:
            for r in range(1, reps_per_seq + 1):
                okB = _add_one_route("B", seqB, exB, seq_other=seqA, ex_other=exA, run_index=r, block_label=block_label)
                if not okB:
                    return False
                okA = _add_one_route("A", seqA, exA, seq_other=seqB, ex_other=exB, run_index=r, block_label=block_label)
                if not okA:
                    return False
            return True

        ok = True

        # Block A: 6 runs of A
        for r in range(1, 6 + 1):
            if not _add_one_route("A", seqA, exA, seq_other=seqB, ex_other=exB, run_index=r, block_label="A"):
                ok = False
                failure_reason = failure_reason or "block_A_route"
                break

        # Block B: interleave B and A, 6 runs each
        if ok:
            ok = _add_routes_interleaved_B_then_A(seqA, exA, seqB, exB, reps_per_seq=6, block_label="B")
            if not ok:
                failure_reason = failure_reason or "block_B_route"

        if ok:
            df = pd.DataFrame(rows)
            if attempt > 1:
                print(f"\n Success on attempt {attempt}")
            return df, seqA, seqB, exA, exB
        else:
            if debug and attempt <= 3:
                print(f"  Attempt {attempt} FAILED: {failure_reason} at {failure_location}")

    # Print summary
    print("TRIAL GENERATION FAILED")
    print(f"Failed after {MAX_SIM_ATTEMPTS} attempts.")
    print(f"\nFailure breakdown:")
    for reason, count in sorted(failure_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            pct = (count / sum(failure_counts.values())) * 100
            print(f"  {reason:35s}: {count:6d} ({pct:5.1f}%)")
    
    raise RuntimeError(
        f"Failed to satisfy constraints within {MAX_SIM_ATTEMPTS} attempts.\n"
        f"Most common failure: {max(failure_counts.items(), key=lambda x: x[1])}"
    )



# ============================================================================
# MAIN EXECUTION - GENERATE ALL 20 PARTICIPANTS
# ============================================================================

if __name__ == "__main__":
    import os
    
    out_dir = r"C:\sync_folder\TSRlearn-task\sequences_new"
    os.makedirs(out_dir, exist_ok=True)
    
    # Generate balanced Sequence A for ALL participants upfront
    sequences_A_balanced = generate_all_sequences_A_balanced(
    n_participants=n_participants,
    middle_concepts=MIDDLE_10_FIXED,
    buffer_pool=buffer_pool,
    seed=SEED,
    max_attempts_per_ppt=100000,
    verbose=True
    )

    # Generate exemplar assignments
    all_concepts_for_exemplars = buffer_pool + MIDDLE_10_FIXED
    
    exemplar_assignments = generate_exemplar_assignments_all_participants(
        n_participants=n_participants,
        all_concepts=all_concepts_for_exemplars,
        n_exemplars=N_EXEMPLARS_PER_CONCEPT,
        seed=SEED
    )

    # Initialize global monitoring counters
    global_counters = initialize_global_counters()
    
    successful_participants = []
    failed_participants = []
    all_participant_distances = {}  # Track distances for each participant
    
    # Generate for all 20 participants
    for ppt in range(n_participants):
        ppt_id = f"{ppt:02d}"
        seed_ppt = SEED + ppt
        
        print(f"Participant {ppt_id} ({ppt+1}/{n_participants})")
        
        try:
            # Generate learning trials
            df_learning, seqA, seqB, exA, exB = build_trials_with_fixed_middle(
                seed_ppt,
                global_counters=global_counters,
                exemplar_assignments=exemplar_assignments,
                participant_idx=ppt,
                debug=False,
                precomputed_sequences_A=sequences_A_balanced,
                middle_10_fixed=MIDDLE_10_FIXED  # NEW: pass this for Seq B generation
            )
            
            # Add trigger columns
            df_learning = _add_learn_trig_cols(df_learning)
            
            # Validate distractor distance constraint
            validate_learning_distractor_distances(df_learning, seqA, seqB, verbose=False)
            
            # Print per-participant distance distribution
            print_participant_distance_distribution(df_learning, seqA, seqB, ppt_id)
            
            # Save learning files
            learning_a_filename = f"learning_blockA_fixed-middle-10_{ppt_id}.xlsx"
            learning_a_path = os.path.join(out_dir, learning_a_filename)
            df_learning_a = df_learning[df_learning['block'] == 'A']
            df_learning_a.to_excel(learning_a_path, sheet_name='learning', index=False)
            print(f" Saved Block A: {len(df_learning_a)} trials")
            
            learning_b_filename = f"learning_blockB_fixed-middle-10_{ppt_id}.xlsx"
            learning_b_path = os.path.join(out_dir, learning_b_filename)
            df_learning_b = df_learning[df_learning['block'] == 'B']
            df_learning_b.to_excel(learning_b_path, sheet_name='learning', index=False)
            print(f" Saved Block B: {len(df_learning_b)} trials")
            
            # Update global counters
            global_counters = update_global_counters(global_counters, df_learning, seqA, seqB)
            
            successful_participants.append(ppt_id)
            
        except Exception as e:
            failed_participants.append((ppt_id, str(e)))
            print(f" FAILED: {e}")
    
    # Final report
    print(f"\nSuccessful: {len(successful_participants)}/{n_participants}")
    if successful_participants:
        print(f"  Participants: {', '.join(successful_participants)}")
    
    if failed_participants:
        print(f"\nFailed: {len(failed_participants)}/{n_participants}")
        for ppt_id, error in failed_participants:
            print(f"  {ppt_id}: {error[:60]}...")
    
    # Print global monitoring report
    print_global_report(global_counters, len(successful_participants))