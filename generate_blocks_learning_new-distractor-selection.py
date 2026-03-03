# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 17:50:47 2026

@author: Sianna.Groesser
"""

"""
Learning trial generation for TSRlearn experiment 
"""

import random
import json
import pandas as pd
from collections import deque, Counter
from typing import Dict, List, Tuple
import numpy as np

from distractor_selection_new import (
    select_two_distractors_ULTRA_BALANCE,
    prepare_distractor_selection_tracking,
    update_distractor_tracking,
    print_distractor_selection_report,
    validate_distractor_difficulties,
    reset_route_tracking,
    finalize_route_tracking
)

from balanced_sequence_generation import (
    generate_all_sequences_A_balanced,
    generate_sequence_B_with_constraints,
    construct_sequence_B_deterministic, 
    SEQB_COMBOS, 
    validate_sequences,
)
# ============================================================================
# SETTINGS
# ============================================================================

# middle 10 are the concepts that always represent the middle 10 images from the sequence
# they are included in the localizer task
# buffer_pool includes remaining concepts that should be added as buffers (2 in the beginning, 2 at the end)

buffer_pool = [
  "car",
  "fish",
  "guitar",
  "lamp",
  "key",
  "pencil",
  "phone",
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

SEED = 100 # randomize properly!!

N_EXEMPLARS_PER_CONCEPT = 40
MAX_SIM_ATTEMPTS = 10000000

n_participants = 20

# map keys to positions on the screen 
POSITION_KEYS = {"left": "left", "center": "center", "right": "right"}

SEQUENCE_RUNS = {"A": 20, "B": 10}  # used to compute position targets
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
        
        seq = seqA if row['learningSeq'] == 'A' else seqB
        seq_lookup = {c: i for i, c in enumerate(seq)}
        
        # combinations of positions as curr, dist0ß1 and dist02
        current_seqpos = seq_lookup[row['promptConcept']]
        dist01_seqpos  = seq_lookup[row['dist01Concept']]
        dist02_seqpos  = seq_lookup[row['dist02Concept']]
        
        key = (current_seqpos, dist01_seqpos, dist02_seqpos)
        group_distractor_tracking["pair_usage"][key] += 1
        
        # positions in the sequence used as distractor
        group_distractor_tracking["position_usage"][dist01_seqpos] += 1
        group_distractor_tracking["position_usage"][dist02_seqpos] += 1
        
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

def print_participant_difficulty_distribution(df_learning: pd.DataFrame, seqA: List[str], seqB: List[str], ppt_id: str) -> None:
    """
    Print the distribution of difficulty scores for a participant.
    Shows how many times each difficulty score occurs for dist01 and dist02.
    
    Difficulty scoring:
      Before distractors: score = -distance (negative = harder)
      After distractors: score = +distance (positive = easier)
    
    Constraint: dist01_difficulty > dist02_difficulty
    (dist01 should be harder, dist02 should be easier)
    """
    from distractor_selection_new import get_difficulty_score
    
    seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
    seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}
    
    difficulty_diffs = Counter()
    dist01_difficulties = Counter()
    dist02_difficulties = Counter()
    
    for _, row in df_learning.iterrows():
        seq_name = row['learningSeq']
        seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup
        
        prompt_idx = seq_lookup[row['promptConcept']]
        dist01_idx = seq_lookup[row['dist01Concept']]
        dist02_idx = seq_lookup[row['dist02Concept']]
        
        # Calculate distances
        dist01_distance = abs(dist01_idx - prompt_idx)
        dist02_distance = abs(dist02_idx - prompt_idx)
        
        # Determine direction (before or after current)
        dist01_is_before = dist01_idx < prompt_idx
        dist02_is_before = dist02_idx < prompt_idx
        
        # Calculate difficulty scores
        dist01_difficulty = get_difficulty_score(dist01_distance, dist01_is_before)
        dist02_difficulty = get_difficulty_score(dist02_distance, dist02_is_before)
        
        # Track difference
        diff = dist02_difficulty - dist01_difficulty
        difficulty_diffs[diff] += 1
        
        # Track individual difficulties
        dist01_difficulties[dist01_difficulty] += 1
        dist02_difficulties[dist02_difficulty] += 1
    
    print(f"Difficulty Distribution for Participant {ppt_id}")
    print(f"Total trials: {len(df_learning)}")
    
    print(f"\ndist01 (HARDER distractor) difficulties:")
    print(f"(Lower/more negative = harder to discriminate)")
    for diff in sorted(dist01_difficulties.keys()):
        count = dist01_difficulties[diff]
        pct = (count / len(df_learning)) * 100
        bar = "█" * max(1, count // 3)
        print(f"  Difficulty {diff:+3.0f}: {count:3d} ({pct:5.1f}%) {bar}")
    
    print(f"\ndist02 (EASIER distractor) difficulties:")
    print(f"(Higher/more positive = easier to discriminate)")
    for diff in sorted(dist02_difficulties.keys()):
        count = dist02_difficulties[diff]
        pct = (count / len(df_learning)) * 100
        bar = "█" * max(1, count // 3)
        print(f"  Difficulty {diff:+3.0f}: {count:3d} ({pct:5.1f}%) {bar}")
    
    print(f"\nDifficulty difference (dist02 - dist01):")
    print(f"(Should be ALL positive if constraint satisfied)")
    for diff in sorted(difficulty_diffs.keys()):
        count = difficulty_diffs[diff]
        pct = (count / len(df_learning)) * 100
        status = "✓" if diff > 0 else "✗"
        bar = "█" * max(1, count // 3)
        print(f"  Diff {diff:+3.0f}: {count:3d} ({pct:5.1f}%) {status} {bar}")
    
    # Convert to arrays for statistics
    dist01_scores = np.array([d for diffs in [[k]*v for k, v in dist01_difficulties.items()] for d in diffs])
    dist02_scores = np.array([d for diffs in [[k]*v for k, v in dist02_difficulties.items()] for d in diffs])
    all_diffs = np.array([d for diffs in [[k]*v for k, v in difficulty_diffs.items()] for d in diffs])
    
    # Summary statistics
    print(f"Summary Statistics")
    print(f"dist01 (harder):")
    print(f"  Mean:     {np.mean(dist01_scores):+7.2f}")
    print(f"  Std dev:  {np.std(dist01_scores):7.2f}")
    print(f"  Min:      {np.min(dist01_scores):+7.2f}")
    print(f"  Max:      {np.max(dist01_scores):+7.2f}")
    
    print(f"\ndist02 (easier):")
    print(f"  Mean:     {np.mean(dist02_scores):+7.2f}")
    print(f"  Std dev:  {np.std(dist02_scores):7.2f}")
    print(f"  Min:      {np.min(dist02_scores):+7.2f}")
    print(f"  Max:      {np.max(dist02_scores):+7.2f}")
    
    print(f"\nDifference (dist02 - dist01):")
    print(f"  Mean:     {np.mean(all_diffs):+7.2f}")
    print(f"  Std dev:  {np.std(all_diffs):7.2f}")
    print(f"  Min:      {np.min(all_diffs):+7.2f}")
    print(f"  Max:      {np.max(all_diffs):+7.2f}")
    
    # Constraint check
    violations = sum(1 for d in all_diffs if d >= 0)
    valid = len(all_diffs) - violations
    print(f"\nConstraint check (dist01_difficulty < dist02_difficulty):")
    print(f"  Valid:      {valid:3d} ({valid/len(all_diffs)*100:5.1f}%)")
    print(f"  Violations: {violations:3d} ({violations/len(all_diffs)*100:5.1f}%)")
    if violations == 0:
        print(f"  ✓ PASS: All trials satisfy constraint")
    else:
        print(f"  ✗ FAIL: {violations} trials violate constraint")
    print(f"{'='*70}")



def reconstruct_sequences(df):
    """
    Reconstruct the sequences from the file by analyzing the prompt-correct pairs.
    Since each trial's correct becomes the next trial's prompt, we can build the sequence.
    Also include all distractor concepts to get the complete picture.
    """
    seqA_order = []
    seqB_order = []
    seqA_all = set()
    seqB_all = set()
    
    # First pass: get prompt-correct pairs to establish order
    df_A = df[df['learningSeq'] == 'A'].reset_index(drop=True)
    df_B = df[df['learningSeq'] == 'B'].reset_index(drop=True)
    
    # For Seq A: build order from prompt-correct pairs
    if len(df_A) > 0:
        for i, (_, row) in enumerate(df_A.iterrows()):
            prompt = row['promptConcept']
            correct = row['correctConcept']
            dist01 = row['dist01Concept']
            dist02 = row['dist02Concept']
            
            seqA_all.add(prompt)
            seqA_all.add(correct)
            seqA_all.add(dist01)
            seqA_all.add(dist02)
            
            if i == 0:
                seqA_order.append(prompt)
            if correct not in seqA_order:
                seqA_order.append(correct)
    
    # For Seq B: build order from prompt-correct pairs
    if len(df_B) > 0:
        for i, (_, row) in enumerate(df_B.iterrows()):
            prompt = row['promptConcept']
            correct = row['correctConcept']
            dist01 = row['dist01Concept']
            dist02 = row['dist02Concept']
            
            seqB_all.add(prompt)
            seqB_all.add(correct)
            seqB_all.add(dist01)
            seqB_all.add(dist02)
            
            if i == 0:
                seqB_order.append(prompt)
            if correct not in seqB_order:
                seqB_order.append(correct)
    else:
        seqB_all = seqA_all
        seqB_order = seqA_order
    
    # If we still have missing concepts (distractors that aren't in sequence order),
    # add them at the end (they might be buffers)
    for concept in sorted(seqA_all):
        if concept not in seqA_order:
            seqA_order.append(concept)
    
    for concept in sorted(seqB_all):
        if concept not in seqB_order:
            seqB_order.append(concept)
    
    return seqA_order, seqB_order

def validate_all_participants(out_dir, n_participants):
    """
    Load and validate distractor selections across all participants.
    
    Reads directly from learning trial files instead of relying on 
    separate report JSON files (which may not exist).
    """
    import json
    import numpy as np
    import pandas as pd
    from distractor_selection_new import get_difficulty_score
    
    all_difficulties = []
    all_direction_usage = {"before": 0, "after": 0}
    all_violations = []
    
    for ppt in range(n_participants):
        ppt_id = f"{ppt:02d}"
        
        # Try both blockA and blockB files
        for block in ['A', 'B']:
            learning_file = os.path.join(out_dir, f"learning_block{block}_fixed-middle-10_{ppt_id}.xlsx")
            
            if not os.path.exists(learning_file):
                print(f"⚠ File not found: {learning_file}")
                continue
            
            try:
                df_learning = pd.read_excel(learning_file, sheet_name='learning')
                
                # Reconstruct sequences from the file
                seqA, seqB = reconstruct_sequences(df_learning)
                seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
                seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}
                
                # Extract difficulty information from trials
                for trial_idx, (_, row) in enumerate(df_learning.iterrows()):
                    seq_name = row['learningSeq']
                    seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup
                    
                    prompt_idx = seq_lookup[row['promptConcept']]
                    dist01_idx = seq_lookup[row['dist01Concept']]
                    dist02_idx = seq_lookup[row['dist02Concept']]
                    
                    # Calculate distances
                    dist01_distance = abs(dist01_idx - prompt_idx)
                    dist02_distance = abs(dist02_idx - prompt_idx)
                    
                    # Determine direction
                    dist01_is_before = dist01_idx < prompt_idx
                    dist02_is_before = dist02_idx < prompt_idx
                    
                    # Calculate difficulty scores
                    dist01_difficulty = get_difficulty_score(dist01_distance, dist01_is_before)
                    dist02_difficulty = get_difficulty_score(dist02_distance, dist02_is_before)
                    
                    # Track for group-level statistics
                    all_difficulties.append(dist01_difficulty)
                    all_difficulties.append(dist02_difficulty)
                    
                    # Track direction usage
                    all_direction_usage["before"] += 1 if dist01_is_before else 0
                    all_direction_usage["after"] += 1 if not dist01_is_before else 0
                    all_direction_usage["before"] += 1 if dist02_is_before else 0
                    all_direction_usage["after"] += 1 if not dist02_is_before else 0
                    
                    # Check constraint
                    if dist01_difficulty <= dist02_difficulty:
                        all_violations.append({
                            'participant': ppt_id,
                            'block': block,
                            'trial': trial_idx,
                            'dist01_difficulty': dist01_difficulty,
                            'dist02_difficulty': dist02_difficulty,
                        })
                
                print(f"✓ Loaded Participant {ppt_id} Block {block}: "
                      f"{len(df_learning)} trials, {len(seqA)} concepts")
                
            except Exception as e:
                print(f"✗ Error loading {learning_file}: {e}")
                continue
    
    # Print group-level report
    print("\n" + "="*70)
    print("GROUP-LEVEL VALIDATION")
    print("="*70)
    
    if not all_difficulties:
        print("⚠ No difficulties calculated - check file paths")
        return
    
    print(f"\nDifficulty Distribution (across all participants):")
    print(f"  Total distractors sampled: {len(all_difficulties)}")
    print(f"  Mean:   {np.mean(all_difficulties):7.2f} (target: 0.00)")
    print(f"  Std:    {np.std(all_difficulties):7.2f}")
    print(f"  Min:    {np.min(all_difficulties):7.2f}")
    print(f"  Max:    {np.max(all_difficulties):7.2f}")
    
    # Histogram
    print(f"\n  Distribution by difficulty bins:")
    bins = [-10, -5, -3, -1, 0, 1, 3, 5, 10]
    for i in range(len(bins) - 1):
        count = sum(1 for d in all_difficulties if bins[i] <= d < bins[i+1])
        pct = (count / len(all_difficulties) * 100) if all_difficulties else 0
        bar = "█" * (count // 20) if count > 0 else ""
        print(f"    [{bins[i]:3d}, {bins[i+1]:3d}): {count:4d} ({pct:5.1f}%) {bar}")
    
    total_dir = all_direction_usage["before"] + all_direction_usage["after"]
    before_pct = (all_direction_usage["before"] / total_dir * 100) if total_dir > 0 else 0
    after_pct = (all_direction_usage["after"] / total_dir * 100) if total_dir > 0 else 0
    
    print(f"\nDirection usage (all participants combined):")
    print(f"  Before (harder): {all_direction_usage['before']:4d} ({before_pct:5.1f}%)")
    print(f"  After (easier):  {all_direction_usage['after']:4d} ({after_pct:5.1f}%)")
    
    # Quality checks
    print(f"\nQuality Checks:")
    
    if 0.4 < abs(np.mean(all_difficulties)) < 0.6:
        print(f"  ✓ Difficulty mean is well-centered (±0.5 of target)")
    else:
        dev = np.mean(all_difficulties)
        print(f"  ⚠ Difficulty mean is {dev:+.2f} away from target (0.0)")
        if dev > 0.6:
            print(f"    → Overall too easy (shift toward harder distractors)")
        else:
            print(f"    → Overall too hard (shift toward easier distractors)")
    
    if np.std(all_difficulties) < 0.3:
        print(f"  ✓ Difficulty std dev is reasonable ({np.std(all_difficulties):.2f})")
    else:
        print(f"  ⚠ Difficulty std dev is high ({np.std(all_difficulties):.2f})")
        print(f"    → Consider more consistent difficulty selection")
    
    if all_violations:
        print(f"\n  ✗ Found {len(all_violations)} constraint violations:")
        print(f"    (dist01_difficulty <= dist02_difficulty)")
        print(f"\n    First 5 violations:")
        for v in all_violations[:5]:
            print(f"      Ppt {v['participant']} Block {v['block']} Trial {v['trial']:2d}: "
                  f"{v['dist01_difficulty']:+5.1f} <= {v['dist02_difficulty']:+5.1f}")
        if len(all_violations) > 5:
            print(f"      ... and {len(all_violations) - 5} more")
        print(f"\n    ✗ FAILED - Fix distractor selection")
    else:
        print(f"  ✓ All distractors satisfy dist01 < dist02 constraint")
    
    # Summary
    print("\n" + "="*70)
    if all_violations == 0 and abs(np.mean(all_difficulties)) < 1.0:
        print("✓ GROUP-LEVEL VALIDATION PASSED")
    else:
        print("⚠ GROUP-LEVEL VALIDATION HAS ISSUES - REVIEW ABOVE")
    print("="*70)

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
    print("  Distance: Count")
    for dist in sorted(distance_counts.keys()):
        count = distance_counts[dist]
        bar = "█" * (count // 5)  # Visual bar (each █ = 5 trials)
        print(f"       {dist:2d} : {count:3d}  {bar}")
    
    return dict(distance_counts)
    



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
    middle_10_fixed: List[str] = None,
    exclude_patterns = None,
    group_distractor_tracking=None,
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
    # seqB = generate_sequence_B_with_constraints(
    #     seqA=seqA,
    #     buffers_A=buffers_A,
    #     middle_10_fixed=middle_10_fixed,
    #     rng=rng,
    #     max_tries=MAX_SIM_ATTEMPTS,
    #     exclude_patterns=exclude_patterns,
    #     verbose=debug
    # )
    combo_id = participant_idx % len(SEQB_COMBOS)
    seqB = construct_sequence_B_deterministic(
        seqA=seqA, buffers_A=buffers_A, combo_id=combo_id, verbose=debug
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

    for attempt in range(1, 100000 + 1):
        rng_attempt = random.Random(seed + attempt)
        
        distractor_tracking = prepare_distractor_selection_tracking(
           n_trials_expected=(stim_per_seq - 1) * sum(SEQUENCE_RUNS.values()),
           seq_length=14
       )
        
        if attempt == 1:
            print("  Generating learning trials...")
        elif attempt % 100 == 0:
            print(f" attempt {attempt}/100000")
        
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
            
            # Track which sequence positions used as distractors in this route
            distractor_coverage = set()
            
            reset_route_tracking(distractor_tracking)

            # Track recent distractor concepts to prevent streaks            
            prev_dist01_idx = None
            prev_dist02_idx = None
            prev_difficulty_pair = None
            
            for i in range(len(seq) - 1):
                curr, nxt = seq[i], seq[i + 1]

                # Select two distractors with distance DIFFERENCE balancing
                try:
                    result = select_two_distractors_ULTRA_BALANCE(
                    seq=seq,
                    current_idx=i,
                    rng=rng_attempt,
                    exclude_indices={i, i + 1},
                    # Global tracking (still needed for position/distance balance across routes)
                    direction_usage=distractor_tracking["direction_usage"],
                    distance_diff_usage=distractor_tracking["distance_diff_usage"],
                    position_as_dist01_usage=distractor_tracking["position_as_dist01_usage"],
                    position_as_dist02_usage=distractor_tracking["position_as_dist02_usage"],
                    position_targets=distractor_tracking["position_targets"],
                    # Hard constraints
                    min_difficulty_difference=0.2,
                    # Coverage
                    distractor_coverage=distractor_coverage,
                    coverage_weight=1,
                    # Distance tracking
                    dist01_distance_usage=distractor_tracking["dist01_distance_usage"],
                    dist02_distance_usage=distractor_tracking["dist02_distance_usage"],
                    # Streak prevention
                    prev_dist01_idx=prev_dist01_idx,
                    prev_dist02_idx=prev_dist02_idx,
                    prev_difficulty_pair=prev_difficulty_pair,
                    # Per-route difficulty (mean + SD + difference — all per route)
                    route_dist01_difficulties=distractor_tracking["current_route_dist01_difficulties"],
                    route_dist02_difficulties=distractor_tracking["current_route_dist02_difficulties"],
                    route_difficulty_diffs=distractor_tracking["current_route_difficulty_diffs"],
                    target_route_dist01_mean=0.6,
                    target_route_dist02_mean=0.3,
                    route_difficulty_tolerance=0.19,
                    target_route_dist01_std=0.2,
                    target_route_dist02_std=0.2,
                    route_std_tolerance=0.15,
                    target_difficulty_diff_mean=0.3,
                    # Position-relative direction balance
                    tracking=distractor_tracking,
                    group_tracking=group_distractor_tracking, 
                    debug=True,
                )
                
                    if result is None:
                        dist01_idx, dist02_idx = None, None
                        selection_info = None
                    else:
                        (dist01_idx, dist02_idx), selection_info = result
                        update_distractor_tracking(distractor_tracking, selection_info)
                        # Update previous trial tracking for streak constraints
                        prev_dist01_idx = dist01_idx
                        prev_dist02_idx = dist02_idx
                        prev_difficulty_pair = (selection_info["dist01_difficulty"], 
                                                selection_info["dist02_difficulty"])
                        
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
                

                # track used distractors to ensure coverage within the route
                distractor_coverage.add(dist01_idx)
                distractor_coverage.add(dist02_idx)

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
                    "dist01_diff": selection_info["dist01_difficulty"],
                    "dist02_diff": selection_info["dist02_difficulty"],
                    "correct_ans": POSITION_KEYS[cpos],
                    "pairTargetPosInSeq": i + 2,
                })
                
                
                # Store for next iteration
                prev_trial_info = (correct_file, dist01_file, dist02_file, cpos, d1pos, d2pos)
                
            # Check all sequence positions used as distractors at least once
            if len(distractor_coverage) < len(seq):
                missing = set(range(len(seq))) - distractor_coverage
                print(f"  Coverage FAILED: missing positions {missing}")
                return False

            finalize_route_tracking(distractor_tracking)
            return True

        def _add_routes_interleaved_B_then_A(seqA, exA, seqB, exB, reps_per_seq: int, block_label: str) -> Tuple[pd.DataFrame, List[str], List[str], Dict[str, int], Dict[str, int]]:
            for r in range(1, reps_per_seq + 1):
                okB = _add_one_route("B", seqB, exB, seq_other=seqA, ex_other=exA, run_index=r, block_label=block_label)
                if not okB:
                    return False
                okA = _add_one_route("A", seqA, exA, seq_other=seqB, ex_other=exB, run_index=r, block_label=block_label)
                if not okA:
                    return False
            return True

        ok = True

        # Block A: 10 runs of A
        for r in range(1, 10 + 1):
            if not _add_one_route("A", seqA, exA, seq_other=seqB, ex_other=exB, run_index=r, block_label="A"):
                ok = False
                failure_reason = failure_reason or "block_A_route"
                break

        # Block B: interleave B and A, 10 runs each
        if ok:
            ok = _add_routes_interleaved_B_then_A(seqA, exA, seqB, exB, reps_per_seq=10, block_label="B")
            if not ok:
                failure_reason = failure_reason or "block_B_route"

        if ok:
            df = pd.DataFrame(rows)
            if attempt > 1:
                print(f"\n Success on attempt {attempt}")
            return df, seqA, seqB, exA, exB, distractor_tracking  
        else:
            if debug and attempt <= 3:
                print(f"  Attempt {attempt} FAILED: {failure_reason} at {failure_location}")

    # Print summary
    print("TRIAL GENERATION FAILED")
    print(f"Failed after 100000 attempts.")
    print(f"\nFailure breakdown:")
    for reason, count in sorted(failure_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            pct = (count / sum(failure_counts.values())) * 100
            print(f"  {reason:35s}: {count:6d} ({pct:5.1f}%)")
    
    raise RuntimeError(
        f"Failed to satisfy constraints within 100000 attempts.\n"
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
    max_attempts_per_ppt=MAX_SIM_ATTEMPTS,
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
    used_patterns = []
    
    # track group level parameters for group level balancing
    group_distractor_tracking = {
    "pair_usage": Counter(),        # (dist01_seqpos, dist02_seqpos, current_seqpos) → count
    "position_usage": Counter(),    # no single sequence position is overused as a distractor across subjects
    }

    # Generate for all 20 participants
    for ppt in range(n_participants):
        
        ppt_id = f"{ppt:02d}"
        
        seed_ppt = SEED* 1000  + ppt
        print(f"Participant {ppt_id} ({ppt+1}/{n_participants})")
        
        try:
            # Generate learning trials
            df_learning, seqA, seqB, exA, exB, distractor_tracking = build_trials_with_fixed_middle( 
                seed_ppt,
                global_counters=global_counters,
                exemplar_assignments=exemplar_assignments,
                participant_idx=ppt,
                debug=False,
                precomputed_sequences_A=sequences_A_balanced,
                middle_10_fixed=MIDDLE_10_FIXED,
                exclude_patterns=used_patterns,
                group_distractor_tracking=group_distractor_tracking
            )
            
            # Add trigger columns
            df_learning = _add_learn_trig_cols(df_learning)
            
            # Validate distractor distance constraint
            validate_distractor_difficulties(df_learning, seqA, seqB, verbose=False)
            
            # Print per-participant distance distribution
            print_participant_difficulty_distribution(df_learning, seqA, seqB, ppt_id)
            print_distractor_selection_report(distractor_tracking, ppt_id)

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
            
            # update seq B tracking so each potential seq B is only used once
            middle_A = [seqA[i] for i in range(2, 12)]
            middle_B = seqB[2:12]
            middle_A_pos = {c: i for i, c in enumerate(middle_A)}
            pattern = tuple(middle_A_pos[c] for c in middle_B)
            used_patterns.append(pattern)
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
    
    
    validate_all_participants(out_dir, n_participants)