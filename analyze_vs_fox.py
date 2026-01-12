#!/usr/bin/env python3
"""
BAYS Soccer Analysis - All Towns vs FOX Baseline
Shows every metric with FOX as the reference point (0%)
"""

import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/bays_teams.csv')
enrollment_df = pd.read_csv('data/school_enrollment.csv')

# Create enrollment lookup
enrollment_map = dict(zip(enrollment_df['town_code'], enrollment_df['enrollment']))

print("=" * 80)
print("BAYS SOCCER ANALYSIS - ALL TOWNS vs FOXBOROUGH BASELINE")
print("=" * 80)
print()

# Town list
towns = ['FOX', 'ASH', 'BEL', 'HOP', 'HOL', 'MAN']
town_names = {
    'FOX': 'Foxborough',
    'ASH': 'Ashland',
    'BEL': 'Bellingham',
    'HOP': 'Hopkinton',
    'HOL': 'Holliston',
    'MAN': 'Mansfield'
}

# Calculate all metrics for all towns
metrics_data = {}

for town in towns:
    town_df = df[df['town_code'] == town]
    enrollment = enrollment_map[town]

    # Metric 1: Participation Rate (Teams per 100 students)
    total_teams = len(town_df)
    teams_per_100 = (total_teams / 10) / enrollment * 100

    # Metric 2: Win Percentage
    total_games = town_df['wins'].sum() + town_df['losses'].sum() + town_df['ties'].sum()
    win_pct = (town_df['wins'].sum() + 0.5 * town_df['ties'].sum()) / total_games * 100 if total_games > 0 else 0

    # Metric 3: Goal Differential per Team
    avg_gd_per_team = town_df['goal_differential'].sum() / len(town_df)

    # Metric 4: Spring Retention Rate
    fall_teams = len(town_df[town_df['season_period'] == 'Fall']) / 5
    spring_teams = len(town_df[town_df['season_period'] == 'Spring']) / 5
    retention_rate = (spring_teams / fall_teams * 100) if fall_teams > 0 else 0

    # Metric 5: Average Division Level (lower = more competitive)
    avg_division = town_df['division_level'].mean()

    # Metric 6: Goals For per Team
    avg_gf_per_team = town_df['goals_for'].sum() / len(town_df)

    metrics_data[town] = {
        'participation': teams_per_100,
        'win_pct': win_pct,
        'avg_gd': avg_gd_per_team,
        'retention': retention_rate,
        'avg_division': avg_division,
        'avg_gf': avg_gf_per_team
    }

# Get FOX baseline values
fox_baseline = metrics_data['FOX']

# ============================================================================
# PRINT RESULTS WITH FOX AS BASELINE
# ============================================================================

print("\n" + "=" * 80)
print("METRIC 1: PARTICIPATION RATE (Teams per 100 Students)")
print("=" * 80 + "\n")
print(f"FOX Baseline: {fox_baseline['participation']:.2f} teams/100 students\n")
print("Town         Value    vs FOX")
print("-" * 40)
for town in towns:
    value = metrics_data[town]['participation']
    diff_pct = ((value - fox_baseline['participation']) / fox_baseline['participation']) * 100
    diff_str = "BASELINE" if town == 'FOX' else f"{diff_pct:+6.1f}%"
    print(f"{town_names[town]:12s} {value:5.2f}    {diff_str}")

print("\n" + "=" * 80)
print("METRIC 2: WIN PERCENTAGE")
print("=" * 80 + "\n")
print(f"FOX Baseline: {fox_baseline['win_pct']:.1f}%\n")
print("Town         Value    vs FOX")
print("-" * 40)
for town in towns:
    value = metrics_data[town]['win_pct']
    diff_pct = ((value - fox_baseline['win_pct']) / fox_baseline['win_pct']) * 100
    diff_str = "BASELINE" if town == 'FOX' else f"{diff_pct:+6.1f}%"
    print(f"{town_names[town]:12s} {value:5.1f}%   {diff_str}")

print("\n" + "=" * 80)
print("METRIC 3: GOAL DIFFERENTIAL PER TEAM")
print("=" * 80 + "\n")
print(f"FOX Baseline: {fox_baseline['avg_gd']:.2f} goals/team\n")
print("Town         Value    vs FOX      (Absolute Diff)")
print("-" * 55)
for town in towns:
    value = metrics_data[town]['avg_gd']
    # For negative baselines, show absolute difference
    abs_diff = value - fox_baseline['avg_gd']
    if town == 'FOX':
        diff_str = "BASELINE"
    else:
        diff_str = f"{abs_diff:+6.2f} goals"
    print(f"{town_names[town]:12s} {value:+6.2f}   {diff_str}")

print("\n" + "=" * 80)
print("METRIC 4: SPRING RETENTION RATE")
print("=" * 80 + "\n")
print(f"FOX Baseline: {fox_baseline['retention']:.1f}%\n")
print("Town         Value    vs FOX")
print("-" * 40)
for town in towns:
    value = metrics_data[town]['retention']
    diff_pct = ((value - fox_baseline['retention']) / fox_baseline['retention']) * 100
    diff_str = "BASELINE" if town == 'FOX' else f"{diff_pct:+6.1f}%"
    print(f"{town_names[town]:12s} {value:5.1f}%   {diff_str}")

print("\n" + "=" * 80)
print("METRIC 5: AVERAGE DIVISION LEVEL (Lower = More Competitive)")
print("=" * 80 + "\n")
print(f"FOX Baseline: Division {fox_baseline['avg_division']:.2f}\n")
print("Town         Value       vs FOX")
print("-" * 45)
for town in towns:
    value = metrics_data[town]['avg_division']
    abs_diff = value - fox_baseline['avg_division']
    if town == 'FOX':
        diff_str = "BASELINE"
    else:
        # Negative diff = more competitive (better)
        diff_str = f"{abs_diff:+5.2f} divisions"
    print(f"{town_names[town]:12s} Div {value:.2f}    {diff_str}")

print("\n" + "=" * 80)
print("METRIC 6: GOALS FOR PER TEAM (Offensive Strength)")
print("=" * 80 + "\n")
print(f"FOX Baseline: {fox_baseline['avg_gf']:.2f} goals/team\n")
print("Town         Value     vs FOX")
print("-" * 45)
for town in towns:
    value = metrics_data[town]['avg_gf']
    diff_pct = ((value - fox_baseline['avg_gf']) / fox_baseline['avg_gf']) * 100
    diff_str = "BASELINE" if town == 'FOX' else f"{diff_pct:+6.1f}%"
    print(f"{town_names[town]:12s} {value:5.2f}     {diff_str}")

# ============================================================================
# DIVISION DISTRIBUTION vs FOX
# ============================================================================

print("\n" + "=" * 80)
print("BONUS METRIC: DIVISION DISTRIBUTION vs FOX")
print("=" * 80 + "\n")

# Calculate FOX division distribution
fox_df = df[df['town_code'] == 'FOX']
fox_total = len(fox_df)
fox_div_pcts = {}
for level in [1, 2, 3, 4]:
    count = len(fox_df[fox_df['division_level'] == level])
    fox_div_pcts[level] = (count / fox_total * 100)

print("FOX Baseline Distribution:")
for level in [1, 2, 3, 4]:
    pct = fox_div_pcts[level]
    print(f"  Division {level}: {pct:5.1f}%")

print("\n" + "-" * 80)
print("\nOther Towns (showing difference from FOX):\n")

for town in [t for t in towns if t != 'FOX']:
    town_df = df[df['town_code'] == town]
    total = len(town_df)

    print(f"{town_names[town]:12s}", end='  ')
    for level in [1, 2, 3, 4]:
        count = len(town_df[town_df['division_level'] == level])
        pct = (count / total * 100)
        diff = pct - fox_div_pcts[level]
        print(f"D{level}: {pct:4.1f}% ({diff:+5.1f})  ", end='')
    print()

# ============================================================================
# COMPREHENSIVE SUMMARY TABLE
# ============================================================================

print("\n" + "=" * 80)
print("COMPREHENSIVE SUMMARY: ALL METRICS vs FOX")
print("=" * 80 + "\n")

summary_data = []
for town in towns:
    m = metrics_data[town]
    f = fox_baseline

    if town == 'FOX':
        summary_data.append({
            'Town': town,
            'Participation': 'BASELINE',
            'Win %': 'BASELINE',
            'Goal Diff': 'BASELINE',
            'Retention': 'BASELINE',
            'Avg Div': 'BASELINE',
            'Goals For': 'BASELINE'
        })
    else:
        summary_data.append({
            'Town': town,
            'Participation': f"{((m['participation'] - f['participation']) / f['participation'] * 100):+.1f}%",
            'Win %': f"{((m['win_pct'] - f['win_pct']) / f['win_pct'] * 100):+.1f}%",
            'Goal Diff': f"{(m['avg_gd'] - f['avg_gd']):+.2f}",
            'Retention': f"{((m['retention'] - f['retention']) / f['retention'] * 100):+.1f}%",
            'Avg Div': f"{(m['avg_division'] - f['avg_division']):+.2f}",
            'Goals For': f"{((m['avg_gf'] - f['avg_gf']) / f['avg_gf'] * 100):+.1f}%"
        })

summary_df = pd.DataFrame(summary_data)
print(summary_df.to_string(index=False))

print("\n" + "=" * 80)
print("KEY FINDINGS")
print("=" * 80 + "\n")

# Find best/worst in each category
print("COMPARED TO FOX:\n")

# Participation
part_sorted = sorted([(t, metrics_data[t]['participation']) for t in towns if t != 'FOX'],
                     key=lambda x: x[1], reverse=True)
print(f"Participation Rate:")
print(f"  Best:  {town_names[part_sorted[0][0]]} ({((part_sorted[0][1] - fox_baseline['participation']) / fox_baseline['participation'] * 100):+.1f}%)")
print(f"  Worst: {town_names[part_sorted[-1][0]]} ({((part_sorted[-1][1] - fox_baseline['participation']) / fox_baseline['participation'] * 100):+.1f}%)")

# Win %
win_sorted = sorted([(t, metrics_data[t]['win_pct']) for t in towns if t != 'FOX'],
                    key=lambda x: x[1], reverse=True)
print(f"\nWin Percentage:")
print(f"  Best:  {town_names[win_sorted[0][0]]} ({((win_sorted[0][1] - fox_baseline['win_pct']) / fox_baseline['win_pct'] * 100):+.1f}%)")
print(f"  Worst: {town_names[win_sorted[-1][0]]} ({((win_sorted[-1][1] - fox_baseline['win_pct']) / fox_baseline['win_pct'] * 100):+.1f}%)")

# Goal Diff
gd_sorted = sorted([(t, metrics_data[t]['avg_gd']) for t in towns if t != 'FOX'],
                   key=lambda x: x[1], reverse=True)
print(f"\nGoal Differential/Team:")
print(f"  Best:  {town_names[gd_sorted[0][0]]} ({(gd_sorted[0][1] - fox_baseline['avg_gd']):+.2f} goals)")
print(f"  Worst: {town_names[gd_sorted[-1][0]]} ({(gd_sorted[-1][1] - fox_baseline['avg_gd']):+.2f} goals)")

# Retention
ret_sorted = sorted([(t, metrics_data[t]['retention']) for t in towns if t != 'FOX'],
                    key=lambda x: x[1], reverse=True)
print(f"\nSpring Retention:")
print(f"  Best:  {town_names[ret_sorted[0][0]]} ({((ret_sorted[0][1] - fox_baseline['retention']) / fox_baseline['retention'] * 100):+.1f}%)")
print(f"  Worst: {town_names[ret_sorted[-1][0]]} ({((ret_sorted[-1][1] - fox_baseline['retention']) / fox_baseline['retention'] * 100):+.1f}%)")

# Competitive level (lower is better)
div_sorted = sorted([(t, metrics_data[t]['avg_division']) for t in towns if t != 'FOX'],
                    key=lambda x: x[1])
print(f"\nCompetitive Level (negative = more competitive):")
print(f"  Best:  {town_names[div_sorted[0][0]]} ({(div_sorted[0][1] - fox_baseline['avg_division']):+.2f} divisions)")
print(f"  Worst: {town_names[div_sorted[-1][0]]} ({(div_sorted[-1][1] - fox_baseline['avg_division']):+.2f} divisions)")

print("\n" + "=" * 80)
print("Analysis Complete")
print("=" * 80)
