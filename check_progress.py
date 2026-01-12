import pandas as pd

df = pd.read_csv('data/bays_teams.csv')
print(f'Total teams: {len(df)}')
print()

seasons = df.groupby(['season_year', 'season_period']).size().reset_index(name='count')
seasons = seasons.sort_values(['season_year', 'season_period'], ascending=[False, False])

print('Teams by season:')
for _, row in seasons.iterrows():
    print(f"  {row['season_period']} {row['season_year']}: {row['count']} teams")

print()
print(f"Unique towns: {df['town_code'].nunique()}")
print(f"Total seasons scraped: {len(seasons)}")
