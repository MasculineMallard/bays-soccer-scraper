"""
Parse the HTML from BAYS standings and save to CSV
"""

import sys
import os
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from csv_manager import CSVManager
from manual_data_entry import create_team_record


def parse_standings_html(html_file, town_code, town_name, season_year, season_period):
    """
    Parse standings HTML and extract team data

    Args:
        html_file: Path to HTML file
        town_code: Town code (e.g., 'FOX')
        town_name: Full town name
        season_year: Year (e.g., 2024)
        season_period: 'Fall' or 'Spring'

    Returns:
        List of team dictionaries
    """

    print("=" * 60)
    print(f"Parsing Standings HTML: {town_code} {season_period} {season_year}")
    print("=" * 60)
    print()

    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the standings table (id="footable--2" or class containing "footable")
    tables = soup.find_all('table', id=lambda x: x and 'footable' in x)

    standings_table = None
    for table in tables:
        # Look for the table with W, L, T, GF, GA headers
        headers = [th.get_text().strip() for th in table.find_all('th')]
        if 'W' in headers and 'GF' in headers:
            standings_table = table
            print(f"[OK] Found standings table with headers: {headers}")
            break

    if not standings_table:
        print("[X] Could not find standings table!")
        return []

    # Parse rows
    rows = standings_table.find('tbody').find_all('tr') if standings_table.find('tbody') else standings_table.find_all('tr')[1:]

    teams = []

    for i, row in enumerate(rows, 1):
        try:
            cells = row.find_all('td')

            if len(cells) < 10:
                print(f"[!]  Row {i}: Not enough cells ({len(cells)})")
                continue

            # The structure appears to be:
            # cells[0] = Gender ("Girls" or "Boys")
            # cells[1] = Grade (age like "8", "6", "5", etc.)
            # cells[2] = Division level ("2", "3", "4")
            # cells[3] = Division tier ("A", "B", "C", etc.)
            # cells[4] = Team name link
            # cells[5] = Team number
            # cells[6] = GADS (full division string like "Girls 8 3/B")
            # cells[7] = W (wins)
            # cells[8] = L (losses)
            # cells[9] = T (ties)
            # cells[10] = F (forfeits?)
            # cells[11] = PTS (points)
            # cells[12] = GF (goals for)
            # cells[13] = GA (goals against)
            # cells[14] = +/- (goal differential)
            # cells[15+] = Coach info

            gender = cells[0].get_text().strip()
            grade = cells[1].get_text().strip()
            div_level = cells[2].get_text().strip()
            div_tier = cells[3].get_text().strip()

            team_name = cells[4].get_text().strip()
            gads = cells[6].get_text().strip() if len(cells) > 6 else ""

            wins = int(cells[7].get_text().strip()) if len(cells) > 7 else 0
            losses = int(cells[8].get_text().strip()) if len(cells) > 8 else 0
            ties = int(cells[9].get_text().strip()) if len(cells) > 9 else 0

            goals_for = int(cells[12].get_text().strip()) if len(cells) > 12 else 0
            goals_against = int(cells[13].get_text().strip()) if len(cells) > 13 else 0

            # Map grade to age group
            grade_to_age = {
                '8': 'U8',
                '7': 'U8',  # 7/8 groups
                '6': 'U10',
                '5': 'U12',
                '4': 'U14',
                '3': 'U16',
                '2': 'U19',
                '1': 'U19'
            }

            age_group = grade_to_age.get(grade, f'U{grade}')

            # Build division string
            if div_tier and div_tier != '':
                division_string = f"{div_level}/{div_tier}"
            else:
                division_string = div_level

            print(f"Row {i}: {team_name} ({gender} {age_group}) Division {division_string} - {wins}-{losses}-{ties}, GF:{goals_for}, GA:{goals_against}")

            # Create team record
            team = create_team_record(
                town_code=town_code,
                town_name=town_name,
                town_population=None,  # Fill later
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
                goals_against=goals_against
            )

            teams.append(team)

        except Exception as e:
            print(f"[X] Error parsing row {i}: {str(e)}")
            # Print first few cells for debugging
            try:
                cell_texts = [c.get_text().strip()[:20] for c in cells[:8]]
                print(f"    Cells: {cell_texts}")
            except:
                pass

    print()
    print(f"[OK] Parsed {len(teams)} teams")
    return teams


if __name__ == "__main__":
    print()

    # Parse the HTML we saved
    html_file = 'data/raw/foxborough_fall2024_final.html'

    teams = parse_standings_html(
        html_file=html_file,
        town_code='FOX',
        town_name='Foxborough Youth Soccer',
        season_year=2024,
        season_period='Fall'
    )

    if teams:
        print()
        print("=" * 60)
        print("Saving to CSV")
        print("=" * 60)
        print()

        manager = CSVManager()
        added, skipped = manager.append_teams(teams)

        print(f"[OK] Added {added} teams to CSV")
        if skipped > 0:
            print(f"[!]  Skipped {skipped} duplicates")

        print()
        print("=" * 60)
        print("SUCCESS!")
        print("=" * 60)
        print()
        print(f"Foxborough Fall 2024 data saved to CSV!")
        print(f"Total teams: {len(teams)}")

    else:
        print()
        print("[X] No teams extracted")

    print()
