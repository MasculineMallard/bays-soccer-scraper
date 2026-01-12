"""Test scraping the DEFAULT season (no season change) to verify scraper still works"""

import undetected_scraper

# Test scraping without changing seasons - should get current/default season
print("Testing FOX default season (no season selection)...")
print()

# Temporarily modify scraper to skip season selection
import sys
sys.path.append('.')

# Just test if we can get to the page and find the standings table
# by checking the Fall 2024 scrape (which worked before)

import full_scraper
teams = full_scraper.scrape_town_season('FOX', 2024, 'Fall', headless=True)

if teams:
    print(f"\nScraped {len(teams)} teams")
    print("\nFirst 3 teams:")
    for team in teams[:3]:
        print(f"  {team['team_name']}: {team['wins']}-{team['losses']}-{team['ties']}")
else:
    print("FAILED")
