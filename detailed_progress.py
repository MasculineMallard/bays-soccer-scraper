import pandas as pd

df = pd.read_csv('data/bays_teams.csv')

print("=" * 60)
print("SCRAPING PROGRESS REPORT")
print("=" * 60)
print()
print(f"Total teams collected: {len(df)}")
print(f"Unique towns: {df['town_code'].nunique()}")
print()

# Group by season and count teams
seasons = df.groupby(['season_year', 'season_period']).agg({
    'team_name': 'count',
    'town_code': 'nunique'
}).reset_index()
seasons.columns = ['year', 'period', 'teams', 'towns']
seasons = seasons.sort_values(['year', 'period'], ascending=[False, False])

print("Teams per season:")
print("-" * 60)
for _, row in seasons.iterrows():
    status = "[OK]" if row['teams'] >= 270 else "[..]"
    print(f"{status} {row['period']:6} {row['year']}: {row['teams']:3} teams from {row['towns']} towns")

print()
print(f"Seasons completed: {len(seasons)}")
print(f"Expected total seasons: 22 (Fall 2025 - Fall 2015)")
print()

# Show breakdown by town for latest incomplete season if exists
incomplete = seasons[seasons['teams'] < 270]
if not incomplete.empty:
    latest = incomplete.iloc[0]
    print(f"Currently scraping: {latest['period']} {latest['year']}")
    print("-" * 60)

    current_season = df[(df['season_year'] == latest['year']) &
                        (df['season_period'] == latest['period'])]
    town_counts = current_season.groupby('town_code').size().sort_index()

    for town, count in town_counts.items():
        print(f"  {town}: {count} teams")
    print()
