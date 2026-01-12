"""
Scheduled scraping script - waits before starting

This script will:
1. Wait for specified time
2. Scrape all 11 towns for Fall 2024
3. Save progress and provide summary
"""

import time
import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from full_scraper import scrape_all_towns_for_season


def scheduled_scrape(wait_minutes=75, season_year=2024, season_period="Fall"):
    """
    Wait for specified time, then scrape all towns

    Args:
        wait_minutes: Minutes to wait before starting
        season_year: Year to scrape
        season_period: 'Fall' or 'Spring'
    """

    print()
    print("=" * 60)
    print("SCHEDULED BAYS.org SCRAPER")
    print("=" * 60)
    print()

    # Calculate start time
    now = datetime.now()
    start_time = now + timedelta(minutes=wait_minutes)

    print(f"Current time:  {now.strftime('%I:%M:%S %p')}")
    print(f"Start time:    {start_time.strftime('%I:%M:%S %p')}")
    print(f"Wait duration: {wait_minutes} minutes")
    print()
    print(f"Task: Scrape all 11 towns for {season_period} {season_year}")
    print()
    print("=" * 60)
    print()

    # Countdown
    remaining = wait_minutes * 60  # Convert to seconds

    while remaining > 0:
        mins, secs = divmod(remaining, 60)

        if remaining % 300 == 0:  # Every 5 minutes
            print(f"[*] Waiting... {mins} minutes remaining until scrape starts")
        elif remaining == 60:  # 1 minute warning
            print(f"[*] Starting in 1 minute...")
        elif remaining == 10:  # 10 second warning
            print(f"[*] Starting in 10 seconds...")

        time.sleep(1)
        remaining -= 1

    # Start scraping
    print()
    print("=" * 60)
    print("STARTING SCRAPE NOW!")
    print("=" * 60)
    print()

    start_scrape_time = datetime.now()

    # Scrape all towns
    all_data = scrape_all_towns_for_season(season_year, season_period)

    end_scrape_time = datetime.now()
    duration = end_scrape_time - start_scrape_time

    # Summary
    print()
    print("=" * 60)
    print("SCRAPING COMPLETE")
    print("=" * 60)
    print()
    print(f"Started:  {start_scrape_time.strftime('%I:%M:%S %p')}")
    print(f"Finished: {end_scrape_time.strftime('%I:%M:%S %p')}")
    print(f"Duration: {duration}")
    print()
    print(f"Towns scraped: {len(all_data)}/{11}")

    total_teams = sum(len(teams) for teams in all_data.values())
    print(f"Total teams:   {total_teams}")
    print()

    # Per-town summary
    print("Per-town results:")
    for town_code, teams in all_data.items():
        print(f"  {town_code}: {len(teams)} teams")

    print()
    print("Data saved to: data/bays_teams.csv")
    print()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Scheduled BAYS.org scraper')
    parser.add_argument('--wait', type=int, default=75, help='Minutes to wait before starting')
    parser.add_argument('--year', type=int, default=2024, help='Season year')
    parser.add_argument('--season', type=str, default='Fall', choices=['Fall', 'Spring'], help='Season period')

    args = parser.parse_args()

    try:
        scheduled_scrape(args.wait, args.year, args.season)
    except KeyboardInterrupt:
        print()
        print()
        print("[!]  Scraping cancelled by user")
        print()
