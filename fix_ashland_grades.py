"""
Fix Ashland Fall 2025 data - correct grade mapping
Grade number = actual school grade, not age group
"""

import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager

# Load CSV
df = pd.read_csv('data/bays_teams.csv')

print("=" * 60)
print("FIXING ASHLAND FALL 2025 GRADE MAPPING")
print("=" * 60)
print()

# Show current incorrect mapping
ash_fall2025 = df[(df['town_code'] == 'ASH') & (df['season_year'] == 2025) & (df['season_period'] == 'Fall')]
print(f"Found {len(ash_fall2025)} Ashland Fall 2025 teams")
print()
print("Current INCORRECT age_group values:")
print(ash_fall2025['age_group'].value_counts().sort_index())
print()

# Remove Ashland Fall 2025 data (we'll re-import with correct grades)
df_cleaned = df[~((df['town_code'] == 'ASH') & (df['season_year'] == 2025) & (df['season_period'] == 'Fall'))]

print(f"Removed {len(ash_fall2025)} Ashland teams")
print(f"Remaining teams: {len(df_cleaned)}")
print()

# Save cleaned CSV
df_cleaned.to_csv('data/bays_teams.csv', index=False)
print("[OK] CSV cleaned, ready for re-import with correct grades")
print()
