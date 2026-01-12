"""
Template for importing manually collected BAYS data

Instructions:
1. Copy this file and rename it (e.g., import_ashland_fall2023.py)
2. Update TOWN_CODE, SEASON_YEAR, SEASON_PERIOD
3. Paste the raw data into RAW_DATA variable
4. Run the script

The script will:
- Parse the tab-separated data
- Convert grades correctly (7/8 -> Grade 7/8, etc.)
- Import to CSV with duplicate detection
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record
from config.towns_config import TOWNS

# ============================================================
# CONFIGURE THESE VALUES
# ============================================================
TOWN_CODE = 'ASH'  # Town code (e.g., 'FOX', 'ASH', 'BEL', etc.)
SEASON_YEAR = 2023  # Year (e.g., 2023, 2024, 2025)
SEASON_PERIOD = 'Fall'  # 'Fall' or 'Spring'

# Paste the raw tab-separated data here
RAW_DATA = """
Team1	1	Boys 8 1/C	5	3	0	0	15	25	15	10	Coach1
Team2	2	Girls 6 2/A	4	4	0	0	12	20	18	2	Coach2
"""

# ============================================================
# PARSING LOGIC (DO NOT MODIFY)
# ============================================================

def get_grade_group(grade):
    """Convert grade number to grade group format"""
    if grade in ['7', '8']:
        return 'Grade 7/8'
    elif grade in ['1', '2', '912']:
        return 'Grade 1/2'
    else:
        return f'Grade {grade}'


def parse_data():
    """Parse the pasted table data into team records"""

    town = TOWNS.get(TOWN_CODE)
    if not town:
        print(f"[X] Unknown town code: {TOWN_CODE}")
        return None

    teams = []
    lines = RAW_DATA.strip().split('\n')

    for line in lines:
        # Skip empty lines
        line = line.strip()
        if not line:
            continue

        # Split by tabs
        parts = line.split('\t')

        if len(parts) < 11:
            print(f"[!] Skipping line (not enough columns): {line[:50]}...")
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
            coaches = parts[11].strip() if len(parts) > 11 else ''

            # Parse GADS (Gender Age Division/Section)
            # Format: "Boys 8 1/C" or "Girls 6 2/A"
            gads_parts = gads.split()
            if len(gads_parts) >= 3:
                gender = gads_parts[0]  # Boys/Girls
                grade = gads_parts[1]   # 8, 7, 6, 5, 4, 3, etc.
                div_info = gads_parts[2]  # 1/C, 2/A, etc.

                # Parse division
                if '/' in div_info:
                    div_level, div_tier = div_info.split('/', 1)
                else:
                    div_level = div_info
                    div_tier = ''

                grade_group = get_grade_group(grade)
                division_string = f"{div_level}/{div_tier}" if div_tier else div_level

                # Parse coaches (format: "LastName" or "LastName/LastName")
                head_coach = None
                assistant_coach = None
                if coaches and coaches != '':
                    if '/' in coaches:
                        coach_parts = coaches.split('/')
                        head_coach = coach_parts[0].strip()
                        assistant_coach = coach_parts[1].strip() if len(coach_parts) > 1 else None
                    else:
                        head_coach = coaches

                # Create team record
                team = create_team_record(
                    town_code=TOWN_CODE,
                    town_name=town['name'],
                    town_population=town['population'],
                    season_year=SEASON_YEAR,
                    season_period=SEASON_PERIOD,
                    team_name=team_name,
                    division_string=division_string,
                    age_group=grade_group,
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
    print(f"IMPORTING {TOWN_CODE} {SEASON_PERIOD} {SEASON_YEAR}")
    print("=" * 60)
    print()

    teams = parse_data()

    if not teams:
        print("[X] No teams parsed. Check the format.")
        return

    print(f"[*] Parsed {len(teams)} teams")
    print()

    # Show grade distribution
    from collections import Counter
    grade_counts = Counter([t['age_group'] for t in teams])
    print("Grade distribution:")
    for grade in sorted(grade_counts.keys()):
        print(f"  {grade}: {grade_counts[grade]} teams")
    print()

    # Show first 3 teams
    print("Sample teams:")
    for team in teams[:3]:
        print(f"  {team['team_name']}: {team['gender']} {team['age_group']} - {team['wins']}-{team['losses']}-{team['ties']}")
    print()

    # Add to CSV
    manager = CSVManager('data/bays_teams.csv')
    added, skipped = manager.append_teams(teams)

    print(f"[OK] Added {added} new teams")
    if skipped > 0:
        print(f"[!] Skipped {skipped} duplicates")
    print()


if __name__ == "__main__":
    main()
