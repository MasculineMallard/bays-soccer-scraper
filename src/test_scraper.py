"""
Test scraper to validate we can access and parse BAYS.org data
This is a proof-of-concept before full-scale scraping

NOTE: This uses requests which may not work due to Cloudflare.
If it fails, we'll use Claude Code Agent approach instead.
"""

import requests
import time
from datetime import datetime


def test_scrape_fox_organization():
    """Test scraping Foxborough organization page"""

    print("=" * 60)
    print("BAYS.org Test Scraper - Foxborough Organization Page")
    print("=" * 60)
    print()

    url = "https://bays.org/bays/organizations/view/FOX"

    print(f"Target URL: {url}")
    print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Respect robots.txt - 10 second delay (though this is first request)
    print("Note: robots.txt requires 10-second crawl delay")
    print("(Not waiting for first request)")
    print()

    # Proper headers to avoid blocks
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
    }

    print("Attempting to fetch page...")

    try:
        response = requests.get(url, headers=headers, timeout=30)

        print(f"[OK] Response Status Code: {response.status_code}")
        print(f"[OK] Response Size: {len(response.content)} bytes")
        print(f"[OK] Content Type: {response.headers.get('Content-Type', 'Unknown')}")
        print()

        if response.status_code == 200:
            # Check if we got HTML content
            content = response.text

            print("=" * 60)
            print("SUCCESS! Page retrieved successfully")
            print("=" * 60)
            print()

            # Basic content checks
            print("Content Analysis:")
            print(f"  - Contains 'Foxboro': {'Yes' if 'Foxboro' in content or 'FOX' in content else 'No'}")
            print(f"  - Contains 'Team': {'Yes' if 'Team' in content else 'No'}")
            print(f"  - Contains 'Division': {'Yes' if 'Division' in content else 'No'}")
            print(f"  - Contains 'Coach': {'Yes' if 'Coach' in content else 'No'}")
            print(f"  - Contains '<table': {'Yes' if '<table' in content else 'No'}")
            print()

            # Check for Cloudflare challenge
            if 'cf-browser-verification' in content or 'Just a moment' in content:
                print("[!]  WARNING: Cloudflare challenge detected!")
                print("    Automated scraping blocked. Will need agent-based approach.")
                return False

            # Save sample output
            sample_file = 'data/raw/test_fox_org_page.html'
            with open(sample_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Sample HTML saved to: {sample_file}")
            print()

            # Try to find key elements
            print("Key Elements Found:")
            if 'footable' in content:
                print("  [OK] Footable (responsive table) detected")
            if 'team/view' in content:
                print("  [OK] Team links detected")
            if 'Boys' in content or 'Girls' in content:
                print("  [OK] Gender information detected")
            print()

            print("=" * 60)
            print("NEXT STEP: Parse HTML to extract team data")
            print("=" * 60)
            print()
            print("Recommendations:")
            print("  1. Use BeautifulSoup to parse the HTML")
            print("  2. Extract team table data")
            print("  3. Test parsing division strings (e.g., '2/A')")
            print("  4. Test with POST data for different seasons")

            return True

        elif response.status_code == 403:
            print("=" * 60)
            print("[X] ACCESS DENIED (403 Forbidden)")
            print("=" * 60)
            print()
            print("This indicates Cloudflare or similar protection is blocking requests.")
            print()
            print("SOLUTION: Use Claude Code Agent approach")
            print("  - Agents can navigate the site like a browser")
            print("  - Can handle JavaScript, Cloudflare challenges, etc.")
            print("  - See Phase 2 of implementation plan")
            return False

        else:
            print(f"[X] Unexpected status code: {response.status_code}")
            print(f"   Response text (first 500 chars):")
            print(f"   {response.text[:500]}")
            return False

    except requests.exceptions.Timeout:
        print("[X] ERROR: Request timed out after 30 seconds")
        print("   The site may be slow or blocking the request")
        return False

    except requests.exceptions.ConnectionError as e:
        print(f"[X] ERROR: Connection failed")
        print(f"   {str(e)}")
        return False

    except Exception as e:
        print(f"[X] ERROR: Unexpected error occurred")
        print(f"   {type(e).__name__}: {str(e)}")
        return False


def test_scrape_with_season():
    """Test scraping with POST data for specific season"""

    print("\n" + "=" * 60)
    print("Testing Season-Specific Request (POST)")
    print("=" * 60)
    print()

    url = "https://bays.org/bays/organizations/view/FOX"

    # POST data for Fall 2025 season (latest available)
    data = {
        'season': 'Fall 2025'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    print(f"URL: {url}")
    print(f"Method: POST")
    print(f"Data: {data}")
    print()

    # Respect 10-second crawl delay
    print("Waiting 10 seconds (robots.txt crawl delay)...")
    time.sleep(10)

    try:
        response = requests.post(url, data=data, headers=headers, timeout=30)

        print(f"Response Status: {response.status_code}")

        if response.status_code == 200:
            print("[OK] POST request successful!")
            print(f"[OK] Content size: {len(response.content)} bytes")

            # Save to different file
            sample_file = 'data/raw/test_fox_org_fall2025.html'
            with open(sample_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"[OK] Saved to: {sample_file}")

            return True
        else:
            print(f"[X] POST request failed with status {response.status_code}")
            return False

    except Exception as e:
        print(f"[X] Error: {str(e)}")
        return False


if __name__ == "__main__":
    print()
    print("=" * 60)
    print("  BAYS.org Test Scraper - Proof of Concept".center(60))
    print("=" * 60)
    print()

    # Test 1: Basic GET request
    success_get = test_scrape_fox_organization()

    # Test 2: POST with season (only if GET worked)
    if success_get:
        success_post = test_scrape_with_season()
    else:
        print("\n[!]  Skipping POST test since GET failed")
        print("   Will need to use Agent-based approach for scraping")

    print()
    print("=" * 60)
    print("Test Complete")
    print("=" * 60)
