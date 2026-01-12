"""
Manual Data Entry Template

For manually entering team data when needed.
Use this for testing or when agent scraping needs manual assistance.
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.csv_manager import CSVManager


def parse_division(division_string: str) -> tuple:
    """
    Parse division string into level and tier

    Examples:
        "2/A" -> (2, 'A')
        "Division 2A" -> (2, 'A')
        "3/B" -> (3, 'B')
        "1" -> (1, None)

    Args:
        division_string: String like "2/A" or "Division 2A"

    Returns:
        Tuple of (level: int, tier: str or None)
    """
    division_string = division_string.strip()

    # Handle format like "2/A"
    if '/' in division_string:
        parts = division_string.split('/')
        level = int(parts[0])
        tier = parts[1].upper() if len(parts) > 1 and parts[1] else None
        return (level, tier)

    # Handle format like "Division 2A"
    if 'Division' in division_string:
        division_string = division_string.replace('Division', '').strip()

    # Extract level (first digit)
    level = None
    for char in division_string:
        if char.isdigit():
            level = int(char)
            break

    # Extract tier (letters after level)
    tier = None
    if level:
        remainder = division_string.replace(str(level), '').strip()
        if remainder and remainder[0].isalpha():
            tier = remainder[0].upper()

    return (level, tier)


def create_team_record(
    town_code: str,
    town_name: str,
    town_population: int,
    season_year: int,
    season_period: str,
    team_name: str,
    division_string: str,
    age_group: str,
    gender: str,
    wins: int,
    losses: int,
    ties: int,
    goals_for: int,
    goals_against: int,
    final_rank: int = None,
    total_teams_in_division: int = None,
    head_coach: str = None,
    assistant_coach: str = None,
    points: int = None,
    goal_differential: int = None
) -> dict:
    """
    Create a team record dictionary from input parameters

    Args:
        town_code: 3-letter town code (e.g., 'FOX', 'HOP')
        town_name: Full organization name
        town_population: Town population for normalization
        season_year: Year (e.g., 2024)
        season_period: 'Fall' or 'Spring'
        team_name: Full team name
        division_string: Division like "2/A" or "Division 2A"
        age_group: Age group like 'U12', 'U14'
        gender: 'Boys', 'Girls', or 'Coed'
        wins: Number of wins
        losses: Number of losses
        ties: Number of ties
        goals_for: Goals scored
        goals_against: Goals conceded
        final_rank: Final rank in division (optional)
        total_teams_in_division: Total teams in division (optional)

    Returns:
        Dictionary matching CSV schema
    """
    level, tier = parse_division(division_string)

    # Reconstruct full division name
    if tier:
        division_full = f"Division {level}{tier}"
    else:
        division_full = f"Division {level}"

    # Calculate goal differential and points if not provided
    if goal_differential is None:
        goal_differential = goals_for - goals_against

    if points is None:
        points = (wins * 3) + ties  # Standard soccer scoring: 3 pts for win, 1 for tie

    return {
        'town_code': town_code,
        'town_name': town_name,
        'town_population': town_population,
        'season_year': season_year,
        'season_period': season_period,
        'team_name': team_name,
        'division_level': level,
        'division_tier': tier,
        'division_full': division_full,
        'age_group': age_group,
        'gender': gender,
        'wins': wins,
        'losses': losses,
        'ties': ties,
        'goals_for': goals_for,
        'goals_against': goals_against,
        'goal_differential': goal_differential,
        'points': points,
        'final_rank': final_rank,
        'total_teams_in_division': total_teams_in_division,
        'head_coach': head_coach,
        'assistant_coach': assistant_coach,
    }


def add_sample_teams():
    """Add sample teams to test CSV manager"""

    manager = CSVManager()

    # Sample teams from different towns and seasons
    sample_teams = [
        create_team_record(
            town_code='FOX',
            town_name='Foxborough Youth Soccer',
            town_population=18000,
            season_year=2024,
            season_period='Fall',
            team_name='Foxboro U12 Boys Blue',
            division_string='2/A',
            age_group='U12',
            gender='Boys',
            wins=8,
            losses=2,
            ties=1,
            goals_for=32,
            goals_against=15,
            final_rank=2,
            total_teams_in_division=10
        ),
        create_team_record(
            town_code='HOP',
            town_name='Hopkinton Youth Soccer',
            town_population=18000,
            season_year=2024,
            season_period='Fall',
            team_name='Hopkinton U14 Girls',
            division_string='Division 3B',
            age_group='U14',
            gender='Girls',
            wins=5,
            losses=4,
            ties=2,
            goals_for=22,
            goals_against=18,
            final_rank=5,
            total_teams_in_division=12
        ),
    ]

    # Batch add
    added, skipped = manager.append_teams(sample_teams)

    print()
    print(f"Added {added} teams, skipped {skipped} duplicates")
    print()

    # Show stats
    stats = manager.get_stats_summary()
    print("CSV Summary:")
    for key, value in stats.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    print("=" * 60)
    print("Manual Data Entry - Sample Teams")
    print("=" * 60)
    print()

    # Test division parsing
    print("Testing division parsing:")
    test_divisions = ["2/A", "Division 3B", "1", "4/C"]
    for div in test_divisions:
        level, tier = parse_division(div)
        print(f"  '{div}' -> Level: {level}, Tier: {tier}")
    print()

    # Add sample teams
    add_sample_teams()

    print()
    print("=" * 60)
    print("Complete")
    print("=" * 60)
