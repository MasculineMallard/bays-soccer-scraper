"""
Convert ALL existing data from U8/U10/etc format to actual grade format

Mapping (reverse of what we had):
- U8 -> Grade 7/8 (younger kids, grades 7-8)
- U10 -> Grade 6
- U12 -> Grade 5
- U14 -> Grade 4
- U16 -> Grade 3
- U19 -> Grade 1/2 (or U912 for high school)
"""

import pandas as pd
import shutil
from datetime import datetime

# Backup first
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = f"data/bays_teams_BACKUP_{timestamp}.csv"

print("=" * 60)
print("CONVERTING ALL DATA TO GRADE FORMAT")
print("=" * 60)
print()

# Create backup
print(f"Creating backup: {backup_file}")
shutil.copy('data/bays_teams.csv', backup_file)
print("[OK] Backup created")
print()

# Load CSV
df = pd.read_csv('data/bays_teams.csv')
print(f"Total teams: {len(df)}")
print()

# Show current age_group distribution
print("Current age_group values:")
print(df['age_group'].value_counts().sort_index())
print()

# Mapping from U-format to Grade format
age_to_grade = {
    'U8': 'Grade 7/8',
    'U10': 'Grade 6',
    'U12': 'Grade 5',
    'U14': 'Grade 4',
    'U16': 'Grade 3',
    'U19': 'Grade 1/2',
    'U912': 'Grade 1/2',  # High school
}

# Apply mapping
df['age_group'] = df['age_group'].apply(lambda x: age_to_grade.get(x, x))

print("New age_group values:")
print(df['age_group'].value_counts().sort_index())
print()

# Save updated CSV
df.to_csv('data/bays_teams.csv', index=False)
print("[OK] Saved updated CSV")
print()

# Verify
df_verify = pd.read_csv('data/bays_teams.csv')
print("Verification:")
print(f"  Total teams: {len(df_verify)}")
print(f"  Age groups: {sorted(df_verify['age_group'].unique())}")
print()

print("Summary:")
print("-" * 60)
print(f"  Backup saved to: {backup_file}")
print(f"  All teams converted to Grade format")
print()
