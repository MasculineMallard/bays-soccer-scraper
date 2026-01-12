#!/usr/bin/env python3
"""
AUTO-SAVE PASTE MONITOR
Automatically saves any paste containing 'youth soccer' to dump file
Then allows parsing and importing from the dump file

WORKFLOW:
1. User pastes data containing 'youth soccer'
2. Script detects it and appends to dump file with timestamp
3. Script can later parse dump file to find missing seasons
4. Script imports cleaned data to CSV
"""

import os
from datetime import datetime
import re


DUMP_FILE = 'data/pastes/paste_dump.txt'
SEPARATOR = '\n' + '='*80 + '\n'


def append_to_dump(paste_content):
    """
    Append pasted content to dump file with timestamp and separator

    Args:
        paste_content: Raw pasted text

    Returns:
        bool: True if saved, False if not soccer data
    """
    # Check if this is soccer data
    if 'youth' not in paste_content.lower() or 'soccer' not in paste_content.lower():
        return False

    # Ensure directory exists
    os.makedirs('data/pastes', exist_ok=True)

    # Create header with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"PASTE TIMESTAMP: {timestamp}\n"

    # Append to dump file
    with open(DUMP_FILE, 'a', encoding='utf-8') as f:
        f.write(SEPARATOR)
        f.write(header)
        f.write(SEPARATOR)
        f.write(paste_content)
        f.write('\n')

    print(f"[OK] Saved paste to dump file at {timestamp}")
    return True


def extract_town_season_from_paste(paste_content):
    """
    Extract town code and season info from paste content

    Looks for patterns like:
    - "Ashland Youth Soccer" -> ASH
    - "Fall 2024" or "Spring 2024" in header

    Returns:
        tuple: (town_code, season_year, season_period) or (None, None, None)
    """
    lines = paste_content.strip().split('\n')

    town_code = None
    season_year = None
    season_period = None

    # Town mapping
    town_mapping = {
        'ashland': 'ASH',
        'foxborough': 'FOX',
        'bellingham': 'BEL',
        'holliston': 'HOL',
        'hopkinton': 'HOP',
        'sudbury': 'SUD',
        'walpole': 'WAL',
        'westborough': 'WSB',
        'medway': 'MDY',
        'norwood': 'NWD',
        'franklin': 'FRA',
        'millis': 'MIL',
        'sherborn': 'SHE',
        'dover': 'DOV',
        'medfield': 'MED',
        'natick': 'NAT',
        'needham': 'NEE',
        'wellesley': 'WEL',
        'norton': 'NOR',
        'sharon': 'SHA',
        'canton': 'CAN',
        'stoughton': 'STO',
        'dedham': 'DED',
        'westwood': 'WWD',
        'norfolk': 'NOK'
    }

    # Search first 10 lines for town and season
    for line in lines[:10]:
        line_lower = line.lower()

        # Find town
        if 'youth soccer' in line_lower or 'youth soccer' in line_lower:
            for town_name, code in town_mapping.items():
                if town_name in line_lower:
                    town_code = code
                    break

        # Find season period and year
        if 'fall' in line_lower:
            season_period = 'Fall'
        elif 'spring' in line_lower:
            season_period = 'Spring'

        # Find year (4 digits)
        year_match = re.search(r'20\d{2}', line)
        if year_match:
            season_year = int(year_match.group())

    return town_code, season_year, season_period


def list_dump_entries():
    """
    List all entries in dump file with extracted metadata

    Returns:
        list: List of dicts with timestamp, town, season, content
    """
    if not os.path.exists(DUMP_FILE):
        print(f"[!] No dump file found at {DUMP_FILE}")
        return []

    with open(DUMP_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by separator
    entries = content.split(SEPARATOR)

    parsed_entries = []
    for entry in entries:
        if not entry.strip():
            continue

        # Extract timestamp
        timestamp_match = re.search(r'PASTE TIMESTAMP: (.+)', entry)
        if not timestamp_match:
            continue

        timestamp = timestamp_match.group(1)

        # Extract town and season
        town_code, season_year, season_period = extract_town_season_from_paste(entry)

        parsed_entries.append({
            'timestamp': timestamp,
            'town_code': town_code,
            'season_year': season_year,
            'season_period': season_period,
            'content': entry.strip()
        })

    return parsed_entries


def save_from_dump_to_paste_file(entry_index):
    """
    Save a specific dump entry to a proper paste file

    Args:
        entry_index: Index of entry from list_dump_entries()

    Returns:
        str: Path to saved paste file
    """
    entries = list_dump_entries()

    if entry_index < 0 or entry_index >= len(entries):
        print(f"[X] Invalid entry index. Must be 0-{len(entries)-1}")
        return None

    entry = entries[entry_index]

    if not entry['town_code'] or not entry['season_year'] or not entry['season_period']:
        print("[X] Could not extract town/season from paste. Manual intervention needed.")
        return None

    # Create filename
    filename = f"data/pastes/{entry['town_code']}_{entry['season_period']}{entry['season_year']}_raw.txt"

    # Extract just the table data (skip timestamp headers)
    lines = entry['content'].split('\n')
    table_start = 0
    for i, line in enumerate(lines):
        if 'Team\tTeam#\tGADS' in line:
            table_start = i
            break

    table_data = '\n'.join(lines[table_start:])

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(table_data)

    print(f"[OK] Saved to: {filename}")
    return filename


def check_missing_seasons():
    """
    Check dump file for any seasons not yet in CSV

    Returns:
        list: List of missing seasons found in dump
    """
    import pandas as pd

    # Get all seasons in dump
    dump_entries = list_dump_entries()

    # Get all seasons in CSV
    df = pd.read_csv('data/bays_teams.csv')

    csv_seasons = set()
    for _, row in df.iterrows():
        csv_seasons.add((row['town_code'], row['season_year'], row['season_period']))

    # Find missing
    missing = []
    for entry in dump_entries:
        if not entry['town_code'] or not entry['season_year'] or not entry['season_period']:
            continue

        key = (entry['town_code'], entry['season_year'], entry['season_period'])
        if key not in csv_seasons:
            missing.append(entry)

    return missing


def import_from_dump():
    """
    Interactive: Import any missing seasons from dump file
    """
    missing = check_missing_seasons()

    if not missing:
        print("[OK] No missing seasons found in dump file. All data is imported!")
        return

    print(f"[!] Found {len(missing)} seasons in dump that are NOT in CSV:")
    print()

    for i, entry in enumerate(missing):
        print(f"  [{i}] {entry['town_code']} {entry['season_period']} {entry['season_year']} (pasted {entry['timestamp']})")

    print()
    print("Import all? (y/n)")
    response = input().strip().lower()

    if response == 'y':
        from universal_import import save_and_import

        for entry in missing:
            print(f"\n[*] Importing {entry['town_code']} {entry['season_period']} {entry['season_year']}...")

            # Extract table data
            lines = entry['content'].split('\n')
            table_start = 0
            for i, line in enumerate(lines):
                if 'Team\tTeam#\tGADS' in line:
                    table_start = i
                    break

            table_data = '\n'.join(lines[table_start:])

            # Import
            save_and_import(table_data, entry['town_code'], entry['season_year'], entry['season_period'])

        print()
        print("[OK] All missing seasons imported!")


def main():
    """Main menu"""
    print("=" * 60)
    print("AUTO-SAVE PASTE MANAGER")
    print("=" * 60)
    print()
    print("Options:")
    print("  1. List all pastes in dump file")
    print("  2. Check for missing seasons (in dump but not CSV)")
    print("  3. Import missing seasons from dump")
    print("  4. Save specific dump entry to paste file")
    print()
    print("Choose option (1-4):")

    choice = input().strip()

    if choice == '1':
        entries = list_dump_entries()
        print()
        print(f"Found {len(entries)} entries in dump file:")
        print()
        for i, entry in enumerate(entries):
            town = entry['town_code'] or '???'
            period = entry['season_period'] or '???'
            year = entry['season_year'] or '????'
            print(f"  [{i}] {town} {period} {year} - {entry['timestamp']}")

    elif choice == '2':
        missing = check_missing_seasons()
        print()
        if missing:
            print(f"Found {len(missing)} seasons in dump NOT in CSV:")
            for entry in missing:
                print(f"  - {entry['town_code']} {entry['season_period']} {entry['season_year']}")
        else:
            print("[OK] No missing seasons. All dump data is imported!")

    elif choice == '3':
        import_from_dump()

    elif choice == '4':
        entries = list_dump_entries()
        print()
        print(f"Found {len(entries)} entries:")
        for i, entry in enumerate(entries):
            print(f"  [{i}] {entry['town_code']} {entry['season_period']} {entry['season_year']}")
        print()
        print("Enter entry number:")
        idx = int(input().strip())
        save_from_dump_to_paste_file(idx)

    else:
        print("[X] Invalid choice")


if __name__ == "__main__":
    main()
