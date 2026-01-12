"""
Interactive paste and import tool
Paste data when prompted, then it will be imported automatically
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record
from config.towns_config import TOWNS

def get_grade_group(grade):
    """Convert grade number to grade group format"""
    if grade in ['7', '8']:
        return 'Grade 7/8'
    elif grade in ['1', '2', '912']:
        return 'Grade 1/2'
    else:
        return f'Grade {grade}'


def parse_data(raw_data, town_code, season_year, season_period):
    """Parse the pasted data"""
    town = TOWNS.get(town_code)
    if not town:
        print(f"[X] Unknown town code: {town_code}")
        return None

    teams = []
    lines = raw_data.strip().split('\n')

    for line in lines:
        line = line.strip()
        if not line or 'Team\t' in line:  # Skip header
            continue

        parts = line.split('\t')
        if len(parts) < 11:
            continue

        try:
            # Column order: Team, Team#, GADS, W, L, T, F, PTS, GF, GA, +/-, Coach, A.Coach
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
            head_coach = parts[11].strip() if len(parts) > 11 and parts[11].strip() not in ['None', ''] else None
            assistant_coach = parts[12].strip() if len(parts) > 12 and parts[12].strip() not in ['None', ''] else None

            # Parse GADS
            gads_parts = gads.split()
            if len(gads_parts) >= 3:
                gender = gads_parts[0]
                grade = gads_parts[1]
                div_info = gads_parts[2]

                if '/' in div_info:
                    div_level, div_tier = div_info.split('/', 1)
                else:
                    div_level = div_info
                    div_tier = ''

                grade_group = get_grade_group(grade)
                division_string = f"{div_level}/{div_tier}" if div_tier else div_level

                team = create_team_record(
                    town_code=town_code,
                    town_name=town['name'],
                    town_population=town['population'],
                    season_year=season_year,
                    season_period=season_period,
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
            print(f"[!] Error: {line[:40]}... - {e}")
            continue

    return teams


def main():
    print("=" * 60)
    print("PASTE DATA IMPORT TOOL")
    print("=" * 60)
    print()

    # Get parameters
    town_code = input("Town code (FOX, ASH, etc.): ").strip().upper()
    season_year = int(input("Season year (e.g., 2025): ").strip())
    season_period = input("Season period (Fall/Spring): ").strip().capitalize()

    print()
    print("Paste the data below, then press Enter followed by Ctrl+Z and Enter on Windows (or Ctrl+D on Mac/Linux):")
    print("-" * 60)

    # Read multi-line input
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    raw_data = '\n'.join(lines)

    teams = parse_data(raw_data, town_code, season_year, season_period)

    if not teams:
        print("[X] No teams parsed")
        return

    print()
    print(f"[*] Parsed {len(teams)} teams")
    print()

    # Show first team
    if teams:
        t = teams[0]
        print("First team:")
        print(f"  {t['team_name']}: {t['gender']} {t['age_group']} Div {t['division_full']}")
        print(f"  {t['wins']}-{t['losses']}-{t['ties']}, {t['goals_for']} GF, {t['goals_against']} GA, {t['goal_differential']} GD, {t['points']} pts")
        print()

    # Confirm
    confirm = input(f"Import {len(teams)} teams? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Cancelled")
        return

    # Import
    manager = CSVManager('data/bays_teams.csv')
    added, skipped = manager.append_teams(teams)

    print()
    print(f"[OK] Added {added} new teams")
    if skipped > 0:
        print(f"[!] Skipped {skipped} duplicates")


if __name__ == "__main__":
    main()
