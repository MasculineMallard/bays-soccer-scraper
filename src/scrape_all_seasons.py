"""
Scrape all available seasons for all working towns

Goes from Fall 2025 back to Fall 2015 (or as far back as data exists)
"""

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from full_scraper import scrape_town_season
from csv_manager import CSVManager
from config.towns_config import TOWNS


def scrape_all_seasons_all_towns():
    """
    Scrape all seasons for all towns

    Seasons to scrape (newest to oldest):
    - Fall 2025, Spring 2025, Fall 2024, Spring 2024, ...
    - Back to Fall 2015
    """

    # Working towns (exclude WSF which has no data)
    working_towns = ['ASH', 'BEL', 'FOX', 'HOL', 'HOP', 'MDY', 'NOB', 'SUD', 'WAL', 'WSB']

    # Generate season list from Fall 2025 back to Fall 2015
    seasons = []
    for year in range(2025, 2014, -1):  # 2025 down to 2015
        seasons.append((year, 'Fall'))
        seasons.append((year, 'Spring'))

    print("=" * 60)
    print("SCRAPING ALL SEASONS - ALL TOWNS")
    print("=" * 60)
    print()
    print(f"Towns: {len(working_towns)}")
    print(f"Seasons: {len(seasons)}")
    print(f"Total scrapes: {len(working_towns) * len(seasons)}")
    print()
    print("This will take approximately 2-3 hours with crawl delays...")
    print()
    print("=" * 60)
    print()

    manager = CSVManager()

    total_scraped = 0
    total_failed = 0
    total_empty = 0

    for year, period in seasons:
        print()
        print("=" * 60)
        print(f"{period} {year}")
        print("=" * 60)
        print()

        season_total = 0

        for town_code in working_towns:
            town_name = TOWNS[town_code]['name']

            try:
                teams = scrape_town_season(town_code, year, period, headless=True)

                if teams:
                    added, skipped = manager.append_teams(teams)

                    if added > 0:
                        print(f"[OK] {town_code} {period} {year}: Saved {added} teams ({skipped} duplicates)")
                        total_scraped += added
                        season_total += added
                    else:
                        print(f"[!]  {town_code} {period} {year}: All {skipped} teams already in CSV")
                else:
                    print(f"[!]  {town_code} {period} {year}: No data available")
                    total_empty += 1

            except Exception as e:
                print(f"[X] {town_code} {period} {year}: Failed - {str(e)}")
                total_failed += 1

            # Crawl delay (10 seconds per robots.txt)
            time.sleep(10)

        print()
        print(f"Season total: {season_total} new teams")

        # Check if we're hitting empty seasons - might be past available data
        if season_total == 0 and year < 2020:
            print()
            print(f"[!]  No data found for {period} {year} across all towns")
            print(f"     Likely past available data range")

    print()
    print("=" * 60)
    print("SCRAPING COMPLETE")
    print("=" * 60)
    print()
    print(f"Total teams scraped: {total_scraped}")
    print(f"Total failed: {total_failed}")
    print(f"Total empty: {total_empty}")
    print()

    # Final summary
    df = manager.load_csv()
    print(f"Total records in CSV: {len(df)}")
    print(f"Towns: {df['town_code'].nunique()}")
    print(f"Seasons: {df[['season_year', 'season_period']].drop_duplicates().shape[0]}")
    print()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Scrape all seasons for all towns')
    parser.add_argument('--confirm', action='store_true', help='Confirm you want to run (takes 2-3 hours)')

    args = parser.parse_args()

    if not args.confirm:
        print()
        print("=" * 60)
        print("SCRAPE ALL SEASONS - ALL TOWNS")
        print("=" * 60)
        print()
        print("This will scrape:")
        print("  - 10 towns")
        print("  - 22 seasons (Fall 2025 - Fall 2015)")
        print("  - ~220 total scrapes")
        print()
        print("Estimated time: 2-3 hours (with 10-second crawl delays)")
        print()
        print("To start, run:")
        print("  python src/scrape_all_seasons.py --confirm")
        print()
    else:
        scrape_all_seasons_all_towns()
