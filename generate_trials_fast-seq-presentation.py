"""
Generate fast_seq_presentation Excel files with SHUFFLED, BALANCED image selection.

Core requirements:
- Use middle 10 images from each learned sequence (positions 2-11)
- For each trial: randomly select 5 images from these 10
- Constraint 1: Valid presentation order - consecutive images in presentation cannot be 
  1 or 2 steps apart in the ORIGINAL SEQUENCE (forward direction only, backward is okay)
- Constraint 2: Balance image selection - each image appears 30 times across 60 trials
- Constraint 3: Balance probe position - each position asked about 12 times across 60 trials

Each row contains: 5 selected images (in valid presentation order), their trigger numbers, 
6 masks (mask_0 through mask_5), probe position, and prompt_image
Structure: 60 rows total (30 repetitions × 2 sequences, interleaved A, B, A, B, ...)

Columns: repetition, sequence,
         fast_img_1...fast_img_5 (selected image paths in valid presentation order),
         fast_img_1_trig...fast_img_5_trig (trigger numbers),
         mask_0_img, mask_1_img...mask_5_img (mask paths, randomly selected from mask_0 to mask_28),
         probe_position (1-5, which position to ask about),
         prompt_image (image directory for the image to ask about)


"""

import pandas as pd
import numpy as np
import os
from pathlib import Path
import random

# ============================================================================
# settings
# ============================================================================

LEARNING_FILE_PATH = r"c:\sync_folder\TSRlearn-task\sequences_new"
OUTPUT_DIR = r"c:\sync_folder\TSRlearn-task\sequences_new"
N_PARTICIPANTS = 20
N_REPETITIONS = 30
SEED_BASE = 42

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


def _build_concept_to_trigger_map():
    """Create mapping of all concepts to trigger numbers."""
    mapping = {}
    for idx, concept in enumerate(MIDDLE_10_FIXED):
        mapping[concept] = idx + 1

    return mapping

CONCEPT_TO_TRIGGER = _build_concept_to_trigger_map()


def _concept_from_path(path: str) -> str:
    """Extract concept name from file path like 'stimuli/bird/bird_01.jpg'"""
    if not path:
        return ""
    parts = path.split("/")
    if len(parts) >= 2:
        return parts[-2]
    return ""


def extract_sequences_from_learning_block(learning_file_path):
    """
    Extract sequences A and B from learning_blockB Excel file.
    Returns full 14-image sequences (for reference) and middle 10 images.
    """
    df = pd.read_excel(learning_file_path)
    
    seqA_run1 = df[(df['learningSeq'] == 'A') & (df['runIndexWithinSeq'] == 1)].sort_values('currPosInSeq')
    seqB_run1 = df[(df['learningSeq'] == 'B') & (df['runIndexWithinSeq'] == 1)].sort_values('currPosInSeq')
    
    # Get full sequences (images 1-13 from promptFile, image 14 from correctFile)
    seq_a_full = seqA_run1['promptFile'].tolist()
    seq_b_full = seqB_run1['promptFile'].tolist()
    
    seq_a_full.append(seqA_run1[seqA_run1['currPosInSeq'] == 13]['correctFile'].values[0])
    seq_b_full.append(seqB_run1[seqB_run1['currPosInSeq'] == 13]['correctFile'].values[0])
    
    # Extract middle 10 images
    seq_a_middle_10 = seq_a_full[2:12]
    seq_b_middle_10 = seq_b_full[2:12]
    
    return {
        'seq_a_full': seq_a_full,
        'seq_b_full': seq_b_full,
        'seq_a_middle_10': seq_a_middle_10,
        'seq_b_middle_10': seq_b_middle_10,
        'num_masks': 6
    }


def generate_mask_images(num_masks):
    """Generate list of mask image paths (0-indexed, so mask_0 through mask_x)."""
    return [f"stimuli/mask_images/mask_{i:02d}.png" for i in range(0, num_masks)]


def get_forbidden_forward_transitions(sequence_length=10):
    """
    Get indices of forbidden FORWARD transitions (1-step and 2-step in forward direction only).
    
    For presentation, from position i, we cannot go to position i+1 or i+2.
    (backward is okay, e.g., from i to i-1 or i-2)
    
    Returns set of frozensets for bidirectional checking in the backward direction,
    but as ordered tuples for forward direction.
    """
    forbidden_forward = set()
    
    # Forward transitions: from i, cannot go to i+1 or i+2
    for i in range(sequence_length - 2):
        forbidden_forward.add((i, i+1))  # 1-step forward
        forbidden_forward.add((i, i+2))  # 2-step forward
    
    return forbidden_forward


def find_valid_presentation_order(selected_indices, forbidden_forward_pairs):
    """
    Find a valid presentation order for 5 selected images.
    
    Constraint: consecutive images in presentation cannot have forward-distance of 1 or 2
    (backward distances are okay).

    selected_indices: list of 5 indices from the original 10-image sequence
    forbidden_forward_pairs: set of (from_idx, to_idx) forbidden forward transitions
    
    Returns valid ordering (list) or None if no valid ordering exists.
    """
    selected_set = set(selected_indices)
    
    def backtrack(ordering, remaining):
        """find valid sequenc eof images by always checking for each transition if its allowed"""
        if not remaining:
            return ordering  # no image remaining, found valid sequence
        
        last_idx = ordering[-1]
        
        # Try each remaining image
        for next_idx in remaining:
            if (last_idx, next_idx) not in forbidden_forward_pairs:
                # Valid transition, re-start function to check next position
                result = backtrack(
                    ordering + [next_idx],
                    remaining - {next_idx}
                )
                if result:
                    return result
        
        return None  # No valid continuation from this state
    
    # Try starting from each image
    for start_idx in selected_set:
        remaining = selected_set - {start_idx}
        result = backtrack([start_idx], remaining)
        if result:
            return result
    
    return None  # No valid ordering exists for this combination


def select_balanced_image_combinations(n_trials=60, n_images=10, selection_size=5, 
                                       forbidden_forward_pairs=None, seed=None):
    """
    Select n_trials combinations of selection_size images from n_images total.
    
    Constraint 1: Balance image distribution - each image appears equally across all trials.
    Constraint 2: Each combo must have a valid presentation order (if forbidden_forward_pairs provided).
    
    Returns list of n_trials combinations (as tuples of indices) and image counts.
    """
    if seed is not None:
        random.seed(seed)
    
    selected = []
    image_counts = {i: 0 for i in range(n_images)}
    combos_requiring_resampling = 0
    
    for trial in range(n_trials):
        best_combo = None
        best_score = float('inf')
        
        # Sample many candidates and pick the best valid one
        sample_size = 10000 if forbidden_forward_pairs else 1000
        for attempt in range(sample_size):
            
            # always pick random subset of 5 images
            combo = tuple(sorted(random.sample(range(n_images), selection_size)))
            
            # check that this combo has a valid ordering
            if forbidden_forward_pairs is not None:
                ordering = find_valid_presentation_order(combo, forbidden_forward_pairs)
                if ordering is None:
                    # This combo has no possible valid ordering, skip it
                    continue
            
            # Score based on balance: prefer combos that keep image counts balanced
            temp_counts = image_counts.copy()
            for img_idx in combo:
                temp_counts[img_idx] += 1
            
            max_count = max(temp_counts.values())
            min_count = min(temp_counts.values())
            balance_score = max_count - min_count
            
            if balance_score < best_score:
                best_score = balance_score
                best_combo = combo
        
        if best_combo is None:
            # Could not find ANY valid combo after many samples
            raise ValueError(
                f"Trial {trial}: Could not find a valid combo with valid ordering after "
                f"{sample_size} samples. This suggests the constraint set may be too restrictive."
            )
        
        selected.append(best_combo)
        for img_idx in best_combo:
            image_counts[img_idx] += 1
    
    # Verify balance
    counts = list(image_counts.values())
    if max(counts) - min(counts) > 1:
        print(f"  Warning: Image count distribution not perfectly balanced: {image_counts}")
    
    return selected, image_counts



def select_balanced_probe_positions(n_trials=60, n_positions=5, seed=None):
    """
    Select which position (1-5) to probe on each trial, balanced across all trials.
    
    Each position appears n_trials / n_positions times.
    Returns list of n_trials position selections (1-indexed).
    """
    if seed is not None:
        random.seed(seed)
    
    # Create balanced list: each position appears exactly n_trials/n_positions times
    positions = list(range(1, n_positions + 1)) * (n_trials // n_positions)
    random.shuffle(positions)
    
    return positions


def create_fast_seq_shuffled_balanced(seq_a_middle_10, seq_b_middle_10, num_masks=6, 
                                      n_repetitions=30, seed=None):
    """
    Create DataFrame with one row per trial.
    
    Each row contains 5 selected images (from 10 middle images) in a valid presentation order,
    their trigger numbers, 6 masks (mask_0 through mask_5), and a probe position.
    
    Constraints:
    - Balanced image selection (each image appears 30 times across 60 trials)
    - Valid presentation order (consecutive images cannot be 1 or 2 steps apart in original 
      sequence, forward direction only - backward is okay)
    - Balanced probe positions (each position 1-5 is selected 12 times)
    
    Design: Interleaved sequences (images from A, B, A, B, ...)
    Total: n_repetitions × 2 sequences)
    
    """
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)
    
    # Build forbidden forward transitions
    forbidden_forward = get_forbidden_forward_transitions(sequence_length=10)
    print(f"  Forbidden forward transitions: {len(forbidden_forward)}")
    
    n_trials = n_repetitions * 2  # A and B sequences
    
    # Select balanced image combinations that have valid orderings
    selected_combos, image_counts = select_balanced_image_combinations(
        n_trials=n_trials, n_images=10, selection_size=5, 
        forbidden_forward_pairs=forbidden_forward,
        seed=seed
    )
    print(f"  Image counts across trials: {image_counts}")
    
    # Find valid presentation orders for each combination
    # (We're guaranteed these will succeed since we filtered during selection)
    presentation_orders = []
    
    for trial_idx, combo in enumerate(selected_combos):
        ordering = find_valid_presentation_order(combo, forbidden_forward)
        
        if ordering is None:
       
            raise RuntimeError(
                f"Trial {trial_idx}: Combo {combo} passed selection but has no valid ordering. "
                "This indicates a logic error."
            )
        
        presentation_orders.append(ordering)
    
    # Select balanced probe positions
    probe_positions = select_balanced_probe_positions(n_trials=n_trials, n_positions=5, seed=seed)
    print(f"  Probe position distribution: {np.bincount(probe_positions)[1::]}")
    
    mask_images = generate_mask_images(num_masks)
    data = []
    
    # Alternate between sequence A and B for n_repetitions each
    sequences = [seq_a_middle_10, seq_b_middle_10] * n_repetitions
    sequence_names = ['A', 'B'] * n_repetitions
    
    for rep_idx, (seq_images, seq_name, ordering, probe_pos) in enumerate(
        zip(sequences, sequence_names, presentation_orders, probe_positions)
    ):
        
        # Calculate repetition number (1-30 for each sequence)
        rep_num = (rep_idx // 2) + 1
        
        # Create one row with 5 selected images (in valid presentation order)
        row = {
            'repetition': rep_num,
            'sequence': seq_name,
            'probe_position': probe_pos,
        }
        
        # Select 5 images in presentation order
        selected_images = [seq_images[idx] for idx in ordering]
        
        # Add 5 image columns with trigger numbers (in presentation order)
        for position, img_path in enumerate(selected_images, 1):
            col_name = f'fast_img_{position}'
            row[col_name] = img_path
            
            concept = _concept_from_path(img_path)
            trigger_num = CONCEPT_TO_TRIGGER.get(concept, 0)
            trig_col_name = f'fast_img_{position}_trig'
            row[trig_col_name] = trigger_num
        
        # Add mask_0 column (randomly selected from mask_0 to mask_5)
        random.shuffle(mask_images)
        mask_file_idx = np.random.randint(0, len(mask_images))
        row['mask_0_img'] = mask_images[mask_file_idx]
        
        # Add mask_1 through mask_5 columns (randomly selected)
        for mask_idx in range(num_masks):
            mask_file = mask_images[mask_idx]
            col_name = f'mask_{mask_idx}_img'
            row[col_name] = mask_file
        
        # Add prompt_image column: the actual image path at the probe position
        prompt_img_path = selected_images[probe_pos - 1]  # probe_pos is 1-indexed
        row['prompt_image'] = prompt_img_path
        data.append(row)
    
    return pd.DataFrame(data)


def main(learning_file_path, output_path, n_repetitions=30, seed=42):
    """Process single file and generate Excel."""
    
    if not os.path.exists(learning_file_path):
        raise FileNotFoundError(f"Learning file not found: {learning_file_path}")
    
    sequences = extract_sequences_from_learning_block(learning_file_path)
    
    if len(sequences['seq_a_middle_10']) != 10:
        raise ValueError(f"Sequence A middle-10 has {len(sequences['seq_a_middle_10'])} images, expected 10")
    if len(sequences['seq_b_middle_10']) != 10:
        raise ValueError(f"Sequence B middle-10 has {len(sequences['seq_b_middle_10'])} images, expected 10")
    
    output_df = create_fast_seq_shuffled_balanced(
        sequences['seq_a_middle_10'],
        sequences['seq_b_middle_10'],
        sequences['num_masks'],
        n_repetitions=n_repetitions,
        seed=seed
    )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    output_df.to_excel(output_path, index=False)
    
    return {
        'success': True,
        'output_path': output_path,
        'total_rows': len(output_df),
        'description': f'Shuffled balanced selection: 5 images per trial from middle-10, {n_repetitions} reps per sequence'
    }


if __name__ == '__main__':
    
    
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    success_count = 0
    error_count = 0
    
    for ppt in range(N_PARTICIPANTS):
        ppt_id = f"{ppt:02d}"
        
        learning_file = os.path.join(
            LEARNING_FILE_PATH,
            f"learning_blockB_fixed-middle-10_{ppt_id}.xlsx"
        )
        out_xlsx = os.path.join(OUTPUT_DIR, f"fastseq_conditions_{ppt_id}.xlsx")
        
        try:
            print(f"[{ppt_id}] Processing...")
            result = main(learning_file, out_xlsx, n_repetitions=N_REPETITIONS, seed=SEED_BASE + ppt)
            print(f"{result['total_rows']} rows, 20 columns")
            success_count += 1
        except FileNotFoundError:
            print(f"File not found: {learning_file}")
            error_count += 1
            continue
        except Exception as e:
            print(f"Error: {e}")
            error_count += 1
            continue
    
    print(f"  Successfully processed: {success_count}/{N_PARTICIPANTS}")
    print(f"  Errors: {error_count}/{N_PARTICIPANTS}")
