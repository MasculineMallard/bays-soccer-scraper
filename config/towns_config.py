"""
Configuration for towns to analyze
Foxborough vs 7 peer towns (similar population/demographics)

Excluded:
- MDY (Medway): Too small, lowest performer
- NOB (Northborough): Removed per user request
- WSF (Westford): No teams registered in recent seasons
"""

# Town codes and names - 8 towns total (Foxborough + 7 peers)
TOWNS = {
    'FOX': {
        'name': 'Foxborough Youth Soccer',
        'url_code': 'FOX',
        'population': 18618,  # 2020 Census
    },
    'HOP': {
        'name': 'Hopkinton Youth Soccer',
        'url_code': 'HOP',
        'population': 18758,
    },
    'WAL': {
        'name': 'Walpole Youth Soccer Association',
        'url_code': 'WAL',
        'population': 24070,
    },
    'WSB': {
        'name': 'Westborough Youth Soccer Association',
        'url_code': 'WSB',
        'population': 21567,
    },
    'MAN': {
        'name': 'Mansfield Youth Soccer',
        'url_code': 'MAN',
        'population': 25067,  # 2020 Census
    },
    'ASH': {
        'name': 'Ashland Youth Soccer',
        'url_code': 'ASH',
        'population': 18832,
    },
    'HOL': {
        'name': 'Holliston Youth Soccer Association',
        'url_code': 'HOL',
        'population': 15494,
    },
    'BEL': {
        'name': 'Bellingham Soccer Association',
        'url_code': 'BEL',
        'population': 16945,
    },
    'MDY': {
        'name': 'Medway Youth Soccer',
        'url_code': 'MDY',
        'population': 13115,  # 2020 Census
    },
}

# Season periods
SEASON_PERIODS = ['Fall', 'Spring']

# Grade groups (actual school grades)
# Note: Grades 7 and 8 are always mixed as "Grade 7/8"
GRADE_GROUPS = ['Grade 7/8', 'Grade 6', 'Grade 5', 'Grade 4', 'Grade 3', 'Grade 1/2']

# Division levels
DIVISION_LEVELS = [1, 2, 3, 4]

# Division tiers (within each level)
DIVISION_TIERS = ['A', 'B', 'C', 'D', 'E']

# Gender categories
GENDERS = ['Boys', 'Girls', 'Coed']
