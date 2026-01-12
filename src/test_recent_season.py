import full_scraper

# Test Fall 2023 (recent historical season)
print("Testing FOX Fall 2023...")
teams_2023 = full_scraper.scrape_town_season('FOX', 2023, 'Fall', headless=False)

if teams_2023:
    print(f"\nScraped {len(teams_2023)} teams")
    print("\nFirst 5 teams:")
    for i, team in enumerate(teams_2023[:5]):
        print(f"  {team['team_name']}: {team['wins']}-{team['losses']}-{team['ties']}, GF={team['goals_for']}, GA={team['goals_against']}")
else:
    print("FAILED to scrape")
