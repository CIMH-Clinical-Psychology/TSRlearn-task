"""
ENHANCED DISTRACTOR SELECTION WITH COMPREHENSIVE BALANCING
===========================================================

Hard constraints:
  H1. dist01 harder than dist02 (difficulty1 > difficulty2)
  H2. Minimum difficulty difference between dist01 and dist02
  H3. No same-role concept repeat on consecutive trials
  H4. No same-distance same-direction pair
  H5. Position overuse cap (2.8x average)
  H6. Per-route difficulty mean (after >=6 trials)
  H7. Per-route difficulty SD (after >=6 trials)
  H8. Per-route difficulty-difference mean (after >=6 trials)

Soft constraints (scored):
  S1. Position-relative direction balance (per position, per role, across runs)
  S2. Distance-to-current balance (per role)
  S3. Distance-difference balance
  S4. Position-as-distractor balance (per role)
"""

import random
from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Optional
import numpy as np
import pandas as pd


# ============================================================================
# DIFFICULTY SCORING
# ============================================================================

def get_difficulty_score(distance_from_current: int, is_before: bool) -> float:
    """
    Lower score = easier, higher score = harder (0 = very easy, 1 = very hard).
    BEFORE distractors: linear increase with distance, primacy drop at 12-13.
    AFTER  distractors: linear — closer = harder, further = easier.
    """
    if is_before:
        dist = abs(distance_from_current)
        if dist <= 11:
            # Linear: dist 2 → 0.0, dist 11 → 1.0
            return round(max(0.0, (dist - 2) / 9.0), 1)
        elif dist == 12:
            return 0.1
        else:  # dist >= 13
            return 0.0
    else:
        return round(max(0.0, min(1.0, 1.0 - (distance_from_current - 2) / 11)), 1)


# ============================================================================
# POSITION-RELATIVE DIRECTION TARGETS
# ============================================================================

MIN_DISTANCE = 2

def calculate_position_direction_targets(seq_length: int) -> Dict[int, Tuple[int, int]]:
    targets = {}
    for i in range(seq_length):
        before_count = max(0, i - MIN_DISTANCE)
        after_count = max(0, seq_length - (i + MIN_DISTANCE + 1))
        targets[i] = (before_count, after_count)
    return targets


def get_position_relative_before_fraction(position: int, position_targets: Dict[int, Tuple[int, int]]) -> float:
    before_count, after_count = position_targets[position]
    total = before_count + after_count
    if total == 0:
        return 0.0
    return before_count / total


# ============================================================================
# TRACKING STRUCTURES
# ============================================================================

def prepare_distractor_selection_tracking(n_trials_expected: int, seq_length: int = 14) -> Dict:
    """Initialize ALL tracking structures for a participant."""
    return {
        "position_targets": calculate_position_direction_targets(seq_length),
        "direction_usage": {"before": 0, "after": 0},
        "difficulty_usage": [],
        "distance_diff_usage": {},
        "position_as_dist01_usage": {},
        "position_as_dist02_usage": {},
        "dist01_distance_usage": {},
        "dist02_distance_usage": {},
        "position_direction_usage": defaultdict(lambda: {
            "dist01_before": 0, "dist01_after": 0,
            "dist02_before": 0, "dist02_after": 0,
        }),
        "current_route_dist01_difficulties": [],
        "current_route_dist02_difficulties": [],
        "current_route_difficulty_diffs": [],
        "route_dist01_means": [],
        "route_dist02_means": [],
        "route_dist01_stds": [],
        "route_dist02_stds": [],
        "route_diff_means": [],
        "direction_history": [],
        "difficulty_history": [],
        "distance_diff_history": [],
        "dist01_distance_history": [],
        "dist02_distance_history": [],
        "difficulty_diff_list": [],
        "target_mean_difficulty": 0.5,
    }


def reset_route_tracking(tracking: Dict):
    """Call at the START of each new route to reset per-route accumulators."""
    tracking["current_route_dist01_difficulties"] = []
    tracking["current_route_dist02_difficulties"] = []
    tracking["current_route_difficulty_diffs"] = []


def finalize_route_tracking(tracking: Dict):
    """Call at the END of each route to record route-level stats."""
    d1 = tracking["current_route_dist01_difficulties"]
    d2 = tracking["current_route_dist02_difficulties"]
    diffs = tracking["current_route_difficulty_diffs"]
    if d1:
        tracking["route_dist01_means"].append(np.mean(d1))
        tracking["route_dist01_stds"].append(np.std(d1))
    if d2:
        tracking["route_dist02_means"].append(np.mean(d2))
        tracking["route_dist02_stds"].append(np.std(d2))
    if diffs:
        tracking["route_diff_means"].append(np.mean(diffs))


def update_distractor_tracking(tracking: Dict, selection_info: Dict):
    """Update all tracking after a successful selection."""
    d1_dir = selection_info["dist01_direction"]
    d2_dir = selection_info["dist02_direction"]
    tracking["direction_usage"][d1_dir] += 1
    tracking["direction_usage"][d2_dir] += 1
    pos = selection_info["current_position"]
    tracking["position_direction_usage"][pos][f"dist01_{d1_dir}"] += 1
    tracking["position_direction_usage"][pos][f"dist02_{d2_dir}"] += 1
    tracking["difficulty_usage"].append(selection_info["dist01_difficulty"])
    tracking["difficulty_usage"].append(selection_info["dist02_difficulty"])
    tracking["current_route_dist01_difficulties"].append(selection_info["dist01_difficulty"])
    tracking["current_route_dist02_difficulties"].append(selection_info["dist02_difficulty"])
    pair_diff = abs(selection_info["dist01_difficulty"] - selection_info["dist02_difficulty"])
    tracking["current_route_difficulty_diffs"].append(pair_diff)
    tracking["difficulty_diff_list"].append(pair_diff)
    distance_diff = selection_info["distance_difference"]
    tracking["distance_diff_usage"][distance_diff] = tracking["distance_diff_usage"].get(distance_diff, 0) + 1
    tracking["distance_diff_history"].append(distance_diff)
    d1_idx = selection_info["dist01_idx"]
    d2_idx = selection_info["dist02_idx"]
    tracking["position_as_dist01_usage"][d1_idx] = tracking["position_as_dist01_usage"].get(d1_idx, 0) + 1
    tracking["position_as_dist02_usage"][d2_idx] = tracking["position_as_dist02_usage"].get(d2_idx, 0) + 1
    d1_dist = selection_info["dist01_distance"]
    d2_dist = selection_info["dist02_distance"]
    tracking["dist01_distance_usage"][d1_dist] = tracking["dist01_distance_usage"].get(d1_dist, 0) + 1
    tracking["dist02_distance_usage"][d2_dist] = tracking["dist02_distance_usage"].get(d2_dist, 0) + 1
    tracking["dist01_distance_history"].append(d1_dist)
    tracking["dist02_distance_history"].append(d2_dist)
    tracking["direction_history"].append({"dist01": d1_dir, "dist02": d2_dir})
    tracking["difficulty_history"].append({
        "dist01": selection_info["dist01_difficulty"],
        "dist02": selection_info["dist02_difficulty"]
    })


# ============================================================================
# SCORING HELPERS
# ============================================================================

def _overuse_ratio(usage_dict: Dict[int, int], key: int, n_keys: int) -> float:
    total = sum(usage_dict.values())
    if total == 0:
        return 0.0
    avg = total / max(1, n_keys)
    return usage_dict.get(key, 0) / max(1e-9, avg)


def _balance_weight(usage_dict: Dict[int, int], key: int, n_keys: int) -> float:
    usage = usage_dict.get(key, 0)
    if usage == 0:
        return 4.0
    total = sum(usage_dict.values())
    if total == 0:
        return 1.0
    avg = total / max(1, n_keys)
    ratio = usage / avg
    if ratio < 0.5:
        return 3.0
    elif ratio < 1.0:
        return 1.5
    elif ratio < 1.5:
        return 0.7
    else:
        return max(0.05, 0.3 / (ratio - 0.5))


def _direction_score_for_candidate(
    is_before: bool, role: str, current_position: int, tracking: Dict,
) -> float:
    position_targets = tracking["position_targets"]
    target_before_frac = get_position_relative_before_fraction(current_position, position_targets)
    target_after_frac = 1.0 - target_before_frac
    pos_usage = tracking["position_direction_usage"][current_position]
    role_before = pos_usage[f"{role}_before"]
    role_after = pos_usage[f"{role}_after"]
    role_total = role_before + role_after
    if role_total == 0:
        return target_before_frac if is_before else target_after_frac
    current_before_frac = role_before / role_total
    if is_before:
        deficit = target_before_frac - current_before_frac
    else:
        deficit = target_after_frac - (1.0 - current_before_frac)
    weight = max(0.1, 1.0 + deficit * 4.0)
    return weight


# ============================================================================
# EDGE CASE DETECTION
# ============================================================================

def is_problematic_pair(
    dist01_distance: int, dist02_distance: int,
    dist01_is_before: bool, dist02_is_before: bool,
) -> bool:
    return (dist01_distance == dist02_distance and
            dist01_is_before == dist02_is_before)


# ============================================================================
# MAIN SELECTION FUNCTION
# ============================================================================

def select_two_distractors_ULTRA_BALANCE(
    seq: List[str],
    current_idx: int,
    rng: random.Random,
    exclude_indices: set = None,
    direction_usage: Dict[str, int] = None,
    distance_diff_usage: Dict[int, int] = None,
    position_as_dist01_usage: Dict[int, int] = None,
    position_as_dist02_usage: Dict[int, int] = None,
    position_targets: Dict[int, Tuple[int, int]] = None,
    min_difficulty_difference: float = 0.2,
    distractor_coverage: set = None,
    coverage_weight: float = 0.50,
    dist01_distance_usage: Dict[int, int] = None,
    dist02_distance_usage: Dict[int, int] = None,
    prev_dist01_idx: int = None,
    prev_dist02_idx: int = None,
    prev_difficulty_pair: Tuple[float, float] = None,
    route_dist01_difficulties: List[float] = None,
    route_dist02_difficulties: List[float] = None,
    route_difficulty_diffs: List[float] = None,
    target_route_dist01_mean: float = None,
    target_route_dist02_mean: float = None,
    route_difficulty_tolerance: float = 0.2,
    target_route_dist01_std: float = 0.25,
    target_route_dist02_std: float = 0.25,
    route_std_tolerance: float = 0.1,
    target_difficulty_diff_mean: float = 0.4,
    tracking: Dict = None,
    group_tracking=None,
    debug: bool = False,
) -> Optional[Tuple[Tuple[int, int], Dict]]:
    """
    Select (dist01_idx, dist02_idx) with hard + soft constraints.
    """
    if exclude_indices is None:
        exclude_indices = set()
    if direction_usage is None:
        direction_usage = {"before": 0, "after": 0}
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
    if route_dist01_difficulties is None:
        route_dist01_difficulties = []
    if route_dist02_difficulties is None:
        route_dist02_difficulties = []
    if route_difficulty_diffs is None:
        route_difficulty_diffs = []

    seq_len = len(seq)

    # ── Build candidate list ──
    candidates = []
    for j in range(seq_len):
        if j in exclude_indices or j == current_idx:
            continue
        distance = abs(j - current_idx)
        if distance < MIN_DISTANCE:
            continue
        is_before = j < current_idx
        difficulty = get_difficulty_score(distance, is_before)
        candidates.append((j, distance, is_before, difficulty))

    if len(candidates) < 2:
        if debug:
            print(f"  Insufficient candidates at pos {current_idx}")
        return None

    # ── Coverage gate: figure out if we MUST pick uncovered positions ──
    uncovered_candidate_set = set()
    if distractor_coverage is not None:
        uncovered_candidate_set = {j for j, _, _, _ in candidates if j not in distractor_coverage}
    remaining_trials = (seq_len - 2) - current_idx  # trials after this one
    total_uncovered = len(set(range(seq_len)) - distractor_coverage) if distractor_coverage is not None else 0
    
    rng.shuffle(candidates)

    # Force coverage when:
    # 1. There are uncovered candidates available, AND
    # 2. We're past the first third of the route OR running low on capacity
    #    (remaining capacity = (remaining+1)*2 slots; need at least total_uncovered covered)
    remaining_capacity = (remaining_trials + 1) * 2
    force_coverage = (
        len(uncovered_candidate_set) > 0
        and total_uncovered > 0
        and (current_idx >= seq_len // 3 or remaining_capacity <= total_uncovered * 3)
    )

    # ── Rejection tracking ──
    rejection_counts = defaultdict(int)

    # ── Two-pass approach ──
    # Pass 0: all constraints + coverage gate
    # Pass 1: relax H6/H7/H8 to rescue coverage (only if pass 0 failed)
    best_pair = None
    best_score = float('inf')

    for relax_pass in range(2):
        relax_route = (relax_pass == 1)
        
        # Only do pass 1 if pass 0 failed and coverage is an issue
        if relax_pass == 1:
            if best_pair is not None:
                break  # pass 0 succeeded
            if not force_coverage and len(uncovered_candidate_set) == 0:
                break  # coverage isn't the problem
            # Reset for second pass
            rejection_counts.clear()

        for c1 in candidates:
            j1, dist1, before1, diff1 = c1

            for c2 in candidates:
                j2, dist2, before2, diff2 = c2
                if j2 == j1:
                    continue

                # ════════════════════════════════════════════
                # HARD CONSTRAINTS
                # ════════════════════════════════════════════

                # H0: Coverage gate — when running low on trials, require uncovered positions
                if force_coverage:
                    if j1 not in uncovered_candidate_set and j2 not in uncovered_candidate_set:
                        rejection_counts["H0_coverage_gate"] += 1
                        continue

                # H1: dist01 must be harder
                if diff1 <= diff2:
                    rejection_counts["H1_d1_not_harder"] += 1
                    continue

                # H2: minimum difficulty difference
                if abs(diff1 - diff2) < min_difficulty_difference:
                    rejection_counts["H2_min_diff"] += 1
                    continue

                # H3a: no dist01 same-role repeat
                if prev_dist01_idx is not None and j1 == prev_dist01_idx:
                    rejection_counts["H3_streak_d1"] += 1
                    continue

                # H3b: no dist02 same-role repeat
                if prev_dist02_idx is not None and j2 == prev_dist02_idx:
                    rejection_counts["H3_streak_d2"] += 1
                    continue

                # H4: no same-distance same-direction
                if is_problematic_pair(dist1, dist2, before1, before2):
                    rejection_counts["H4_same_dist_dir"] += 1
                    continue

                # H5: position overuse cap (2.8x average) — dist01
                d1_usage = position_as_dist01_usage.get(j1, 0)
                total_d1 = sum(position_as_dist01_usage.values())
                if total_d1 > 0:
                    avg_d1 = total_d1 / seq_len
                    if d1_usage > avg_d1 * 1.8:
                        rejection_counts["H5_overuse_d1"] += 1
                        continue

                # H5: position overuse cap — dist02
                d2_usage = position_as_dist02_usage.get(j2, 0)
                total_d2 = sum(position_as_dist02_usage.values())
                if total_d2 > 0:
                    avg_d2 = total_d2 / seq_len
                    if d2_usage > avg_d2 * 1.8:
                        rejection_counts["H5_overuse_d2"] += 1
                        continue

                # ════════════════════════════════════════════
                # H6/H7/H8: ROUTE DIFFICULTY CONSTRAINTS
                # Skipped on pass 1 (relaxed for coverage rescue)
                # ════════════════════════════════════════════

                if not relax_route:
                    # H6: per-route difficulty mean
                    if target_route_dist01_mean is not None and len(route_dist01_difficulties) >= 6:
                        new_d1_mean = np.mean(route_dist01_difficulties + [diff1])
                        if abs(new_d1_mean - target_route_dist01_mean) > route_difficulty_tolerance:
                            rejection_counts["H6_route_mean_d1"] += 1
                            continue

                    if target_route_dist02_mean is not None and len(route_dist02_difficulties) >= 6:
                        new_d2_mean = np.mean(route_dist02_difficulties + [diff2])
                        if abs(new_d2_mean - target_route_dist02_mean) > route_difficulty_tolerance:
                            rejection_counts["H6_route_mean_d2"] += 1
                            continue

                    # H8: per-route difficulty difference mean
                    pair_diff_val = abs(diff1 - diff2)
                    if len(route_difficulty_diffs) >= 6:
                        new_diff_mean = np.mean(route_difficulty_diffs + [pair_diff_val])
                        if abs(new_diff_mean - target_difficulty_diff_mean) > route_difficulty_tolerance:
                            rejection_counts["H8_route_diff_mean"] += 1
                            continue

                    # H7: per-route difficulty SD
                    if target_route_dist01_std is not None and len(route_dist01_difficulties) >= 6:
                        new_d1_std = np.std(route_dist01_difficulties + [diff1])
                        if abs(new_d1_std - target_route_dist01_std) > route_std_tolerance:
                            rejection_counts["H7_route_sd_d1"] += 1
                            continue

                    if target_route_dist02_std is not None and len(route_dist02_difficulties) >= 6:
                        new_d2_std = np.std(route_dist02_difficulties + [diff2])
                        if abs(new_d2_std - target_route_dist02_std) > route_std_tolerance:
                            rejection_counts["H7_route_sd_d2"] += 1
                            continue

                # ════════════════════════════════════════════
                # ════════════════════════════════════════════
                # SOFT CONSTRAINTS — compute score
                # ════════════════════════════════════════════

                score = 0.0

                # S1: Position-relative direction balance (per role)
                if tracking is not None:
                    dir_score_d1 = _direction_score_for_candidate(
                        before1, "dist01", current_idx, tracking)
                    dir_score_d2 = _direction_score_for_candidate(
                        before2, "dist02", current_idx, tracking)
                    score += 1.0 / (dir_score_d1 + 0.01) **5
                    score += 1.0 / (dir_score_d2 + 0.01) **5

                # S2: Distance-to-current balance (per role)
                d1_dist_w = _balance_weight(dist01_distance_usage, dist1, seq_len - MIN_DISTANCE)
                d2_dist_w = _balance_weight(dist02_distance_usage, dist2, seq_len - MIN_DISTANCE)
                score += 1.0 / (d1_dist_w ** 4 + 0.001) * 0.15
                score += 1.0 / (d2_dist_w ** 4 + 0.001) * 0.15

                # S3: Distance-difference balance
                abs_dist_diff = abs(dist1 - dist2)
                dd_w = _balance_weight(distance_diff_usage, abs_dist_diff, seq_len - 1)
                score += 1.0 / (dd_w ** 2 + 0.001) * 0.10

                # S4: Position-as-distractor balance
                d1_pos_w = _balance_weight(position_as_dist01_usage, j1, seq_len)
                d2_pos_w = _balance_weight(position_as_dist02_usage, j2, seq_len)
                score += 1.0 / (d1_pos_w ** 2 + 0.001) * 0.05
                score += 1.0 / (d2_pos_w ** 2 + 0.001) * 0.05

                # S5: Coverage boost — strongly prefer uncovered positions
                if distractor_coverage is not None:
                    j1_uncovered = j1 not in distractor_coverage
                    j2_uncovered = j2 not in distractor_coverage
                    if j1_uncovered and j2_uncovered:
                        score -= coverage_weight * 2.0
                    elif j1_uncovered or j2_uncovered:
                        score -= coverage_weight * 1.0
                        
                
                # S6: group-level pair reuse penalty
                pair_key = (current_idx, j1, j2)
                group_usage = group_tracking["pair_usage"].get(pair_key, 0)
                score += group_usage * 0.3
                
                # S7 in selection:
                score += group_tracking["position_usage"].get(j1, 0) * 0.1
                score += group_tracking["position_usage"].get(j2, 0) * 0.1

                # Penalize pass 1 (relaxed) to prefer pass 0 solutions
                if relax_route:
                    score += 50.0
                
                score += rng.uniform(0, 0.005)  # small jitter to break ties differently per subject
                
                # ── Keep best ──
                if score < best_score:
                    best_score = score
                    best_pair = (j1, j2, dist1, dist2, before1, before2, diff1, diff2, abs_dist_diff)

    if best_pair is None:
        # ════════════════════════════════════════════════════════
        # FAILURE DIAGNOSTICS
        # ════════════════════════════════════════════════════════
        total_pairs = len(candidates) * (len(candidates) - 1)
        total_rej = sum(rejection_counts.values())
        print(f"\n{'='*60}")
        print(f"DISTRACTOR SELECTION FAILED at position {current_idx}")
        print(f"{'='*60}")
        print(f"  Candidates: {len(candidates)}, Pairs tested: {total_pairs}, Rejected: {total_rej}")
        print(f"  Coverage: force={force_coverage}, uncovered_total={total_uncovered}, uncovered_in_candidates={len(uncovered_candidate_set)}, remaining_trials={remaining_trials}")
        print(f"  Rejection breakdown:")
        for name, count in sorted(rejection_counts.items(), key=lambda x: -x[1]):
            pct = count / total_rej * 100 if total_rej > 0 else 0
            bar = "#" * max(1, int(pct / 2))
            print(f"    {name:<30s}: {count:>6d} ({pct:5.1f}%) {bar}")

        # Show which route constraints are active
        n_d1 = len(route_dist01_difficulties)
        n_d2 = len(route_dist02_difficulties)
        n_dd = len(route_difficulty_diffs)
        print(f"\n  Route state (trial {max(n_d1, n_d2) + 1}/13):")
        print(f"    H6 active: {'YES' if n_d1 >= 6 else f'NO (need 6, have {n_d1})'}")
        print(f"    H7 active: {'YES' if n_d1 >= 6 else f'NO (need 6, have {n_d1})'}")
        if route_dist01_difficulties:
            print(f"    d1 difficulties: {[f'{x:.1f}' for x in route_dist01_difficulties]} → mean={np.mean(route_dist01_difficulties):.3f} (target={target_route_dist01_mean}, tol={route_difficulty_tolerance})")
        if route_dist02_difficulties:
            print(f"    d2 difficulties: {[f'{x:.1f}' for x in route_dist02_difficulties]} → mean={np.mean(route_dist02_difficulties):.3f} (target={target_route_dist02_mean}, tol={route_difficulty_tolerance})")
        if route_difficulty_diffs:
            print(f"    diffs:           {[f'{x:.1f}' for x in route_difficulty_diffs]} → mean={np.mean(route_difficulty_diffs):.3f} (target={target_difficulty_diff_mean})")

        # Show overuse state
        if position_as_dist01_usage:
            total_d1 = sum(position_as_dist01_usage.values())
            avg_d1 = total_d1 / seq_len if total_d1 > 0 else 0
            cap_d1 = avg_d1 * 2.8
            over = {k: v for k, v in position_as_dist01_usage.items() if v > cap_d1}
            print(f"\n  H5 d1 overuse: avg={avg_d1:.1f}, cap={cap_d1:.1f}, over-cap={over if over else 'none'}")
        if position_as_dist02_usage:
            total_d2 = sum(position_as_dist02_usage.values())
            avg_d2 = total_d2 / seq_len if total_d2 > 0 else 0
            cap_d2 = avg_d2 * 2.8
            over = {k: v for k, v in position_as_dist02_usage.items() if v > cap_d2}
            print(f"  H5 d2 overuse: avg={avg_d2:.1f}, cap={cap_d2:.1f}, over-cap={over if over else 'none'}")

        # Show candidate difficulty values
        cand_info = [(j, f"d={dist}", "B" if bef else "A", f"diff={diff:.1f}") for j, dist, bef, diff in candidates]
        print(f"\n  Available candidates:")
        for c in cand_info:
            print(f"    pos={c[0]:>2}, {c[1]}, dir={c[2]}, {c[3]}")

        print(f"{'='*60}")
        return None

    j1, j2, dist1, dist2, before1, before2, diff1, diff2, abs_dist_diff = best_pair

    return (j1, j2), {
        "dist01_direction": "before" if before1 else "after",
        "dist02_direction": "before" if before2 else "after",
        "dist01_difficulty": diff1,
        "dist02_difficulty": diff2,
        "dist01_distance": dist1,
        "dist02_distance": dist2,
        "distance_difference": abs_dist_diff,
        "dist01_idx": j1,
        "dist02_idx": j2,
        "current_position": current_idx,
    }


# ============================================================================
# VALIDATION
# ============================================================================

def validate_distractor_difficulties(df_learning: pd.DataFrame, seqA: List[str], seqB: List[str], *, verbose=False) -> None:
    """Validates that dist01_difficulty > dist02_difficulty for all trials."""
    seqA_lookup = {concept: idx for idx, concept in enumerate(seqA)}
    seqB_lookup = {concept: idx for idx, concept in enumerate(seqB)}

    violations = []
    for trial_idx, (_, row) in enumerate(df_learning.iterrows()):
        seq_name = row['learningSeq']
        seq_lookup = seqA_lookup if seq_name == 'A' else seqB_lookup

        prompt_idx = seq_lookup[row['promptConcept']]
        dist01_idx = seq_lookup[row['dist01Concept']]
        dist02_idx = seq_lookup[row['dist02Concept']]

        d1_dist = abs(dist01_idx - prompt_idx)
        d2_dist = abs(dist02_idx - prompt_idx)
        d1_before = dist01_idx < prompt_idx
        d2_before = dist02_idx < prompt_idx

        d1_diff = get_difficulty_score(d1_dist, d1_before)
        d2_diff = get_difficulty_score(d2_dist, d2_before)

        if d1_diff <= d2_diff:
            violations.append({'trial': trial_idx, 'seq': seq_name,
                               'dist01_difficulty': d1_diff, 'dist02_difficulty': d2_diff})

    if violations:
        print(f"DISTRACTOR DIFFICULTY VALIDATION FAILED: {len(violations)}/{len(df_learning)} violations")
        raise AssertionError(
            f"Distractor difficulty constraint violated in {len(violations)}/{len(df_learning)} trials.")

    if verbose:
        print(f"PASS: All {len(df_learning)} trials satisfy dist01_difficulty > dist02_difficulty")


# ============================================================================
# REPORTING
# ============================================================================

def print_distractor_selection_report(tracking: Dict, participant_id: str):
    """Print comprehensive report."""
    print(f"\n{'='*70}")
    print(f"Distractor Selection Report - Participant {participant_id}")
    print(f"{'='*70}")

    total_dir = tracking["direction_usage"]["before"] + tracking["direction_usage"]["after"]
    if total_dir > 0:
        bpct = tracking["direction_usage"]["before"] / total_dir * 100
        print(f"\n1. Global Direction: before={tracking['direction_usage']['before']} ({bpct:.1f}%), "
              f"after={tracking['direction_usage']['after']} ({100-bpct:.1f}%)")

    print("\n2. Position-Relative Direction Balance (per role):")
    pos_targets = tracking["position_targets"]
    print(f"  {'Pos':>4} {'Target%B':>9} | {'d1_B':>5} {'d1_A':>5} {'d1_%B':>7} | {'d2_B':>5} {'d2_A':>5} {'d2_%B':>7}")
    for pos in sorted(tracking["position_direction_usage"].keys()):
        target_b_frac = get_position_relative_before_fraction(pos, pos_targets)
        u = tracking["position_direction_usage"][pos]
        d1_total = u["dist01_before"] + u["dist01_after"]
        d2_total = u["dist02_before"] + u["dist02_after"]
        d1_bpct = (u["dist01_before"] / d1_total * 100) if d1_total > 0 else 0
        d2_bpct = (u["dist02_before"] / d2_total * 100) if d2_total > 0 else 0
        print(f"  {pos:>4} {target_b_frac*100:>8.1f}% | {u['dist01_before']:>5} {u['dist01_after']:>5} {d1_bpct:>6.1f}% | "
              f"{u['dist02_before']:>5} {u['dist02_after']:>5} {d2_bpct:>6.1f}%")

    if tracking["route_dist01_means"]:
        d1_means = np.array(tracking["route_dist01_means"])
        d2_means = np.array(tracking["route_dist02_means"])
        d1_stds = np.array(tracking["route_dist01_stds"])
        d2_stds = np.array(tracking["route_dist02_stds"])
        diff_means = np.array(tracking["route_diff_means"])
        print(f"\n3. Per-Route Difficulty Stats:")
        print(f"  dist01 means: grand mean={np.mean(d1_means):.3f}, SD across routes={np.std(d1_means):.3f}")
        print(f"  dist01 SDs:   mean within-route SD={np.mean(d1_stds):.3f}")
        print(f"  dist02 means: grand mean={np.mean(d2_means):.3f}, SD across routes={np.std(d2_means):.3f}")
        print(f"  dist02 SDs:   mean within-route SD={np.mean(d2_stds):.3f}")
        print(f"  |d1-d2|: grand mean={np.mean(diff_means):.3f}, SD across routes={np.std(diff_means):.3f}")

    for role, usage_key in [("dist01", "dist01_distance_usage"), ("dist02", "dist02_distance_usage")]:
        usage = tracking[usage_key]
        if usage:
            vals = list(usage.values())
            ratio = max(vals) / min(vals) if min(vals) > 0 else float('inf')
            print(f"\n4. {role} Distance Balance: {dict(sorted(usage.items()))}")
            print(f"   min={min(vals)}, max={max(vals)}, ratio={ratio:.2f}")

    for role, usage_key in [("dist01", "position_as_dist01_usage"), ("dist02", "position_as_dist02_usage")]:
        usage = tracking[usage_key]
        if usage:
            vals = list(usage.values())
            ratio = max(vals) / min(vals) if min(vals) > 0 else float('inf')
            n_used = len(usage)
            print(f"\n5. {role} Position Balance: {n_used}/14 positions used, ratio={ratio:.2f}")

    if tracking["difficulty_history"]:
        d1s = [d["dist01"] for d in tracking["difficulty_history"]]
        d2s = [d["dist02"] for d in tracking["difficulty_history"]]
        violations = sum(1 for a, b in zip(d1s, d2s) if a <= b)
        print(f"\n6. dist01>dist02 violations: {violations}/{len(d1s)}")