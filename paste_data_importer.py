"""
Interactive tool to paste manually collected data and import to CSV

Usage:
1. Run this script
2. Paste the table data you copied from BAYS.org
3. Enter town code and season info when prompted
4. Data will be automatically parsed and added to CSV
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record
from config.towns_config import TOWNS


def parse_pasted_data(raw_text, town_code, season_year, season_period):
    """Parse the pasted table data into team records"""

    town = TOWNS.get(town_code)
    if not town:
        print(f"[X] Unknown town code: {town_code}")
        return None

    teams = []
    lines = raw_text.strip().split('\n')

    # Grade to age mapping
    grade_to_age = {
        '8': 'U8', '7': 'U8',
        '6': 'U10',
        '5': 'U12',
        '4': 'U14',
        '3': 'U16',
        '2': 'U19', '1': 'U19',
        '912': 'U19'  # High school
    }

    for line in lines:
        # Skip empty lines and headers
        line = line.strip()
        if not line or line.startswith('Team') or line.startswith('Show'):
            continue

        # Split by tabs (copied from HTML table)
        parts = line.split('\t')

        if len(parts) < 13:
            continue

        try:
            team_name = parts[0].strip()
            team_num = parts[1].strip()
            gads = parts[2].strip()
            wins = int(parts[3].strip())
            losses = int(parts[4].strip())
            ties = int(parts[5].strip())
            forfeits = int(parts[6].strip())
            points = int(parts[7].strip())
            goals_for = int(parts[8].strip())
            goals_against = int(parts[9].strip())
            goal_diff = int(parts[10].strip())
            head_coach = parts[11].strip() if len(parts) > 11 and parts[11].strip() else None
            assistant_coach = parts[12].strip() if len(parts) > 12 and parts[12].strip() else None

            # Parse GADS (Gender Age Division/Section)
            # Format: "Boys 8 2/C" or "Girls 6 4/A"
            gads_parts = gads.split()
            if len(gads_parts) >= 3:
                gender = gads_parts[0]  # Boys/Girls
                grade = gads_parts[1]   # 8, 6, 5, etc.
                div_info = gads_parts[2]  # 2/C, 4/A, etc.

                # Parse division
                if '/' in div_info:
                    div_level, div_tier = div_info.split('/', 1)
                else:
                    div_level = div_info
                    div_tier = ''

                age_group = grade_to_age.get(grade, f'U{grade}')
                division_string = f"{div_level}/{div_tier}" if div_tier else div_level

                # Clean coach names
                if head_coach in ['None', '', 'none']:
                    head_coach = None
                if assistant_coach in ['None', '', 'none']:
                    assistant_coach = None

                # Create team record
                team = create_team_record(
                    town_code=town_code,
                    town_name=town['name'],
                    town_population=town.get('population'),
                    season_year=season_year,
                    season_period=season_period,
                    team_name=team_name,
                    division_string=division_string,
                    age_group=age_group,
                    gender=gender,
                    wins=wins,
                    losses=losses,
                    ties=ties,
                    goals_for=goals_for,
                    goals_against=goals_against,
                    goal_differential=goal_diff,
                    points=points,
                    head_coach=head_coach,
                    assistant_coach=assistant_coach
                )

                teams.append(team)

        except Exception as e:
            print(f"[!] Error parsing line: {line[:50]}... - {e}")
            continue

    return teams


def main():
    print("=" * 60)
    print("MANUAL DATA IMPORT TOOL")
    print("=" * 60)
    print()

    # Get town code
    print("Town codes: FOX, ASH, BEL, HOL, HOP, MDY, NOB, SUD, WAL, WSB")
    town_code = input("Enter town code: ").strip().upper()

    if town_code not in TOWNS:
        print(f"[X] Invalid town code: {town_code}")
        return

    # Get season info
    season_year = int(input("Enter season year (e.g., 2023): ").strip())
    season_period = input("Enter season period (Fall/Spring): ").strip().capitalize()

    if season_period not in ['Fall', 'Spring']:
        print(f"[X] Invalid season period: {season_period}")
        return

    print()
    print("Paste the table data below (copy from BAYS.org), then press Enter twice:")
    print("-" * 60)

    # Collect pasted data
    lines = []
    while True:
        try:
            line = input()
            if not line and lines:  # Two enters to finish
                break
            lines.append(line)
        except EOFError:
            break

    raw_text = '\n'.join(lines)

    if not raw_text.strip():
        print("[X] No data provided")
        return

    print()
    print("[*] Parsing data...")

    teams = parse_pasted_data(raw_text, town_code, season_year, season_period)

    if not teams:
        print("[X] No teams parsed. Check the format.")
        return

    print(f"[OK] Parsed {len(teams)} teams")
    print()

    # Show sample
    print("First 3 teams:")
    for team in teams[:3]:
        print(f"  {team['team_name']}: {team['wins']}-{team['losses']}-{team['ties']}")
    print()

    # Confirm before saving
    confirm = input(f"Add {len(teams)} teams to CSV? (yes/no): ").strip().lower()

    if confirm != 'yes':
        print("Cancelled")
        return

    # Add to CSV
    manager = CSVManager('data/bays_teams.csv')
    added, skipped = manager.append_teams(teams)

    print()
    print(f"[OK] Added {added} new teams")
    if skipped > 0:
        print(f"[!] Skipped {skipped} duplicates")
    print()


if __name__ == "__main__":
    main()
