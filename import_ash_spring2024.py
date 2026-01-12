#!/usr/bin/env python3
"""Import ASH Spring 2024 data"""

from universal_import import save_and_import

# Read the paste file
with open('data/pastes/ASH_Spring2024_raw.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

# Import it
save_and_import(raw_data, 'ASH', 2024, 'Spring')
