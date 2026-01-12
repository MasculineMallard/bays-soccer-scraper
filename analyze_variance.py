import pandas as pd

df = pd.read_csv('data/bays_teams.csv')

print("=" * 60)
print("TEAM COUNT VARIANCE ANALYSIS")
print("=" * 60)
print()

# Check if team counts vary by season for each town
for town in sorted(df['town_code'].unique()):
    town_data = df[df['town_code'] == town]
    season_counts = town_data.groupby(['season_year', 'season_period']).size()

    print(f"{town}:")
    print("-" * 40)

    for (year, period), count in season_counts.sort_index(ascending=False).items():
        print(f"  {period:6} {year}: {count:2} teams")

    unique_counts = season_counts.unique()
    if len(unique_counts) == 1:
        print(f"  WARNING: Same count ({unique_counts[0]}) for all seasons!")
    else:
        print(f"  Range: {season_counts.min()} - {season_counts.max()} teams")

    print()
