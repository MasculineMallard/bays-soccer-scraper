"""
Import Foxborough Fall 2025 - CORRECTED
Division format: number = division level, letter = section/tier
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record
from config.towns_config import TOWNS

RAW_DATA = open('data/pastes/FOX_Fall2025.txt', 'r', encoding='utf-8').read()

def get_grade_group(grade):
    if grade in ['7', '8']:
        return 'Grade 7/8'
    elif grade in ['1', '2', '912']:
        return 'Grade 1/2'
    else:
        return f'Grade {grade}'

def parse_data():
    town = TOWNS['FOX']
    teams = []
    lines = RAW_DATA.strip().split('\n')

    for line in lines[1:]:  # Skip header
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t')
        if len(parts) < 11:
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
            head_coach = parts[11].strip() if len(parts) > 11 and parts[11].strip() not in ['None', ''] else None
            assistant_coach = parts[12].strip() if len(parts) > 12 and parts[12].strip() not in ['None', ''] else None

            # Parse GADS: "Girls 8 3/B"
            gads_parts = gads.split()
            if len(gads_parts) >= 3:
                gender = gads_parts[0]  # Girls/Boys
                grade = gads_parts[1]   # 8, 6, 5, 4, 3
                div_info = gads_parts[2]  # 3/B, 4/K, etc.

                # CRITICAL: Parse division correctly
                # div_info format: "3/B" means Division 3, Section B
                if '/' in div_info:
                    div_level, div_tier = div_info.split('/', 1)
                else:
                    div_level = div_info
                    div_tier = ''

                grade_group = get_grade_group(grade)
                division_string = f"{div_level}/{div_tier}" if div_tier else div_level

                team = create_team_record(
                    town_code='FOX',
                    town_name=town['name'],
                    town_population=town['population'],
                    season_year=2025,
                    season_period='Fall',
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
            print(f"[!] Error: {line[:50]}... - {e}")
            import traceback
            traceback.print_exc()
            continue

    return teams

def main():
    print("=" * 60)
    print("IMPORTING FOXBOROUGH FALL 2025 (CORRECTED)")
    print("=" * 60)
    print()

    teams = parse_data()
    print(f"[*] Parsed {len(teams)} teams")
    print()

    if teams:
        t = teams[0]
        print("First team verification:")
        print(f"  Team: {t['team_name']}")
        print(f"  Gender: {t['gender']}, Grade: {t['age_group']}")
        print(f"  Division Level: {t['division_level']}, Tier: {t['division_tier']}, Full: {t['division_full']}")
        print(f"  Record: {t['wins']}-{t['losses']}-{t['ties']}")
        print(f"  Goals: {t['goals_for']} GF, {t['goals_against']} GA, {t['goal_differential']} GD")
        print(f"  Points: {t['points']}")
        print(f"  Head Coach: {t['head_coach']}, Asst: {t['assistant_coach']}")
        print()
        print("Expected: Division 3, Section B, 7-1-2, 20 GF, 13 GA, 7 GD, 23 pts")
        print("         Shawn Higgins / Khaled Alshara")
        print()

    manager = CSVManager('data/bays_teams.csv')
    added, skipped = manager.append_teams(teams)

    print(f"[OK] Added {added} new teams")
    if skipped > 0:
        print(f"[!] Skipped {skipped} duplicates")
    print()

if __name__ == "__main__":
    main()
