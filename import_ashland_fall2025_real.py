"""
Import Ashland Fall 2025 - REAL DATA from BAYS website
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record
from config.towns_config import TOWNS

# REAL Ashland Fall 2025 data from BAYS.org
RAW_DATA = """Barracuda	10952	Girls 8 3/E	4	5	1	0	13	15	19	-4	Keith Elwell	Eric Appelstein
Leopards	32154	Girls 8 4/G	2	6	2	0	8	11	18	-7	Mark Pelletier	None
Bobcats	32096	Girls 6 4/A	9	0	1	0	28	38	5	33	Kristen Tilton	None
Renegades	32979	Girls 6 4/F	1	9	0	0	3	11	38	-27	John Brinegar	Meghan Baker
Cyclones	32981	Girls 5 2/C	5	3	2	0	17	25	20	5	Tessa Piantedosi	Rob Piantedosi
Eagles	34009	Girls 4 3/D	5	2	3	0	16	30	16	14	Adam Blasi	Michael Koziara
Panthers	34765	Girls 4 4/G	6	3	1	0	18	35	16	19	Lucas Hernandez	Carlos Quintanilla
United	34766	Girls 3 3/C2	8	1	1	0	25	31	8	23	Christopher Brown	Stephanie Brown
Dragons	34767	Girls 3 4/C2	3	2	3	0	12	16	14	2	Jacob Coolberth	None
Pumas	10949	Boys 8 2/B	2	3	0	0	6	6	13	-7	Jason Brown	Sean Gilhooly
Pythons	31324	Boys 8 3/L	6	0	4	0	22	18	5	13	Christopher Brown	Colin Weymouth
Lions	32100	Boys 8 4/J	2	7	1	0	7	12	26	-14	James Cole	Jacob Coolberth
Raptors	32104	Boys 6 3/B	4	6	0	0	12	20	32	-12	Jay Culverwell	Scott Romano
Hawks	32102	Boys 6 4/A	3	5	2	0	11	20	27	-7	Ryan Ewell	None
Strikers	34779	Boys 6 4/J	7	0	3	0	24	32	12	20	Deveka Bhardwaj	None
Titans	32984	Boys 5 1/B	3	5	2	0	11	30	33	-3	Justin Pryce	Alan Galiwango
Outlaws	32985	Boys 5 3/G	6	3	1	0	19	33	29	4	Chris Ramsey	John Heming
Marauders	33942	Boys 5 4/C	7	1	2	0	23	29	22	7	David Noah	Kathleen Strawn
Scorpions	33944	Boys 5 4/G	1	9	0	0	3	14	47	-33	Shaun Adamec	None
Spartans	33945	Boys 4 3/A	5	4	0	0	15	32	34	-2	Ryan Garnick	Peter DeMasi
Tigers	33946	Boys 4 4/A	4	2	3	0	15	35	29	6	Piyush Patel	Josh Smith
Predators	34775	Boys 4 4/H	9	1	0	0	22	45	6	39	Dimitri Apostola	None
Bulldogs	34776	Boys 3 2/D	4	4	2	0	14	29	24	5	Pam McQuillan	Peter Fuller
Galacticos	34777	Boys 3 3/F	2	6	2	0	8	21	27	-6	Porter Woodward	Stephen Marks
Sharks	34778	Boys 3 4/D	3	4	3	0	12	22	25	-3	Tigin Thomas	None"""


def get_grade_group(grade):
    """Convert grade number to grade group format"""
    if grade in ['7', '8']:
        return 'Grade 7/8'
    elif grade in ['1', '2', '912']:
        return 'Grade 1/2'
    else:
        return f'Grade {grade}'


def parse_data():
    """Parse the REAL data from BAYS"""
    town = TOWNS['ASH']
    teams = []
    lines = RAW_DATA.strip().split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t')
        if len(parts) < 12:
            print(f"[!] Skipping line (only {len(parts)} columns): {line[:50]}...")
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
            head_coach = parts[11].strip() if parts[11].strip() not in ['None', ''] else None
            assistant_coach = parts[12].strip() if len(parts) > 12 and parts[12].strip() not in ['None', ''] else None

            # Parse GADS: "Girls 8 3/E"
            gads_parts = gads.split()
            if len(gads_parts) >= 3:
                gender = gads_parts[0]  # Boys/Girls
                grade = gads_parts[1]   # 8, 6, 5, 4, 3
                div_info = gads_parts[2]  # 3/E, 4/G, etc.

                # Parse division (handle cases like "3/C2")
                if '/' in div_info:
                    div_level, div_tier = div_info.split('/', 1)
                else:
                    div_level = div_info
                    div_tier = ''

                grade_group = get_grade_group(grade)
                division_string = f"{div_level}/{div_tier}" if div_tier else div_level

                team = create_team_record(
                    town_code='ASH',
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
            print(f"[!] Error parsing: {line[:50]}... - {e}")
            import traceback
            traceback.print_exc()
            continue

    return teams


def main():
    print("=" * 60)
    print("IMPORTING ASHLAND FALL 2025 - REAL DATA")
    print("=" * 60)
    print()

    teams = parse_data()
    print(f"[*] Parsed {len(teams)} teams")
    print()

    # Show first team in detail to verify
    if teams:
        t = teams[0]
        print("First team (Barracuda) - verification:")
        print(f"  Team: {t['team_name']}")
        print(f"  Gender: {t['gender']}, Grade: {t['age_group']}")
        print(f"  Division: {t['division_full']}")
        print(f"  Record: {t['wins']}-{t['losses']}-{t['ties']}")
        print(f"  Points: {t['points']}")
        print(f"  Goals: {t['goals_for']} for, {t['goals_against']} against, {t['goal_differential']} diff")
        print(f"  Coaches: {t['head_coach']}, {t['assistant_coach']}")
        print()

        # Expected: 4-5-1, 13 pts, 15 GF, 19 GA, -4 GD, Keith Elwell/Eric Appelstein
        print("Expected: 4-5-1, 13 pts, 15 GF, 19 GA, -4 GD")
        print()

    # Import
    manager = CSVManager('data/bays_teams.csv')
    added, skipped = manager.append_teams(teams)

    print(f"[OK] Added {added} new teams")
    if skipped > 0:
        print(f"[!] Skipped {skipped} duplicates")
    print()


if __name__ == "__main__":
    main()
