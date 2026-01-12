"""
Batch import all Ashland seasons
"""

import sys
sys.path.append('.')
from universal_import import save_and_import

# Read all saved files
with open('data/pastes/ASH_Fall2023_raw.txt', 'r', encoding='utf-8') as f:
    fall2023 = f.read()

with open('data/pastes/ASH_Spring2023_raw.txt', 'r', encoding='utf-8') as f:
    spring2023 = f.read()

with open('data/pastes/ASH_Fall2022_raw.txt', 'r', encoding='utf-8') as f:
    fall2022 = f.read()

with open('data/pastes/ASH_Spring2022_raw.txt', 'r', encoding='utf-8') as f:
    spring2022 = f.read()

with open('data/pastes/ASH_Fall2021_raw.txt', 'r', encoding='utf-8') as f:
    fall2021 = f.read()

with open('data/pastes/ASH_Spring2021_raw.txt', 'r', encoding='utf-8') as f:
    spring2021 = f.read()

print("=" * 60)
print("BATCH IMPORTING ALL ASHLAND SEASONS")
print("=" * 60)
print()

seasons = [
    (fall2023, 'ASH', 2023, 'Fall'),
    (spring2023, 'ASH', 2023, 'Spring'),
    (fall2022, 'ASH', 2022, 'Fall'),
    (spring2022, 'ASH', 2022, 'Spring'),
    (fall2021, 'ASH', 2021, 'Fall'),
    (spring2021, 'ASH', 2021, 'Spring'),
]

total_added = 0
for data, town, year, period in seasons:
    print(f"\n{'='*60}")
    print(f"IMPORTING {town} {period} {year}")
    print('='*60)
    added, skipped = save_and_import(data, town, year, period)
    total_added += added

print()
print("=" * 60)
print(f"BATCH IMPORT COMPLETE: {total_added} total teams added")
print("=" * 60)
