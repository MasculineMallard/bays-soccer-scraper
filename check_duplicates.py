import pandas as pd

df = pd.read_csv('data/bays_teams.csv')

print("=" * 60)
print("CHECKING FOR DUPLICATES")
print("=" * 60)
print()

# Check for exact duplicates across all key fields
duplicates = df.duplicated(subset=['town_code', 'team_name', 'season_year', 'season_period',
                                     'age_group', 'gender', 'division_level', 'division_tier'],
                            keep=False)

print(f"Total rows in CSV: {len(df)}")
print(f"Duplicate rows: {duplicates.sum()}")
print()

if duplicates.sum() > 0:
    print("Sample duplicate entries:")
    print("-" * 60)
    dup_df = df[duplicates][['town_code', 'team_name', 'season_year', 'season_period',
                              'age_group', 'gender', 'division_level', 'division_tier']].head(20)
    print(dup_df)
    print()

# Check team counts by town per season
print("=" * 60)
print("TEAMS BY TOWN - SAMPLE SEASONS")
print("=" * 60)
print()

for season_year in [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018]:
    for period in ['Fall', 'Spring']:
        season_data = df[(df['season_year'] == season_year) & (df['season_period'] == period)]
        if len(season_data) > 0:
            print(f"{period} {season_year}:")
            town_counts = season_data.groupby('town_code').size().sort_index()
            for town, count in town_counts.items():
                print(f"  {town}: {count:2} teams")
            print(f"  TOTAL: {len(season_data)} teams")
            print()
            break  # Just show one season per year
    else:
        continue
    break  # Just show first few seasons
