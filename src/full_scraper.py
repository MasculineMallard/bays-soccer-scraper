"""
Complete integrated scraper: Selenium + BeautifulSoup + CSV saving

This script combines all steps:
1. Navigate to BAYS.org organization page
2. Click "Standings" link
3. Extract standings table HTML
4. Parse the data
5. Save to CSV

Can be run for any town and season.
"""

import time
import sys
import os
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.towns_config import TOWNS
from src.csv_manager import CSVManager
from src.manual_data_entry import create_team_record


def scrape_town_season(town_code, season_year=2024, season_period="Fall", headless=True):
    """
    Scrape a single town for a single season

    Args:
        town_code: Town code (e.g., 'FOX', 'HOP')
        season_year: Year (e.g., 2024)
        season_period: 'Fall' or 'Spring'
        headless: Run browser in headless mode

    Returns:
        List of team dictionaries or None if failed
    """

    town = TOWNS.get(town_code)
    if not town:
        print(f"[X] Unknown town code: {town_code}")
        return None

    print("=" * 60)
    print(f"Scraping: {town['name']} - {season_period} {season_year}")
    print("=" * 60)
    print()

    # Setup Chrome
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

    driver = None
    teams = []

    try:
        # Start browser
        print("[*] Starting Chrome...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate
        url = f"https://bays.org/bays/organizations/view/{town_code}"
        print(f"[*] Navigating to: {url}")
        driver.get(url)

        # Wait for initial load
        print("[*] Waiting for page load...")
        time.sleep(5)

        print(f"[OK] Page loaded: {driver.title}")

        # Select the season first
        season_string = f"{season_period} {season_year}"
        print(f"[*] Selecting season: {season_string}")
        try:
            wait = WebDriverWait(driver, 15)

            # Find and scroll to the season selector
            season_form = wait.until(
                EC.presence_of_element_located((By.ID, "bays-season-selected-menu"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", season_form)
            time.sleep(1)

            # Click "Change" checkbox using JavaScript (more reliable)
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
            time.sleep(1)

            # Click Submit button using JavaScript
            submit_button = driver.find_element(By.ID, "edit-submit")
            driver.execute_script("arguments[0].click();", submit_button)
            print("[OK] Submitted season selection")
            print("[*] Waiting for page to reload...")
            time.sleep(3)

            # Wait for Cloudflare check to complete (title changes from "Just a moment...")
            max_cloudflare_wait = 30
            cloudflare_start = time.time()
            while time.time() - cloudflare_start < max_cloudflare_wait:
                current_title = driver.title
                if "Just a moment" in current_title:
                    print("[*] Waiting for Cloudflare check...")
                    time.sleep(2)
                else:
                    print(f"[OK] Cloudflare passed, page loaded: {current_title}")
                    break
            else:
                print("[!]  Warning: Cloudflare check took too long")

            # Additional wait for page content to load
            time.sleep(3)

        except Exception as e:
            import traceback
            print(f"[X] Error selecting season: {str(e)}")
            print(traceback.format_exc())
            return None

        # Click "Standings" link
        print("[*] Looking for 'Standings' link...")
        try:
            wait = WebDriverWait(driver, 20)

            # After season change, page reloads - need to wait for standings link
            # Try different methods to find the link
            try:
                standings_link = wait.until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Standings"))
                )
            except:
                # Try finding by exact text
                standings_link = wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Standings"))
                )

            # Scroll to the link and click with JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", standings_link)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", standings_link)
            print("[OK] Clicked standings")
            time.sleep(5)  # Wait for content to expand and load
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

                # Extract data from cells
                # Extract ALL columns from table
                gender = cells[0].get_text().strip()
                grade = cells[1].get_text().strip()
                div_level = cells[2].get_text().strip()
                div_tier = cells[3].get_text().strip()
                team_name = cells[4].get_text().strip()
                # cell 5 = team number
                # cell 6 = GADS (Gender Age Division/Section string)

                wins = int(cells[7].get_text().strip())
                losses = int(cells[8].get_text().strip())
                ties = int(cells[9].get_text().strip())
                # cell 10 = F (forfeits)
                points = int(cells[11].get_text().strip()) if len(cells) > 11 else (wins * 3 + ties)
                goals_for = int(cells[12].get_text().strip())
                goals_against = int(cells[13].get_text().strip())
                goal_diff = int(cells[14].get_text().strip()) if len(cells) > 14 else (goals_for - goals_against)

                # Coach info (cells 15 and 16)
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
                print(f"[!]  Row {i} parse error: {str(e)}")

        print(f"[OK] Parsed {len(teams)} teams")

    except Exception as e:
        print(f"[X] Scraping error: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            driver.quit()

    return teams


def scrape_all_towns_for_season(season_year=2024, season_period="Fall"):
    """
    Scrape all 11 towns for a given season

    Args:
        season_year: Year (e.g., 2024)
        season_period: 'Fall' or 'Spring'

    Returns:
        Dictionary of {town_code: teams_list}
    """

    print()
    print("=" * 60)
    print(f"SCRAPING ALL TOWNS: {season_period} {season_year}")
    print("=" * 60)
    print()

    all_data = {}
    manager = CSVManager()

    for town_code in TOWNS.keys():
        print()
        teams = scrape_town_season(town_code, season_year, season_period, headless=True)

        if teams:
            all_data[town_code] = teams

            # Save to CSV immediately
            added, skipped = manager.append_teams(teams)
            print(f"[OK] {town_code}: Saved {added} teams ({skipped} duplicates)")

        else:
            print(f"[X] {town_code}: Failed to scrape")

        # Wait 10 seconds between towns (robots.txt crawl delay)
        print("[*] Waiting 10 seconds (robots.txt crawl delay)...")
        time.sleep(10)

    print()
    print("=" * 60)
    print("ALL TOWNS COMPLETE")
    print("=" * 60)
    print()

    total_teams = sum(len(teams) for teams in all_data.values())
    print(f"Total teams scraped: {total_teams}")
    print(f"Towns successful: {len(all_data)}/{len(TOWNS)}")

    return all_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Scrape BAYS.org soccer data')
    parser.add_argument('--town', type=str, help='Town code (e.g., FOX, HOP)')
    parser.add_argument('--all', action='store_true', help='Scrape all towns')
    parser.add_argument('--year', type=int, default=2024, help='Season year')
    parser.add_argument('--season', type=str, default='Fall', choices=['Fall', 'Spring'], help='Season period')
    parser.add_argument('--visible', action='store_true', help='Show browser window')

    args = parser.parse_args()

    print()

    if args.all:
        # Scrape all towns
        scrape_all_towns_for_season(args.year, args.season)

    elif args.town:
        # Scrape single town
        teams = scrape_town_season(args.town.upper(), args.year, args.season, headless=not args.visible)

        if teams:
            # Save to CSV
            manager = CSVManager()
            added, skipped = manager.append_teams(teams)

            print()
            print(f"[OK] Saved {added} teams ({skipped} duplicates)")

    else:
        print("Usage:")
        print("  Single town:  python full_scraper.py --town FOX --year 2024 --season Fall")
        print("  All towns:    python full_scraper.py --all --year 2024 --season Fall")
        print("  Show browser: python full_scraper.py --town FOX --visible")

    print()
