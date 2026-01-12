"""
CSV schema definition for BAYS soccer team data
Each row represents one team-season combination
"""

# CSV Column Definitions
CSV_COLUMNS = [
    'town_code',              # FOX, HOP, etc.
    'town_name',              # Foxborough Youth Soccer
    'town_population',        # Population for normalization
    'season_year',            # 2024, 2023, etc.
    'season_period',          # Fall, Spring
    'team_name',              # Full team name
    'division_level',         # 1, 2, 3, or 4 (CRITICAL - now includes Division 1)
    'division_tier',          # A, B, C, etc. (e.g., 2A = Div 2 top tier)
    'division_full',          # Full division name (e.g., "U12 Boys Division 2A")
    'age_group',              # U8, U10, U12, U14, U16, U19
    'gender',                 # Boys, Girls, Coed
    'wins',                   # Total wins
    'losses',                 # Total losses
    'ties',                   # Total ties
    'goals_for',              # Goals scored
    'goals_against',          # Goals conceded
    'goal_differential',      # GF - GA
    'points',                 # Total points
    'final_rank',             # Rank in division (optional)
    'total_teams_in_division', # Number of teams competing
    'head_coach',             # Head coach name
    'assistant_coach',        # Assistant coach name
    'scrape_date',            # When data was scraped
]

# CSV file path
CSV_FILE_PATH = 'data/bays_teams.csv'

# Data types for validation
CSV_DTYPES = {
    'town_code': str,
    'town_name': str,
    'town_population': int,
    'season_year': int,
    'season_period': str,
    'team_name': str,
    'division_level': int,
    'division_tier': str,
    'division_full': str,
    'age_group': str,
    'gender': str,
    'wins': int,
    'losses': int,
    'ties': int,
    'goals_for': int,
    'goals_against': int,
    'final_rank': float,  # nullable, so use float
    'total_teams_in_division': int,
    'scrape_date': str,
}
