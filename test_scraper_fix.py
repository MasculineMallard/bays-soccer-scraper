"""Test the fixed scraper to verify it pulls different data for different seasons"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.full_scraper import scrape_town_season

# Test scraping FOX for Fall 2019
print("Testing FOX Fall 2019...")
teams_2019 = scrape_town_season('FOX', 2019, 'Fall', headless=False)

if teams_2019:
    print(f"\nScraped {len(teams_2019)} teams")
    print("\nFirst 3 teams:")
    for i, team in enumerate(teams_2019[:3]):
        print(f"  {team['team_name']}: {team['wins']}-{team['losses']}-{team['ties']}, GF={team['goals_for']}, GA={team['goals_against']}")
else:
    print("FAILED to scrape")
