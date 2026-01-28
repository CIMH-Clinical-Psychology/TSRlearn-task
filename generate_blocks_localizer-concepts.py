
"""
LOCALIZER CONDITION GENERATOR FOR TSRLEARN EXPERIMENT

Creates localizer trials with match/mismatch detection task for EEG/MEG.
Each participant sees 300 trials (30 exemplars × 10 fixed concepts).

Outputs per participant:
 - XX_localizer_conditions.xlsx - Complete trial schedule with timing

"""
import os
import random
import pandas as pd
from collections import deque, Counter, defaultdict
from typing import Dict, List

# ============================================================================
# settings
# ============================================================================

n_participants = 20
base_name = "localizer_conditions"
SEED = 10 # change later!! changed from 7

# Trial structure
N_EXEMPLARS_PER_CONCEPT = 20  # 20 exemplars per concept (2 from learning + 18 random)
MISMATCH_RATIO = 0.10         # 10% mismatch trials (2 per concept)
N_BLOCKS = 4                  # 4 blocks per participant
N_POSITION_SEGMENTS = 10      # For position-based balancing

# Fixed concepts (trigger numbers 1-10 based on order)
MIDDLE_10_FIXED = [
    "ball",      # trigger 1
    "bicycle",   # trigger 2
    "bread",     # trigger 3
    "chair",     # trigger 4
    "dog",       # trigger 5
    "flower",    # trigger 6
    "hammer",    # trigger 7
    "hand",      # trigger 8
    "house",     # trigger 9
    "jacket",    # trigger 10
]

# Response keys
MATCH_KEY = None           # Match trials: no button press
NONMATCH_KEY = "right"     # Mismatch trials: press right
SCREEN_POSITIONS = ["left", "right"]

# ITI settings
ITI_RANGE = (0.75, 1.25)

# Generation constraints
MAX_STREAK = 1           # Max identical concepts/words in a row
MAX_ATTEMPTS = 20000     # Max attempts to build valid schedule

# ============================================================================
# translations
# ============================================================================

folder_name_map = {c: c for c in MIDDLE_10_FIXED}

german_map = {
    "ball": "Ball",
    "bicycle": "Fahrrad",
    "bread": "Brot",
    "chair": "Stuhl",
    "dog": "Hund",
    "flower": "Blume",
    "hammer": "Hammer",
    "hand": "Hand",
    "house": "Haus",
    "jacket": "Jacke",
}

french_map = {
    "ball": "Ballon",
    "bicycle": "Vélo",
    "bread": "Pain",
    "chair": "Chaise",
    "dog": "Chien",
    "flower": "Fleur",
    "hammer": "Marteau",
    "hand": "Main",
    "house": "Maison",
    "jacket": "Veste",
}

# ============================================================================
# constraint
# ============================================================================

"""
GROUP-LEVEL CONSTRAINTS (Across all participants):
-----------------------------------------------------
1. Fixed concept set: All participants use MIDDLE_10_FIXED (10 concepts)
2. Fixed exemplar count: Each concept has exactly 20 exemplars shown in localizer
   - 2 exemplars MUST be from learning trials (middle 10 positions from sequences A & B)
   - 18 exemplars randomly selected from remaining available exemplars
3. Fixed mismatch ratio: 10% mismatches per concept (2 out of 20)
4. Fixed total trials: 200 trials per participant
5. Consistent trigger mapping: Triggers 1-10 assigned by MIDDLE_10_FIXED order
6. Fixed block structure: 4 blocks of 50 trials each
7. Balance Transitions: Each image→image transition balanced across participants
   - 90 possible transitions (10×9, no A→A due to MAX_STREAK)
8. Position balance: Each concept appears in each position equally across participants
   - Position 1-200 tracked across all participants
   - Target: Each concept equally distributed across positions

INDIVIDUAL CONSTRAINTS (Per participant):
------------------------------------------
01. MAX_STREAK (concept): No more than 1 identical concept image in a row
02. MAX_STREAK (word): No more than 1 identical word in a row
03. Block balance: Concepts distributed evenly across 4 blocks
    - Target: 20 trials / 4 blocks = 5 per block per concept
04. Total mismatches per block = 5 (HARD CONSTRAINT - 20 total / 4 blocks)
05. Mismatch segment balance: Mismatches evenly distributed across all segments 
    - Each block divided into 5 segments of 10 trials
    - Target: 1 mismatch per segment (prevents clustering at beginning/end)
    - gets relaxed a bit after 80% of max attempts 
06. Mismatch block balance per concept: Mismatches distributed evenly across blocks
    - Target: 2 mismatches / 4 blocks ≈ 0.5 per block per concept
07. Position segment balance: Concepts distributed across 10 segments
    - 200 trials / 10 segments = 20 trials per segment
    - Target: 20 trials / 10 concepts = 2 per segment per concept
08. balanced transitions between concepts: Balanced within participant
    - 199 transitions / (10×9 = 90 possible) ≈ 2.2 times each
09. Exemplar spread: Each exemplar (1-20) spread across 200 trials
    - Prevents same exemplars always appearing at same positions
    - we don't really need that on the concept localizer since each exemplar only used once
10. Mismatch partner balance: Mismatch pairings well-distributed
    - E.g., "ball" image + "dog" word shouldn't occur too often
11. After mismatch transition: balance mismatch word -> next concept transitions 
    and mismatch image -> next concept transition
11. ITI randomization: Random 0.75-1.25s per trial

FIXED RESPONSE MAPPING (No balancing needed):
----------------------------------------------
- Match trials (90%): MATCH_KEY = None (no button press)
- Mismatch trials (10%): NONMATCH_KEY = "right"
"""

# ============================================================================
# global tracking function
# ============================================================================

def initialize_global_counters():
    """Initialize global counters for cross-participant balancing."""
    return {
        'transitions': Counter(),  # (concept_A, concept_B) -> count
        'positions': Counter(),    # (concept, position) -> count
    }


def update_global_counters(global_counters: dict, df: pd.DataFrame) -> dict:
    """
    Update global counters after a participant's schedule is generated.
    
    Inputs:
        global_counters: Dictionary with 'transitions' and 'positions' Counters
        df: DataFrame with the participant's complete schedule
    
    Returns:
        Updated global_counters
    """
    # Track transitions
    for i in range(len(df) - 1):
        concept_from = df.iloc[i]['concept']
        concept_to = df.iloc[i + 1]['concept']
        transition = (concept_from, concept_to)
        global_counters['transitions'][transition] += 1
    
    # Track positions
    for position, row in enumerate(df.itertuples()):
        concept = row.concept
        global_counters['positions'][(concept, position)] += 1
    
    return global_counters


def save_global_counters(filepath: str, counters: dict):
    """Save global counters to JSON file."""
    import json
    
    # Convert tuple keys to strings for JSON
    transitions_str = {f"{k[0]}→{k[1]}": v for k, v in counters['transitions'].items()}
    positions_str = {f"{k[0]}@{k[1]}": v for k, v in counters['positions'].items()}
    
    with open(filepath, 'w') as f:
        json.dump({
            'transitions': transitions_str,
            'positions': positions_str
        }, f, indent=2)


def print_global_report(counters: dict, n_participants: int, concepts: List[str]):
    """Print final report of transitions and position counts on a group level."""
    # to do: change this function to compute exüected transition and position counts for specific settings
    print("GLOBAL BALANCE REPORT")
    
    print(f"\nParticipants analyzed: {n_participants}")
    
    # Transition balance
    print("\n[TRANSITION BALANCE]")
    print("  Expected: ~3.3 per transition per participant")
    print(f"  Total transitions tracked: {sum(counters['transitions'].values())}")
    
    if counters['transitions']:
        transition_counts = list(counters['transitions'].values())
        expected = n_participants * 199 / 90  # (n_ppts * transitions_per_ppt) / possible_transitions
        print(f"  Expected per transition: {expected:.1f}")
        print(f"  Min: {min(transition_counts)}")
        print(f"  Max: {max(transition_counts)}")
        print(f"  Range: {max(transition_counts) - min(transition_counts)}")
        
        # Show most and least common transitions
        most_common = counters['transitions'].most_common(5)
        least_common = sorted(counters['transitions'].items(), key=lambda x: x[1])[:5]
        
        print(f"\n  Most common transitions:")
        for (c1, c2), count in most_common:
            print(f"    {c1:10s} → {c2:10s}: {count:4d} ({count/expected:.2f}x expected)")
        
        print(f"\n  Least common transitions:")
        for (c1, c2), count in least_common:
            print(f"    {c1:10s} → {c2:10s}: {count:4d} ({count/expected:.2f}x expected)")
    
    # Position balance
    print("\n[POSITION BALANCE]")
    print("  Checking if concepts equally distributed across trial positions...")
    
    # Group by concept
    position_by_concept = defaultdict(list)
    for (concept, position), count in counters['positions'].items():
        position_by_concept[concept].append(count)
    
    print(f"  Expected: {n_participants} appearances per position per concept")
    
    for concept in concepts:
        counts = position_by_concept[concept]
        if counts:
            print(f"    {concept:10s}: min={min(counts)}, max={max(counts)}, range={max(counts)-min(counts)}")
    


# ============================================================================
# helper functions for preparing for trial list generation
# ============================================================================

def extract_exemplar_number(file_path: str) -> int:
    """Extract exemplar number from file path like 'berry\\berry_05.jpg'"""
    if pd.isna(file_path):
        return None
    filename = str(file_path).split("/")[-1].split("\\")[-1]  # Handle both / and \
    exemplar_str = filename.split("_")[-1].split(".")[0]
    try:
        return int(exemplar_str)
    except:
        return None


def load_learning_exemplars(learning_file: str) -> Dict[str, set]:
    """
    Extract the 2 learning exemplars per concept from middle 10 positions (3-12).
    
    Inputs:
        learning_file: Path to learning_blockB_fixed-middle-10_XX.xlsx
    
    Returns:
        Dictionary mapping concept -> set of 2 exemplar numbers used in learning
    """
    if not os.path.exists(learning_file):
        raise FileNotFoundError(f"Learning file not found: {learning_file}")
    
    df = pd.read_excel(learning_file)
    
    available_sequences = df['learningSeq'].unique()
    if 'A' not in available_sequences or 'B' not in available_sequences:
        raise ValueError(f"Need both sequence 'A' and 'B'. Available: {available_sequences}")
        
    exemplar_by_concept = defaultdict(set)
    
    for seq in ['A', 'B']:
        df_seq = df[df['learningSeq'] == seq]
        
        if df_seq.empty:
            raise ValueError(f"No trials found for sequence {seq}")
        
        # Filter for middle 10 positions (3-12)
        df_middle = df_seq[(df_seq['currPosInSeq'] >= 3) & (df_seq['currPosInSeq'] <= 12)]
        
        if df_middle.empty:
            raise ValueError(f"No trials found in positions 3-12 for sequence {seq}")
        
        for _, row in df_middle.iterrows():
            concept = row['promptConcept']
            
            if 'promptFile' in row and pd.notna(row['promptFile']):
                try:
                    ex_num = extract_exemplar_number(row['promptFile'])
                    if ex_num is not None:
                        exemplar_by_concept[concept].add(ex_num)
                except:
                    pass
    
    # Verify we have exactly 2 exemplars per concept
    for concept, exemplars in exemplar_by_concept.items():
        if len(exemplars) != 2:
            print(f"  WARNING: Concept '{concept}' has {len(exemplars)} learning exemplars, expected 2")
    
    print(f"Loaded learning exemplars for {len(exemplar_by_concept)} concepts")
    
    return dict(exemplar_by_concept)


def validate_translations(concepts: List[str], german_map: dict, french_map: dict) -> bool:
    """Validate that all concepts have translations."""
    missing_german = [c for c in concepts if c not in german_map]
    missing_french = [c for c in concepts if c not in french_map]
    
    if missing_german or missing_french:
        error_msg = "Translation mapping incomplete:\n"
        if missing_german:
            error_msg += f"  Missing in German map: {missing_german}\n"
        if missing_french:
            error_msg += f"  Missing in French map: {missing_french}\n"
        raise ValueError(error_msg)
    
    return True


# ============================================================================
# helper functions for during trial list generation
# ============================================================================

def pick_nonmatching_word(
    concept: str,
    used_mismatches: dict,
    rng: random.Random,
    concepts: List[str]
) -> str:
    """
    Pick a non-matching word from available concepts.
    Tracks usage to ensure balanced mismatch partner distribution.
    """
    candidates = [w for w in concepts if w != concept and w not in used_mismatches[concept]]
    
    if not candidates:
        used_mismatches[concept].clear()
        candidates = [w for w in concepts if w != concept]
    
    if not candidates:
        raise ValueError(f"No candidates for mismatch word for concept '{concept}'")
    
    chosen = rng.choice(candidates)
    used_mismatches[concept].add(chosen)
    return chosen


def calculate_transition_targets(n_concepts: int, n_trials: int) -> float:
    """
    Calculate target appearance count for each transition.
    
    For 10 concepts and 300 trials:
    - 299 transitions total (300 trials - 1)
    - 10×9 = 90 possible transitions (A→B where A≠B, due to MAX_STREAK=1)
    - Target: 299 / 90 ≈ 3.3 times each transition
    """
    n_transitions = n_trials - 1
    n_possible_transitions = n_concepts * (n_concepts - 1)
    target_per_transition = n_transitions / n_possible_transitions
    return target_per_transition


def build_valid_schedule(
    trials: List[Dict],
    rng: random.Random,
    max_attempts: int,
    max_streak: int,
    n_exemplars_per_concept: int,
    concepts: List[str],
    global_counters: dict,
    n_blocks: int = 4,
    n_position_segments: int = 10,
    block_tol: int = 0 # no tolerance when trying to fullfill constraints
) -> List[Dict]:
    """
    Build valid schedule satisfying all individual AND group-level constraints.
    
    Uses progressive constraint relaxation:
    - Early attempts: Strict enforcement of all constraints
    - Later attempts: Gradual relaxation of soft constraints
    - Final attempts: Only hard constraints enforced
    
    Returns:
        List of trials in valid order, or empty list if failed
    """
    total = len(trials)
    if total == 0:
        return []
    
    n_concepts = len(concepts)
    
    # calculate target variables for some of the constraints
    
    # how often each concept gets shown per block 
    concept_target_per_block = {}
    for c in concepts:
        total_count = sum(1 for t in trials if t["concept"] == c)
        target_per_block = total_count // n_blocks
        concept_target_per_block[c] = target_per_block
    
    # how often each concept should appear in each segment 
    concept_target_per_segment = {}
    for c in concepts:
        total_count = sum(1 for t in trials if t["concept"] == c)
        target_per_segment = total_count // n_position_segments
        concept_target_per_segment[c] = target_per_segment
    
    # how often each mismatch appears per concept per block 
    mismatch_count_by_concept = {c: 0 for c in concepts}
    for t in trials:
        if t.get("is_mismatch", 0) == 1:
            mismatch_count_by_concept[t["concept"]] += 1
    
    mismatch_target_per_block = {}
    for c in concepts:
        tot_mismatches = mismatch_count_by_concept[c]
        target_per_block = max(1, tot_mismatches // n_blocks)
        mismatch_target_per_block[c] = target_per_block
    
    # how often each possible transition between concept images should appear 
    transition_target = calculate_transition_targets(n_concepts, total)
    
    # Attempt to build schedule
    for attempt_num in range(max_attempts):
        remaining = trials[:]
        rng.shuffle(remaining)
        schedule = []
        
        # Streak trackers
        last_concepts = deque(maxlen=max_streak)
        last_words = deque(maxlen=max_streak)
        last_transitions_local = Counter()
        
        # Per-block counters
        concept_counts_block = {c: [0] * n_blocks for c in concepts}
        mismatch_counts_block = {c: [0] * n_blocks for c in concepts}
        
        # Per-position-segment counters
        concept_counts_segment = {c: [0] * n_position_segments for c in concepts}
        
        # Exemplar position tracker
        exemplar_positions = defaultdict(list)
        
        # Mismatch partner tracking
        mismatch_pairs = Counter()
        
        # Track total mismatches per block (across all concepts)
        total_mismatches_per_block = [0] * n_blocks
        
        # Mismatch position segment balance (200 trials / 10 segments = 20 trials per segment)
        mismatch_counts_position_segment = [0] * n_position_segments
        mismatch_target_per_position_segment = max(1, (sum(1 for t in trials if t.get("is_mismatch", 0) == 1)) // n_position_segments)
        
        # Post-mismatch transition tracking
        post_mismatch_transitions_image = Counter()  # (mismatch_image_concept, next_concept) -> count
        post_mismatch_transitions_word = Counter()   # (mismatch_word_concept, next_concept) -> count
        post_mismatch_transition_target = max(1, 20 // 9)  # ~2.2 per transition (20 mismatches / 9 other concepts)
        
        # Progress indicator
        if attempt_num == 0:
            pass  # First attempt, no message
        elif attempt_num == 2000:
            print(f"    ... attempt {attempt_num}: relaxing global balancing constraints")
        elif attempt_num % 5000 == 0:
            print(f"    ... attempt {attempt_num}/{max_attempts}")
        
        # Determine if we should use global balancing of transitions and positions (disable after many attempts)
        use_global_balancing = (attempt_num <= 2000)
        
        ok = True
        
        for i in range(total):
            block_num = (i * n_blocks) // total
            segment_num = (i * n_position_segments) // total
            current_position = len(schedule)
        
            # Score all remaining candidates
            scored_candidates = []
            
            for idx, cand in enumerate(remaining):
                c = cand["concept"]
                w = cand["word_shown_english"]
                is_mismatch = (cand.get("is_mismatch", 0) == 1)
                
                # CONSTRAINT 01: Concept streak
                c_streak = sum(1 for prev_c in reversed(last_concepts) if prev_c == c)
                if c_streak >= max_streak:
                    continue
                
                # CONSTRAINT 02: Word streak
                w_streak = sum(1 for prev_w in reversed(last_words) if prev_w == w)
                if w_streak >= max_streak:
                    continue
                
                # CONSTRAINT 03: Per-block balance of concept use
                if concept_counts_block[c][block_num] >= concept_target_per_block[c] + block_tol:
                    continue
                
                # CONSTRAINT 04: Per-segment balance
                if concept_counts_segment[c][segment_num] >= concept_target_per_segment[c]: # no tol?
                    continue
                
                # CONSTRAINT: Total mismatches per block (exactly 5) ---
                if is_mismatch:
                    # Each block must have exactly 5 mismatches total
                    if total_mismatches_per_block[block_num] >= 5:
                        continue
                
               # CONSTRAINT: Mismatch position segment balance
                if is_mismatch:
                    # Divide all 200 trials into 10 position segments, target 2 mismatches per segment
                    if attempt_num < max_attempts * 0.8:
                        # Strict: Max 2 mismatches per position segment
                        if mismatch_counts_position_segment[segment_num] >= mismatch_target_per_position_segment:
                            continue
                    elif attempt_num >= max_attempts * 0.8:
                        # Relaxed: Max 3 mismatches per position segment
                        if mismatch_counts_position_segment[segment_num] >= mismatch_target_per_position_segment + 1:
                            continue
                
                # CONSTRAINT: Transitions after mismatches 
                if len(schedule) > 0 and schedule[-1].get("is_mismatch", 0) == 1:
                    # The previous trial was a mismatch, so control which image and word will be used now
                    last_mismatch_image_concept = schedule[-1]["concept"]
                    last_mismatch_word_concept = schedule[-1]["word_shown_english"]
                    
                    #if attempt_num < max_attempts * 0.8:
                        # Strict early: prevent the same post mismatch transition twice
                    if (post_mismatch_transitions_image.get((last_mismatch_image_concept, c), 0) >= 1 or
                        post_mismatch_transitions_word.get((last_mismatch_word_concept, c), 0) >= 1):
                        continue
                
                # CONSTRAINT: Mismatch per-block balance (per concept)
                if is_mismatch:
                    if mismatch_counts_block[c][block_num] >= mismatch_target_per_block[c] + block_tol: # no tol
                        continue
                
                # CONSTRAINT: transitions between concepts
                if len(last_concepts) > 0:
                    prev_c = last_concepts[-1]
                    transition = (prev_c, c)
                    if last_transitions_local[transition] > transition_target: # tolerance?
                        continue
                
                # CONSTRAINT: Exemplar position spread
                ex_str = cand["image_shown"].split("_")[-1].split(".")[0]
                ex_id = int(ex_str)
                exemplar_key = (c, ex_id)
                
                if exemplar_positions[exemplar_key]:
                    last_position = exemplar_positions[exemplar_key][-1]
                    gap = current_position - last_position
                    # min_gap = 3 if attempt_num < max_attempts * 0.8 else 2
                    min_gap = 5 # kind of random 

                    if gap < min_gap:
                        continue
                
                # CONSTRAINT: Mismatch partner balance ---
                if is_mismatch == 1:
                    mismatch_partner = cand["word_shown_english"]
                    pair = tuple(sorted([c, mismatch_partner]))
                    if mismatch_pairs[pair] > 1:

                        continue
                
                # All hard constraints passed - now calculate score for global balancing
                score = 0
                
                # Scoring penalty for post-mismatch transitions (soft balancing)
                # could delete this since we put hard constraint before 
                if len(schedule) > 0 and schedule[-1].get("is_mismatch", 0) == 1:
                    last_mismatch_image_concept = schedule[-1]["concept"]
                    last_mismatch_word_concept = schedule[-1]["word_shown_english"]
                    
                    image_trans_count = post_mismatch_transitions_image.get((last_mismatch_image_concept, c), 0)
                    word_trans_count = post_mismatch_transitions_word.get((last_mismatch_word_concept, c), 0)
                    
                    if image_trans_count > post_mismatch_transition_target:
                        score += (image_trans_count - post_mismatch_transition_target) * 100
                    if word_trans_count > post_mismatch_transition_target:
                        score += (word_trans_count - post_mismatch_transition_target) * 100
                        
                if use_global_balancing:
                    # Global transition balance
                    if len(last_concepts) > 0:
                        prev_c = last_concepts[-1]
                        global_transition = (prev_c, c)
                        transition_usage = global_counters['transitions'].get(global_transition, 0)
                        score += transition_usage * 100  
                    
                    # GROUP-LEVEL CONSTRAINT 8: Global position balance
                    position_usage = global_counters['positions'].get((c, current_position), 0)
                    score += position_usage * 100  # Weight positions 
                
                scored_candidates.append((score, idx, cand))
            
            if not scored_candidates:
                ok = False
                break
            
            # Select candidate with lowest score (least used globally)
            if scored_candidates:
                scored_candidates.sort(key=lambda x: x[0])
                min_score = scored_candidates[0][0]
                best_candidates = [x for x in scored_candidates if x[0] == min_score]
                _, picked_idx, item = rng.choice(best_candidates)
            
            
            # Remove from remaining and add to schedule
            remaining.pop(remaining.index(item))
            schedule.append(item)
            
            last_concepts.append(item["concept"])
            last_words.append(item["word_shown_english"])
            
            # Update local transition tracker
            if len(last_concepts) > 1:
                transition = (list(last_concepts)[-2], item["concept"])
                last_transitions_local[transition] += 1
            
            # Update counters
            concept_counts_block[item["concept"]][block_num] += 1
            concept_counts_segment[item["concept"]][segment_num] += 1
            
            if item.get("is_mismatch", 0) == 1:
                mismatch_counts_block[item["concept"]][block_num] += 1
                total_mismatches_per_block[block_num] += 1 
                
                # Track mismatch position segment (across all 200 trials)
                mismatch_counts_position_segment[segment_num] += 1
                
                pair = tuple(sorted([item["concept"], item["word_shown_english"]]))
                mismatch_pairs[pair] += 1
            
            # Track exemplar position
            ex_str = item["image_shown"].split("_")[-1].split(".")[0]
            ex_id = int(ex_str)
            exemplar_key = (item["concept"], ex_id)
            exemplar_positions[exemplar_key].append(len(schedule) - 1)
        
            # Track post-mismatch transitions (for next iteration)
            # If this trial comes after a mismatch, record the transition
            if len(schedule) > 1 and schedule[-2].get("is_mismatch", 0) == 1:
                mismatch_trial = schedule[-2]
                mismatch_image_concept = mismatch_trial["concept"]
                mismatch_word_concept = mismatch_trial["word_shown_english"]
                current_concept = item["concept"]
                
                post_mismatch_transitions_image[(mismatch_image_concept, current_concept)] += 1
                post_mismatch_transitions_word[(mismatch_word_concept, current_concept)] += 1
                
        if ok and not remaining:
            if attempt_num > 1:
                mode = "with global transition and position balancing" if use_global_balancing else "no global balancing"
                print(f"Succeeded on attempt {attempt_num} ({mode})")
            return schedule
    
    # Failed to find valid schedule
    return []


# ============================================================================
# main generation function
# ============================================================================

def build_localizer_for_participant(
    ppt_id: str,
    seed: int,
    out_xlsx: str,
    global_counters: dict,
    learning_file: str = None
) -> pd.DataFrame:
    """
    Build localizer conditions for a specific participant.
    
    Inputs:
        ppt_id: Participant ID (e.g., "00", "01")
        seed: Random seed for this participant
        out_xlsx: Output file path
        global_counters: Dictionary tracking cross-participant balance
        learning_file: Path to learning file to extract exemplars from
    
    Returns:
        DataFrame with complete trial schedule
    """
    rng = random.Random(seed)
    concepts = MIDDLE_10_FIXED
    
    print(f"Participant {ppt_id}")
    print("Generating localizer trials...")
    
    # Validate translations
    validate_translations(concepts, german_map, french_map)
    
    # Load learning exemplars (2 per concept)
    if learning_file is None:
        raise ValueError("learning_file must be provided to ensure learning exemplars are included")
    
    learning_exemplars = load_learning_exemplars(learning_file)
    
    # Assign trigger numbers (1-10 based on position in MIDDLE_10_FIXED)
    concept_to_num = {c: i+1 for i, c in enumerate(MIDDLE_10_FIXED)}
    
    # Build base trial list with learning exemplars + random other
    trials = []
    selected_exemplars_by_concept = {}  # Track which exemplars we selected
    
    for c in concepts:
        folder = folder_name_map[c]
        
        # Get the 2 learning exemplars for this concept
        if c not in learning_exemplars:
            raise ValueError(f"No learning exemplars found for concept '{c}'")
        
        learning_ex_set = learning_exemplars[c]
        if len(learning_ex_set) != 2:
            raise ValueError(f"Expected 2 learning exemplars for '{c}', got {len(learning_ex_set)}")
        
        # All available exemplars (1-40)
        all_exemplars = set(range(1, 41))  # A40 total exemplars available
        
        # Select 18 additional random exemplars (excluding the 2 learning ones)
        remaining_exemplars = list(all_exemplars - learning_ex_set)
        rng.shuffle(remaining_exemplars)
        additional_exemplars = remaining_exemplars[:18]
        
        # Combine: 2 learning + 18 random = 20 total
        selected_exemplars = sorted(list(learning_ex_set) + additional_exemplars)
        selected_exemplars_by_concept[c] = selected_exemplars
        

        # Create trials for all selected exemplars
        for ex in selected_exemplars:
            img = f"{folder}\\{folder}_{ex:02d}.jpg"
            trials.append({
                "concept": c,
                "image_shown": img,
                "concept_num": concept_to_num[c],
                "is_learning_exemplar": 1 if ex in learning_ex_set else 0
            })
    
    
    # Assign mismatches (2 per concept from the selected 20 exemplars)
    mismatch_index_by_concept = {}
    mismatches_per_concept = int(round(MISMATCH_RATIO * N_EXEMPLARS_PER_CONCEPT))  # Should be 2
    
    
    for c in concepts:
        # Get the selected exemplars for this concept
        selected_ex = selected_exemplars_by_concept[c]
        
        # Randomly choose 2 of the 20 selected exemplars to be mismatches
        selected_ex_shuffled = selected_ex.copy()
        rng.shuffle(selected_ex_shuffled)
        mismatch_ids = set(selected_ex_shuffled[:mismatches_per_concept])
        mismatch_index_by_concept[c] = mismatch_ids
        
    
    # Validate total mismatch count
    total_mismatches_assigned = sum(len(mismatch_index_by_concept[c]) for c in concepts)
    print(f"\nTotal mismatch exemplars assigned: {total_mismatches_assigned} (expected 20)")
    if total_mismatches_assigned != 20:
        raise RuntimeError(f"Expected 20 total mismatches, got {total_mismatches_assigned}")
    
    # add word assignments
    enriched = []
    used_mismatches = {c: set() for c in concepts}
    
    for base in trials:
        c = base["concept"]
        ex_str = base["image_shown"].split("_")[-1].split(".")[0]
        ex_id = int(ex_str)
        
        is_mismatch = 1 if ex_id in mismatch_index_by_concept[c] else 0
        
        # Choose the word
        if is_mismatch == 1:
            w_en = pick_nonmatching_word(c, used_mismatches, rng, concepts)
        else:
            w_en = c
        
        # Get translations
        w_de = german_map[w_en]
        w_fr = french_map[w_en]
        
        enriched.append({
            **base,
            "is_prompt": 1,
            "prompt_idx": 1,
            "is_mismatch": is_mismatch,
            "word_shown_english": w_en,
            "word_shown_german": w_de,
            "word_shown_french": w_fr,
        })
    
    # Validate trials have correct mismatch count
    enriched_mismatch_count = sum(1 for t in enriched if t["is_mismatch"] == 1)
    if enriched_mismatch_count != 20:
        # show per-concept counts
        for c in concepts:
            concept_trials = [t for t in enriched if t["concept"] == c]
            concept_mismatches = sum(1 for t in concept_trials if t["is_mismatch"] == 1)
            print(f" {c:10s}: {concept_mismatches} mismatches")
        raise RuntimeError(
            f"all trials have {enriched_mismatch_count} mismatches, expected 20"
        )
    
    # Build valid schedule with global balancing
    sched = build_valid_schedule(
        enriched,
        rng=rng,
        max_attempts=MAX_ATTEMPTS,
        max_streak=MAX_STREAK,
        n_exemplars_per_concept=N_EXEMPLARS_PER_CONCEPT,
        concepts=concepts,
        global_counters=global_counters,
        n_blocks=N_BLOCKS,
        n_position_segments=N_POSITION_SEGMENTS,
        block_tol=0
    )
    
    if not sched:
        raise RuntimeError(
            f"Failed to build valid schedule after {MAX_ATTEMPTS} attempts"
        )
    
    # add ITI and response keys 
    rows = []
    block_size = len(sched) // N_BLOCKS
    
    for trial_idx, t in enumerate(sched):
        iti = rng.uniform(*ITI_RANGE)
        block_num = trial_idx // block_size + 1
        
        # Fixed key mapping
        if t["is_mismatch"] == 0:
            correct_resp = MATCH_KEY
        else:
            correct_resp = NONMATCH_KEY
        
        nonmatch_pres_side = rng.choice(SCREEN_POSITIONS) if t["is_mismatch"] == 1 else MATCH_KEY
        
        rows.append({
            "block": block_num,
            "trial_in_block": (trial_idx % block_size) + 1,
            "concept": t["concept"],
            "concept_num": t["concept_num"],
            "image_shown": t["image_shown"],
            "word_shown_english": t["word_shown_english"],
            "word_shown_german": t["word_shown_german"],
            "word_shown_french": t["word_shown_french"],
            "is_prompt": 1,
            "is_mismatch": int(t["is_mismatch"]),
            "ITI_length": round(iti, 2),
            "correct_response": correct_resp,
            "nonmatch_pres_side": nonmatch_pres_side,
        })
    
    df = pd.DataFrame(rows)
    
    # Check mismatches per block
    for block_num in range(1, N_BLOCKS + 1):
        block_df = df[df["block"] == block_num]
        block_mismatches = int((block_df["is_mismatch"] == 1).sum())
        if block_mismatches != 5:
            raise RuntimeError(
                f"Block {block_num} has {block_mismatches} mismatches, expected exactly 5. "
                f"This indicates the hard constraint failed."
            )
    
    # Check mismatches per concept
    for c in concepts:
        concept_mismatches = int(((df["concept"] == c) & (df["is_mismatch"] == 1)).sum())
        if concept_mismatches != 2:
            raise RuntimeError(
                f"Concept '{c}' has {concept_mismatches} mismatches, expected exactly 2. "
                f"This indicates mismatch assignment failed."
            )
    
    # Validation & Summary 
    print_validation_summary(df, concepts, concept_to_num, ppt_id, N_POSITION_SEGMENTS)
    
    # Export
    df.to_excel(out_xlsx, index=False)
    print(f"Wrote {out_xlsx}")
    
    return df


def print_validation_summary(
    df: pd.DataFrame,
    concepts: List[str],
    concept_to_num: dict,
    ppt_id: str,
    n_segments: int
):
    """Print validation summary for participant."""
  
    
    print(f"\n  [SUMMARY for {ppt_id}]")
    print(f"    Total trials: {len(df)}")
    print(f"    Blocks: {N_BLOCKS} ({len(df)//N_BLOCKS} trials each)")
    
    
    # Check within-segment 
    print("\n  [WITHIN-BLOCK DISTRIBUTION]")
    trials_per_block = len(df) // N_BLOCKS
    segment_size = len(df) // n_segments
    
    segment_mismatch_counts = []
    for seg in range(n_segments):
        seg_start = seg * segment_size
        seg_end = (seg + 1) * segment_size if seg < n_segments - 1 else len(df)
        segment_df = df.iloc[seg_start:seg_end].reset_index(drop=True)
                
      
        seg_mismatches = int((segment_df["is_mismatch"] == 1).sum())
        segment_mismatch_counts.append(seg_mismatches)
        
        # Count concept distribution in segment
        concept_counts_in_segment = segment_df['concept'].value_counts().to_dict()
        
        # Count transitions in segment
        transitions_in_segment = Counter()
        for i in range(len(segment_df) - 1):
            trans = (segment_df.iloc[i]['concept'], segment_df.iloc[i+1]['concept'])
            transitions_in_segment[trans] += 1
        
        
        print(f"    Segment {seg}: ")
        print(f"      Mismatches: {seg_mismatches}")
        print("      Concepts: ", end="")
        concept_dist = [f"{c}:{concept_counts_in_segment.get(c, 0)}" for c in concepts]
        print(", ".join(concept_dist))
        
        # Transitions (show top transitions if any)
        if transitions_in_segment:
           trans_count_dist = Counter(transitions_in_segment.values())
           print(f"      Transitions ({len(transitions_in_segment)} unique): ", end="")
           dist_str = [f"{cnt}×({freq})" for cnt in sorted(trans_count_dist.keys()) 
                      for freq in [trans_count_dist[cnt]]]
           print(", ".join(dist_str))  # e.g., "1×(5), 2×(8), 3×(2)" means 5 transitions appear 1 time, 8 appear 2 times, etc.
   
    
    print("\n [PER-CONCEPT BREAKDOWN]")
    for concept in concepts:
        concept_df = df[df["concept"] == concept]
        concept_mismatches = int((concept_df["is_mismatch"] == 1).sum())
        concept_total = len(concept_df)
        concept_trigger = concept_to_num[concept]
        print(f"    {concept:12s} (trigger {concept_trigger:2d}): "
              f"{concept_total:3d} trials ({concept_mismatches:2d} mismatches)")


# ============================================================================
# main execution
# ============================================================================

if __name__ == "__main__":
    import argparse
    
    ap = argparse.ArgumentParser(description="Generate localizer conditions for TSRlearn")
    ap.add_argument("--n_participants", type=int, default=20)
    ap.add_argument("--out_dir", default=r"c:\sync_folder\TSRlearn-task\sequences_new")
    ap.add_argument("--learning_dir", default=r"c:\sync_folder\TSRlearn-task\sequences_new",
                    help="Directory containing learning condition files")
    args = ap.parse_args()
    
    os.makedirs(args.out_dir, exist_ok=True)
    
    
    # Initialize global counters
    global_counters = initialize_global_counters()
    
    for ppt in range(args.n_participants):
        ppt_id = f"{ppt:02d}"
        out_xlsx = os.path.join(args.out_dir, f"{base_name}_{ppt_id}.xlsx")
        learning_file = os.path.join(args.learning_dir, f"learning_blockB_fixed-middle-10_{ppt_id}.xlsx")
        
        try:
            df = build_localizer_for_participant(
                ppt_id=ppt_id,
                seed=SEED + ppt,
                out_xlsx=out_xlsx,
                global_counters=global_counters,
                learning_file=learning_file
            )
            
            # Update global counters after successful generation
            global_counters = update_global_counters(global_counters, df)
            
        except Exception as e:
            print(f"ERROR [Participant {ppt_id}]: {e}")
            continue
    
    # Save and print global balance report
    counters_file = os.path.join(args.out_dir, "global_balance_counters.json")
    save_global_counters(counters_file, global_counters)
    
    print_global_report(global_counters, args.n_participants, MIDDLE_10_FIXED)
    
    
    # ========================================================================
    # validation checks
    # ========================================================================
    
    print("CROSS-PARTICIPANT VALIDATION")
    
    # Load all dataframes
    dfs = []
    for ppt in range(args.n_participants):
        ppt_id = f"{ppt:02d}"
        xlsx_path = os.path.join(args.out_dir, f"{base_name}_{ppt_id}.xlsx")
        if os.path.exists(xlsx_path):
            dfs.append(pd.read_excel(xlsx_path))
    
    
    if not dfs:
        print("  No files to validate!")
    else:
        # Check 1: All participants have same trial count
        trial_counts = [len(df) for df in dfs]
        assert len(set(trial_counts)) == 1, "Participants have different trial counts"
        print(f"All participants have {trial_counts[0]} trials")
        
        # Check 2: All participants have same concept distribution
        for df in dfs:
            concept_counts = df['concept'].value_counts().to_dict()
            expected_count = N_EXEMPLARS_PER_CONCEPT
            for c in MIDDLE_10_FIXED:
                assert concept_counts[c] == expected_count, \
                    f"Concept {c} has {concept_counts[c]} trials, expected {expected_count}"
        print(f"All participants have {N_EXEMPLARS_PER_CONCEPT} trials per concept")
        
        # Check 3: All participants have same mismatch count
        mismatch_counts = [(df['is_mismatch'] == 1).sum() for df in dfs]
        assert len(set(mismatch_counts)) == 1, "Participants have different mismatch counts"
        print(f"All participants have {mismatch_counts[0]} mismatches")
        
        # Check 4: Per-concept mismatch distribution
        expected_mismatches_per_concept = int(round(MISMATCH_RATIO * N_EXEMPLARS_PER_CONCEPT))
        for df in dfs:
            for c in MIDDLE_10_FIXED:
                concept_mismatches = ((df['concept'] == c) & (df['is_mismatch'] == 1)).sum()
                assert concept_mismatches == expected_mismatches_per_concept, \
                    f"Concept {c} has {concept_mismatches} mismatches, expected {expected_mismatches_per_concept}"
        print(f"All concepts have {expected_mismatches_per_concept} mismatches per participant")
        
        # Check 5: Block structure
        for df in dfs:
            block_counts = df['block'].value_counts().to_dict()
            expected_block_size = len(df) // N_BLOCKS
            for block_num in range(1, N_BLOCKS + 1):
                assert block_counts[block_num] == expected_block_size, \
                    f"Block {block_num} has {block_counts[block_num]} trials, expected {expected_block_size}"
        print(f"All participants have {N_BLOCKS} blocks with {len(dfs[0])//N_BLOCKS} trials each")
        
        # Check 6: Concept streak validation
        max_streaks = []
        for df in dfs:
            streak = 1
            max_streak_found = 1
            for i in range(1, len(df)):
                if df.iloc[i]['concept'] == df.iloc[i-1]['concept']:
                    streak += 1
                    max_streak_found = max(max_streak_found, streak)
                else:
                    streak = 1
            max_streaks.append(max_streak_found)
        
        assert all(s <= MAX_STREAK for s in max_streaks), \
            f"Some participants exceed MAX_STREAK={MAX_STREAK}: {max_streaks}"
        print(f"No concept streaks exceed MAX_STREAK={MAX_STREAK}")
        
        # Check 7: Trigger number consistency
        for df in dfs:
            for c in MIDDLE_10_FIXED:
                trigger = df[df['concept'] == c]['concept_num'].iloc[0]
                expected_trigger = MIDDLE_10_FIXED.index(c) + 1
                assert trigger == expected_trigger, \
                    f"Concept {c} has trigger {trigger}, expected {expected_trigger}"
        print("Trigger numbers consistent across all participants (1-10)")
    
                
        
        # Check 8: post-mismatch transition balance
        print("\n  [POST-MISMATCH TRANSITION BALANCE]")
        print("    (Informational - checked at participant level)")
        
        # Count transitions after mismatches
        post_mismatch_image_trans = Counter()
        post_mismatch_word_trans = Counter()
        
        for i in range(1, len(df)):
            if df.iloc[i-1]['is_mismatch'] == 1:
                mismatch_image = df.iloc[i-1]['concept']
                mismatch_word = df.iloc[i-1]['word_shown_english']
                next_concept = df.iloc[i]['concept']
                
                post_mismatch_image_trans[(mismatch_image, next_concept)] += 1
                post_mismatch_word_trans[(mismatch_word, next_concept)] += 1
        
        if post_mismatch_image_trans:
            trans_counts = list(post_mismatch_image_trans.values())
            print(f"    Image→Next transitions: min={min(trans_counts)}, max={max(trans_counts)}, "
                  f"range={max(trans_counts)-min(trans_counts)}")
        if post_mismatch_word_trans:
            trans_counts = list(post_mismatch_word_trans.values())
            print(f"    Word→Next transitions: min={min(trans_counts)}, max={max(trans_counts)}, "
                  f"range={max(trans_counts)-min(trans_counts)}")
