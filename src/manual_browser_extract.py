"""
Manual Browser Data Extraction Guide

Since automated scraping is blocked by Cloudflare, this script provides
a simple manual extraction workflow.

STEPS:
1. Open https://bays.org/bays/organizations/view/FOX in your browser
2. Select "Fall 2024" season if not already selected
3. Copy the teams table (you can use browser DevTools or just select the table)
4. Paste the data below in the MANUAL_DATA section
5. Run this script to parse and save to CSV
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from csv_manager import CSVManager
from manual_data_entry import parse_division, create_team_record


# =============================================================================
# PASTE YOUR DATA HERE (one team per line, tab-separated)
# =============================================================================
# Format: Team Name [TAB] Division [TAB] W [TAB] L [TAB] T [TAB] GF [TAB] GA
#
# Example:
# Foxboro U12 Boys Blue    2/A    8    2    1    32    15
# Foxboro U14 Girls        3/B    5    4    2    22    18
#
MANUAL_DATA = """

"""
# =============================================================================


def parse_manual_data(data_str, town_code, town_name, season_year, season_period):
    """
    Parse manually pasted data into team records

    Args:
        data_str: Tab-separated data (one team per line)
        town_code: Town code (e.g., 'FOX')
        town_name: Full town name
        season_year: Year (e.g., 2024)
        season_period: 'Fall' or 'Spring'

    Returns:
        List of team record dictionaries
    """
    teams = []

    lines = [line.strip() for line in data_str.split('\n') if line.strip()]

    for line_num, line in enumerate(lines, 1):
        try:
            # Split by tabs
            parts = line.split('\t')

            if len(parts) < 7:
                print(f"[!]  Line {line_num}: Not enough columns - {parts}")
                continue

            team_name = parts[0].strip()
            division_str = parts[1].strip()
            wins = int(parts[2].strip())
            losses = int(parts[3].strip())
            ties = int(parts[4].strip())
            goals_for = int(parts[5].strip())
            goals_against = int(parts[6].strip())

            # Extract age group from team name
            age_group = None
            for age in ['U8', 'U10', 'U12', 'U14', 'U16', 'U19']:
                if age in team_name:
                    age_group = age
                    break

            # Extract gender from team name
            gender = None
            if 'Boys' in team_name:
                gender = 'Boys'
            elif 'Girls' in team_name:
                gender = 'Girls'
            else:
                gender = 'Coed'

            # Create team record
            team = create_team_record(
                town_code=town_code,
                town_name=town_name,
                town_population=None,  # Fill in later
                season_year=season_year,
                season_period=season_period,
                team_name=team_name,
                division_string=division_str,
                age_group=age_group,
                gender=gender,
                wins=wins,
                losses=losses,
                ties=ties,
                goals_for=goals_for,
                goals_against=goals_against
            )

            teams.append(team)

            print(f"[OK] Parsed: {team_name} ({division_str}) - {wins}-{losses}-{ties}")

        except Exception as e:
            print(f"[X] Error parsing line {line_num}: {line}")
            print(f"    {str(e)}")

    return teams


def save_to_csv(teams):
    """Save teams to CSV using CSVManager"""
    if not teams:
        print("[!]  No teams to save")
        return

    manager = CSVManager()
    added, skipped = manager.append_teams(teams)

    print()
    print(f"[OK] Saved {added} teams to CSV")
    if skipped > 0:
        print(f"[!]  Skipped {skipped} duplicates")


if __name__ == "__main__":
    print("=" * 60)
    print("Manual Browser Data Extraction")
    print("=" * 60)
    print()

    if not MANUAL_DATA.strip():
        print("[!]  No data found in MANUAL_DATA section")
        print()
        print("=" * 60)
        print("INSTRUCTIONS")
        print("=" * 60)
        print()
        print("1. Open your browser and go to:")
        print("   https://bays.org/bays/organizations/view/FOX")
        print()
        print("2. Select 'Fall 2024' season")
        print()
        print("3. Find the teams table and copy it")
        print()
        print("4. Paste the data in this script in the MANUAL_DATA section")
        print("   Format: Team Name [TAB] Division [TAB] W [TAB] L [TAB] T [TAB] GF [TAB] GA")
        print()
        print("5. Run this script again")
        print()
        print("=" * 60)
        print()
        print("ALTERNATIVE: Use browser console to extract data")
        print()
        print("Open browser console (F12) and run this JavaScript:")
        print()
        print("""
// Extract table data and copy to clipboard
let table = document.querySelector('table');
let rows = Array.from(table.querySelectorAll('tr')).slice(1); // Skip header
let data = rows.map(row => {
    let cells = Array.from(row.querySelectorAll('td')).map(cell => cell.innerText.trim());
    return cells.join('\\t');
}).join('\\n');
console.log(data);
copy(data); // Copies to clipboard
alert('Table data copied to clipboard!');
        """)
        print()

    else:
        # Parse the data
        print("Parsing manual data...")
        print()

        teams = parse_manual_data(
            MANUAL_DATA,
            town_code='FOX',
            town_name='Foxborough Youth Soccer',
            season_year=2024,
            season_period='Fall'
        )

        print()
        print(f"Total teams parsed: {len(teams)}")
        print()

        # Save to CSV
        if teams:
            save_to_csv(teams)

        print()
        print("=" * 60)
        print("Complete")
        print("=" * 60)
