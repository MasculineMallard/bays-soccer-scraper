"""
Microsoft Edge Selenium Scraper for BAYS.org

Uses Edge browser (pre-installed on Windows) to bypass Cloudflare.
"""

import time
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.towns_config import TOWNS
from csv_manager import CSVManager
from manual_data_entry import parse_division, create_team_record


def scrape_with_edge(town_code, season_year, season_period):
    """
    Scrape using Microsoft Edge browser

    Args:
        town_code: Town code (e.g., 'FOX')
        season_year: Year (e.g., 2024)
        season_period: 'Fall' or 'Spring'

    Returns:
        List of team dictionaries or None if failed
    """

    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.edge.service import Service as EdgeService
        from selenium.webdriver.edge.options import Options as EdgeOptions
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
    except ImportError:
        print("[X] Selenium not installed!")
        print("    Install with: pip install selenium webdriver-manager")
        return None

    town = TOWNS.get(town_code)
    if not town:
        print(f"[X] Unknown town code: {town_code}")
        return None

    print("=" * 60)
    print(f"Scraping: {town['name']} - {season_period} {season_year}")
    print("=" * 60)
    print()

    # Setup Edge options
    edge_options = EdgeOptions()
    # edge_options.add_argument('--headless')  # Comment out for debugging
    edge_options.add_argument('--no-sandbox')
    edge_options.add_argument('--disable-dev-shm-usage')
    edge_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    driver = None
    teams_data = []

    try:
        print("[*] Starting Edge browser...")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)

        # Navigate to page
        url = f"https://bays.org/bays/organizations/view/{town_code}"
        print(f"[*] Navigating to: {url}")
        driver.get(url)

        # Wait for page to load (give Cloudflare time)
        print("[*] Waiting for page to load (10 seconds for Cloudflare)...")
        time.sleep(10)

        # Check page title
        print(f"[*] Page title: {driver.title}")

        # Check if blocked
        if "403" in driver.title or "Forbidden" in driver.page_source[:1000]:
            print("[X] Cloudflare blocked the request")
            print("    This may require manual browser interaction")
            return None

        print("[OK] Page loaded successfully")
        print()

        # Save HTML for inspection
        html_file = f'data/raw/{town_code}_{season_period.lower()}{season_year}.html'
        os.makedirs(os.path.dirname(html_file), exist_ok=True)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

        print(f"[OK] Saved HTML to: {html_file}")
        print()

        # Look for season form/selector
        print("[*] Checking for season selector...")
        try:
            # Try to find season dropdown/form
            selects = driver.find_elements(By.TAG_NAME, "select")

            season_found = False
            for select in selects:
                if 'season' in select.get_attribute('name').lower():
                    from selenium.webdriver.support.ui import Select
                    season_select = Select(select)

                    # Try to select the season
                    try:
                        season_select.select_by_visible_text(f"{season_period} {season_year}")
                        print(f"[OK] Selected {season_period} {season_year}")
                        time.sleep(5)  # Wait for table reload
                        season_found = True
                        break
                    except:
                        pass

            if not season_found:
                print("[!]  No season selector found - using default view")

        except Exception as e:
            print(f"[!]  Could not interact with season selector: {str(e)}")

        # Find and parse the teams table
        print("[*] Looking for teams table...")

        tables = driver.find_elements(By.TAG_NAME, "table")
        print(f"[*] Found {len(tables)} table(s)")

        if not tables:
            print("[X] No tables found on page!")
            return None

        # Use the first table (or look for specific class)
        teams_table = tables[0]

        print("[*] Parsing table...")

        # Get rows
        rows = teams_table.find_elements(By.TAG_NAME, "tr")
        print(f"[*] Found {len(rows)} rows")

        if len(rows) < 2:
            print("[X] Table has no data rows")
            return None

        # Get headers
        header_cells = rows[0].find_elements(By.TAG_NAME, "th")
        if not header_cells:
            header_cells = rows[0].find_elements(By.TAG_NAME, "td")

        headers = [cell.text.strip() for cell in header_cells]
        print(f"[*] Headers: {headers}")
        print()

        # Parse data rows
        print("[*] Extracting team data...")
        for i, row in enumerate(rows[1:], 1):
            cells = row.find_elements(By.TAG_NAME, "td")

            if not cells or len(cells) < 3:
                continue

            cell_data = [cell.text.strip() for cell in cells]

            print(f"  Row {i}: {cell_data}")

            # Try to extract team data (this depends on column order)
            # Common column orders:
            # [Team Name, Division, W, L, T, GF, GA] or similar

            try:
                # This is a GUESS - you'll need to adjust based on actual table structure
                team_data = {
                    'row': i,
                    'raw_data': cell_data,
                    'headers': headers
                }

                teams_data.append(team_data)

            except Exception as e:
                print(f"    [!]  Could not parse row: {str(e)}")

        print()
        print(f"[OK] Extracted {len(teams_data)} rows")

    except Exception as e:
        print(f"[X] Error during scraping: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            print("[*] Closing browser...")
            driver.quit()

    return teams_data


if __name__ == "__main__":
    print()

    # Test with Foxborough Fall 2024
    teams = scrape_with_edge('FOX', 2024, 'Fall')

    if teams:
        print()
        print("=" * 60)
        print("SUCCESS - Data Extracted")
        print("=" * 60)
        print()
        print(f"Total rows: {len(teams)}")
        print()
        print("Next steps:")
        print("  1. Inspect the saved HTML file in data/raw/")
        print("  2. Identify the correct column mappings")
        print("  3. Update parsing logic to map columns correctly")
        print("  4. Convert to CSV format using CSVManager")
    else:
        print()
        print("=" * 60)
        print("SCRAPING FAILED")
        print("=" * 60)
        print()
        print("Try:")
        print("  1. Remove --headless mode to see what's happening")
        print("  2. Manually complete Cloudflare challenge if needed")
        print("  3. Use manual extraction script instead")

    print()
