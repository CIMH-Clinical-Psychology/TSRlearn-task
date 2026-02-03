"""
ENHANCED DISTRACTOR SELECTION WITH COMPREHENSIVE BALANCING:
1. Before/after direction balancing (per position)
2. Difficulty scoring (negative for before=harder, positive for after=easier)
3. dist01 (harder) vs dist02 (easier) selection
4. DISTANCE DIFFERENCE BALANCING 
5. DISTRACTOR POSITION BALANCING 
6. Minimum difficulty difference constraint 
7. Edge case detection and avoidance
"""

import random
from collections import Counter, defaultdict
from typing import List, Tuple, Dict
import numpy as np
import pandas as pd

# ============================================================================
# DIFFICULTY SCORING AND DIRECTION BALANCING
# ============================================================================

def get_difficulty_score(distance_from_current: int, is_before: bool) -> float:
    """
    Calculate difficulty score for a distractor.
    
    For BEFORE distractors (before current image):
      - Further distance = HARDER (negative score)
      - Example: distance 3 before → score = -3
    
    For AFTER distractors (after current image):
      - Further distance = EASIER (positive score)
      - Example: distance 3 after → score = +3
    
    Higher score = easier choice, lower score = harder choice
    """
    RECENCY_BONUS = 8.0  # How much easier "before" stimuli are
    
    if is_before:
        return -distance_from_current + RECENCY_BONUS  # ADD THE BONUS
    else:
        return +distance_from_current

def calculate_position_direction_targets(seq_length: int) -> Dict[int, Tuple[int, int]]:
    """
    For each position in sequence, calculate how many valid before/after candidates exist.
    
    Returns:
        {position: (before_count, after_count), ...}
    
    Example for 14-item sequence:
        pos 0: (0 before, 11 after)
        pos 4: (2 before, 9 after)
        pos 13: (11 before, 0 after)
    """
    targets = {}
    
    MIN_DISTANCE = 2  # Both before and after require distance >= 2
    
    for i in range(seq_length):
        # Count valid before candidates (must be >= distance 2)
        before_count = max(0, i - MIN_DISTANCE)
        
        # Count valid after candidates (must be >= distance 2)
        after_count = max(0, seq_length - (i + MIN_DISTANCE + 1))
        
        targets[i] = (before_count, after_count)
    
    return targets


def get_direction_preference(
    position: int,
    direction_usage: Dict[str, int],
    position_targets: Dict[int, Tuple[int, int]]
) -> Tuple[float, float]:
    """
    Calculate preference weights for before vs after at this position.
    
    Args:
        position: Current position in sequence
        direction_usage: {"before": count, "after": count} tracking usage so far
        position_targets: Results from calculate_position_direction_targets()
    
    Returns:
        (before_weight, after_weight) - higher weight = more preferred
    """
    before_available, after_available = position_targets[position]
    total_available = before_available + after_available
    
    if total_available == 0:
        return 0.0, 0.0
    
    # Expected proportions based on available candidates
    expected_before_prop = before_available / total_available if total_available > 0 else 0
    expected_after_prop = after_available / total_available if total_available > 0 else 0
    
    # Current usage totals
    total_used = direction_usage["before"] + direction_usage["after"]
    
    if total_used == 0:
        # No preferences yet, use available proportions
        return expected_before_prop, expected_after_prop
    
    current_before_prop = direction_usage["before"] / total_used
    current_after_prop = direction_usage["after"] / total_used
    
    # Prefer whichever direction is underrepresented
    before_deficit = expected_before_prop - current_before_prop
    after_deficit = expected_after_prop - current_after_prop
    
    # Convert deficits to weights (add 1 to ensure positive)
    before_weight = max(0.5, 1.0 + before_deficit * 2)
    after_weight = max(0.5, 1.0 + after_deficit * 2)
    
    # Normalize to sum to 2 (for compatibility)
    total = before_weight + after_weight
    before_weight = before_weight / total * 2
    after_weight = after_weight / total * 2
    
    return before_weight, after_weight


# ============================================================================
# DISTANCE DIFFERENCE BALANCING
# ============================================================================

def get_distance_diff_preference(
    distance_diff_usage: Dict[int, int],
    seq_length: int
) -> Dict[int, float]:
    """
     distance difference preference: Exponentially penalize overused diffs.
    """
    max_diff = seq_length - 1
    possible_diffs = set(range(1, max_diff + 1))
    
    if not distance_diff_usage:
        return {d: 1.0 for d in possible_diffs}
    
    usage_values = [distance_diff_usage.get(d, 0) for d in possible_diffs]
    avg_usage = np.mean(usage_values) if usage_values else 0
    
    weights = {}
    for diff in possible_diffs:
        usage = distance_diff_usage.get(diff, 0)
        
        if usage == 0:
            weights[diff] = 5.0  # 5x boost for unused (was 1.0)
        else:
            ratio = usage / max(1, avg_usage)
            if ratio < 0.5:
                weights[diff] = 3.0  # Strong boost for underused
            elif ratio < 1.0:
                weights[diff] = 1.8
            elif ratio < 1.5:
                weights[diff] = 0.6
            else:
                weights[diff] = 0.2 / (ratio - 0.5)  # Aggressive penalty
    
    return weights

# ============================================================================
# DISTRACTOR DISTANCE FROM CURRENT BALANCING
# ============================================================================

def get_distance_preference(
    distance_usage: Dict[int, int],
    seq_length: int
) -> Dict[int, float]:
    """
    AGGRESSIVE distance preference: Exponentially penalize overused distances.
    """
    MIN_DISTANCE = 2
    max_distance = seq_length - MIN_DISTANCE
    possible_distances = set(range(MIN_DISTANCE, max_distance + 1))
    
    if not distance_usage:
        return {d: 1.0 for d in possible_distances}
    
    usage_values = [distance_usage.get(d, 0) for d in possible_distances]
    avg_usage = np.mean(usage_values) if usage_values else 0
    
    weights = {}
    for dist in possible_distances:
        usage = distance_usage.get(dist, 0)
        
        if usage == 0:
            weights[dist] = 4.0  # 4x boost for completely unused (was 2.0)
        else:
            # EXPONENTIAL penalty for overuse
            ratio = usage / max(1, avg_usage)
            if ratio < 0.5:  # Underused (< 50% average)
                weights[dist] = 2.5  # Boost underused
            elif ratio < 1.0:  # Slightly underused
                weights[dist] = 1.5
            elif ratio < 1.5:  # At or slightly over average
                weights[dist] = 0.7
            else:  # Significantly overused (> 150% average)
                weights[dist] = 0.3 / (ratio - 1.0)  # Exponentially penalize
    
    return weights

# ============================================================================
# DISTRACTOR POSITION BALANCING
# ============================================================================

def get_position_preference(
    position: int,
    valid_positions: List[int],
    position_usage: Dict[int, int]
) -> Dict[int, float]:
    """
    Calculate preference weights for using each position as a distractor.
    
    Positions should be used equally often as distractors.
    
    Args:
        position: Current position (cannot be used as distractor)
        valid_positions: List of positions that can be used as distractors
        position_usage: {pos: count, ...} tracking how often each position used
    
    Returns:
        {pos: weight, ...} - higher weight = more preferred
    """
    if not valid_positions:
        return {}
    
    if not position_usage:
        # All valid positions equally preferred initially
        return {p: 1.0 for p in valid_positions}
    
    # Calculate average usage (only for valid positions)
    usage_of_valid = [position_usage.get(p, 0) for p in valid_positions]
    avg_usage = np.mean(usage_of_valid) if usage_of_valid else 0
    
    # Create weights: prefer underused positions
    weights = {}
    for pos in valid_positions:
        usage = position_usage.get(pos, 0)
        if usage == 0:
            weights[pos] = 2.0  # Strongly prefer unused
        else:
            weights[pos] = max(0.5, 1.0 / (usage / max(1, avg_usage)))
    
    return weights


# ============================================================================
# EDGE CASE DETECTION
# ============================================================================

def is_problematic_pair(
    dist01_idx: int,
    dist02_idx: int,
    current_idx: int,
    dist01_distance: int,
    dist02_distance: int,
    dist01_is_before: bool,
    dist02_is_before: bool,
    min_difficulty_difference: float = 1.0
) -> bool:
    """
    Detect edge cases where the pair might not provide good contrast.
    
    Edge cases:
    1. Both same distance but opposite directions (e.g., before-2 vs after-2)
       - These may not provide sufficient difficulty difference
    2. Same distance AND same direction (should not happen with current logic)
    3. Difficulty difference too small
    
    Returns:
        True if pair is problematic, False if acceptable
    """
    # Case 1: Same absolute distance, opposite directions
    #if (dist01_distance == dist02_distance and 
        #dist01_is_before != dist02_is_before):
        # This is problematic: -2 vs +2 provides only 4 points difference
        # but psychologically might not be meaningful
        # Consider requiring greater separation
        #return True
    
    # Case 2: Same distance and same direction (should not occur)
    if (dist01_distance == dist02_distance and 
        dist01_is_before == dist02_is_before):
        return True
    
    return False



def get_direction_preference_ULTRA(
    position: int,
    direction_usage: Dict[str, int],
    position_targets: Dict[int, Tuple[int, int]],
    total_selections: int
) -> Tuple[float, float]:
    """
    ULTRA version: Extremely aggressive direction balancing.
    
    Target: 50% before, 50% after
    If imbalanced, heavily penalize the overused direction
    """
    before_count = direction_usage.get("before", 0)
    after_count = direction_usage.get("after", 0)
    
    if total_selections == 0:
        # No preference yet
        before_weight, after_weight = get_direction_preference(
            position, direction_usage, position_targets
        )
        return before_weight, after_weight
    
    # Target: 50/50
    target_per_direction = total_selections / 2
    
    before_deviation = before_count - target_per_direction
    after_deviation = after_count - target_per_direction
    
    # Exponential penalty for overused direction
    if before_deviation > 0:
        # Before is overused: heavily penalize
        before_weight = 1.0 / (1.0 + before_deviation / max(1, target_per_direction) * 3)
    else:
        # Before is underused: boost
        before_weight = 1.0 + abs(before_deviation) / max(1, target_per_direction) * 3
    
    if after_deviation > 0:
        # After is overused: heavily penalize
        after_weight = 1.0 / (1.0 + after_deviation / max(1, target_per_direction) * 3)
    else:
        # After is underused: boost
        after_weight = 1.0 + abs(after_deviation) / max(1, target_per_direction) * 3
    
    # Normalize
    total = before_weight + after_weight
    before_weight = before_weight / total * 2
    
    return before_weight, after_weight


def select_two_distractors_ULTRA_BALANCE(
    seq: List[str],
    current_idx: int,
    rng: random.Random,
    exclude_indices: set = None,
    direction_usage: Dict[str, int] = None,
    difficulty_usage: List[float] = None,
    distance_diff_usage: Dict[int, int] = None,
    position_as_dist01_usage: Dict[int, int] = None,
    position_as_dist02_usage: Dict[int, int] = None,
    position_targets: Dict[int, Tuple[int, int]] = None,
    target_difficulty_mean: float = 0.0,
    target_difficulty_std: float = 3.0,  
    min_difficulty_difference: float = 1.0,
    distractor_coverage: set = None,
    coverage_weight: float = 0.50,
    dist01_distance_usage: Dict[int, int] = None, 
    dist02_distance_usage: Dict[int, int] = None,  
    debug: bool = False
) -> Tuple[int, int, Dict] | None:
    """
    ULTRA balancing: Aggressive search with strong enforcement.
    
    Key features:
    3.  enforces direction balance (50/50)
    4.  enforces difficulty mean (close to 0.0)
    5.  enforces position balance (but only for dist01?)
    """
    
    if exclude_indices is None:
        exclude_indices = set()
    if direction_usage is None:
        direction_usage = {"before": 0, "after": 0}
    if difficulty_usage is None:
        difficulty_usage = []
    if distance_diff_usage is None:
        distance_diff_usage = {}
    if position_as_dist01_usage is None:
        position_as_dist01_usage = {}
    if position_as_dist02_usage is None:
        position_as_dist02_usage = {}
    if position_targets is None:
        position_targets = calculate_position_direction_targets(len(seq))
    if distractor_coverage is None:
       distractor_coverage = set()
    if dist01_distance_usage is None:
        dist01_distance_usage = {}
    if dist02_distance_usage is None:
        dist02_distance_usage = {}
        
    MIN_DISTANCE = 2
    max_attempts = 150  # 
    
    # Total selections so far (for direction balance calculation)
    total_selections = direction_usage["before"] + direction_usage["after"]
    
    # Get ULTRA direction preferences
    before_weight, after_weight = get_direction_preference_ULTRA(
        current_idx, direction_usage, position_targets, total_selections
    )
    
    # Separate candidates
    before_candidates = []
    after_candidates = []
    
    for j in range(len(seq)):
        if j in exclude_indices or j == current_idx:
            continue
        
        distance = abs(j - current_idx)
        if distance < MIN_DISTANCE:
            continue
        
        if j < current_idx:
            before_candidates.append((j, distance, True))
        else:
            after_candidates.append((j, distance, False))
    
    if len(before_candidates) + len(after_candidates) < 2:
        if debug:
            print(f"  Insufficient candidates at pos {current_idx}")
        return None
    
    # Try to find a good pair
    for attempt in range(max_attempts):
        # Create weighted candidate pools
        weighted_pool = []
        
        for j, distance, is_before in before_candidates:
            weight_int = max(1, int(round(before_weight * 8)))  # Stronger weighting
            weighted_pool.extend([(j, distance, is_before)] * weight_int)
        
        for j, distance, is_before in after_candidates:
            weight_int = max(1, int(round(after_weight * 8)))  # Stronger weighting
            weighted_pool.extend([(j, distance, is_before)] * weight_int)
        
        if not weighted_pool:
            return None
        
        rng.shuffle(weighted_pool)
        
        # Try MANY dist01 options (400)
        for idx1_idx, (j1, dist1, is_before1) in enumerate(weighted_pool[:min(400, len(weighted_pool))]):
            difficulty1 = get_difficulty_score(dist1, is_before1)
            
            # Find best dist02
            best_dist02_info = None
            best_score = float('inf')
            
            for idx2_idx, (j2, dist2, is_before2) in enumerate(weighted_pool):
                if j2 == j1:
                    continue
                
                difficulty2 = get_difficulty_score(dist2, is_before2)
                
                # Constraint 1: dist01 must be harder
                if difficulty1 >= difficulty2:
                    continue
                
                # Constraint 2: Minimum difficulty difference
                diff_amount = difficulty2 - difficulty1
                if diff_amount < min_difficulty_difference:
                    continue
                
                # Constraint 3: Avoid edge cases
                if is_problematic_pair(
                    j1, j2, current_idx,
                    dist1, dist2,
                    is_before1, is_before2,
                    min_difficulty_difference
                ):
                    continue
                
                # Constraint 4: Enforce difficulty mean 
                new_difficulties = difficulty_usage + [difficulty1, difficulty2]
                new_mean = np.mean(new_difficulties)
                mean_deviation = abs(new_mean - target_difficulty_mean)
               
                # Strongly penalize if mean drifts too far
                if mean_deviation > 0.5:
                    # Too far from target, penalize heavily
                    continue
                
                # CONSTRAINT 4b: Enforce difficulty STD
                if len(new_difficulties) >= 50:  # Only check after 50+ trials
                    new_std = np.std(new_difficulties)
                    std_tolerance = target_difficulty_std * 0.50

                    std_deviation = abs(new_std - target_difficulty_std)
                    
                    if std_deviation > std_tolerance:
                        continue
                    
                # Constraint 5: Prefer dist02 positions that are underused 
                # Penalize using position 13 if it's already been used a lot
                # HARD CONSTRAINT: No position can be used > 1.5x average
                dist01_usage = position_as_dist01_usage.get(j1, 0)
                total_dist01_used = sum(position_as_dist01_usage.values())
                if total_dist01_used > 0:
                    target_dist01_per_pos = total_dist01_used / max(1, len(seq))
                    dist01_overuse = dist01_usage / max(1, target_dist01_per_pos)
                    if dist01_overuse > 1.5:  # change to 2.0?
                        continue
                
                # Also check dist02
                dist02_usage = position_as_dist02_usage.get(j2, 0)
                total_dist02_used = sum(position_as_dist02_usage.values())
                if total_dist02_used > 0:
                    target_dist02_per_pos = total_dist02_used / max(1, len(seq))
                    dist02_overuse = dist02_usage / max(1, target_dist02_per_pos)
                    if dist02_overuse > 1.5:  # Check BOTH now
                        continue
                
                # Prefer unused positions heavily
                dist02_pos_weight = 1.0 if dist02_usage == 0 else max(0.1, 1.0 / ((1.0 + dist02_usage) ** 2))
                
                # Also balance dist01 positions with exponential scoring
                dist01_pos_weight = 1.0 if dist01_usage == 0 else max(0.1, 1.0 / ((1.0 + dist01_usage) ** 2))
                
                # Apply coverage boost to dist01 as well
                if j1 not in distractor_coverage:
                    dist01_pos_weight *= (1.0 - coverage_weight)  # Boost by 10%
                    
                if j2 not in distractor_coverage:
                   dist02_pos_weight *= (1.0 - coverage_weight)  # Boost by 10%
                   
                # Constraint 6: Baöance distance between dist01 position and dist02 position
                # get weights based on uses of this distance already
                distance_diff_prefs = get_distance_diff_preference(distance_diff_usage, len(seq))
    
                # Calculate distance difference
                distance_diff = abs(dist2 - dist1)
                
                # get weight for this specific distance
                distance_diff_weight = distance_diff_prefs.get(distance_diff, 1.0)   
                
                # score, lower means more likely to be picked
                distance_diff_score = 1.0 / ((distance_diff_weight ** 2) + 0.001) 

                # Constraint 7: balance distance of distractors to current image
                # Get distance preferences
                dist01_distance_prefs = get_distance_preference(
                    dist01_distance_usage,
                    len(seq)
                )
                dist02_distance_prefs = get_distance_preference(
                    dist02_distance_usage,
                    len(seq)
                )
                
                # Get weights for this specific distance
                dist01_dist_weight = dist01_distance_prefs.get(dist1, 1.0)
                dist02_dist_weight = dist02_distance_prefs.get(dist2, 1.0)
                
                # Scoring: lower is better
                # Higher weight = much lower score = much preferred
                dist01_distance_score = 1.0 / ((dist01_dist_weight ** 2) + 0.001)
                dist02_distance_score = 1.0 / ((dist02_dist_weight ** 2) + 0.001)
                
                # OR use exponential directly
                #dist01_distance_score = np.exp(-dist01_dist_weight ** 2)
                #dist02_distance_score = np.exp(-dist02_dist_weight ** 2)
                
                # Combined score (weighted equally: 25% each)
                score = (distance_diff_score * 0.25 + 
                         dist02_pos_weight * 0.25 + 
                         dist01_distance_score * 0.25 + 
                         dist02_distance_score * 0.25)
                
                if score < best_score:
                    best_score = score
                    best_dist02_info = (j2, dist2, is_before2, difficulty2, distance_diff)
            
            if best_dist02_info is not None:
                j2, dist2, is_before2, difficulty2, distance_diff = best_dist02_info
                
                return (j1, j2), {
                    "dist01_direction": "before" if is_before1 else "after",
                    "dist02_direction": "before" if is_before2 else "after",
                    "dist01_difficulty": difficulty1,
                    "dist02_difficulty": difficulty2,
                    "dist01_distance": dist1,
                    "dist02_distance": dist2,
                    "distance_difference": distance_diff,
                    "dist01_idx": j1,
                    "dist02_idx": j2,
                }
    
    if debug:
        print(f"  Could not find valid pair at pos {current_idx} after {max_attempts} attempts")
    
    return None



# ============================================================================
# INTEGRATION HELPER - UPDATED
# ============================================================================

def prepare_distractor_selection_tracking(n_trials_expected: int, seq_length: int = 14) -> Dict:
    """
    Initialize tracking structures for a participant.
    
    Returns:
        dict with all tracking fields
    """
    return {
        "position_targets": calculate_position_direction_targets(seq_length),
        "direction_usage": {"before": 0, "after": 0},
        "difficulty_usage": [],
        "distance_diff_usage": {},
        "position_as_dist01_usage": {},
        "position_as_dist02_usage": {},
        "dist01_distance_usage": {},  
        "dist02_distance_usage": {},  
        "target_mean_difficulty": 0.0,
        "direction_history": [],
        "difficulty_history": [],
        "distance_diff_history": [],
        "dist01_distance_history": [],  
        "dist02_distance_history": [],  
    }


def update_distractor_tracking(tracking: Dict, selection_info: Dict):
    """Update tracking after successful selection."""
    tracking["direction_usage"][selection_info["dist01_direction"]] += 1
    tracking["direction_usage"][selection_info["dist02_direction"]] += 1
    
    tracking["difficulty_usage"].append(selection_info["dist01_difficulty"])
    tracking["difficulty_usage"].append(selection_info["dist02_difficulty"])
    
    # Track distance differences
    distance_diff = selection_info["distance_difference"]
    tracking["distance_diff_usage"][distance_diff] = tracking["distance_diff_usage"].get(distance_diff, 0) + 1
    
    # Track position usage as dist01 and dist02
    dist01_idx = selection_info["dist01_idx"]
    dist02_idx = selection_info["dist02_idx"]
    tracking["position_as_dist01_usage"][dist01_idx] = tracking["position_as_dist01_usage"].get(dist01_idx, 0) + 1
    tracking["position_as_dist02_usage"][dist02_idx] = tracking["position_as_dist02_usage"].get(dist02_idx, 0) + 1
    
    # Track absolute distances from current image
    dist01_distance = selection_info["dist01_distance"]
    dist02_distance = selection_info["dist02_distance"]
    tracking["dist01_distance_usage"][dist01_distance] = tracking["dist01_distance_usage"].get(dist01_distance, 0) + 1
    tracking["dist02_distance_usage"][dist02_distance] = tracking["dist02_distance_usage"].get(dist02_distance, 0) + 1
    
    tracking["direction_history"].append({
        "dist01": selection_info["dist01_direction"],
        "dist02": selection_info["dist02_direction"]
    })
    
    tracking["difficulty_history"].append({
        "dist01": selection_info["dist01_difficulty"],
        "dist02": selection_info["dist02_difficulty"]
    })
    
    tracking["distance_diff_history"].append(distance_diff)
    
    # Track distance histories
    tracking["dist01_distance_history"].append(dist01_distance)
    tracking["dist02_distance_history"].append(dist02_distance)


# ============================================================================
# VALIDATION - Keep original for now
# ============================================================================

def validate_distractor_difficulties(df_learning: pd.DataFrame, seqA: List[str], seqB: List[str], *, verbose=False) -> None:
    """Validates that dist01_difficulty < dist02_difficulty for all trials."""
    seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
    seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}
    
    violations = []
    
    for trial_idx, (_, row) in enumerate(df_learning.iterrows()):
        seq_name = row['learningSeq']
        seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup
        
        prompt_idx = seq_lookup[row['promptConcept']]
        dist01_idx = seq_lookup[row['dist01Concept']]
        dist02_idx = seq_lookup[row['dist02Concept']]
        
        dist01_distance = abs(dist01_idx - prompt_idx)
        dist02_distance = abs(dist02_idx - prompt_idx)
        dist01_is_before = dist01_idx < prompt_idx
        dist02_is_before = dist02_idx < prompt_idx
        
        dist01_difficulty = get_difficulty_score(dist01_distance, dist01_is_before)
        dist02_difficulty = get_difficulty_score(dist02_distance, dist02_is_before)
        
        if dist01_difficulty >= dist02_difficulty:
            violations.append({
                'trial': trial_idx,
                'seq': seq_name,
                'dist01_difficulty': dist01_difficulty,
                'dist02_difficulty': dist02_difficulty,
            })
    
    if violations:
        print(f"\n{'='*70}")
        print(f"DISTRACTOR DIFFICULTY VALIDATION FAILED")
        print(f"{'='*70}")
        print(f"Found {len(violations)}/{len(df_learning)} violations\n")
        raise AssertionError(
            f"Distractor difficulty constraint violated in {len(violations)}/{len(df_learning)} trials."
        )
    
    if verbose:
        print(f"✓ PASS: All {len(df_learning)} trials satisfy dist01_difficulty < dist02_difficulty")


# ============================================================================
# REPORTING
# ============================================================================

def print_distractor_selection_report(tracking: Dict, participant_id: str):
    """Print comprehensive report on all balancing constraints."""
    print(f"\n{'='*70}")
    print(f"Distractor Selection Report - Participant {participant_id}")
    print(f"{'='*70}")
    
    # Direction usage
    total_distractors = tracking["direction_usage"]["before"] + tracking["direction_usage"]["after"]
    before_pct = (tracking["direction_usage"]["before"] / total_distractors * 100) if total_distractors > 0 else 0
    after_pct = (tracking["direction_usage"]["after"] / total_distractors * 100) if total_distractors > 0 else 0
    
    print(f"\n1. Direction Usage:")
    print(f"   Before (harder): {tracking['direction_usage']['before']:3d} ({before_pct:5.1f}%)")
    print(f"   After (easier):  {tracking['direction_usage']['after']:3d} ({after_pct:5.1f}%)")
    
    # Difficulty distribution
    if tracking["difficulty_usage"]:
        difficulties = np.array(tracking["difficulty_usage"])
        print(f"\n2. Difficulty Distribution:")
        print(f"   Mean:     {np.mean(difficulties):+7.2f} (target: 0.00)")
        print(f"   Std Dev:  {np.std(difficulties):7.2f}")
        print(f"   Min:      {np.min(difficulties):+7.2f}")
        print(f"   Max:      {np.max(difficulties):+7.2f}")
    
    # Distance difference balance
    if tracking["distance_diff_usage"]:
        print(f"\n3. Distance Difference Balance :")
        print(f"   Possible differences: {sorted(tracking['distance_diff_usage'].keys())}")
        for diff in sorted(tracking["distance_diff_usage"].keys()):
            count = tracking["distance_diff_usage"][diff]
            pct = (count / len(tracking["distance_diff_history"]) * 100) if tracking["distance_diff_history"] else 0
            print(f"   Diff {diff:2d}: {count:3d} ({pct:5.1f}%)")
        
        # Check balance
        usage_vals = list(tracking["distance_diff_usage"].values())
        balance_ratio = max(usage_vals) / min(usage_vals) if usage_vals and min(usage_vals) > 0 else float('inf')
        print(f"   Balance ratio (max/min): {balance_ratio:.2f} (target: <1.3)")
    
    # Position as dist01 balance
    if tracking["position_as_dist01_usage"]:
        print(f"\n4. Position Usage as dist01:")
        usage_vals = list(tracking["position_as_dist01_usage"].values())
        print(f"   Positions used: {sorted(tracking['position_as_dist01_usage'].keys())}")
        print(f"   Mean usage: {np.mean(usage_vals):.1f}")
        print(f"   Min usage: {min(usage_vals)}")
        print(f"   Max usage: {max(usage_vals)}")
        balance_ratio = max(usage_vals) / min(usage_vals) if usage_vals and min(usage_vals) > 0 else float('inf')
        print(f"   Balance ratio (max/min): {balance_ratio:.2f} (target: <1.3)")
    
    # Position as dist02 balance
    if tracking["position_as_dist02_usage"]:
        print(f"\n5. Position Usage as dist02:")
        usage_vals = list(tracking["position_as_dist02_usage"].values())
        print(f"   Positions used: {sorted(tracking['position_as_dist02_usage'].keys())}")
        print(f"   Mean usage: {np.mean(usage_vals):.1f}")
        print(f"   Min usage: {min(usage_vals)}")
        print(f"   Max usage: {max(usage_vals)}")
        balance_ratio = max(usage_vals) / min(usage_vals) if usage_vals and min(usage_vals) > 0 else float('inf')
        print(f"   Balance ratio (max/min): {balance_ratio:.2f} (target: <1.3)")
    
    # dist01 vs dist02 comparison
    if tracking["difficulty_history"]:
        dist01_diffs = [d["dist01"] for d in tracking["difficulty_history"]]
        dist02_diffs = [d["dist02"] for d in tracking["difficulty_history"]]
        
        print(f"\n6. dist01 vs dist02 Comparison:")
        print(f"   dist01 (harder) mean:  {np.mean(dist01_diffs):+7.2f}")
        print(f"   dist02 (easier) mean:  {np.mean(dist02_diffs):+7.2f}")
        print(f"   Difference mean:       {np.mean(np.array(dist02_diffs) - np.array(dist01_diffs)):+7.2f}")
        
        violations = sum(1 for d1, d2 in zip(dist01_diffs, dist02_diffs) if d1 >= d2)
        print(f"   Constraint violations: {violations}/{len(dist01_diffs)}")
        
    #  Distance balance for dist01
    if tracking["dist01_distance_usage"]:
        print(f"\n6. dist01 Distance Balance:")
        print(f"   Distances used: {sorted(tracking['dist01_distance_usage'].keys())}")
        usage_vals = list(tracking["dist01_distance_usage"].values())
        print(f"   Mean usage: {np.mean(usage_vals):.1f}")
        print(f"   Min usage: {min(usage_vals)}")
        print(f"   Max usage: {max(usage_vals)}")
        balance_ratio = max(usage_vals) / min(usage_vals) if usage_vals and min(usage_vals) > 0 else float('inf')
        print(f"   Balance ratio (max/min): {balance_ratio:.2f} (target: <1.3)")
    
    # Distance balance for dist02
    if tracking["dist02_distance_usage"]:
        print(f"\n7. dist02 Distance Balance):")
        print(f"   Distances used: {sorted(tracking['dist02_distance_usage'].keys())}")
        usage_vals = list(tracking["dist02_distance_usage"].values())
        print(f"   Mean usage: {np.mean(usage_vals):.1f}")
        print(f"   Min usage: {min(usage_vals)}")
        print(f"   Max usage: {max(usage_vals)}")
        balance_ratio = max(usage_vals) / min(usage_vals) if usage_vals and min(usage_vals) > 0 else float('inf')
        print(f"   Balance ratio (max/min): {balance_ratio:.2f} (target: <1.3)")
    
    print(f"{'='*70}")