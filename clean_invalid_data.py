"""
Clean invalid historical data from CSV

Keep ONLY Fall 2024 data (273 teams) - the only confirmed valid season.
All other seasons are duplicated Fall 2025 data and must be removed.
"""

import pandas as pd
import shutil
from datetime import datetime

# Backup the original CSV first
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = f"data/bays_teams_BACKUP_{timestamp}.csv"

print("=" * 60)
print("CLEANING INVALID DATA FROM CSV")
print("=" * 60)
print()

# Create backup
print(f"Creating backup: {backup_file}")
shutil.copy('data/bays_teams.csv', backup_file)
print("[OK] Backup created")
print()

# Load CSV
df = pd.read_csv('data/bays_teams.csv')
print(f"Current total teams: {len(df)}")
print()

# Show what we're keeping vs removing
fall2024 = df[(df['season_year'] == 2024) & (df['season_period'] == 'Fall')]
print(f"Fall 2024 teams (VALID - keeping): {len(fall2024)}")

invalid = df[~((df['season_year'] == 2024) & (df['season_period'] == 'Fall'))]
print(f"Other seasons (INVALID - removing): {len(invalid)}")
print()

if len(invalid) > 0:
    print("Seasons being removed:")
    for (year, period), count in invalid.groupby(['season_year', 'season_period']).size().items():
        print(f"  {period} {year}: {count} teams")
    print()

# Keep only Fall 2024
df_clean = fall2024.copy()

# Save cleaned CSV
df_clean.to_csv('data/bays_teams.csv', index=False)
print(f"[OK] Saved cleaned CSV: {len(df_clean)} teams")
print()

# Verify
df_verify = pd.read_csv('data/bays_teams.csv')
print("Verification:")
print(f"  Total teams: {len(df_verify)}")
print(f"  Unique seasons: {df_verify[['season_year', 'season_period']].drop_duplicates().shape[0]}")
print(f"  Season: {df_verify['season_period'].iloc[0]} {df_verify['season_year'].iloc[0]}")
print()

print("Summary:")
print("-" * 60)
print(f"  Backup saved to: {backup_file}")
print(f"  Teams removed: {len(invalid)}")
print(f"  Teams remaining: {len(df_clean)}")
print(f"  CSV is now clean with ONLY valid Fall 2024 data")
print()
