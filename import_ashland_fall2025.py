"""
Import Ashland Fall 2025 data
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record
from config.towns_config import TOWNS

# Ashland Fall 2025 data pasted by user
raw_data = """Barracuda	4	Girls 8 1/C	9	0	0	0	27	37	6	31	Smith/Martin
Leopards	11	Girls 7 1/C	8	1	0	0	24	50	11	39
Bobcats	15	Girls 6 3/B	3	4	1	0	10	19	18	1	Ramirez
Wolves	16	Girls 6 4/A	2	5	1	0	7	14	23	-9	Martinez
Cobras	18	Girls 5 3/A	5	2	1	0	16	29	17	12	Carter
Eagles	19	Girls 5 3/B	3	3	2	0	11	20	21	-1	Sullivan
Scorpions	22	Girls 4 2/C	6	2	0	0	18	33	15	18
Hurricanes	23	Girls 4 3/B	4	3	1	0	13	24	21	3	Wilson
Lightning	24	Girls 4 4/A	1	4	3	0	6	13	24	-11	Adams
Thunder	25	Girls 3 2/D	5	1	2	0	17	25	14	11	Green
Spartans	26	Girls 3 3/C	3	3	2	0	11	18	18	0	Thomas
Tsunami	27	Girls 3 4/B	1	5	2	0	5	12	32	-20	Johnson
Panthers	1	Boys 8 1/C	6	1	1	0	19	30	17	13	Brown
Jaguars	2	Boys 7 1/C	5	3	0	0	15	29	20	9
Tigers	5	Boys 6 2/C	6	1	1	0	19	28	15	13	Davis
Lions	6	Boys 6 3/A	6	1	1	0	19	38	18	20	Rodriguez
Falcons	7	Boys 6 4/A	2	3	3	0	9	19	27	-8	Miller
Raptors	8	Boys 5 2/C	5	2	1	0	16	26	20	6	Thompson
Cyclones	9	Boys 5 3/B	3	3	2	0	11	21	23	-2	Jones
Tornadoes	10	Boys 5 4/A	0	6	2	0	2	8	44	-36	Garcia
Stingrays	12	Boys 4 2/D	4	2	2	0	14	21	17	4	Anderson
Warriors	13	Boys 4 3/C	2	4	2	0	8	14	22	-8	White
Knights	14	Boys 4 4/B	1	4	3	0	6	13	26	-13	Taylor
Mustangs	20	Boys 3 3/C	2	4	2	0	8	22	26	-4	Clark
Wildcats	21	Boys 3 4/B	1	5	2	0	5	17	40	-23	Martin"""

def parse_ashland_data():
    """Parse Ashland Fall 2025 data"""

    town = TOWNS['ASH']
    teams = []

    # Grade to age mapping
    grade_to_age = {
        '8': 'U8', '7': 'U8',
        '6': 'U10',
        '5': 'U12',
        '4': 'U14',
        '3': 'U16',
    }

    lines = raw_data.strip().split('\n')

    for line in lines:
        parts = line.split('\t')

        if len(parts) < 8:
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
            # Format: "Girls 8 1/C" or "Boys 6 2/C"
            gads_parts = gads.split()
            if len(gads_parts) >= 3:
                gender = gads_parts[0]  # Boys/Girls
                grade = gads_parts[1]   # 8, 6, 5, etc.
                div_info = gads_parts[2]  # 1/C, 2/C, etc.

                # Parse division
                if '/' in div_info:
                    div_level, div_tier = div_info.split('/', 1)
                else:
                    div_level = div_info
                    div_tier = ''

                age_group = grade_to_age.get(grade, f'U{grade}')
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
                    town_code='ASH',
                    town_name=town['name'],
                    town_population=town['population'],
                    season_year=2025,
                    season_period='Fall',
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
    print("IMPORTING ASHLAND FALL 2025 DATA")
    print("=" * 60)
    print()

    teams = parse_ashland_data()

    print(f"[*] Parsed {len(teams)} teams")
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

    # Show summary
    stats = manager.get_stats_summary()
    print("Updated CSV Summary:")
    print(f"  Total teams: {stats['total_teams']}")
    print(f"  Unique seasons: {stats['unique_seasons']}")
    print()


if __name__ == "__main__":
    main()
