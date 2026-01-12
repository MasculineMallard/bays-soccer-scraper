#!/usr/bin/env python3
"""Check completion status of all towns"""

import pandas as pd

df = pd.read_csv('data/bays_teams.csv')

print('=== DATABASE STATUS ===')
print()

for town in ['FOX', 'ASH', 'BEL', 'HOP', 'HOL', 'MAN', 'WAL']:
    town_df = df[df['town_code'] == town]
    seasons = town_df.groupby(['season_year', 'season_period']).size().reset_index(name='teams')
    seasons = seasons.sort_values(['season_year', 'season_period'], ascending=[False, False])

    print(f'{town}: {len(town_df)} teams, {len(seasons)} seasons')
    for _, row in seasons.iterrows():
        mark = '[X]' if row['teams'] > 0 else '[ ]'
        print(f'  {mark} {row["season_period"]} {row["season_year"]} - {row["teams"]} teams')
    print()

print(f'TOTAL: {len(df)} teams across all towns')
