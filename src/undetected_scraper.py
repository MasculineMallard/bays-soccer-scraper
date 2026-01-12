"""
Scraper using undetected-chromedriver to bypass Cloudflare
"""

import time
import sys
import os
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from config.towns_config import TOWNS
from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record


def scrape_town_season(town_code, season_year=2024, season_period="Fall", headless=True):
    """
    Scrape a single town for a single season using undetected-chromedriver
    """

    town = TOWNS.get(town_code)
    if not town:
        print(f"[X] Unknown town code: {town_code}")
        return None

    print("=" * 60)
    print(f"Scraping: {town['name']} - {season_period} {season_year}")
    print("=" * 60)
    print()

    # Setup undetected Chrome
    options = uc.ChromeOptions()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = None
    teams = []

    try:
        # Start browser with undetected-chromedriver
        print("[*] Starting undetected Chrome...")
        driver = uc.Chrome(options=options, version_main=None)

        # Navigate
        url = f"https://bays.org/bays/organizations/view/{town_code}"
        print(f"[*] Navigating to: {url}")
        driver.get(url)

        # Wait for initial Cloudflare check
        print("[*] Waiting for initial Cloudflare check...")
        max_initial_wait = 60
        start_time = time.time()
        while time.time() - start_time < max_initial_wait:
            current_title = driver.title
            if "Just a moment" in current_title:
                print(f"[*] Cloudflare checking... ({int(time.time() - start_time)}s)")
                time.sleep(3)
            elif town['name'] in current_title or "Boston Area Youth Soccer" in current_title:
                print(f"[OK] Page loaded: {current_title}")
                break
            else:
                # Unknown title, keep waiting
                time.sleep(2)
        else:
            print(f"[!] Warning: Initial page load timeout (title: {driver.title})")

        # Additional wait for page to fully render
        time.sleep(5)

        # Select the season
        season_string = f"{season_period} {season_year}"
        print(f"[*] Selecting season: {season_string}")
        try:
            wait = WebDriverWait(driver, 20)

            # Find and scroll to the season selector
            season_form = wait.until(
                EC.presence_of_element_located((By.ID, "bays-season-selected-menu"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", season_form)
            time.sleep(2)

            # Click "Change" checkbox using JavaScript
            change_checkbox = driver.find_element(By.ID, "edit-change-season")
            driver.execute_script("arguments[0].click();", change_checkbox)
            print("[OK] Clicked change season checkbox")
            time.sleep(2)

            # Select the season from dropdown
            season_dropdown = wait.until(
                EC.visibility_of_element_located((By.ID, "edit-season"))
            )
            select = Select(season_dropdown)
            select.select_by_visible_text(season_string)
            print(f"[OK] Selected {season_string} from dropdown")
            time.sleep(2)

            # Click Submit button using JavaScript
            submit_button = driver.find_element(By.ID, "edit-submit")
            driver.execute_script("arguments[0].click();", submit_button)
            print("[OK] Submitted season selection")
            print("[*] Waiting for page to reload...")
            time.sleep(5)

            # Wait for Cloudflare check to complete
            max_wait = 45
            start = time.time()
            while time.time() - start < max_wait:
                current_title = driver.title
                if "Just a moment" in current_title:
                    print("[*] Waiting for Cloudflare check...")
                    time.sleep(3)
                elif town['name'] in current_title or "Boston Area Youth Soccer" in current_title:
                    print(f"[OK] Page reloaded: {current_title}")
                    break
                else:
                    time.sleep(2)
            else:
                print("[!] Warning: Long wait for page reload")

            # Additional wait for page content
            time.sleep(5)

        except Exception as e:
            import traceback
            print(f"[X] Error selecting season: {str(e)}")
            print(traceback.format_exc())
            return None

        # Click "Standings" link
        print("[*] Looking for 'Standings' link...")
        try:
            wait = WebDriverWait(driver, 20)

            # Try to find and click Standings
            try:
                standings_link = wait.until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Standings"))
                )
            except:
                standings_link = wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Standings"))
                )

            # Scroll and click
            driver.execute_script("arguments[0].scrollIntoView();", standings_link)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", standings_link)
            print("[OK] Clicked standings")
            time.sleep(7)  # Wait for content to expand and load

        except Exception as e:
            import traceback
            print(f"[X] Error clicking standings: {str(e)}")
            print(traceback.format_exc())
            return None

        # Get page HTML
        html = driver.page_source

        # Save HTML for debugging
        html_file = f'data/raw/{town_code}_{season_period.lower()}{season_year}.html'
        os.makedirs(os.path.dirname(html_file), exist_ok=True)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[OK] Saved HTML to: {html_file}")

        # Parse the HTML
        print("[*] Parsing standings table...")
        soup = BeautifulSoup(html, 'html.parser')

        # Find standings table
        tables = soup.find_all('table', id=lambda x: x and 'footable' in x)

        standings_table = None
        for table in tables:
            headers = [th.get_text().strip() for th in table.find_all('th')]
            if 'W' in headers and 'GF' in headers:
                standings_table = table
                print(f"[OK] Found standings table")
                break

        if not standings_table:
            print("[X] Could not find standings table!")
            return None

        # Parse rows
        rows = standings_table.find('tbody').find_all('tr') if standings_table.find('tbody') else standings_table.find_all('tr')[1:]

        for i, row in enumerate(rows, 1):
            try:
                cells = row.find_all('td')

                if len(cells) < 10:
                    continue

                # Extract ALL columns from table
                gender = cells[0].get_text().strip()
                grade = cells[1].get_text().strip()
                div_level = cells[2].get_text().strip()
                div_tier = cells[3].get_text().strip()
                team_name = cells[4].get_text().strip()

                wins = int(cells[7].get_text().strip())
                losses = int(cells[8].get_text().strip())
                ties = int(cells[9].get_text().strip())
                points = int(cells[11].get_text().strip()) if len(cells) > 11 else (wins * 3 + ties)
                goals_for = int(cells[12].get_text().strip())
                goals_against = int(cells[13].get_text().strip())
                goal_diff = int(cells[14].get_text().strip()) if len(cells) > 14 else (goals_for - goals_against)

                # Coach info
                head_coach = cells[15].get_text().strip() if len(cells) > 15 else None
                assistant_coach = cells[16].get_text().strip() if len(cells) > 16 else None

                # Clean up "None" text
                if head_coach == 'None' or not head_coach:
                    head_coach = None
                if assistant_coach == 'None' or not assistant_coach:
                    assistant_coach = None

                # Map grade to age group
                grade_to_age = {
                    '8': 'U8', '7': 'U8',
                    '6': 'U10',
                    '5': 'U12',
                    '4': 'U14',
                    '3': 'U16',
                    '2': 'U19', '1': 'U19'
                }
                age_group = grade_to_age.get(grade, f'U{grade}')

                # Build division string
                division_string = f"{div_level}/{div_tier}" if div_tier else div_level

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
                print(f"[!] Row {i} parse error: {str(e)}")

        print(f"[OK] Parsed {len(teams)} teams")

    except Exception as e:
        print(f"[X] Scraping error: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            driver.quit()

    return teams


if __name__ == "__main__":
    # Test scraper
    teams = scrape_town_season('FOX', 2023, 'Fall', headless=True)
    if teams:
        print(f"\nSuccessfully scraped {len(teams)} teams")
        print("\nFirst 3 teams:")
        for team in teams[:3]:
            print(f"  {team['team_name']}: {team['wins']}-{team['losses']}-{team['ties']}")
