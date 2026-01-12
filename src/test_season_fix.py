import full_scraper

teams = full_scraper.scrape_town_season('FOX', 2019, 'Fall', headless=False)

print()
print(f"Scraped {len(teams) if teams else 0} teams")

if teams:
    print("\nFirst 3 teams:")
    for i, team in enumerate(teams[:3]):
        print(f"  {team['team_name']}: {team['wins']}-{team['losses']}-{team['ties']}, GF={team['goals_for']}")
