import full_scraper

# Test Fall 2023 with headless=True (what we'll use for bulk scraping)
print("Testing FOX Fall 2023 (headless)...")
teams_2023 = full_scraper.scrape_town_season('FOX', 2023, 'Fall', headless=True)

if teams_2023:
    print(f"\nScraped {len(teams_2023)} teams")
    print("\nFirst 5 teams:")
    for i, team in enumerate(teams_2023[:5]):
        print(f"  {team['team_name']}: {team['wins']}-{team['losses']}-{team['ties']}, GF={team['goals_for']}, GA={team['goals_against']}")
else:
    print("FAILED to scrape")
