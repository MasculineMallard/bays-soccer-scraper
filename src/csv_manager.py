"""
CSV Manager for BAYS Soccer Data

Handles all CSV operations for storing and retrieving team data.
Ensures data integrity and prevents duplicates.
"""

import os
import pandas as pd
from datetime import datetime
from typing import List, Dict, Set, Tuple
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.csv_schema import CSV_COLUMNS, CSV_FILE_PATH


class CSVManager:
    """Manages CSV data storage for BAYS soccer team data"""

    def __init__(self, csv_path: str = CSV_FILE_PATH):
        """
        Initialize CSV Manager

        Args:
            csv_path: Path to CSV file (default from config)
        """
        self.csv_path = csv_path
        self.ensure_csv_exists()

    def ensure_csv_exists(self):
        """Create CSV with headers if it doesn't exist"""
        if not os.path.exists(self.csv_path):
            # Create parent directory if needed
            os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)

            # Create empty DataFrame with schema columns
            df = pd.DataFrame(columns=CSV_COLUMNS)
            df.to_csv(self.csv_path, index=False)
            print(f"[OK] Created new CSV file: {self.csv_path}")
        else:
            print(f"[OK] CSV file exists: {self.csv_path}")

    def append_team(self, team_data: Dict) -> bool:
        """
        Append single team record to CSV

        Args:
            team_data: Dictionary with team data matching CSV_COLUMNS schema

        Returns:
            True if successful, False if duplicate or error
        """
        # Add scrape date if not provided
        if 'scrape_date' not in team_data:
            team_data['scrape_date'] = datetime.now().strftime('%Y-%m-%d')

        # Check for duplicate
        if self.is_duplicate(team_data):
            print(f"[!]  Duplicate record skipped: {team_data.get('team_name')} - {team_data.get('season_period')} {team_data.get('season_year')}")
            return False

        try:
            # Create DataFrame with single row
            df_new = pd.DataFrame([team_data])

            # Append to CSV
            df_new.to_csv(self.csv_path, mode='a', header=False, index=False)
            print(f"[OK] Added team: {team_data.get('team_name')} - {team_data.get('season_period')} {team_data.get('season_year')}")
            return True

        except Exception as e:
            print(f"[X] Error appending team: {str(e)}")
            return False

    def append_teams(self, teams_data: List[Dict]) -> Tuple[int, int]:
        """
        Append multiple team records to CSV (batch operation)

        Args:
            teams_data: List of dictionaries with team data

        Returns:
            Tuple of (added_count, skipped_count)
        """
        added = 0
        skipped = 0

        # Get existing teams to check duplicates once
        existing = self.get_existing_teams()

        # Filter out duplicates
        teams_to_add = []
        for team in teams_data:
            # Add scrape date if not provided
            if 'scrape_date' not in team:
                team['scrape_date'] = datetime.now().strftime('%Y-%m-%d')

            # Create unique key - include age_group, gender, and division
            key = (
                team.get('town_code'),
                team.get('season_year'),
                team.get('season_period'),
                team.get('team_name'),
                team.get('age_group'),
                team.get('gender'),
                team.get('division_level'),
                team.get('division_tier') if team.get('division_tier') else ''
            )

            if key in existing:
                skipped += 1
            else:
                teams_to_add.append(team)
                existing.add(key)  # Add to set to prevent duplicates within this batch
                added += 1

        # Batch append if we have teams to add
        if teams_to_add:
            try:
                df_new = pd.DataFrame(teams_to_add)
                df_new.to_csv(self.csv_path, mode='a', header=False, index=False)
                print(f"[OK] Batch added {added} teams")
            except Exception as e:
                print(f"[X] Error in batch append: {str(e)}")
                return (0, len(teams_data))

        if skipped > 0:
            print(f"[!]  Skipped {skipped} duplicate records")

        return (added, skipped)

    def load_csv(self) -> pd.DataFrame:
        """
        Load entire CSV into DataFrame

        Returns:
            DataFrame with all team data
        """
        try:
            if os.path.exists(self.csv_path):
                df = pd.read_csv(self.csv_path)
                print(f"[OK] Loaded {len(df)} records from CSV")
                return df
            else:
                print("[!]  CSV file does not exist, returning empty DataFrame")
                return pd.DataFrame(columns=CSV_COLUMNS)
        except Exception as e:
            print(f"[X] Error loading CSV: {str(e)}")
            return pd.DataFrame(columns=CSV_COLUMNS)

    def get_existing_teams(self) -> Set[Tuple]:
        """
        Get set of existing team-season combinations to avoid duplicates

        Returns:
            Set of (town_code, season_year, season_period, team_name, age_group, gender) tuples
        """
        try:
            if not os.path.exists(self.csv_path):
                return set()

            df = pd.read_csv(self.csv_path)

            # Create set of unique keys - include age_group, gender, AND division
            # for towns where teams have the same name (e.g., Medway "Mustangs" has multiple teams per age/gender)
            existing = set()
            for _, row in df.iterrows():
                key = (
                    row['town_code'],
                    row['season_year'],
                    row['season_period'],
                    row['team_name'],
                    row['age_group'],
                    row['gender'],
                    row['division_level'],
                    row['division_tier'] if pd.notna(row['division_tier']) else ''
                )
                existing.add(key)

            return existing

        except Exception as e:
            print(f"[X] Error getting existing teams: {str(e)}")
            return set()

    def is_duplicate(self, team_data: Dict) -> bool:
        """
        Check if team record already exists

        Args:
            team_data: Dictionary with team data

        Returns:
            True if duplicate, False if new
        """
        existing = self.get_existing_teams()
        key = (
            team_data.get('town_code'),
            team_data.get('season_year'),
            team_data.get('season_period'),
            team_data.get('team_name'),
            team_data.get('age_group'),
            team_data.get('gender'),
            team_data.get('division_level'),
            team_data.get('division_tier') if team_data.get('division_tier') else ''
        )
        return key in existing

    def get_stats_summary(self) -> Dict:
        """
        Get summary statistics about the CSV data

        Returns:
            Dictionary with summary stats
        """
        try:
            df = self.load_csv()

            if df.empty:
                return {
                    'total_records': 0,
                    'towns': 0,
                    'seasons': 0,
                    'age_groups': 0,
                    'divisions': 0
                }

            return {
                'total_records': len(df),
                'towns': df['town_code'].nunique(),
                'seasons': df[['season_year', 'season_period']].drop_duplicates().shape[0],
                'age_groups': df['age_group'].nunique(),
                'divisions': df['division_full'].nunique(),
                'earliest_season': f"{df['season_period'].iloc[-1]} {df['season_year'].min()}" if len(df) > 0 else 'N/A',
                'latest_season': f"{df['season_period'].iloc[0]} {df['season_year'].max()}" if len(df) > 0 else 'N/A',
            }

        except Exception as e:
            print(f"[X] Error getting stats: {str(e)}")
            return {}


# Convenience function for quick access
def get_manager() -> CSVManager:
    """Get a CSVManager instance with default settings"""
    return CSVManager()


if __name__ == "__main__":
    # Test the CSV manager
    print("=" * 60)
    print("CSV Manager Test")
    print("=" * 60)
    print()

    manager = CSVManager()

    # Test adding a sample team
    sample_team = {
        'town_code': 'FOX',
        'town_name': 'Foxborough Youth Soccer',
        'town_population': 18000,  # Placeholder
        'season_year': 2024,
        'season_period': 'Fall',
        'team_name': 'Foxboro U12 Boys Blue',
        'division_level': 2,
        'division_tier': 'A',
        'division_full': 'Division 2A',
        'age_group': 'U12',
        'gender': 'Boys',
        'wins': 8,
        'losses': 2,
        'ties': 1,
        'goals_for': 32,
        'goals_against': 15,
        'final_rank': 2,
        'total_teams_in_division': 10,
    }

    print("Testing single team append...")
    manager.append_team(sample_team)
    print()

    print("Testing duplicate detection...")
    manager.append_team(sample_team)  # Should be skipped
    print()

    print("CSV Summary:")
    stats = manager.get_stats_summary()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print()

    print("=" * 60)
    print("Test Complete")
    print("=" * 60)
