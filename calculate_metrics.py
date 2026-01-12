"""
Calculate metrics 3-7 for current data
"""
import pandas as pd
import numpy as np

df = pd.read_csv('data/bays_teams.csv')
df_clean = df[df['town_code'].isin(['FOX', 'ASH', 'BEL'])].copy()

print('=' * 80)
print('METRIC 3: WIN RATE BY DIVISION LEVEL')
print('=' * 80)
print()

# Calculate win percentage
def calc_win_pct(row):
    total = row['wins'] + row['losses'] + row['ties']
    if total == 0:
        return 0
    return (row['wins'] + 0.5 * row['ties']) / total * 100

df_clean['win_pct'] = df_clean.apply(calc_win_pct, axis=1)

# Group by town and division level
division_perf = df_clean.groupby(['town_code', 'division_level']).agg({
    'wins': 'sum',
    'losses': 'sum',
    'ties': 'sum',
    'team_name': 'count',
    'win_pct': 'mean'
}).reset_index()
division_perf.columns = ['town_code', 'division_level', 'total_wins', 'total_losses', 'total_ties', 'num_teams', 'avg_win_pct']

print('Win Rate by Division Level:')
print()
for level in sorted(division_perf['division_level'].unique()):
    print(f'Division {level}:')
    level_data = division_perf[division_perf['division_level'] == level]
    for _, row in level_data.iterrows():
        total_games = row['total_wins'] + row['total_losses'] + row['total_ties']
        print(f"  {row['town_code']}: {row['avg_win_pct']:.1f}% avg ({int(row['total_wins'])}-{int(row['total_losses'])}-{int(row['total_ties'])} across {int(row['num_teams'])} teams)")
    print()

print()
print('=' * 80)
print('METRIC 4: PROGRAM DEPTH (DIVISION DISTRIBUTION)')
print('=' * 80)
print()

# Count teams by division for each town
div_dist = df_clean.groupby(['town_code', 'division_level']).size().reset_index(name='team_count')
town_totals = df_clean.groupby('town_code').size().reset_index(name='total_teams')

div_dist = div_dist.merge(town_totals, on='town_code')
div_dist['pct_of_teams'] = (div_dist['team_count'] / div_dist['total_teams'] * 100).round(1)

print('Distribution of Teams by Division Level:')
print()
for town in ['FOX', 'ASH']:
    town_data = div_dist[div_dist['town_code'] == town]
    print(f'{town}:')
    for _, row in town_data.iterrows():
        print(f"  Division {int(row['division_level'])}: {int(row['team_count'])} teams ({row['pct_of_teams']}%)")

    # Program strength indicator
    div2_pct = town_data[town_data['division_level'] == 2]['pct_of_teams'].values
    div2_pct = div2_pct[0] if len(div2_pct) > 0 else 0
    div34_pct = town_data[town_data['division_level'].isin([3, 4])]['pct_of_teams'].sum()

    if div2_pct > div34_pct:
        strength = 'STRONG (more Division 2 teams)'
    elif div2_pct > 30:
        strength = 'MODERATE (balanced across divisions)'
    else:
        strength = 'DEVELOPING (more Division 3/4 teams)'

    print(f'  Program Strength: {strength}')
    print()

print()
print('=' * 80)
print('METRIC 5: GENDER BALANCE')
print('=' * 80)
print()

# Count by gender
gender_dist = df_clean.groupby(['town_code', 'gender']).size().reset_index(name='team_count')
gender_totals = df_clean.groupby('town_code').size().reset_index(name='total_teams')
gender_dist = gender_dist.merge(gender_totals, on='town_code')
gender_dist['pct'] = (gender_dist['team_count'] / gender_dist['total_teams'] * 100).round(1)

print('Gender Distribution:')
print()
for town in ['FOX', 'ASH']:
    town_data = gender_dist[gender_dist['town_code'] == town]
    print(f'{town}:')
    boys = town_data[town_data['gender'] == 'Boys']['team_count'].values[0] if len(town_data[town_data['gender'] == 'Boys']) > 0 else 0
    girls = town_data[town_data['gender'] == 'Girls']['team_count'].values[0] if len(town_data[town_data['gender'] == 'Girls']) > 0 else 0

    for _, row in town_data.iterrows():
        print(f"  {row['gender']}: {int(row['team_count'])} teams ({row['pct']}%)")

    # Boys/Girls ratio
    if girls > 0:
        ratio = boys / girls
        print(f'  Boys/Girls Ratio: {ratio:.2f}:1')
        if ratio > 1.2:
            print(f'  Balance: Boys-heavy')
        elif ratio < 0.8:
            print(f'  Balance: Girls-heavy')
        else:
            print(f'  Balance: Well-balanced')
    print()

print()
print('=' * 80)
print('METRIC 6: GOALS PER GAME')
print('=' * 80)
print()

# Calculate goals per game
df_clean['total_games'] = df_clean['wins'] + df_clean['losses'] + df_clean['ties']
df_clean['goals_per_game'] = df_clean.apply(
    lambda row: row['goals_for'] / row['total_games'] if row['total_games'] > 0 else 0,
    axis=1
)

# By town
goals_by_town = df_clean.groupby('town_code').agg({
    'goals_for': 'sum',
    'total_games': 'sum',
    'goals_per_game': 'mean'
}).reset_index()

print('Average Goals Per Game (Overall):')
print()
for _, row in goals_by_town.iterrows():
    avg_gpg = row['goals_for'] / row['total_games'] if row['total_games'] > 0 else 0
    print(f"{row['town_code']}: {avg_gpg:.2f} goals/game ({int(row['goals_for'])} goals in {int(row['total_games'])} games)")

print()
print('By Division Level:')
print()
goals_by_div = df_clean.groupby(['town_code', 'division_level']).agg({
    'goals_for': 'sum',
    'total_games': 'sum'
}).reset_index()
goals_by_div['gpg'] = goals_by_div['goals_for'] / goals_by_div['total_games']

for level in sorted(goals_by_div['division_level'].unique()):
    print(f'Division {level}:')
    level_data = goals_by_div[goals_by_div['division_level'] == level]
    for _, row in level_data.iterrows():
        print(f"  {row['town_code']}: {row['gpg']:.2f} goals/game")
    print()

print()
print('=' * 80)
print('METRIC 7: GOAL DIFFERENTIAL')
print('=' * 80)
print()

# Calculate goal differential
goal_diff = df_clean.groupby('town_code').agg({
    'goals_for': 'sum',
    'goals_against': 'sum',
    'team_name': 'count'
}).reset_index()
goal_diff['total_diff'] = goal_diff['goals_for'] - goal_diff['goals_against']
goal_diff['avg_diff_per_team'] = goal_diff['total_diff'] / goal_diff['team_name']

print('Goal Differential (Overall):')
print()
for _, row in goal_diff.iterrows():
    status = 'POSITIVE' if row['total_diff'] > 0 else 'NEGATIVE'
    print(f"{row['town_code']}: {row['total_diff']:+d} total ({row['avg_diff_per_team']:+.1f} per team) {status}")
    print(f"  Scored {int(row['goals_for'])} | Conceded {int(row['goals_against'])}")

print()
print('By Division Level:')
print()
diff_by_div = df_clean.groupby(['town_code', 'division_level']).agg({
    'goals_for': 'sum',
    'goals_against': 'sum',
    'team_name': 'count'
}).reset_index()
diff_by_div['diff'] = diff_by_div['goals_for'] - diff_by_div['goals_against']
diff_by_div['avg_diff'] = diff_by_div['diff'] / diff_by_div['team_name']

for level in sorted(diff_by_div['division_level'].unique()):
    print(f'Division {level}:')
    level_data = diff_by_div[diff_by_div['division_level'] == level]
    for _, row in level_data.iterrows():
        status = 'POSITIVE' if row['diff'] > 0 else 'NEGATIVE'
        print(f"  {row['town_code']}: {row['diff']:+d} total ({row['avg_diff']:+.1f} per team) {status}")
    print()
