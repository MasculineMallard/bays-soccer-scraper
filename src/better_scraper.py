"""
Improved Selenium scraper with better waiting logic
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


def scrape_foxborough():
    """Scrape with better waiting logic"""

    print("=" * 60)
    print("BAYS.org Improved Scraper - Foxborough Fall 2024")
    print("=" * 60)
    print()

    # Setup Chrome
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

    driver = None

    try:
        print("[*] Starting Chrome...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate
        url = "https://bays.org/bays/organizations/view/FOX"
        print(f"[*] Navigating to: {url}")
        driver.get(url)

        print("[*] Waiting for page content...")
        time.sleep(20)  # Long wait for JavaScript

        print(f"[*] Page title: {driver.title}")
        print()

        # Try to find the actual content div
        print("[*] Looking for main content...")

        # Look for any divs, tables, or content
        try:
            # Wait for any table to appear
            wait = WebDriverWait(driver, 30)

            # Try different selectors
            selectors_to_try = [
                "table.footable",
                "table",
                "div.view-content",
                "div#content",
                "div.region-content"
            ]

            found_element = None
            for selector in selectors_to_try:
                try:
                    print(f"[*] Trying selector: {selector}")
                    elements = driver.find_elements(By.CSS_SELECTOR, selector)

                    if elements:
                        print(f"    Found {len(elements)} elements")

                        for i, elem in enumerate(elements):
                            text = elem.text.strip()
                            if text and len(text) > 50:  # Has meaningful content
                                print(f"    Element {i} has content ({len(text)} chars)")
                                print(f"    Preview: {text[:200]}...")
                                found_element = elem
                                break

                    if found_element:
                        break

                except Exception as e:
                    print(f"    Error with selector: {str(e)}")

        except Exception as e:
            print(f"[X] Error finding content: {str(e)}")

        # Save full page HTML
        html_file = 'data/raw/foxborough_fall2024_improved.html'
        os.makedirs(os.path.dirname(html_file), exist_ok=True)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

        print()
        print(f"[OK] Saved HTML to: {html_file}")
        print()

        # Get page source length to check if content loaded
        page_source = driver.page_source
        print(f"[*] Page source length: {len(page_source)} bytes")

        # Search for keywords
        keywords = ['Team', 'Division', 'Foxboro', 'Boys', 'Girls', 'U12', 'U14']
        for kw in keywords:
            count = page_source.count(kw)
            if count > 0:
                print(f"    '{kw}' found {count} times")

        print()
        print("Browser will stay open for 30 seconds so you can inspect...")
        print("Check what you see in the browser window!")
        time.sleep(30)

    except Exception as e:
        print(f"[X] Error: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            print("[*] Closing browser...")
            driver.quit()


if __name__ == "__main__":
    scrape_foxborough()
