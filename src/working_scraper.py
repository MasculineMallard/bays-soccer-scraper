"""
Working Selenium scraper that clicks to reveal standings data
"""

import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


def scrape_foxborough_standings(season_year=2024, season_period="Fall"):
    """
    Scrape Foxborough standings with proper clicking

    Args:
        season_year: Year (e.g., 2024)
        season_period: 'Fall' or 'Spring'

    Returns:
        List of team dictionaries or None if failed
    """

    print("=" * 60)
    print(f"BAYS.org Scraper - Foxborough {season_period} {season_year}")
    print("=" * 60)
    print()

    # Setup Chrome
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

    driver = None
    teams_data = []

    try:
        print("[*] Starting Chrome...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate
        url = "https://bays.org/bays/organizations/view/FOX"
        print(f"[*] Navigating to: {url}")
        driver.get(url)

        print("[*] Waiting for initial page load...")
        time.sleep(5)

        print(f"[OK] Page loaded: {driver.title}")
        print()

        # Step 1: Click on "Foxboro Soccer Association Standings" to reveal the data
        print("[*] Step 1: Clicking 'Foxboro Soccer Association Standings' link...")
        try:
            wait = WebDriverWait(driver, 15)

            # Find the link/element containing "Standings"
            standings_link = wait.until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Standings"))
            )

            print(f"    Found standings link: {standings_link.text}")
            standings_link.click()

            print("[OK] Clicked standings link")
            time.sleep(3)  # Wait for content to expand

        except Exception as e:
            print(f"[X] Error clicking standings link: {str(e)}")
            print("    Trying alternative method...")

            # Try finding by text content
            try:
                elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Standings')]")
                for elem in elements:
                    if 'Foxboro' in elem.text or 'Association' in elem.text:
                        elem.click()
                        print("[OK] Clicked standings section")
                        time.sleep(3)
                        break
            except Exception as e2:
                print(f"[X] Alternative method also failed: {str(e2)}")

        # Step 2: Click "change" hyperlink to select season
        print("[*] Step 2: Looking for 'change' link to select season...")
        try:
            change_link = wait.until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "change"))
            )

            print("[OK] Found 'change' link")
            change_link.click()

            print("[OK] Clicked 'change' link")
            time.sleep(2)  # Wait for season selector to appear

        except Exception as e:
            print(f"[!]  Could not find 'change' link: {str(e)}")
            print("    Season selector might already be visible or not needed")

        # Step 3: Select the season
        print(f"[*] Step 3: Selecting {season_period} {season_year} season...")
        try:
            # Look for season dropdown or radio buttons
            selects = driver.find_elements(By.TAG_NAME, "select")

            season_selected = False
            for select_elem in selects:
                try:
                    select = Select(select_elem)
                    options = [opt.text for opt in select.options]

                    # Check if this is the season selector
                    season_text = f"{season_period} {season_year}"
                    if season_text in options:
                        select.select_by_visible_text(season_text)
                        print(f"[OK] Selected '{season_text}' from dropdown")
                        season_selected = True

                        # Click submit button if exists
                        try:
                            submit_btn = driver.find_element(By.ID, "edit-submit")
                            submit_btn.click()
                            print("[OK] Clicked submit button")
                        except:
                            pass

                        time.sleep(5)  # Wait for table to reload
                        break

                except Exception as e:
                    continue

            if not season_selected:
                print("[!]  Could not select season - may already be showing correct season")

        except Exception as e:
            print(f"[!]  Error selecting season: {str(e)}")

        # Step 4: Extract the standings table
        print("[*] Step 4: Extracting standings table data...")

        try:
            # Look for table with class 'footable' or containing standings data
            tables = driver.find_elements(By.TAG_NAME, "table")

            print(f"[*] Found {len(tables)} table(s) on page")

            standings_table = None
            for i, table in enumerate(tables):
                table_html = table.get_attribute('outerHTML')[:500]

                # Check if this table has team data
                if 'footable' in table.get_attribute('class'):
                    print(f"    Table {i}: Has 'footable' class")
                    standings_table = table
                    break

            if not standings_table and tables:
                # Use the largest table as fallback
                standings_table = max(tables, key=lambda t: len(t.text))
                print(f"    Using largest table (fallback)")

            if standings_table:
                # Get table rows
                rows = standings_table.find_elements(By.TAG_NAME, "tr")
                print(f"[*] Found {len(rows)} rows in table")

                if len(rows) > 0:
                    # Get headers
                    header_row = rows[0]
                    headers = []
                    for th in header_row.find_elements(By.TAG_NAME, "th"):
                        headers.append(th.text.strip())

                    if not headers:
                        # Try td in first row
                        for td in header_row.find_elements(By.TAG_NAME, "td"):
                            headers.append(td.text.strip())

                    print(f"[*] Headers: {headers}")
                    print()

                    # Extract data rows
                    for row_num, row in enumerate(rows[1:], 1):
                        cells = row.find_elements(By.TAG_NAME, "td")

                        if not cells or len(cells) < 3:
                            continue

                        cell_data = [cell.text.strip() for cell in cells]

                        print(f"Row {row_num}: {cell_data}")

                        teams_data.append({
                            'row': row_num,
                            'cells': cell_data,
                            'headers': headers
                        })

                    print()
                    print(f"[OK] Extracted {len(teams_data)} team rows")

        except Exception as e:
            print(f"[X] Error extracting table: {str(e)}")
            import traceback
            traceback.print_exc()

        # Save HTML
        html_file = f'data/raw/foxborough_{season_period.lower()}{season_year}_final.html'
        os.makedirs(os.path.dirname(html_file), exist_ok=True)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

        print(f"[OK] Saved HTML to: {html_file}")
        print()

        print("Browser will stay open for 15 seconds for you to inspect...")
        time.sleep(15)

    except Exception as e:
        print(f"[X] Error: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            print("[*] Closing browser...")
            driver.quit()

    return teams_data


if __name__ == "__main__":
    print()

    teams = scrape_foxborough_standings(2024, "Fall")

    if teams:
        print()
        print("=" * 60)
        print("SUCCESS")
        print("=" * 60)
        print(f"Total teams extracted: {len(teams)}")
        print()
        print("Next: Parse the data and write to CSV")
    else:
        print()
        print("=" * 60)
        print("NO DATA EXTRACTED")
        print("=" * 60)
        print("Check the browser window to see what's displayed")

    print()
