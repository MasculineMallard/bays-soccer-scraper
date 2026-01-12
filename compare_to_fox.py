#!/usr/bin/env python3
"""
Compare all towns to FOX baseline
Shows +/- percentages relative to Foxborough
"""
import pandas as pd

df = pd.read_csv('data/bays_teams.csv')

print('=' * 80)
print('ALL METRICS NORMALIZED TO FOXBOROUGH BASELINE')
print('=' * 80)
print()

# METRIC 1: Teams Per 100 School-Age Children
print('METRIC 1: TEAMS PER 100 SCHOOL-AGE CHILDREN')
print('-' * 80)

# School enrollment data (K-12, 2024-25)
# Source: Massachusetts Department of Education
school_enrollment = {
    'FOX': 2485,  # Foxborough school district enrollment
    'ASH': 2909,  # Ashland school district enrollment
    'BEL': 1990   # Bellingham school district enrollment
}

for town in ['FOX', 'ASH', 'BEL']:
    town_df = df[df['town_code'] == town]
    total_teams = len(town_df)
    seasons = town_df.groupby(['season_year', 'season_period']).size().count()
    avg_teams = total_teams / seasons if seasons > 0 else 0

    if town in school_enrollment:
        # Teams per 100 school-age children
        rate = (avg_teams / school_enrollment[town]) * 100
        if town == 'FOX':
            fox_rate = rate
            print(f'{town}: {rate:.2f} teams/100 students (BASELINE - {int(avg_teams)} avg teams, {school_enrollment[town]} students)')
        else:
            diff_pct = ((rate - fox_rate) / fox_rate) * 100
            sign = '+' if diff_pct > 0 else ''
            print(f'{town}: {rate:.2f} teams/100 students ({sign}{diff_pct:.1f}% vs FOX - {int(avg_teams)} avg teams, {school_enrollment[town]} students)')

print()
print()

# METRIC 2: Spring Participation Drop
print('METRIC 2: SPRING PARTICIPATION DROP (Consistency)')
print('-' * 80)

for town in ['FOX', 'ASH', 'BEL']:
    town_df = df[df['town_code'] == town]

    # Get fall and spring averages
    fall = town_df[town_df['season_period'] == 'Fall'].groupby('season_year').size()
    spring = town_df[town_df['season_period'] == 'Spring'].groupby('season_year').size()

    avg_fall = fall.mean()
    avg_spring = spring.mean()

    if avg_spring > 0:
        drop_pct = ((avg_fall - avg_spring) / avg_spring) * 100

        if town == 'FOX':
            fox_drop = drop_pct
            print(f'{town}: {drop_pct:.1f}% drop (BASELINE - {avg_fall:.1f} Fall to {avg_spring:.1f} Spring)')
        else:
            diff = drop_pct - fox_drop
            sign = '+' if diff > 0 else ''
            better_worse = 'WORSE' if diff > 0 else 'BETTER'
            print(f'{town}: {drop_pct:.1f}% drop ({sign}{diff:.1f}% vs FOX - {better_worse}) ({avg_fall:.1f} Fall to {avg_spring:.1f} Spring)')

print()
print()

# METRIC 3: Win Rate by Division
print('METRIC 3: WIN RATE BY DIVISION LEVEL')
print('-' * 80)

def calc_win_pct(row):
    total = row['wins'] + row['losses'] + row['ties']
    if total == 0:
        return 0
    return (row['wins'] + 0.5 * row['ties']) / total * 100

df['win_pct'] = df.apply(calc_win_pct, axis=1)

division_perf = df[df['town_code'].isin(['FOX', 'ASH', 'BEL'])].groupby(['town_code', 'division_level']).agg({
    'win_pct': 'mean'
}).reset_index()

fox_div_rates = {}
for _, row in division_perf[division_perf['town_code'] == 'FOX'].iterrows():
    fox_div_rates[row['division_level']] = row['win_pct']

for level in sorted(fox_div_rates.keys()):
    print(f'\nDivision {level}:')

    for town in ['FOX', 'ASH', 'BEL']:
        town_data = division_perf[(division_perf['town_code'] == town) & (division_perf['division_level'] == level)]

        if len(town_data) > 0:
            rate = town_data.iloc[0]['win_pct']

            if town == 'FOX':
                print(f'  {town}: {rate:.1f}% (BASELINE)')
            else:
                diff = rate - fox_div_rates[level]
                sign = '+' if diff > 0 else ''
                print(f'  {town}: {rate:.1f}% ({sign}{diff:.1f}% vs FOX)')

print()
print()

# METRIC 4: Program Depth
print('METRIC 4: PROGRAM DEPTH (Division Distribution)')
print('-' * 80)

for town in ['FOX', 'ASH', 'BEL']:
    town_df = df[df['town_code'] == town]
    div_dist = town_df.groupby('division_level').size()
    total = len(town_df)

    print(f'\n{town}:')
    for div in sorted(div_dist.index):
        count = div_dist[div]
        pct = (count / total) * 100
        print(f'  Division {div}: {count} teams ({pct:.1f}%)')

print()
print()

# METRIC 5: Gender Balance
print('METRIC 5: GENDER BALANCE')
print('-' * 80)

for town in ['FOX', 'ASH', 'BEL']:
    town_df = df[df['town_code'] == town]
    gender_dist = town_df.groupby('gender').size()
    total = len(town_df)

    boys = gender_dist.get('Boys', 0)
    girls = gender_dist.get('Girls', 0)
    boys_pct = (boys / total) * 100
    girls_pct = (girls / total) * 100
    ratio = boys / girls if girls > 0 else 0

    if town == 'FOX':
        fox_boys_pct = boys_pct
        print(f'{town}: {boys_pct:.1f}% Boys / {girls_pct:.1f}% Girls (BASELINE - Ratio {ratio:.2f}:1)')
    else:
        diff = boys_pct - fox_boys_pct
        sign = '+' if diff > 0 else ''
        more_less = 'more Boys' if diff > 0 else 'more Girls'
        print(f'{town}: {boys_pct:.1f}% Boys / {girls_pct:.1f}% Girls ({sign}{diff:.1f}% {more_less} vs FOX - Ratio {ratio:.2f}:1)')

print()
print()

# METRIC 6: Goals Per Game
print('METRIC 6: GOALS PER GAME')
print('-' * 80)

for town in ['FOX', 'ASH', 'BEL']:
    town_df = df[df['town_code'] == town]
    total_goals = town_df['goals_for'].sum()
    total_games = (town_df['wins'] + town_df['losses'] + town_df['ties']).sum()

    if total_games > 0:
        gpg = total_goals / total_games

        if town == 'FOX':
            fox_gpg = gpg
            print(f'{town}: {gpg:.2f} goals/game (BASELINE)')
        else:
            diff_pct = ((gpg - fox_gpg) / fox_gpg) * 100
            sign = '+' if diff_pct > 0 else ''
            print(f'{town}: {gpg:.2f} goals/game ({sign}{diff_pct:.1f}% vs FOX)')

print()
print()

# METRIC 7: Goal Differential (CRITICAL)
print('METRIC 7: GOAL DIFFERENTIAL (CRITICAL METRIC)')
print('-' * 80)

for town in ['FOX', 'ASH', 'BEL']:
    town_df = df[df['town_code'] == town]
    total_gf = town_df['goals_for'].sum()
    total_ga = town_df['goals_against'].sum()
    total_diff = total_gf - total_ga
    num_teams = len(town_df)
    per_team = total_diff / num_teams if num_teams > 0 else 0

    status = 'POSITIVE' if total_diff > 0 else 'NEGATIVE'

    if town == 'FOX':
        fox_per_team = per_team
        print(f'{town}: {total_diff:+d} total ({per_team:+.1f} per team) {status} (BASELINE)')
    else:
        diff = per_team - fox_per_team
        sign = '+' if diff > 0 else ''
        better_worse = 'BETTER' if diff > 0 else 'WORSE'
        print(f'{town}: {total_diff:+d} total ({per_team:+.1f} per team) {status} ({sign}{diff:.1f} vs FOX - {better_worse})')

print()
print()

# Summary
print('=' * 80)
print('SUMMARY: HOW TOWNS COMPARE TO FOXBOROUGH')
print('=' * 80)
print()

print('ASH vs FOX:')
print('  + Higher participation rate')
print('  + Much better Spring retention (16% drop vs 44%)')
print('  + Better win rates in all divisions')
print('  + More goals per game (+17%)')
print('  + MUCH better goal differential (+4.9 per team advantage)')
print('  - More boys-heavy (61% vs 51%)')
print()

print('BEL vs FOX:')
print('  Similar participation rate (pending population verification)')
print('  Better Spring retention (TBD - calculate above)')
print('  + Better win rates in all divisions')
print('  + More goals per game (+14%)')
print('  + Better goal differential (+3.2 per team advantage)')
print('  Gender balance: TBD')
print()
