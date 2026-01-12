"""
Import Medway (MDY) data in chunks
Just paste each chunk when prompted
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from universal_import import save_and_import

def import_chunk():
    """Import one chunk of data"""

    print("=" * 60)
    print("MEDWAY DATA IMPORT")
    print("=" * 60)
    print()

    # Get season info
    print("Season options:")
    print("  1. Fall 2025")
    print("  2. Spring 2025")
    print("  3. Fall 2024")
    print("  4. Spring 2024")
    print("  5. Fall 2023")
    print("  6. Spring 2023")
    print()

    season_choice = input("Choose season (1-6): ").strip()

    seasons = {
        '1': (2025, 'Fall'),
        '2': (2025, 'Spring'),
        '3': (2024, 'Fall'),
        '4': (2024, 'Spring'),
        '5': (2023, 'Fall'),
        '6': (2023, 'Spring'),
    }

    if season_choice not in seasons:
        print("[X] Invalid choice")
        return

    season_year, season_period = seasons[season_choice]

    print()
    print(f"Selected: {season_period} {season_year}")
    print()
    print("Paste the data below, then press Enter followed by Ctrl+Z and Enter:")
    print("-" * 60)

    # Read multi-line input
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass

    raw_data = '\n'.join(lines)

    if not raw_data.strip():
        print("[X] No data provided")
        return

    print()
    added, skipped = save_and_import(raw_data, 'MDY', season_year, season_period)

    print()
    print(f"[DONE] {season_period} {season_year} - Added {added} teams")
    print()

    # Ask if more chunks
    more = input("Import another chunk? (y/n): ").strip().lower()
    if more == 'y':
        print()
        import_chunk()

if __name__ == "__main__":
    import_chunk()
