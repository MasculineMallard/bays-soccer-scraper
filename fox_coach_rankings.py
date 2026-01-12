#!/usr/bin/env python3
"""
Foxborough Coach Rankings Analysis
Ranks all FOX coaches by win percentage with 3+ season minimum
"""

import pandas as pd

df = pd.read_csv('data/bays_teams.csv')
fox_df = df[df['town_code'] == 'FOX']

coaches = {}
for _, team in fox_df.iterrows():
    coach = team['head_coach']
    if pd.isna(coach) or coach.strip() == '' or coach.lower() == 'none':
        continue

    if coach not in coaches:
        coaches[coach] = {
            'seasons': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'total_games': 0, 'gd': 0
        }

    coaches[coach]['seasons'] += 1
    coaches[coach]['wins'] += int(team['wins'])
    coaches[coach]['losses'] += int(team['losses'])
    coaches[coach]['ties'] += int(team['ties'])
    coaches[coach]['total_games'] += int(team['wins'] + team['losses'] + team['ties'])
    coaches[coach]['gd'] += int(team['goal_differential'])

# Filter for 3+ seasons
qualified_coaches = {name: stats for name, stats in coaches.items() if stats['seasons'] >= 3}

# Calculate win percentage and avg GD
for coach, stats in qualified_coaches.items():
    if stats['total_games'] > 0:
        stats['win_pct'] = ((stats['wins'] + 0.5 * stats['ties']) / stats['total_games']) * 100
    else:
        stats['win_pct'] = 0.0
    stats['avg_gd'] = stats['gd'] / stats['seasons']

# Sort by win percentage
sorted_coaches = sorted(qualified_coaches.items(), key=lambda x: x[1]['win_pct'], reverse=True)

print('=' * 110)
print('FOXBOROUGH COACHES - COMPLETE RANKINGS (3+ Season Minimum)')
print('=' * 110)
print()
print(f'Total Qualified Coaches: {len(sorted_coaches)}')
print()
print(f'{"Rank":<6} {"Coach":<25} {"Seas":<5} {"Record":<16} {"Win %":<9} {"GD":<10} {"Games":<6}')
print('-' * 110)

for i, (coach, stats) in enumerate(sorted_coaches, 1):
    record = f"{stats['wins']}-{stats['losses']}-{stats['ties']}"
    avg_gd = stats['avg_gd']
    print(f'{i:<6} {coach:<25} {stats["seasons"]:<5} {record:<16} {stats["win_pct"]:.1f}%{"":5} {avg_gd:+6.2f}{"":4} {stats["total_games"]:<6}')

print()
print('=' * 110)
print('GD = Average Goal Differential per Season')
print('=' * 110)
