"""
retrieval trial generation for TSRlearn experiment 
"""

import os
import sys
import pandas as pd
import random
from collections import deque, Counter
from typing import Dict, List, Tuple, Optional, Set
import numpy as np

# ============================================================================
# SETTINGS
# ============================================================================

LEARNING_DIR = r"C:\sync_folder\TSRlearn-task\sequences_new"
OUTPUT_DIR = r"C:\sync_folder\TSRlearn-task\sequences_new"
PARTICIPANT_IDS = None # if none, it reads all learning files from the folder

SEED = 42 # change!!
MAX_SIM_ATTEMPTS = 500000

MIDDLE_10_FIXED = [
    "ball", "bicycle", "bread", "chair", "dog",
    "flower", "hammer", "hand", "house", "jacket",
]

buffer_pool = [
    "bed", "bird", "boat", "book", "broom", "candle", "car", "cat", "door", "fish",
    "fork", "glasses", "guitar", "horse", "key", "lamp", "pencil", "phone", "plane",
    "shoe", "train", "tree"
]

DIST_KEY_MAP_0_TO_4 = {0: "1", 1: "2", 2: "3", 3: "4", 4: "5"}
YES_KEY = 'left'
NO_KEY = 'right'


# ============================================================================
# function to map trigger numbers to each concept name 
# ============================================================================

def _build_concept_to_trigger_map():
    """Create mapping of all concepts to trigger numbers."""
    mapping = {}
    
    # MIDDLE_10_FIXED: 1-10
    for idx, concept in enumerate(MIDDLE_10_FIXED):
        mapping[concept] = idx + 1
    
    return mapping

CONCEPT_TO_TRIGGER = _build_concept_to_trigger_map()


def _add_retr_trig_cols(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["img_firstTrigNumber"]  = df["img_first"].apply(lambda p: CONCEPT_TO_TRIGGER.get(_concept_from_path(p), 0) if p else 0)
    df["img_secondTrigNumber"] = df["img_second"].apply(lambda p: CONCEPT_TO_TRIGGER.get(_concept_from_path(p), 0) if p else 0)
    df["img_thirdTrigNumber"]  = df["img_third"].apply(lambda p: CONCEPT_TO_TRIGGER.get(_concept_from_path(p), 0) if p else 0)
    return df

# ============================================================================
# the generation fails a lot, so this helps us see which constraint caused it 
# ============================================================================

class ConstraintLog:
    def __init__(self, miniblock_idx, seq_label, block_label):
        self.miniblock_idx = miniblock_idx
        self.seq_label = seq_label
        self.block_label = block_label
        self.notes = []
    
    def add_note(self, note: str):
        self.notes.append(note)
    
    def print_report(self):
        if not self.notes:
            return
        print(f"\n    [MB {self.miniblock_idx} {self.seq_label}] Notes:")
        for note in self.notes:
            print(f"      • {note}")

# ============================================================================
# helper functions for getting image files and distance between images
# ============================================================================

def _file(concept: str, exemplar_id: int) -> str:
    return f"stimuli/{concept}/{concept}_{exemplar_id:02d}.jpg"

def _concept_from_path(path: str) -> str:
    if not path:
        return ""
    parts = path.split("/")
    if len(parts) >= 2:
        return parts[-2]
    return ""

def _distance(i, j):
    i, j = sorted([i, j])
    return (j - i) - 1

# ============================================================================
# Step 1: extract the sequences used during learning 
# ============================================================================

def extract_sequences_from_learning(learning_file: str) -> Dict[str, List[str]]:
    try:
        df = pd.read_excel(learning_file)
    except Exception as e:
        print(f"  ERROR reading {learning_file}: {e}")
        raise
    
    required_cols = ['learningSeq', 'currPosInSeq', 'promptConcept', 'correctConcept']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    sequences = {}
    
    for seq_label in df['learningSeq'].unique():
        seq_df = df[df['learningSeq'] == seq_label].copy()
        seq_df = seq_df.sort_values('currPosInSeq').reset_index(drop=True)
        
        sequence = []
        for i, row in seq_df.iterrows():
            concept = row['promptConcept']
            if concept not in sequence:
                sequence.append(concept)
        
        # the last image in the sequence is never the prompt images, so get it
        # from the correctConcept column
        if len(seq_df) > 0:
            last_correct = seq_df.iloc[-1]['correctConcept']
            if last_correct not in sequence:
                sequence.append(last_correct)
        
        sequences[seq_label] = sequence
    
    return sequences

def extract_exemplars_from_learning(learning_file: str) -> Dict[str, Dict[str, int]]:
    """extract concept exemplars used on learning trials so we can reuse"""
    
    try:
        df = pd.read_excel(learning_file)
    except Exception as e:
        print(f"  ERROR reading {learning_file}: {e}")
        raise
    
    required_cols = ['learningSeq', 'promptConcept', 'promptFile', 'correctConcept', 'correctFile']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    exemplars = {}
    
    for seq_label in df['learningSeq'].unique():
        seq_df = df[df['learningSeq'] == seq_label]
        ex = {}
        
        for _, row in seq_df.iterrows():
            prompt_concept = row['promptConcept']
            prompt_file = row['promptFile']
            
            if prompt_concept not in ex and prompt_file and pd.notna(prompt_file):
                try:
                    exemplar_id = int(prompt_file.split('_')[-1].split('.')[0])
                    ex[prompt_concept] = exemplar_id
                except:
                    pass
            
            correct_concept = row['correctConcept']
            correct_file = row['correctFile']
            
            if correct_concept not in ex and correct_file and pd.notna(correct_file):
                try:
                    exemplar_id = int(correct_file.split('_')[-1].split('.')[0])
                    ex[correct_concept] = exemplar_id
                except:
                    pass
        
        exemplars[seq_label] = ex
    
    return exemplars

# ============================================================================
# Step 2: create balanced schedule for which distances retrieval trials cover
# ============================================================================

def make_balanced_trial_type_schedule_with_positions(
    n_miniblocks: int,
    distances=(0, 1, 2, 3, 4),
    rng=None
) -> dict:
    """Creates schedule with trial type distribution."""
    if rng is None:
        rng = random.Random(0)
    
    distances = list(distances)
    # miniblocks are set of 5 retrieval tirals that follow each learn route
    n_miniblocks = max(n_miniblocks, 2)
    
    print(f"\n  Phase 1: Creating image-distance-to-trial-type schedule for {n_miniblocks} miniblocks...")
    
    # potential distributions of distances for trial types: 2*T1, 2*T2, 1*T3
    templates = [
        ([0, 1], [2, 3], [4]),
        ([0, 1], [2, 4], [3]),
        ([0, 1], [3, 4], [2]),
        ([0, 2], [1, 3], [4]),
        ([0, 2], [1, 4], [3]),
        ([0, 2], [3, 4], [1]),
        ([0, 3], [1, 2], [4]),
        ([0, 3], [1, 4], [2]),
        ([0, 3], [2, 4], [1]),
        ([0, 4], [1, 2], [3]),
        ([0, 4], [1, 3], [2]),
        ([0, 4], [2, 3], [1]),
        ([1, 2], [0, 3], [4]),
        ([1, 2], [0, 4], [3]),
        ([1, 2], [3, 4], [0]),
        ([1, 3], [0, 2], [4]),
        ([1, 3], [0, 4], [2]),
        ([1, 3], [2, 4], [0]),
        ([1, 4], [0, 2], [3]),
        ([1, 4], [0, 3], [2]),
        ([1, 4], [2, 3], [0]),
        ([2, 3], [0, 1], [4]),
        ([2, 3], [0, 4], [1]),
        ([2, 3], [1, 4], [0]),
        ([2, 4], [0, 1], [3]),
        ([2, 4], [0, 3], [1]),
        ([2, 4], [1, 3], [0]),
        ([3, 4], [0, 1], [2]),
        ([3, 4], [0, 2], [1]),
        ([3, 4], [1, 2], [0]),
    ] # maybe don't generate here, not really flexible 
    
    selected_distance_templates = []
    counts_per_type = {1: Counter(), 2: Counter(), 3: Counter()}
    
    # how often each distance is used for each retrieval question type 

    max_per_type_1 = max(2, (n_miniblocks * 2 + 4) // 5)
    max_per_type_2 = max(2, (n_miniblocks * 2 + 4) // 5)
    max_per_type_3 = max(1, (n_miniblocks + 4) // 5)
    
    for mb in range(n_miniblocks):
        best_template = None
        best_score = -float('inf')
        candidates = []
        
        for template in templates:
            t1_dists, t2_dists, t3_dists = template
            
            valid = True
            for d in t1_dists: 
                # break if ditstance has already been used too often on this trial type
                if counts_per_type[1][d] >= max_per_type_1:
                    valid = False
                    break
            if valid:
                for d in t2_dists:
                    if counts_per_type[2][d] >= max_per_type_2:
                        valid = False
                        break
            if valid:
                for d in t3_dists:
                    if counts_per_type[3][d] >= max_per_type_3:
                        valid = False
                        break
            
            if valid:
                # BEFORE scoring, simulate what counts would be AFTER this template
                projected_counts = {1: counts_per_type[1].copy(), 
                                   2: counts_per_type[2].copy(), 
                                   3: counts_per_type[3].copy()}
    
                # Apply this template's distances
                for d in t1_dists:
                    projected_counts[1][d] += 1
                for d in t2_dists:
                    projected_counts[2][d] += 1
                for d in t3_dists:
                    projected_counts[3][d] += 1
                
                # Lower std = more balanced distances within each trial type
                balance_scores = []
                for trial_type in [1, 2, 3]:
                    freq_values = list(projected_counts[trial_type].values())
                    if freq_values:
                        balance_scores.append(-np.std(freq_values))
                
                score = sum(balance_scores)
                
                if score > best_score:
                    best_score = score
                    candidates = [template]
                elif score == best_score:
                    candidates.append(template)
                    
        if not candidates:
            raise RuntimeError(f"Cannot construct distance schedule at miniblock {mb}")
        
        best_template = rng.choice(candidates)
        selected_distance_templates.append(best_template)
        
        t1_dists, t2_dists, t3_dists = best_template
        # update counters for the used distances in this specific miniblock
        for d in t1_dists:
            counts_per_type[1][d] += 1
        for d in t2_dists:
            counts_per_type[2][d] += 1
        for d in t3_dists:
            counts_per_type[3][d] += 1
    
    print("Distance schedule created")
    
    schedule = {}
    for mb in range(n_miniblocks):
        t1_dists, t2_dists, t3_dists = selected_distance_templates[mb]
        
        schedule[mb] = {
            'type1_distances': list(t1_dists),
            'type2_distances': list(t2_dists),
            'type3_distances': list(t3_dists),
        }
    
    return schedule

# ============================================================================
# Step 3: decide which images the retrieval trials use
# ============================================================================

def get_trial_positions(pair_info: Tuple, trial_type: int) -> Set[int]:
    """
    Get positions shown in this trial (relevant for coverage).
    
    Type 2: anchor + correct choice (not incorrect)
    Type 1/3: both positions
    """
    if trial_type == 2:
        # Type 2: anchor + closer
        anchor, closer, farther = pair_info
        return {anchor, closer}
    else:
        # Type 1, 3: both positions
        i, j = pair_info
        return {i, j}

def find_valid_miniblock_with_coverage(
    type1_distances: List[int],
    type2_distances: List[int],
    type3_distances: List[int],
    seq: List[str],
    ex: Dict,
    rng: random.Random,
    miniblock_idx: int = None,
    max_attempts: int = 10000,
) -> Optional[List[Tuple]]:
    """
    Backtracking search to find valid miniblock that:
    1. Covers all 10 middle positions
    2. no consecutive-trial image repetition
    3. covers all image distances from 1-5 once
    4. Maintains trial type distribution
    
    Returns: list of (pair_info, trial_type, distance) or None
    """
    
    middle = list(range(2, 12)) # middle 10 images have indices 2-11
    
    # Build list of required (trial_type, distance) pairs
    required_trials = (
        [(1, d) for d in type1_distances] +
        [(2, d) for d in type2_distances] +
        [(3, d) for d in type3_distances]
    )
    
    def get_candidates_for_trial_spec(trial_type: int, distance: int) -> List[Tuple]:
        """collect candidate image pairs for a given trial type and set distance"""
        candidates = []
        
        if trial_type == 1:
            for i in middle:
                j = i + distance + 1
                if j <= 11:
                    pair = (i, j)
                    candidates.append(pair)
        
        elif trial_type == 2:
            for anchor in middle:
                for closer in middle:
                    if closer == anchor:
                        continue
                    if _distance(anchor, closer) != distance:
                        continue
                    for farther in middle:
                        if farther in (anchor, closer):
                            continue
                        if _distance(anchor, farther) > distance:
                            # CONSTRAINT: Anchor must be OUTSIDE the (closer, farther) pair
                            # i.e., anchor comes before or after both choices in sequence
                            min_choice = min(closer, farther)
                            max_choice = max(closer, farther)
                            
                            # OUTSIDE: anchor < min_choice OR anchor > max_choice
                            if anchor < min_choice or anchor > max_choice:
                                triplet = (anchor, closer, farther)
                                candidates.append(triplet)
        
        elif trial_type == 3:
            for i in middle:
                j = i + distance + 1
                if j <= 11:
                    pair = (i, j)
                    candidates.append(pair)
        
        return candidates
    
    def can_still_cover(covered: Set[int], remaining_count: int) -> bool:
        """
        Heuristic: check if we can still cover all positions in the image sequence.
        Each trial covers at most 2 new positions.
        """
        needed = set(middle) - covered
        if not needed:
            return True
        
        # If we need more positions than we have trials left to cover them
        if len(needed) > remaining_count * 2:
            return False
        
        return True
    
    def backtrack(
        placed_trials: List[Tuple],
        remaining_trial_specs: List[Tuple],
        covered_positions: Set[int],
        used_pairs: Set[Tuple],
        prev_trial_positions: Set[int],
    ) -> Optional[List[Tuple]]:
        """
        When placing each trial in the miniblock., check if we can still meet all constraints.
        """
        
        # Success: all trials placed and all positions covered
        if not remaining_trial_specs:
            if covered_positions == set(middle):
                return placed_trials
            else:
                return None
        
        # can we still cover all positions based on current selection?
        if not can_still_cover(covered_positions, len(remaining_trial_specs)):
            return None
        
        # Try each remaining trial spec (planned trials for current attempt)
        for spec_idx, (trial_type, distance) in enumerate(remaining_trial_specs):
            # Get candidates for this trial
            candidates = get_candidates_for_trial_spec(trial_type, distance)
            
            if not candidates:
                continue
            
            # Shuffle candidates for randomness
            rng.shuffle(candidates)
            
            for pair_info in candidates:
                # Get positions shown in this trial
                trial_positions = get_trial_positions(pair_info, trial_type)
                
                # Check 1: no image repetitions between trials 
                if placed_trials:
                    if trial_positions & prev_trial_positions:
                        continue  
                
                # Check 2: Don't use same pair twice
                if pair_info in used_pairs:
                    continue
                
                # Try placing this trial
                new_covered = covered_positions | trial_positions
                new_used = used_pairs | {pair_info}
                other_remaining = remaining_trial_specs[:spec_idx] + remaining_trial_specs[spec_idx+1:]
                
                result = backtrack(
                    placed_trials + [(pair_info, trial_type, distance)],
                    other_remaining,
                    new_covered,
                    new_used,
                    trial_positions
                )
                
                if result is not None:
                    return result
        
        return None
    
    # take the dist-to trial type mapping for this miniblock determined before
    # assign image pairs to each trial in miniblock and check if other constraints are met
    for shuffle_attempt in range(max_attempts):
        shuffled_specs = required_trials.copy()
        rng.shuffle(shuffled_specs)
        
        result = backtrack([], shuffled_specs, set(), set(), set())
        if result is not None:
            return result
    
    return None

# ============================================================================
# Step 4: build rows with all information required for each trial 
# ============================================================================

def build_retrieval_miniblock_from_specs(
    trial_specs: List[Tuple],
    seq: List[str],
    ex: Dict,
    rng: random.Random,
    block_label: str,
    seq_label: str,
    run_index_within_seq: int,
    miniblock_idx: int,
    pair_usage_by_type: Dict,
    recent_pairs: deque,
) -> List[Dict]:
    """Build actual trial rows from valid trial specifications"""
    
    rows = []
    bumps = []
    
    for pair_info, trial_type, distance in trial_specs:
        if trial_type == 1:
            i, j = pair_info
            c1, c2 = seq[i], seq[j]
            img1, img2 = _file(c1, ex[c1]), _file(c2, ex[c2])
            
            # is correct answer yes 
            is_yes = (len(rows) % 2 == 0)
            rows.append({
                "trial_type": 1,
                "sequence_name": seq_label,
                "blockLabel": block_label,
                "runIndexWithinSeq": run_index_within_seq,
                "img_first": img1,
                "img_second": img2,
                "img_third": "",
                "opt_left": "yes",
                "opt_right": "no",
                "correct_side": YES_KEY if is_yes else NO_KEY,
                "correct_key": YES_KEY if is_yes else NO_KEY,
                "is_yes": 1 if is_yes else 0,
                "distance_correct": distance,
                "image_dur_retr": 1.2,
                "fix_dur_retr": 0.2,
            })
            
            bumps.append((1, distance, i, j))
        
        elif trial_type == 2:
            anchor_idx, closer_idx, farther_idx = pair_info
            anchor_c = seq[anchor_idx]
            closer_c = seq[closer_idx]
            farther_c = seq[farther_idx]
            
            correct_side = rng.choice([YES_KEY, NO_KEY])
            if correct_side == YES_KEY:
                left_c, right_c = closer_c, farther_c
            else:
                left_c, right_c = farther_c, closer_c
            
            anchor_img = _file(anchor_c, ex[anchor_c])
            left_img = _file(left_c, ex[left_c])
            right_img = _file(right_c, ex[right_c])
            
            rows.append({
                "trial_type": 2,
                "sequence_name": seq_label,
                "blockLabel": block_label,
                "runIndexWithinSeq": run_index_within_seq,
                "img_first": anchor_img,
                "img_second": left_img,
                "img_third": right_img,
                "opt_left": left_img,
                "opt_right": right_img,
                "correct_side": correct_side,
                "correct_key": correct_side,
                "distance_correct": distance,
                "image_dur_retr": 1.5,
                "fix_dur_retr": 0.2,
            })
            
            bumps.append((2, distance, anchor_idx, closer_idx))
        
        elif trial_type == 3:
            i, j = pair_info
            c1, c2 = seq[i], seq[j]
            img1, img2 = _file(c1, ex[c1]), _file(c2, ex[c2])
            
            rows.append({
                "trial_type": 3,
                "sequence_name": seq_label,
                "blockLabel": block_label,
                "runIndexWithinSeq": run_index_within_seq,
                "img_first": img1,
                "img_second": img2,
                "img_third": "",
                "opt_left": "",
                "opt_right": "",
                "correct_side": "",
                "correct_key": DIST_KEY_MAP_0_TO_4[distance],
                "distance_correct": distance,
                "image_dur_retr": 2.0,
                "fix_dur_retr": 0.5,
            })
            
            bumps.append((3, distance, i, j))
    
    # Update pair usage statistics
    for (trial_type, distance, i, j) in bumps:
        i, j = sorted([i, j])
        pair_usage_by_type[trial_type][distance][(i, j)] += 1
        recent_pairs.append((trial_type, distance, i, j))
    
    return rows


# ============================================================================
# step 5: build blocks of 5 trials for sequence A and B respetively
# ============================================================================

def build_retrieval_block_A_participant_balanced(seqA, exA, *, block_label="A", seed, n_runs=6):
    rng = random.Random(seed)
    
    n_miniblocks = n_runs
    
    schedule_rng = random.Random(seed + 1000)
    schedule = make_balanced_trial_type_schedule_with_positions(
        n_miniblocks=n_miniblocks,
        distances=(0, 1, 2, 3, 4),
        rng=schedule_rng
    )
    
    pair_usage_by_type = {
        1: {d: Counter() for d in range(0, 5)},
        2: {d: Counter() for d in range(0, 5)},
        3: {d: Counter() for d in range(0, 5)},
    }
    
    recent_pairs = deque(maxlen=20)
    all_rows = []
    
    print("\n  Building miniblocks...")
    print("  Sequence A (1/1):")
    
    for run_idx in range(1, n_runs + 1):
        trial_schedule = schedule[run_idx - 1]
        
        print(f"Run {run_idx}/{n_runs} (MB {run_idx - 1})...", end=" ", flush=True)
        
        # Find valid miniblock with coverage
        trial_specs = find_valid_miniblock_with_coverage(
            trial_schedule['type1_distances'],
            trial_schedule['type2_distances'],
            trial_schedule['type3_distances'],
            seqA, exA, rng,
            miniblock_idx=run_idx - 1,
            max_attempts=500000,
        )
        
        if trial_specs is None:
            raise RuntimeError(
                f"Failed to construct valid retrieval miniblock {run_idx - 1} "
                f"for {block_label} (no valid miniblock found with coverage constraint)"
            )
        
        miniblock_rows = build_retrieval_miniblock_from_specs(
            trial_specs, seqA, exA, rng,
            block_label=block_label,
            seq_label="A",
            run_index_within_seq=run_idx,
            miniblock_idx=run_idx - 1,
            pair_usage_by_type=pair_usage_by_type,
            recent_pairs=recent_pairs,
        )
        
        all_rows.extend(miniblock_rows)
        
        print("retrieval trials block A finished")
    
    df = pd.DataFrame(all_rows)
    df = _add_retr_trig_cols(df)
    
    print("\n  Pair balancing report:")
    for trial_type in [1, 2, 3]:
        print(f"\n    Trial Type {trial_type}:")
        for distance in range(0, 5):
            pair_counter = pair_usage_by_type[trial_type][distance]
            if pair_counter:
                total = sum(pair_counter.values())
                n_unique = len(pair_counter)
                print(f"      Distance {distance}: {n_unique} unique pairs, {total} total uses")
    
    return df

def build_retrieval_block_B_participant_balanced(seqA, exA, seqB, exB, *, block_label="B", seed, n_runs_each=6):
    rng = random.Random(seed)
    
    schedule_rng_A = random.Random(seed + 1000)
    schedule_A = make_balanced_trial_type_schedule_with_positions(
        n_miniblocks=n_runs_each,
        distances=(0, 1, 2, 3, 4),
        rng=schedule_rng_A
    )
    
    schedule_rng_B = random.Random(seed + 2000)
    schedule_B = make_balanced_trial_type_schedule_with_positions(
        n_miniblocks=n_runs_each,
        distances=(0, 1, 2, 3, 4),
        rng=schedule_rng_B
    )
    
    pair_usage_by_type_A = {
        1: {d: Counter() for d in range(0, 5)},
        2: {d: Counter() for d in range(0, 5)},
        3: {d: Counter() for d in range(0, 5)},
    }
    
    pair_usage_by_type_B = {
        1: {d: Counter() for d in range(0, 5)},
        2: {d: Counter() for d in range(0, 5)},
        3: {d: Counter() for d in range(0, 5)},
    }
    
    recent_pairs = deque(maxlen=20)
    all_rows = []
    
    print("\n  Building miniblocks...")
    
    for r in range(1, n_runs_each + 1):
        print(f"  Sequence B ({r}/{n_runs_each}):")
        trial_schedule = schedule_B[r - 1]
        
        print(f"    Run {r}...", end=" ", flush=True)
        
        trial_specs = find_valid_miniblock_with_coverage(
            trial_schedule['type1_distances'],
            trial_schedule['type2_distances'],
            trial_schedule['type3_distances'],
            seqB, exB, rng,
            miniblock_idx=r - 1,
            max_attempts=500000,
        )
        
        if trial_specs is None:
            raise RuntimeError(
                f"Failed to construct valid retrieval miniblock {r - 1} "
                f"for B (no valid miniblock found with coverage constraint)"
            )
        
        miniblock_rows = build_retrieval_miniblock_from_specs(
            trial_specs, seqB, exB, rng,
            block_label=block_label,
            seq_label="B",
            run_index_within_seq=r,
            miniblock_idx=r - 1,
            pair_usage_by_type=pair_usage_by_type_B,
            recent_pairs=recent_pairs,
        )
        
        all_rows.extend(miniblock_rows)
        print("Block B retrieval miniblocks build for sequence B")
        
        trial_schedule = schedule_A[r - 1]
        
        
        trial_specs = find_valid_miniblock_with_coverage(
            trial_schedule['type1_distances'],
            trial_schedule['type2_distances'],
            trial_schedule['type3_distances'],
            seqA, exA, rng,
            miniblock_idx=r - 1,
            max_attempts=500000,
        )
        
        if trial_specs is None:
            raise RuntimeError(
                f"Failed to construct valid retrieval miniblock {r - 1} "
                f"for A (no valid miniblock found with coverage constraint)"
            )
        
        miniblock_rows = build_retrieval_miniblock_from_specs(
            trial_specs, seqA, exA, rng,
            block_label=block_label,
            seq_label="A",
            run_index_within_seq=r,
            miniblock_idx=r - 1,
            pair_usage_by_type=pair_usage_by_type_A,
            recent_pairs=recent_pairs,
        )
        
        all_rows.extend(miniblock_rows)
        print("Block B retrieval miniblocks build for sequence A")

    
    df = pd.DataFrame(all_rows)
    df = _add_retr_trig_cols(df)
    
    print("\n  Pair balancing (Sequence B):")
    for trial_type in [1, 2, 3]:
        print(f"\n    Trial Type {trial_type}:")
        for distance in range(0, 5):
            pair_counter = pair_usage_by_type_B[trial_type][distance]
            if pair_counter:
                total = sum(pair_counter.values())
                n_unique = len(pair_counter)
                print(f"      Distance {distance}: {n_unique} unique pairs, {total} total uses")
    
    print("\n  Pair balancing (Sequence A):")
    for trial_type in [1, 2, 3]:
        print(f"\n    Trial Type {trial_type}:")
        for distance in range(0, 5):
            pair_counter = pair_usage_by_type_A[trial_type][distance]
            if pair_counter:
                total = sum(pair_counter.values())
                n_unique = len(pair_counter)
                print(f"      Distance {distance}: {n_unique} unique pairs, {total} total uses")
    
    return df

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def generate_retrieval_for_participant(
    learning_file: str,
    block_label: str,
    ppt_id: str,
    seed: int,
    output_dir: str,
) -> str:
    
    print(f"Generating {block_label} Retrieval for Participant {ppt_id}")
    
    print(f"\nExtracting sequences from: {learning_file}")
    sequences = extract_sequences_from_learning(learning_file)
    exemplars = extract_exemplars_from_learning(learning_file)
    
    for seq_label, seq in sequences.items():
        ex = exemplars.get(seq_label, {})
        print(f"  Sequence {seq_label}: {len(seq)} concepts, {len(ex)} exemplars assigned")
    
    
    if block_label == "A":
        seqA = sequences["A"]
        exA = exemplars.get("A", {})
        
        df_retrieval = build_retrieval_block_A_participant_balanced(
            seqA, exA,
            block_label="A",
            seed=seed,
            n_runs=6,
        )
        
        output_file = os.path.join(output_dir, f"retrieval_blockA_fixed-middle-10_{ppt_id}.xlsx")
    
    else:
        seqA = sequences["A"]
        seqB = sequences["B"]
        exA = exemplars.get("A", {})
        exB = exemplars.get("B", {})
        
        df_retrieval = build_retrieval_block_B_participant_balanced(
            seqA, exA, seqB, exB,
            block_label="B",
            seed=seed,
            n_runs_each=6,
        )
        
        output_file = os.path.join(output_dir, f"retrieval_blockB_fixed-middle-10_{ppt_id}.xlsx")
    
    os.makedirs(output_dir, exist_ok=True)
    df_retrieval.to_excel(output_file, sheet_name='retrieval', index=False)
    
    print(f"\nSaved {block_label} retrieval: {len(df_retrieval)} trials")
    
    return output_file

def main():
    
    learning_dir = LEARNING_DIR
    output_dir = OUTPUT_DIR
    specific_ppts = PARTICIPANT_IDS
    
    if not os.path.isdir(learning_dir):
        print(f"ERROR: Learning directory not found: {learning_dir}")
        sys.exit(1)
    
    os.makedirs(output_dir, exist_ok=True)
    
    
    all_files = sorted(os.listdir(learning_dir))
    
    learning_files = {}
    learning_block_files = [f for f in all_files if f.startswith('learning_block')]
    
    if not learning_block_files:
        print("\nNo files starting with 'learning_block' found")
        sys.exit(1)
    
    
    for filename in learning_block_files:
        if not filename.endswith('.xlsx'):
            continue
        
        name_without_ext = filename.replace('.xlsx', '')
        
        if not name_without_ext.startswith('learning_block'):
            continue
        
        after_prefix = name_without_ext[len('learning_block'):]
        
        if not after_prefix or after_prefix[0] not in ['A', 'B']:
            continue
        
        block = after_prefix[0]
        last_underscore = after_prefix.rfind('_')
        
        if last_underscore == -1:
            continue
        
        ppt_id = after_prefix[last_underscore+1:]
        
        if not ppt_id.isdigit() or len(ppt_id) != 2:
            continue
        
        if specific_ppts is not None and ppt_id not in specific_ppts:
            continue
        
        if ppt_id not in learning_files:
            learning_files[ppt_id] = {}
        
        learning_files[ppt_id][block] = os.path.join(learning_dir, filename)
        print(f"    Loaded: {filename} (Block {block}, Participant {ppt_id})")
    
    
    
    success_count = 0
    fail_count = 0
    
    for ppt_id in sorted(learning_files.keys()):
        blocks = learning_files[ppt_id]
        
        for block_label in sorted(blocks.keys()):
            learning_file = blocks[block_label]
            seed = SEED + int(ppt_id)
            
            try:
                generate_retrieval_for_participant(
                    learning_file=learning_file,
                    block_label=block_label,
                    ppt_id=ppt_id,
                    seed=seed,
                    output_dir=output_dir,
                )
                success_count += 1
            except Exception as e:
                print(f"\nFAILED generating {block_label} for participant {ppt_id}")
                print(f"Error: {e}")
                fail_count += 1
    
    print(f"Successfully generated: {success_count} retrieval files")
    if fail_count > 0:
        print(f"Failed: {fail_count} retrieval files")


if __name__ == "__main__":
    main()