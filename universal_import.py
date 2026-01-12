"""
UNIVERSAL IMPORT SCRIPT - ASHLAND FORMAT (HARDCODED RULE)

This is the ONLY way to import soccer data going forward.
All pasted data MUST follow this exact format.

Format Rules (based on Ashland):
1. Columns: Team | Team# | GADS | W | L | T | F | PTS | GF | GA | +/- | Coach | A. Coach
2. GADS format: "Gender Grade Division/Section" (e.g., "Girls 8 3/E")
3. Division number = division_level (e.g., 3)
4. Division letter = division_tier/section (e.g., E)
5. Grade 7 or 8 = "Grade 7/8"
6. Grade 1-6 = "Grade {number}"
7. Coach column may contain "Name1/Name2" or just "Name1"
8. A. Coach column may be separate or None
9. Division full = "Division {level}{tier}" (e.g., "Division 3E")

NEVER DEVIATE FROM THIS FORMAT.
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record
from config.towns_config import TOWNS


def get_grade_group(grade):
    """
    Convert grade number to grade group format
    Grades 7 and 8 are ALWAYS "Grade 7/8"
    """
    if grade in ['7', '8']:
        return 'Grade 7/8'
    elif grade in ['1', '2', '912']:
        return 'Grade 1/2'
    else:
        return f'Grade {grade}'


def parse_universal(raw_data, town_code, season_year, season_period):
    """
    Parse pasted data using ASHLAND FORMAT (universal standard)

    Column order (MANDATORY):
    0: Team name
    1: Team number
    2: GADS (Gender Age Division/Section)
    3: Wins
    4: Losses
    5: Ties
    6: Forfeits
    7: Points
    8: Goals For
    9: Goals Against
    10: Goal Differential (+/-)
    11: Head Coach
    12: Assistant Coach (optional)
    """

    town = TOWNS.get(town_code)
    if not town:
        print(f"[X] Unknown town code: {town_code}")
        return None

    teams = []
    lines = raw_data.strip().split('\n')

    for line_num, line in enumerate(lines, 1):
        line = line.strip()

        # Skip empty lines and header
        if not line or 'Team\t' in line:
            continue

        parts = line.split('\t')

        # Must have at least 11 columns (up to head coach)
        if len(parts) < 11:
            print(f"[!] Line {line_num}: Skipping (only {len(parts)} columns, need 11+)")
            continue

        try:
            # Parse columns according to ASHLAND FORMAT
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
            head_coach = parts[11].strip() if len(parts) > 11 and parts[11].strip() not in ['None', '', 'none'] else None
            assistant_coach = parts[12].strip() if len(parts) > 12 and parts[12].strip() not in ['None', '', 'none'] else None

            # Parse GADS: "Gender Grade Division/Section"
            # Example: "Girls 8 3/E" = Girls, Grade 8, Division 3, Section E
            gads_parts = gads.split()

            if len(gads_parts) < 3:
                print(f"[!] Line {line_num}: Invalid GADS format: {gads}")
                continue

            gender = gads_parts[0]  # Boys/Girls
            grade = gads_parts[1]   # 8, 7, 6, 5, 4, 3, etc.
            div_info = gads_parts[2]  # 3/E, 4/G, 2/C, etc.

            # CRITICAL: Parse division into level and tier
            # Format: "3/E" means Division Level 3, Tier/Section E
            if '/' in div_info:
                div_level, div_tier = div_info.split('/', 1)
            else:
                div_level = div_info
                div_tier = ''

            # Convert grade to grade group
            grade_group = get_grade_group(grade)

            # Build division string for create_team_record
            division_string = f"{div_level}/{div_tier}" if div_tier else div_level

            # Create team record
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
            print(f"[!] Line {line_num} error: {line[:50]}... - {e}")
            import traceback
            traceback.print_exc()
            continue

    return teams


def save_and_import(raw_data, town_code, season_year, season_period):
    """
    Step 1: Save to dump file (ALWAYS - ALL PASTES)
    Step 2: Save to specific paste file
    Step 3: Parse and import
    """

    # STEP 0: SAVE TO DUMP FILE (AUTOMATIC BACKUP)
    os.makedirs('data/pastes', exist_ok=True)
    dump_file = 'data/pastes/paste_dump.txt'
    separator = '\n' + '='*80 + '\n'
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dump_header = f"PASTE TIMESTAMP: {timestamp_str}\n"
    dump_header += f"TOWN: {town_code} | SEASON: {season_period} {season_year}\n"

    with open(dump_file, 'a', encoding='utf-8') as f:
        f.write(separator)
        f.write(dump_header)
        f.write(separator)
        f.write(raw_data)
        f.write('\n')

    print(f"[OK] Auto-saved to dump file")

    # STEP 1: SAVE TO SPECIFIC PASTE FILE
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/pastes/{town_code}_{season_period}{season_year}_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(raw_data)

    print(f"[OK] Saved to: {filename}")
    print()

    # STEP 2: PARSE AND IMPORT
    teams = parse_universal(raw_data, town_code, season_year, season_period)

    if not teams:
        print("[X] No teams parsed")
        return 0, 0

    print(f"[*] Parsed {len(teams)} teams")
    print()

    # Show first team for verification
    if teams:
        t = teams[0]
        print("First team verification:")
        print(f"  Team: {t['team_name']}")
        print(f"  Gender: {t['gender']}, Grade: {t['age_group']}")
        print(f"  Division: Level={t['division_level']}, Tier={t['division_tier']}, Full={t['division_full']}")
        print(f"  Record: {t['wins']}-{t['losses']}-{t['ties']}, Points: {t['points']}")
        print(f"  Goals: {t['goals_for']} GF, {t['goals_against']} GA, {t['goal_differential']} GD")
        print(f"  Coaches: {t['head_coach']} / {t['assistant_coach']}")
        print()

    # Import to database
    manager = CSVManager('data/bays_teams.csv')
    added, skipped = manager.append_teams(teams)

    print(f"[OK] Added {added} new teams")
    if skipped > 0:
        print(f"[!] Skipped {skipped} duplicates")
    print()

    return added, skipped


def main():
    """Interactive mode"""
    print("=" * 60)
    print("UNIVERSAL SOCCER DATA IMPORT (ASHLAND FORMAT)")
    print("=" * 60)
    print()

    # Get parameters
    town_code = input("Town code (FOX, ASH, BEL, etc.): ").strip().upper()

    if town_code not in TOWNS:
        print(f"[X] Invalid town code. Valid codes: {', '.join(TOWNS.keys())}")
        return

    season_year = int(input("Season year (e.g., 2025): ").strip())
    season_period = input("Season period (Fall/Spring): ").strip().capitalize()

    if season_period not in ['Fall', 'Spring']:
        print(f"[X] Invalid season period. Must be Fall or Spring.")
        return

    print()
    print("Paste the data below, then press Enter followed by Ctrl+Z and Enter (Windows):")
    print("or Ctrl+D (Mac/Linux)")
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
    save_and_import(raw_data, town_code, season_year, season_period)


if __name__ == "__main__":
    main()
