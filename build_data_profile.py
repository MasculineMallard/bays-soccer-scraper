"""
Build a data profile from Fall 2024 (known good data)
This profile will be used to validate future scrapes
"""

import pandas as pd
import json

# Load the CSV
df = pd.read_csv('data/bays_teams.csv')

# Filter to ONLY Fall 2024 (known good data)
fall2024 = df[(df['season_year'] == 2024) & (df['season_period'] == 'Fall')].copy()

print("=" * 60)
print("BUILDING DATA PROFILE FROM FALL 2024")
print("=" * 60)
print()

# Create profile
profile = {
    'season': 'Fall 2024',
    'total_teams': len(fall2024),
    'date_collected': fall2024['scrape_date'].iloc[0] if len(fall2024) > 0 else None,

    # Teams per town (this should be relatively stable year-over-year)
    'teams_per_town': {},

    # Age group distribution
    'age_groups': {},

    # Gender distribution
    'gender_distribution': {},

    # Division levels
    'division_levels': {},

    # Statistical ranges (for validation)
    'stats_ranges': {
        'wins': {'min': int(fall2024['wins'].min()), 'max': int(fall2024['wins'].max()), 'mean': float(fall2024['wins'].mean())},
        'losses': {'min': int(fall2024['losses'].min()), 'max': int(fall2024['losses'].max()), 'mean': float(fall2024['losses'].mean())},
        'goals_for': {'min': int(fall2024['goals_for'].min()), 'max': int(fall2024['goals_for'].max()), 'mean': float(fall2024['goals_for'].mean())},
        'goals_against': {'min': int(fall2024['goals_against'].min()), 'max': int(fall2024['goals_against'].max()), 'mean': float(fall2024['goals_against'].mean())},
    },

    # Expected team name patterns per town (sample)
    'team_name_samples': {},
}

# Fill in town-specific data
for town in sorted(fall2024['town_code'].unique()):
    town_data = fall2024[fall2024['town_code'] == town]
    profile['teams_per_town'][town] = {
        'count': len(town_data),
        'age_groups': sorted(town_data['age_group'].unique().tolist()),
        'sample_names': town_data['team_name'].head(3).tolist(),
    }

# Age groups
for ag in sorted(fall2024['age_group'].unique()):
    profile['age_groups'][ag] = int((fall2024['age_group'] == ag).sum())

# Gender distribution
for gender in ['Boys', 'Girls', 'Coed']:
    count = int((fall2024['gender'] == gender).sum())
    if count > 0:
        profile['gender_distribution'][gender] = count

# Division levels
for div in sorted(fall2024['division_level'].unique()):
    profile['division_levels'][str(div)] = int((fall2024['division_level'] == div).sum())

# Save profile
with open('data/fall2024_profile.json', 'w') as f:
    json.dump(profile, f, indent=2)

# Print summary
print("Fall 2024 Profile:")
print("-" * 60)
print(f"Total teams: {profile['total_teams']}")
print()

print("Teams by town:")
for town, data in profile['teams_per_town'].items():
    print(f"  {town}: {data['count']:2} teams  (sample: {data['sample_names'][0] if data['sample_names'] else 'N/A'})")

print()
print(f"Age groups: {', '.join(profile['age_groups'].keys())}")
print(f"Gender: Boys={profile['gender_distribution'].get('Boys', 0)}, " +
      f"Girls={profile['gender_distribution'].get('Girls', 0)}, " +
      f"Coed={profile['gender_distribution'].get('Coed', 0)}")

print()
print("Stats ranges (for validation):")
print(f"  Wins: {profile['stats_ranges']['wins']['min']}-{profile['stats_ranges']['wins']['max']} (avg: {profile['stats_ranges']['wins']['mean']:.1f})")
print(f"  Losses: {profile['stats_ranges']['losses']['min']}-{profile['stats_ranges']['losses']['max']} (avg: {profile['stats_ranges']['losses']['mean']:.1f})")
print(f"  Goals For: {profile['stats_ranges']['goals_for']['min']}-{profile['stats_ranges']['goals_for']['max']} (avg: {profile['stats_ranges']['goals_for']['mean']:.1f})")
print(f"  Goals Against: {profile['stats_ranges']['goals_against']['min']}-{profile['stats_ranges']['goals_against']['max']} (avg: {profile['stats_ranges']['goals_against']['mean']:.1f})")

print()
print("Profile saved to: data/fall2024_profile.json")
print()
