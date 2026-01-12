"""
Selenium-based scraper for BAYS.org

Uses browser automation to bypass Cloudflare protection.
Requires: selenium, webdriver-manager
"""

import time
import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.towns_config import TOWNS
from csv_manager import CSVManager


def scrape_foxborough_fall2024():
    """
    Scrape Foxborough Fall 2024 data using Selenium

    NOTE: This is a proof of concept. You'll need to:
    1. Install Selenium: pip install selenium webdriver-manager
    2. Have Chrome installed on your system
    """

    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
    except ImportError:
        print("[X] Selenium not installed!")
        print("    Install with: pip install selenium webdriver-manager")
        return None

    print("=" * 60)
    print("BAYS.org Selenium Scraper - Foxborough Fall 2024")
    print("=" * 60)
    print()

    # Setup Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run in background - DISABLED for debugging
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Add user agent
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    driver = None
    teams_data = []

    try:
        print("[*] Starting Chrome browser...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to page
        url = "https://bays.org/bays/organizations/view/FOX"
        print(f"[*] Navigating to: {url}")
        driver.get(url)

        # Wait for page to load
        print("[*] Waiting for page to load...")
        time.sleep(15)  # Give Cloudflare + JavaScript time to process

        # Check if we got blocked
        if "403" in driver.title or "Forbidden" in driver.page_source:
            print("[X] Cloudflare blocked the request")
            print("    Try running without --headless mode")
            return None

        print(f"[OK] Page loaded: {driver.title}")
        print()

        # Try to find season selector
        print("[*] Looking for season selector...")
        try:
            # This is a guess - need to inspect the actual page structure
            season_select = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "season"))
            )

            # Select Fall 2024
            from selenium.webdriver.support.ui import Select
            select = Select(season_select)
            select.select_by_visible_text("Fall 2024")

            print("[OK] Selected Fall 2024 season")
            time.sleep(3)  # Wait for table to reload

        except Exception as e:
            print(f"[!]  Could not find season selector: {str(e)}")
            print("    The page might already show Fall 2024 by default")

        # Find the teams table
        print("[*] Looking for teams table...")
        try:
            # Try common table selectors
            tables = driver.find_elements(By.TAG_NAME, "table")

            if not tables:
                print("[X] No tables found on page")
                return None

            print(f"[OK] Found {len(tables)} table(s)")

            # Look for the main teams table (usually has class 'footable' or similar)
            teams_table = None
            for table in tables:
                if 'team' in table.get_attribute('class').lower() or 'footable' in table.get_attribute('class').lower():
                    teams_table = table
                    break

            if not teams_table:
                teams_table = tables[0]  # Use first table as fallback

            print("[*] Parsing table rows...")

            # Get all rows
            rows = teams_table.find_elements(By.TAG_NAME, "tr")

            print(f"[OK] Found {len(rows)} rows")

            # Parse header to identify columns
            header_row = rows[0]
            headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, "th")]

            print(f"[*] Table headers: {headers}")
            print()

            # Parse data rows
            for i, row in enumerate(rows[1:], 1):  # Skip header
                cells = row.find_elements(By.TAG_NAME, "td")

                if not cells:
                    continue

                row_data = [cell.text.strip() for cell in cells]

                print(f"Row {i}: {row_data}")

                # Store raw data for now - we'll parse it later
                teams_data.append({
                    'row_number': i,
                    'cells': row_data,
                    'headers': headers
                })

            print()
            print(f"[OK] Extracted {len(teams_data)} teams")

        except Exception as e:
            print(f"[X] Error parsing table: {str(e)}")
            import traceback
            traceback.print_exc()

        # Save raw HTML for inspection
        html_file = 'data/raw/foxborough_fall2024.html'
        os.makedirs(os.path.dirname(html_file), exist_ok=True)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

        print(f"[OK] Saved HTML to: {html_file}")
        print()

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

    teams = scrape_foxborough_fall2024()

    if teams:
        print()
        print("=" * 60)
        print("SUCCESS - Data Extracted")
        print("=" * 60)
        print()
        print(f"Total teams: {len(teams)}")
        print()
        print("Next steps:")
        print("  1. Inspect data/raw/foxborough_fall2024.html")
        print("  2. Identify correct column mappings")
        print("  3. Parse division strings")
        print("  4. Write to CSV using CSVManager")
    else:
        print()
        print("=" * 60)
        print("SCRAPING FAILED")
        print("=" * 60)
        print()
        print("Recommendations:")
        print("  1. Try running without --headless mode")
        print("  2. Manually inspect the page HTML structure")
        print("  3. Update table/form selectors in code")

    print()
