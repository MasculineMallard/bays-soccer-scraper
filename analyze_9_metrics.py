#!/usr/bin/env python3
"""
BAYS Soccer Analysis - All 9 Core Metrics
Complete rankings for all towns including WAL
"""

import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/bays_teams.csv')
enrollment_df = pd.read_csv('data/school_enrollment.csv')

# Create enrollment lookup
enrollment_map = dict(zip(enrollment_df['town_code'], enrollment_df['enrollment']))

print("=" * 80)
print("BAYS SOCCER - 9 CORE METRICS ANALYSIS")
print("=" * 80)
print()

# Town list - now includes WAL
towns = ['FOX', 'ASH', 'BEL', 'HOP', 'HOL', 'MAN', 'WAL']
town_names = {
    'FOX': 'Foxborough',
    'ASH': 'Ashland',
    'BEL': 'Bellingham',
    'HOP': 'Hopkinton',
    'HOL': 'Holliston',
    'MAN': 'Mansfield',
    'WAL': 'Walpole'
}

# Calculate all 9 metrics for all towns
all_metrics = {}

for town in towns:
    town_df = df[df['town_code'] == town]
    enrollment = enrollment_map[town]
    total = len(town_df)

    # Metric 1: Participation Rate
    teams_per_100 = (total / 10) / enrollment * 100

    # Metric 2: Win Percentage
    total_games = town_df['wins'].sum() + town_df['losses'].sum() + town_df['ties'].sum()
    win_pct = (town_df['wins'].sum() + 0.5 * town_df['ties'].sum()) / total_games * 100 if total_games > 0 else 0

    # Metric 3: Goal Differential per Team
    avg_gd = town_df['goal_differential'].sum() / total

    # Metric 4: Spring Retention Rate
    fall_teams = len(town_df[town_df['season_period'] == 'Fall']) / 5
    spring_teams = len(town_df[town_df['season_period'] == 'Spring']) / 5
    retention = (spring_teams / fall_teams * 100) if fall_teams > 0 else 0

    # Metric 5: Goals For per Team
    avg_gf = town_df['goals_for'].sum() / total

    # Metric 6: Goals Against per Team
    avg_ga = town_df['goals_against'].sum() / total

    # Metric 7: Division Distribution (Average Division Level)
    avg_division = town_df['division_level'].mean()

    # Also get division breakdown
    div_pcts = {}
    for level in [1, 2, 3, 4]:
        count = len(town_df[town_df['division_level'] == level])
        div_pcts[level] = (count / total * 100)

    # Metric 8: Gender Balance (% Boys vs Girls)
    boys = len(town_df[town_df['gender'] == 'Boys'])
    girls = len(town_df[town_df['gender'] == 'Girls'])
    boys_pct = (boys / total * 100)
    girls_pct = (girls / total * 100)

    # Calculate balance score (closer to 50/50 = better)
    gender_balance_score = 100 - abs(50 - boys_pct) * 2  # 100 = perfect balance, 0 = all one gender

    # Metric 9: Growth Rate (Fall 2021 → Fall 2025)
    fall2021 = len(town_df[(town_df['season_year'] == 2021) & (town_df['season_period'] == 'Fall')])
    fall2025 = len(town_df[(town_df['season_year'] == 2025) & (town_df['season_period'] == 'Fall')])

    if fall2021 > 0:
        growth_pct = ((fall2025 - fall2021) / fall2021) * 100
        growth_abs = fall2025 - fall2021
    else:
        growth_pct = 0
        growth_abs = 0

    all_metrics[town] = {
        'participation': teams_per_100,
        'win_pct': win_pct,
        'avg_gd': avg_gd,
        'retention': retention,
        'avg_gf': avg_gf,
        'avg_ga': avg_ga,
        'avg_division': avg_division,
        'div_pcts': div_pcts,
        'boys_pct': boys_pct,
        'girls_pct': girls_pct,
        'gender_balance': gender_balance_score,
        'fall2021': fall2021,
        'fall2025': fall2025,
        'growth_pct': growth_pct,
        'growth_abs': growth_abs
    }

# ============================================================================
# METRIC 1: PARTICIPATION RATE
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 1: PARTICIPATION RATE (Teams per 100 Students)")
print("=" * 80 + "\n")

part_ranked = sorted([(t, all_metrics[t]['participation']) for t in towns],
                     key=lambda x: x[1], reverse=True)

for rank, (town, value) in enumerate(part_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    print(f"{medal} {rank}. {town_names[town]:15s} {value:5.2f} teams/100 students")

# ============================================================================
# METRIC 2: WIN PERCENTAGE
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 2: WIN PERCENTAGE")
print("=" * 80 + "\n")

win_ranked = sorted([(t, all_metrics[t]['win_pct']) for t in towns],
                    key=lambda x: x[1], reverse=True)

for rank, (town, value) in enumerate(win_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    print(f"{medal} {rank}. {town_names[town]:15s} {value:5.1f}%")

# ============================================================================
# METRIC 3: GOAL DIFFERENTIAL PER TEAM
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 3: GOAL DIFFERENTIAL PER TEAM")
print("=" * 80 + "\n")

gd_ranked = sorted([(t, all_metrics[t]['avg_gd']) for t in towns],
                   key=lambda x: x[1], reverse=True)

for rank, (town, value) in enumerate(gd_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    print(f"{medal} {rank}. {town_names[town]:15s} {value:+6.2f} goals/team")

# ============================================================================
# METRIC 4: SPRING RETENTION RATE
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 4: SPRING RETENTION RATE")
print("=" * 80 + "\n")

ret_ranked = sorted([(t, all_metrics[t]['retention']) for t in towns],
                    key=lambda x: x[1], reverse=True)

for rank, (town, value) in enumerate(ret_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    print(f"{medal} {rank}. {town_names[town]:15s} {value:5.1f}%")

# ============================================================================
# METRIC 5: OFFENSIVE STRENGTH (Goals For per Team)
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 5: OFFENSIVE STRENGTH (Goals For per Team)")
print("=" * 80 + "\n")

gf_ranked = sorted([(t, all_metrics[t]['avg_gf']) for t in towns],
                   key=lambda x: x[1], reverse=True)

for rank, (town, value) in enumerate(gf_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    print(f"{medal} {rank}. {town_names[town]:15s} {value:5.2f} goals/team")

# ============================================================================
# METRIC 6: DEFENSIVE STRENGTH (Goals Against per Team - Lower is Better)
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 6: DEFENSIVE STRENGTH (Goals Against per Team)")
print("=" * 80 + "\n")

ga_ranked = sorted([(t, all_metrics[t]['avg_ga']) for t in towns],
                   key=lambda x: x[1])  # Lower is better

for rank, (town, value) in enumerate(ga_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    print(f"{medal} {rank}. {town_names[town]:15s} {value:5.2f} goals/team (lower = better)")

# ============================================================================
# METRIC 7: COMPETITIVE LEVEL (Division Distribution)
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 7: COMPETITIVE LEVEL (Average Division)")
print("=" * 80 + "\n")

div_ranked = sorted([(t, all_metrics[t]['avg_division']) for t in towns],
                    key=lambda x: x[1])  # Lower is better

for rank, (town, value) in enumerate(div_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    print(f"{medal} {rank}. {town_names[town]:15s} Division {value:.2f} (lower = more competitive)")

print("\n--- Detailed Division Distribution ---\n")
print("Town          Div 1%  Div 2%  Div 3%  Div 4%")
print("-" * 50)
for town, _ in div_ranked:
    div = all_metrics[town]['div_pcts']
    print(f"{town_names[town]:13s} {div[1]:5.1f}%  {div[2]:5.1f}%  {div[3]:5.1f}%  {div[4]:5.1f}%")

# ============================================================================
# METRIC 8: GENDER BALANCE
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 8: GENDER BALANCE (Closer to 50/50 = Better)")
print("=" * 80 + "\n")

gender_ranked = sorted([(t, all_metrics[t]['gender_balance']) for t in towns],
                       key=lambda x: x[1], reverse=True)

for rank, (town, score) in enumerate(gender_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    boys = all_metrics[town]['boys_pct']
    girls = all_metrics[town]['girls_pct']
    print(f"{medal} {rank}. {town_names[town]:15s} Balance Score: {score:5.1f}/100  (Boys: {boys:.1f}%, Girls: {girls:.1f}%)")

# ============================================================================
# METRIC 9: GROWTH RATE (Fall 2021 → Fall 2025)
# ============================================================================
print("\n" + "=" * 80)
print("METRIC 9: GROWTH RATE (Fall 2021 -> Fall 2025)")
print("Ranked by % growth (higher % = better)")
print("=" * 80 + "\n")

growth_ranked = sorted([(t, all_metrics[t]['growth_pct']) for t in towns],
                       key=lambda x: x[1], reverse=True)

for rank, (town, growth) in enumerate(growth_ranked, 1):
    medal = ["[1]", "[2]", "[3]"][rank-1] if rank <= 3 else "   "
    f2021 = all_metrics[town]['fall2021']
    f2025 = all_metrics[town]['fall2025']
    abs_change = all_metrics[town]['growth_abs']
    print(f"{medal} {rank}. {town_names[town]:15s} {growth:+6.1f}%  ({f2021:2d} -> {f2025:2d} teams)")

# ============================================================================
# COMPREHENSIVE SUMMARY TABLE
# ============================================================================
print("\n" + "=" * 80)
print("COMPREHENSIVE RANKINGS SUMMARY")
print("=" * 80 + "\n")

# Calculate average rank for each town
rank_summary = {}
for town in towns:
    ranks = []

    # Get rank in each metric
    ranks.append(next(i for i, (t, _) in enumerate(part_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(win_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(gd_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(ret_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(gf_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(ga_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(div_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(gender_ranked, 1) if t == town))
    ranks.append(next(i for i, (t, _) in enumerate(growth_ranked, 1) if t == town))

    rank_summary[town] = {
        'ranks': ranks,
        'avg_rank': sum(ranks) / len(ranks),
        'top3_count': sum(1 for r in ranks if r <= 3)
    }

# Print ranking table
print("Town          M1  M2  M3  M4  M5  M6  M7  M8  M9  Avg  Top-3")
print("-" * 70)
for town in sorted(towns, key=lambda t: rank_summary[t]['avg_rank']):
    ranks = rank_summary[town]['ranks']
    avg = rank_summary[town]['avg_rank']
    top3 = rank_summary[town]['top3_count']
    print(f"{town_names[town]:13s} {ranks[0]}   {ranks[1]}   {ranks[2]}   {ranks[3]}   {ranks[4]}   {ranks[5]}   {ranks[6]}   {ranks[7]}   {ranks[8]}   {avg:.1f}   {top3}/9")

print("\nMetrics:")
print("  M1 = Participation Rate")
print("  M2 = Win Percentage")
print("  M3 = Goal Differential")
print("  M4 = Spring Retention")
print("  M5 = Offensive Strength")
print("  M6 = Defensive Strength")
print("  M7 = Competitive Level")
print("  M8 = Gender Balance")
print("  M9 = Growth Rate")

# ============================================================================
# KEY INSIGHTS
# ============================================================================
print("\n" + "=" * 80)
print("KEY INSIGHTS")
print("=" * 80 + "\n")

# Best overall (lowest avg rank)
best_overall = min(towns, key=lambda t: rank_summary[t]['avg_rank'])
print(f"Best Overall Program: {town_names[best_overall]}")
print(f"  Average Rank: {rank_summary[best_overall]['avg_rank']:.1f}")
print(f"  Top-3 Finishes: {rank_summary[best_overall]['top3_count']}/9 metrics")

# Worst overall
worst_overall = max(towns, key=lambda t: rank_summary[t]['avg_rank'])
print(f"\nWorst Overall Program: {town_names[worst_overall]}")
print(f"  Average Rank: {rank_summary[worst_overall]['avg_rank']:.1f}")
print(f"  Top-3 Finishes: {rank_summary[worst_overall]['top3_count']}/9 metrics")

# Most balanced
most_balanced = max(towns, key=lambda t: all_metrics[t]['gender_balance'])
print(f"\nBest Gender Balance: {town_names[most_balanced]}")
print(f"  Boys: {all_metrics[most_balanced]['boys_pct']:.1f}%, Girls: {all_metrics[most_balanced]['girls_pct']:.1f}%")

# Most competitive
most_competitive = min(towns, key=lambda t: all_metrics[t]['avg_division'])
print(f"\nMost Competitive: {town_names[most_competitive]}")
print(f"  Average Division: {all_metrics[most_competitive]['avg_division']:.2f}")
print(f"  Division 1 Teams: {all_metrics[most_competitive]['div_pcts'][1]:.1f}%")

# Fastest growing
fastest_growth = max(towns, key=lambda t: all_metrics[t]['growth_pct'])
print(f"\nFastest Growing: {town_names[fastest_growth]}")
print(f"  Growth: {all_metrics[fastest_growth]['growth_pct']:+.1f}% (F21: {all_metrics[fastest_growth]['fall2021']} -> F25: {all_metrics[fastest_growth]['fall2025']})")

print("\n" + "=" * 80)
print("Analysis Complete - All 9 Core Metrics")
print("=" * 80)
