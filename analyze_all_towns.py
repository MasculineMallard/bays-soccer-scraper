#!/usr/bin/env python3
"""
Comprehensive BAYS Soccer Analysis - All 6 Towns
Compares FOX, ASH, BEL, HOP, HOL, MAN across all key metrics
"""

import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/bays_teams.csv')
enrollment_df = pd.read_csv('data/school_enrollment.csv')

# Create enrollment lookup
enrollment_map = dict(zip(enrollment_df['town_code'], enrollment_df['enrollment']))

print("=" * 80)
print("BAYS SOCCER COMPREHENSIVE ANALYSIS - 6 TOWNS")
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

# ============================================================================
# SECTION 1: PROGRAM SIZE & PARTICIPATION
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 1: PROGRAM SIZE & PARTICIPATION")
print("=" * 80 + "\n")

size_data = []
for town in towns:
    town_df = df[df['town_code'] == town]
    enrollment = enrollment_map[town]

    total_teams = len(town_df)
    teams_per_100 = (total_teams / 10) / enrollment * 100  # Avg per season / enrollment * 100

    size_data.append({
        'Town': town_names[town],
        'Code': town,
        'Enrollment': enrollment,
        'Total Teams': total_teams,
        'Avg/Season': total_teams / 10,
        'Teams/100 Students': round(teams_per_100, 2)
    })

size_df = pd.DataFrame(size_data)
size_df = size_df.sort_values('Teams/100 Students', ascending=False)
print(size_df.to_string(index=False))

# Normalized to FOX
fox_rate = size_df[size_df['Code'] == 'FOX']['Teams/100 Students'].values[0]
print(f"\n--- Participation Rate vs FOX (baseline = {fox_rate}) ---")
for _, row in size_df.iterrows():
    diff = ((row['Teams/100 Students'] - fox_rate) / fox_rate) * 100
    print(f"{row['Code']}: {row['Teams/100 Students']:.2f} ({diff:+.1f}%)")

# ============================================================================
# SECTION 2: COMPETITIVE PERFORMANCE
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 2: COMPETITIVE PERFORMANCE")
print("=" * 80 + "\n")

perf_data = []
for town in towns:
    town_df = df[df['town_code'] == town]

    total_games = town_df['wins'].sum() + town_df['losses'].sum() + town_df['ties'].sum()
    win_pct = (town_df['wins'].sum() + 0.5 * town_df['ties'].sum()) / total_games * 100 if total_games > 0 else 0

    total_gd = town_df['goal_differential'].sum()
    avg_gd_per_team = total_gd / len(town_df)

    avg_gf = town_df['goals_for'].sum() / len(town_df)
    avg_ga = town_df['goals_against'].sum() / len(town_df)

    perf_data.append({
        'Town': town_names[town],
        'Code': town,
        'Win %': round(win_pct, 1),
        'Total GD': int(total_gd),
        'Avg GD/Team': round(avg_gd_per_team, 2),
        'Avg GF/Team': round(avg_gf, 2),
        'Avg GA/Team': round(avg_ga, 2)
    })

perf_df = pd.DataFrame(perf_data)
perf_df = perf_df.sort_values('Total GD', ascending=False)
print(perf_df.to_string(index=False))

# ============================================================================
# SECTION 3: SPRING RETENTION (Fall → Spring)
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 3: SPRING RETENTION RATE")
print("=" * 80 + "\n")

retention_data = []
for town in towns:
    town_df = df[df['town_code'] == town]

    fall_teams = town_df[town_df['season_period'] == 'Fall']['team_name'].count()
    spring_teams = town_df[town_df['season_period'] == 'Spring']['team_name'].count()

    avg_fall = fall_teams / 5  # 5 fall seasons
    avg_spring = spring_teams / 5  # 5 spring seasons

    retention_rate = (avg_spring / avg_fall * 100) if avg_fall > 0 else 0
    drop_pct = 100 - retention_rate

    retention_data.append({
        'Town': town_names[town],
        'Code': town,
        'Avg Fall': round(avg_fall, 1),
        'Avg Spring': round(avg_spring, 1),
        'Retention %': round(retention_rate, 1),
        'Drop %': round(drop_pct, 1)
    })

retention_df = pd.DataFrame(retention_data)
retention_df = retention_df.sort_values('Retention %', ascending=False)
print(retention_df.to_string(index=False))

# ============================================================================
# SECTION 4: DIVISION DISTRIBUTION
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 4: DIVISION DISTRIBUTION")
print("=" * 80 + "\n")

print("--- Teams by Division Level (%) ---\n")

# For each town, calculate % in each division
for town in towns:
    town_df = df[df['town_code'] == town]
    total = len(town_df)

    div_counts = town_df['division_level'].value_counts().sort_index()

    print(f"{town_names[town]} ({town}):")
    for level in [1, 2, 3, 4]:
        count = div_counts.get(level, 0)
        pct = (count / total * 100) if total > 0 else 0
        print(f"  Division {level}: {count:3d} teams ({pct:5.1f}%)")
    print()

# Summary table
print("\n--- Division Distribution Summary ---\n")
dist_data = []
for town in towns:
    town_df = df[df['town_code'] == town]
    total = len(town_df)

    div_counts = town_df['division_level'].value_counts()

    dist_data.append({
        'Town': town,
        'Div 1 %': round((div_counts.get(1, 0) / total * 100), 1),
        'Div 2 %': round((div_counts.get(2, 0) / total * 100), 1),
        'Div 3 %': round((div_counts.get(3, 0) / total * 100), 1),
        'Div 4 %': round((div_counts.get(4, 0) / total * 100), 1),
        'Avg Level': round(town_df['division_level'].mean(), 2)
    })

dist_df = pd.DataFrame(dist_data)
dist_df = dist_df.sort_values('Avg Level')
print(dist_df.to_string(index=False))

print("\n(Lower Avg Level = Higher competitive level overall)")

# ============================================================================
# SECTION 5: GENDER DISTRIBUTION
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 5: GENDER DISTRIBUTION")
print("=" * 80 + "\n")

gender_data = []
for town in towns:
    town_df = df[df['town_code'] == town]
    total = len(town_df)

    boys = len(town_df[town_df['gender'] == 'Boys'])
    girls = len(town_df[town_df['gender'] == 'Girls'])
    coed = len(town_df[town_df['gender'] == 'Coed'])

    gender_data.append({
        'Town': town,
        'Boys': boys,
        'Boys %': round(boys / total * 100, 1),
        'Girls': girls,
        'Girls %': round(girls / total * 100, 1),
        'Coed': coed,
        'Coed %': round(coed / total * 100, 1) if coed > 0 else 0
    })

gender_df = pd.DataFrame(gender_data)
print(gender_df.to_string(index=False))

# ============================================================================
# SECTION 6: YEAR-OVER-YEAR TRENDS
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 6: YEAR-OVER-YEAR TRENDS (Fall Seasons)")
print("=" * 80 + "\n")

print("Teams per Fall season:\n")
for town in towns:
    town_df = df[(df['town_code'] == town) & (df['season_period'] == 'Fall')]
    yearly = town_df.groupby('season_year').size().sort_index(ascending=False)

    print(f"{town_names[town]:15s} ", end='')
    for year in [2025, 2024, 2023, 2022, 2021]:
        count = yearly.get(year, 0)
        print(f"{year}: {count:2d}  ", end='')

    # Calculate trend
    if len(yearly) >= 2:
        trend = yearly.iloc[0] - yearly.iloc[-1]
        trend_str = f"({trend:+d})" if trend != 0 else "(flat)"
    else:
        trend_str = "(N/A)"
    print(f"  {trend_str}")

# ============================================================================
# SECTION 7: GRADE-LEVEL PARTICIPATION
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 7: GRADE-LEVEL PARTICIPATION")
print("=" * 80 + "\n")

grade_data = []
for town in towns:
    town_df = df[df['town_code'] == town]
    total = len(town_df)

    grade_counts = town_df['age_group'].value_counts()

    grade_data.append({
        'Town': town,
        'Grade 7/8': grade_counts.get('Grade 7/8', 0),
        'Grade 6': grade_counts.get('Grade 6', 0),
        'Grade 5': grade_counts.get('Grade 5', 0),
        'Grade 4': grade_counts.get('Grade 4', 0),
        'Grade 3': grade_counts.get('Grade 3', 0),
        'Grade 1-2': grade_counts.get('Grade 1-2', 0),
        'K': grade_counts.get('Kindergarten', 0)
    })

grade_df = pd.DataFrame(grade_data)
print(grade_df.to_string(index=False))

# ============================================================================
# SECTION 8: SUMMARY RANKINGS
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 8: SUMMARY RANKINGS")
print("=" * 80 + "\n")

# Compile rankings
rankings = []
for town in towns:
    town_df = df[df['town_code'] == town]
    enrollment = enrollment_map[town]

    # Participation rate
    teams_per_100 = (len(town_df) / 10) / enrollment * 100

    # Win rate
    total_games = town_df['wins'].sum() + town_df['losses'].sum() + town_df['ties'].sum()
    win_pct = (town_df['wins'].sum() + 0.5 * town_df['ties'].sum()) / total_games * 100

    # Goal differential
    total_gd = town_df['goal_differential'].sum()

    # Retention
    fall_teams = len(town_df[town_df['season_period'] == 'Fall']) / 5
    spring_teams = len(town_df[town_df['season_period'] == 'Spring']) / 5
    retention = (spring_teams / fall_teams * 100) if fall_teams > 0 else 0

    # Competitive level (lower = better)
    avg_div = town_df['division_level'].mean()

    rankings.append({
        'Town': town,
        'Teams/100': round(teams_per_100, 2),
        'Win %': round(win_pct, 1),
        'Total GD': int(total_gd),
        'Retention %': round(retention, 1),
        'Avg Div': round(avg_div, 2)
    })

rank_df = pd.DataFrame(rankings)
print("Overall Performance Summary:\n")
print(rank_df.to_string(index=False))

print("\n" + "=" * 80)
print("KEY INSIGHTS")
print("=" * 80 + "\n")

# Find leaders in each category
best_participation = rank_df.loc[rank_df['Teams/100'].idxmax()]
best_winning = rank_df.loc[rank_df['Win %'].idxmax()]
best_gd = rank_df.loc[rank_df['Total GD'].idxmax()]
best_retention = rank_df.loc[rank_df['Retention %'].idxmax()]
best_competitive = rank_df.loc[rank_df['Avg Div'].idxmin()]

print(f"[*] Highest Participation Rate: {best_participation['Town']} ({best_participation['Teams/100']:.2f} teams/100 students)")
print(f"[*] Best Win Rate: {best_winning['Town']} ({best_winning['Win %']:.1f}%)")
print(f"[*] Best Goal Differential: {best_gd['Town']} ({best_gd['Total GD']:+d})")
print(f"[*] Best Spring Retention: {best_retention['Town']} ({best_retention['Retention %']:.1f}%)")
print(f"[*] Highest Competitive Level: {best_competitive['Town']} (Avg Division {best_competitive['Avg Div']:.2f})")

print("\n" + "=" * 80)
print("Analysis complete. Data saved to: data/bays_teams.csv")
print("=" * 80)
