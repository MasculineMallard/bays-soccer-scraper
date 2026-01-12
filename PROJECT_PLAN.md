# BAYS Soccer Scraper - Detailed Implementation Plan

## Project Overview
Scrape historical soccer data from bays.org for 10 towns over 10 seasons to analyze and compare team performance across towns.

**Target Website:** https://bays.org
**Primary Example:** https://bays.org/bays/organizations/view/FOX (Foxborough)

---

## Target Towns (Organizations)

1. **FOX** - Foxborough Youth Soccer
2. **HOP** - Hopkinton Youth Soccer
3. **WAL** - Walpole Youth Soccer Association
4. **WES** - Westborough Youth Soccer Association
5. **SUD** - Sudbury Youth Soccer
6. **ASH** - Ashland Youth Soccer
7. **HOL** - Holliston Youth Soccer Association
8. **BEL** - Bellingham Soccer Association
9. **NOR** - Northborough Youth Soccer Association
10. **MED** - Medway Youth Soccer Association
11. **WEF** - Westford Youth Soccer Association

*Note: 11 towns total (10 comparison towns + Foxborough)*

---

## Robots.txt Compliance Requirements

**CRITICAL:** Must respect robots.txt rules:
- ✅ **Crawl-delay: 10 seconds** between requests (MANDATORY)
- ✅ Allow: Public organization pages, team data, standings
- ❌ Disallow: /admin/, /user/, /search/, /node/add/, etc.
- ✅ Content-signal: search=yes (we can index for search purposes)
- ❌ Content-signal: ai-train=no (no AI training on this data)
- ⚠️ **Cloudflare Protection:** Site uses Cloudflare - need proper headers and rate limiting

---

## Technical Stack Recommendation

### Core Technologies
- **Language:** Python 3.9+
- **Web Scraping:**
  - **PRIMARY: Claude Code Agent** for manual scraping (if API doesn't work)
  - `requests` with `requests-cache` (for caching and rate limiting - if API works)
  - `BeautifulSoup4` (HTML parsing)
  - `selenium` (backup if JavaScript rendering needed)
- **Data Storage:**
  - **Single CSV file** (row-level data in project folder)
  - Simple, portable, easy to inspect
- **Data Analysis:**
  - `pandas` (data manipulation)
  - `numpy` (numerical operations)
- **Visualization/BI Tool:**
  - **Streamlit** (FREE, Python-based, you already use it in mmolb-stats)

---

## Implementation Plan - Broken into Coding Chunks

### **PHASE 1: Project Setup & Research** (2-3 coding sessions)

#### Chunk 1.1: Project Structure & Environment
**Goal:** Set up project directory and dependencies
**Files to create:**
- `bays-soccer-scraper/`
  - `README.md` - Project documentation
  - `requirements.txt` - Python dependencies
  - `.env.example` - Environment variables template
  - `.gitignore` - Git ignore file
  - `config/`
    - `scraper_config.py` - Scraping configuration
    - `towns_config.py` - Town codes and names
  - `src/` - Source code directory
  - `data/` - Data storage
    - `raw/` - Raw scraped data
    - `processed/` - Cleaned data
    - `database/` - SQLite database
  - `logs/` - Scraping logs
  - `tests/` - Unit tests

**Code tasks:**
```python
# requirements.txt content needed:
# pandas>=2.0.0
# numpy>=1.24.0
# streamlit>=1.28.0
# plotly>=5.17.0
# requests>=2.31.0  (optional - if API scraping works)
# beautifulsoup4>=4.12.0  (optional - if API scraping works)
# lxml>=4.9.0  (optional - if API scraping works)
```

#### Chunk 1.2: Initial Reconnaissance
**Goal:** Manually explore bays.org structure and identify data patterns
**Tasks:**
- Visit each town's organization page
- Document URL patterns (e.g., `/bays/organizations/view/{TOWN_CODE}`)
- Identify links to team pages, standings, schedules
- Determine season selection mechanism
- Screenshot key page layouts
- Map out data hierarchy: Organization → Seasons → Divisions → Teams → Games

**Deliverable:** Document `docs/site_structure.md` with findings

#### Chunk 1.3: Test Single Page Scrape
**Goal:** Prove we can successfully scrape one organization page
**File:** `src/test_scraper.py`
**Code:**
```python
import requests
import time
from bs4 import BeautifulSoup

def test_scrape_fox():
    """Test scraping Foxborough organization page"""
    url = "https://bays.org/bays/organizations/view/FOX"

    # Respect robots.txt - 10 second delay
    time.sleep(10)

    # Proper headers to avoid blocks
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; BAYSResearchBot/1.0; +http://yoursite.com/bot)',
        'Accept': 'text/html,application/xhtml+xml',
    }

    response = requests.get(url, headers=headers, timeout=30)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        # Extract organization name, teams, etc.
        print(f"Success! Page title: {soup.title.string}")
    else:
        print(f"Failed: {response.status_code}")

if __name__ == "__main__":
    test_scrape_fox()
```

---

### **PHASE 2: Core Scraper Development** (4-5 coding sessions)

#### Chunk 2.1: Configuration Management
**Goal:** Centralize all configuration
**File:** `config/scraper_config.py`
```python
# Scraper settings
CRAWL_DELAY = 10  # seconds - respects robots.txt
REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
CACHE_EXPIRE_DAYS = 7

# Database
DB_PATH = "data/database/bays_soccer.db"

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "logs/scraper.log"
```

**File:** `config/towns_config.py`
```python
TOWNS = {
    'FOX': {'name': 'Foxborough Youth Soccer', 'url_code': 'FOX'},
    'HOP': {'name': 'Hopkinton Youth Soccer', 'url_code': 'HOP'},
    'WAL': {'name': 'Walpole Youth Soccer Association', 'url_code': 'WAL'},
    # ... etc for all 11 towns
}

# Seasons to scrape (adjust based on what's available)
SEASONS = [
    '2024-Fall', '2024-Spring',
    '2023-Fall', '2023-Spring',
    '2022-Fall', '2022-Spring',
    '2021-Fall', '2021-Spring',
    '2020-Fall', '2020-Spring',
]
```

#### Chunk 2.2: HTTP Client with Rate Limiting
**Goal:** Build a robust HTTP client that respects robots.txt
**File:** `src/http_client.py`
```python
import time
import logging
from typing import Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests_cache import CachedSession

class BAYSClient:
    """HTTP client for bays.org with rate limiting and caching"""

    def __init__(self, crawl_delay: int = 10):
        self.crawl_delay = crawl_delay
        self.last_request_time = 0

        # Setup caching
        self.session = CachedSession(
            'bays_cache',
            expire_after=604800,  # 7 days
        )

        # Setup retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; ResearchBot/1.0)',
            'Accept': 'text/html,application/xhtml+xml',
        }

    def get(self, url: str) -> Optional[requests.Response]:
        """GET request with rate limiting"""
        # Enforce crawl delay
        elapsed = time.time() - self.last_request_time
        if elapsed < self.crawl_delay:
            time.sleep(self.crawl_delay - elapsed)

        try:
            response = self.session.get(url, headers=self.headers, timeout=30)
            self.last_request_time = time.time()
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"Request failed for {url}: {e}")
            return None
```

#### Chunk 2.3: HTML Parser
**Goal:** Extract data from organization/team pages
**File:** `src/parser.py`
```python
from bs4 import BeautifulSoup
from typing import Dict, List

class BAYSParser:
    """Parse BAYS organization and team pages"""

    def parse_organization_page(self, html: str) -> Dict:
        """Extract organization info and team links"""
        soup = BeautifulSoup(html, 'lxml')

        data = {
            'org_name': None,
            'teams': [],
            'seasons_available': [],
        }

        # TODO: Actual parsing logic based on site structure
        # This is a template - needs site inspection

        return data

    def parse_team_page(self, html: str) -> Dict:
        """Extract team details, roster, schedule"""
        soup = BeautifulSoup(html, 'lxml')

        data = {
            'team_name': None,
            'division': None,
            'age_group': None,
            'record': {'wins': 0, 'losses': 0, 'ties': 0},
            'games': [],
        }

        # TODO: Actual parsing logic

        return data

    def parse_standings_page(self, html: str) -> List[Dict]:
        """Extract division standings"""
        soup = BeautifulSoup(html, 'lxml')

        standings = []
        # TODO: Parse standings table

        return standings
```

#### Chunk 2.4: URL Discovery
**Goal:** Find all relevant URLs to scrape
**File:** `src/url_builder.py`
```python
from typing import List
from config.towns_config import TOWNS, SEASONS

class URLBuilder:
    """Build URLs for scraping BAYS data"""

    BASE_URL = "https://bays.org"

    @staticmethod
    def get_organization_url(town_code: str) -> str:
        """Get organization main page URL"""
        return f"{URLBuilder.BASE_URL}/bays/organizations/view/{town_code}"

    @staticmethod
    def get_all_organization_urls() -> List[str]:
        """Get URLs for all target towns"""
        return [
            URLBuilder.get_organization_url(code)
            for code in TOWNS.keys()
        ]

    # Additional methods will be added after site exploration
    # e.g., get_team_url, get_standings_url, get_season_url
```

#### Chunk 2.5: Main Scraper Orchestrator
**Goal:** Coordinate the scraping process
**File:** `src/scraper.py`
```python
import logging
from typing import Dict, List
from src.http_client import BAYSClient
from src.parser import BAYSParser
from src.url_builder import URLBuilder
from config.towns_config import TOWNS

class BAYSScraper:
    """Main scraper for BAYS organization data"""

    def __init__(self):
        self.client = BAYSClient(crawl_delay=10)
        self.parser = BAYSParser()
        self.url_builder = URLBuilder()
        self.data = []

    def scrape_organization(self, town_code: str) -> Dict:
        """Scrape all data for one organization"""
        logging.info(f"Scraping organization: {town_code}")

        url = self.url_builder.get_organization_url(town_code)
        response = self.client.get(url)

        if not response:
            return None

        org_data = self.parser.parse_organization_page(response.text)

        # TODO: Follow links to teams, standings, etc.

        return org_data

    def scrape_all_organizations(self) -> List[Dict]:
        """Scrape all target organizations"""
        results = []

        for town_code in TOWNS.keys():
            org_data = self.scrape_organization(town_code)
            if org_data:
                results.append(org_data)

        return results

    def save_raw_data(self, data: Dict, filename: str):
        """Save raw scraped data to JSON"""
        import json
        import os

        os.makedirs('data/raw', exist_ok=True)
        with open(f'data/raw/{filename}.json', 'w') as f:
            json.dump(data, f, indent=2)
```

---

### **PHASE 3: CSV Data Storage** (1 coding session)

#### Chunk 3.1: CSV Schema Definition
**Goal:** Define single CSV structure for all scraped data
**File:** `config/csv_schema.py`
```python
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
    'final_rank',             # Rank in division (optional)
    'total_teams_in_division', # Number of teams competing
    'scrape_date',            # When data was scraped
]

# CSV file path
CSV_FILE_PATH = 'data/bays_teams.csv'
```

#### Chunk 3.2: CSV Manager
**Goal:** Create utility to read/write CSV data safely
**File:** `src/csv_manager.py`
```python
import pandas as pd
import os
from datetime import datetime
from config.csv_schema import CSV_COLUMNS, CSV_FILE_PATH

class CSVManager:
    """Manage CSV data storage"""

    def __init__(self, csv_path: str = CSV_FILE_PATH):
        self.csv_path = csv_path
        self.ensure_csv_exists()

    def ensure_csv_exists(self):
        """Create CSV with headers if it doesn't exist"""
        if not os.path.exists(self.csv_path):
            os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)
            df = pd.DataFrame(columns=CSV_COLUMNS)
            df.to_csv(self.csv_path, index=False)

    def append_team(self, team_data: dict):
        """Append single team row to CSV"""
        # Validate data has all required columns
        team_data['scrape_date'] = datetime.now().strftime('%Y-%m-%d')

        df_new = pd.DataFrame([team_data])

        # Append to existing CSV
        df_new.to_csv(self.csv_path, mode='a', header=False, index=False)

    def append_teams(self, teams_data: list):
        """Append multiple team rows to CSV"""
        if not teams_data:
            return

        df_new = pd.DataFrame(teams_data)
        df_new['scrape_date'] = datetime.now().strftime('%Y-%m-%d')

        # Append to existing CSV
        df_new.to_csv(self.csv_path, mode='a', header=False, index=False)

    def load_csv(self) -> pd.DataFrame:
        """Load entire CSV into DataFrame"""
        return pd.read_csv(self.csv_path)

    def get_existing_teams(self) -> set:
        """Get set of existing team-season combinations to avoid duplicates"""
        df = self.load_csv()
        return set(
            df[['town_code', 'season_year', 'season_period', 'team_name']]
            .apply(tuple, axis=1)
        )
```

#### Chunk 3.3: Data Collection Template
**Goal:** Template for manually entering scraped data
**File:** `src/manual_data_entry.py`
```python
from src.csv_manager import CSVManager

def add_team_manually():
    """Interactive prompt to add team data manually"""
    csv_manager = CSVManager()

    print("=== Manual Team Data Entry ===")

    team_data = {
        'town_code': input("Town code (FOX, HOP, etc.): ").upper(),
        'town_name': input("Town name: "),
        'town_population': int(input("Town population: ")),
        'season_year': int(input("Season year (2024): ")),
        'season_period': input("Season period (Fall/Spring): "),
        'team_name': input("Team name: "),
        'division_level': int(input("Division level (2, 3, or 4): ")),
        'division_full': input("Full division name (e.g., U12 Boys Division 2): "),
        'age_group': input("Age group (U8, U10, etc.): "),
        'gender': input("Gender (Boys/Girls/Coed): "),
        'wins': int(input("Wins: ")),
        'losses': int(input("Losses: ")),
        'ties': int(input("Ties: ")),
        'goals_for': int(input("Goals for: ")),
        'goals_against': int(input("Goals against: ")),
        'final_rank': input("Final rank (leave blank if unknown): ") or None,
        'total_teams_in_division': int(input("Total teams in division: ")),
    }

    csv_manager.append_team(team_data)
    print(f"✅ Team added: {team_data['team_name']}")

if __name__ == "__main__":
    add_team_manually()
```

---

### **PHASE 4: Data Validation & Quality** (1-2 coding sessions)

#### Chunk 4.1: Data Validation
**Goal:** Ensure scraped data quality
**File:** `src/validation.py`
```python
import pandas as pd
from typing import Dict, List

class DataValidator:
    """Validate scraped data quality"""

    @staticmethod
    def validate_team_record(team: Dict) -> bool:
        """Validate team record makes sense"""
        # Check wins + losses + ties equals games played
        # Check goals_for and goals_against are non-negative
        # etc.
        pass

    @staticmethod
    def validate_completeness(df: pd.DataFrame) -> Dict:
        """Check data completeness"""
        report = {
            'total_rows': len(df),
            'missing_values': df.isnull().sum().to_dict(),
            'duplicate_rows': df.duplicated().sum(),
        }
        return report

    @staticmethod
    def validate_season_coverage(db_path: str) -> Dict:
        """Verify we have data for all target seasons/towns"""
        # Check each town has data for each season
        pass
```

#### Chunk 4.2: Error Handling & Logging
**Goal:** Robust error handling and audit trail
**File:** `src/utils/logging_config.py`
```python
import logging
import os

def setup_logging():
    """Configure logging for scraper"""
    os.makedirs('logs', exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/scraper.log'),
            logging.StreamHandler()
        ]
    )

# Track scraping progress
class ProgressTracker:
    """Track which URLs have been scraped"""

    def __init__(self, checkpoint_file='logs/progress.json'):
        self.checkpoint_file = checkpoint_file
        self.completed_urls = self.load_progress()

    def load_progress(self):
        """Load previously completed URLs"""
        import json
        if os.path.exists(self.checkpoint_file):
            with open(self.checkpoint_file, 'r') as f:
                return set(json.load(f))
        return set()

    def mark_completed(self, url: str):
        """Mark URL as scraped"""
        self.completed_urls.add(url)
        self.save_progress()

    def save_progress(self):
        """Save progress to file"""
        import json
        with open(self.checkpoint_file, 'w') as f:
            json.dump(list(self.completed_urls), f)
```

---

### **PHASE 5: Data Analysis & Transformation** (2-3 coding sessions)

#### Chunk 5.1: Data Aggregation
**Goal:** Create analysis-ready datasets
**File:** `src/analysis/aggregator.py`
```python
import pandas as pd
from src.database.db_manager import DatabaseManager

class DataAggregator:
    """Aggregate data for analysis"""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def get_town_performance_by_season(self) -> pd.DataFrame:
        """Aggregate performance metrics by town and season"""
        # Query database
        # Group by organization, season
        # Calculate: total wins, win %, avg goals, etc.
        pass

    def get_division_performance(self, division: str) -> pd.DataFrame:
        """Performance in specific division across towns"""
        pass

    def get_head_to_head(self, town1: str, town2: str) -> pd.DataFrame:
        """Head-to-head record between two towns"""
        pass

    def export_to_csv(self):
        """Export analysis datasets to CSV for BI tools"""
        # Export various views for Streamlit/BI consumption
        os.makedirs('data/processed', exist_ok=True)

        # Town summary
        town_summary = self.get_town_performance_by_season()
        town_summary.to_csv('data/processed/town_summary.csv', index=False)

        # Division breakdown
        # Head-to-head matrix
        # etc.
```

#### Chunk 5.2: Metrics Calculation (WITH POPULATION NORMALIZATION)
**Goal:** Calculate comparative metrics normalized by population
**File:** `src/analysis/metrics.py`
```python
import pandas as pd

class MetricsCalculator:
    """Calculate performance metrics with population normalization"""

    @staticmethod
    def calculate_win_percentage(wins, losses, ties):
        """Win percentage (ties count as 0.5 wins)"""
        total_games = wins + losses + ties
        if total_games == 0:
            return 0.0
        return (wins + 0.5 * ties) / total_games

    @staticmethod
    def calculate_goal_differential(goals_for, goals_against):
        """Goal differential"""
        return goals_for - goals_against

    @staticmethod
    def calculate_per_capita_metrics(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate per-capita metrics normalized by population
        CRITICAL: This allows fair comparison between towns
        """
        # Teams per 1000 residents (by division level)
        df['teams_per_1000'] = (df['team_count'] / df['town_population']) * 1000

        # Wins per 1000 residents
        df['wins_per_1000'] = (df['total_wins'] / df['town_population']) * 1000

        # Goals per 1000 residents
        df['goals_per_1000'] = (df['total_goals_for'] / df['town_population']) * 1000

        return df

    @staticmethod
    def calculate_division_level_performance(df: pd.DataFrame, level: int) -> pd.DataFrame:
        """
        Performance metrics for specific division level (2, 3, or 4)
        This is the PRIMARY analysis - controlling for level
        """
        df_level = df[df['division_level'] == level].copy()

        # Group by town
        grouped = df_level.groupby('town_code').agg({
            'wins': 'sum',
            'losses': 'sum',
            'ties': 'sum',
            'goals_for': 'sum',
            'goals_against': 'sum',
            'team_name': 'count',  # Number of teams
            'town_population': 'first',
            'town_name': 'first',
        }).reset_index()

        grouped.rename(columns={'team_name': 'team_count'}, inplace=True)

        # Calculate metrics
        grouped['win_pct'] = grouped.apply(
            lambda row: MetricsCalculator.calculate_win_percentage(
                row['wins'], row['losses'], row['ties']
            ), axis=1
        )
        grouped['goal_diff'] = grouped['goals_for'] - grouped['goals_against']

        # Per-capita normalization
        grouped['teams_per_1000'] = (grouped['team_count'] / grouped['town_population']) * 1000
        grouped['wins_per_team'] = grouped['wins'] / grouped['team_count']
        grouped['goals_per_team'] = grouped['goals_for'] / grouped['team_count']

        # Rank
        grouped['rank'] = grouped['win_pct'].rank(ascending=False)

        return grouped.sort_values('win_pct', ascending=False)

    @staticmethod
    def calculate_foxboro_vs_peers(df: pd.DataFrame, level: int) -> dict:
        """
        Compare Foxboro to peer average for specific division level
        Returns dict with comparison metrics
        """
        df_level = MetricsCalculator.calculate_division_level_performance(df, level)

        fox_data = df_level[df_level['town_code'] == 'FOX'].iloc[0]
        peer_data = df_level[df_level['town_code'] != 'FOX']

        comparison = {
            'level': level,
            'foxboro_win_pct': fox_data['win_pct'],
            'peer_avg_win_pct': peer_data['win_pct'].mean(),
            'foxboro_vs_peer_win_pct': fox_data['win_pct'] - peer_data['win_pct'].mean(),
            'foxboro_goal_diff': fox_data['goal_diff'],
            'peer_avg_goal_diff': peer_data['goal_diff'].mean(),
            'foxboro_vs_peer_goal_diff': fox_data['goal_diff'] - peer_data['goal_diff'].mean(),
            'foxboro_teams': fox_data['team_count'],
            'peer_avg_teams': peer_data['team_count'].mean(),
            'foxboro_teams_per_1000': fox_data['teams_per_1000'],
            'peer_avg_teams_per_1000': peer_data['teams_per_1000'].mean(),
            'foxboro_rank': fox_data['rank'],
            'total_towns': len(df_level),
        }

        return comparison

    @staticmethod
    def calculate_program_strength(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate program strength indicator
        Higher % in Div 1/2A = stronger program depth
        """
        # Count teams by division level for each town
        town_dist = df.groupby(['town_code', 'division_level', 'division_tier']).size().reset_index(name='team_count')

        # Calculate % in high divisions (1, 2A) vs low (3, 4)
        def classify_strength(row):
            if row['division_level'] == 1:
                return 'Elite'
            elif row['division_level'] == 2 and row['division_tier'] == 'A':
                return 'High'
            elif row['division_level'] == 2:
                return 'Medium'
            else:  # 3, 4
                return 'Low'

        town_dist['strength_tier'] = town_dist.apply(classify_strength, axis=1)

        # Aggregate by town
        strength_summary = town_dist.groupby('town_code')['team_count'].agg(['sum']).reset_index()
        elite_count = town_dist[town_dist['strength_tier'] == 'Elite'].groupby('town_code')['team_count'].sum()
        high_count = town_dist[town_dist['strength_tier'] == 'High'].groupby('town_code')['team_count'].sum()

        strength_summary['elite_pct'] = (elite_count / strength_summary['sum']) * 100
        strength_summary['elite_high_pct'] = ((elite_count + high_count) / strength_summary['sum']) * 100

        return strength_summary

    @staticmethod
    def calculate_lag_indicators(df: pd.DataFrame, town_code: str = 'FOX') -> dict:
        """
        Calculate trend indicators to show if Foxboro is improving or declining
        Returns creative lag metrics
        """
        # Sort by season chronologically
        df_sorted = df.sort_values(['season_year', 'season_period'])

        # Calculate win % by season for town and peers
        town_trends = []
        peer_trends = []

        for season in df_sorted[['season_year', 'season_period']].drop_duplicates().values:
            season_data = df_sorted[
                (df_sorted['season_year'] == season[0]) &
                (df_sorted['season_period'] == season[1])
            ]

            town_season = season_data[season_data['town_code'] == town_code]
            peer_season = season_data[season_data['town_code'] != town_code]

            if len(town_season) > 0:
                town_wp = MetricsCalculator.calculate_win_percentage(
                    town_season['wins'].sum(),
                    town_season['losses'].sum(),
                    town_season['ties'].sum()
                )
                town_trends.append(town_wp)

                peer_wp = MetricsCalculator.calculate_win_percentage(
                    peer_season['wins'].sum(),
                    peer_season['losses'].sum(),
                    peer_season['ties'].sum()
                )
                peer_trends.append(peer_wp)

        # Calculate trend slopes (simple linear regression)
        import numpy as np
        if len(town_trends) > 2:
            x = np.arange(len(town_trends))
            town_slope = np.polyfit(x, town_trends, 1)[0]
            peer_slope = np.polyfit(x, peer_trends, 1)[0]

            return {
                'town_trend': 'Improving' if town_slope > 0 else 'Declining',
                'town_slope': town_slope,
                'peer_slope': peer_slope,
                'relative_trend': 'Outpacing peers' if town_slope > peer_slope else 'Lagging peers',
                'trend_differential': town_slope - peer_slope,
            }

        return None
```

---

### **PHASE 6: Visualization & Dashboard** (3-4 coding sessions)

#### Chunk 6.1: Streamlit Dashboard Setup
**Goal:** Create interactive dashboard (following mmolb-stats pattern)
**File:** `app.py`
```python
import streamlit as st
import pandas as pd
import plotly.express as px
from src.database.db_manager import DatabaseManager
from src.analysis.aggregator import DataAggregator

st.set_page_config(
    page_title="BAYS Soccer Analysis",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ BAYS Soccer Town Comparison")
st.markdown("Compare performance across 11 towns over 10 seasons")

# Sidebar filters
st.sidebar.header("Filters")
seasons = st.sidebar.multiselect("Select Seasons", options=get_all_seasons())
towns = st.sidebar.multiselect("Select Towns", options=get_all_towns())
divisions = st.sidebar.multiselect("Select Divisions", options=get_all_divisions())

# Main content
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🏆 Town Rankings",
    "⚔️ Head-to-Head",
    "📈 Trends"
])

with tab1:
    show_overview_metrics()

with tab2:
    show_town_rankings()

with tab3:
    show_head_to_head()

with tab4:
    show_trends_over_time()
```

#### Chunk 6.2: Overview Dashboard
**File:** `streamlit_pages/overview.py`
```python
import streamlit as st
import plotly.express as px

def show_overview_metrics():
    """Display high-level overview"""

    # Key metrics in columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Teams Tracked", "450")
        st.metric("Total Games", "2,340")

    with col2:
        st.metric("Seasons Analyzed", "10")
        st.metric("Towns Compared", "11")

    with col3:
        st.metric("Top Performing Town", "Sudbury")
        st.metric("Avg Win Rate", "52.3%")

    with col4:
        st.metric("Most Competitive Division", "U12 Boys D1")
        st.metric("Total Goals Scored", "8,432")

    # Win percentage by town - bar chart
    st.subheader("Win Percentage by Town (All Seasons)")
    # Plot bar chart with plotly

    # Goals scored over time - line chart
    st.subheader("Total Goals by Season")
    # Plot line chart
```

#### Chunk 6.3: Division Level Rankings Page (MAIN ANALYSIS)
**File:** `streamlit_pages/rankings.py`
```python
import streamlit as st
import pandas as pd
from src.analysis.metrics import MetricsCalculator

def show_town_rankings():
    """Interactive town rankings BY DIVISION LEVEL"""

    st.subheader("🏆 Town Performance Rankings by Division Level")
    st.markdown("**Controlling for division level (2, 3, 4) - normalized by population**")

    # Division level selector
    level = st.selectbox(
        "Select Division Level",
        [1, 2, 3, 4],
        format_func=lambda x: f"Division {x}"
    )

    # Gender selector
    gender = st.selectbox(
        "Select Gender",
        ["All", "Boys", "Girls"]
    )

    # Load data
    df = load_csv_data()
    df_level = MetricsCalculator.calculate_division_level_performance(df, level)

    # Highlight Foxboro
    def highlight_foxboro(row):
        if row['town_code'] == 'FOX':
            return ['background-color: #fffacd'] * len(row)
        return [''] * len(row)

    # Display table
    st.dataframe(
        df_level.style.apply(highlight_foxboro, axis=1),
        column_config={
            "rank": st.column_config.NumberColumn("Rank", format="%d"),
            "town_name": "Town",
            "team_count": st.column_config.NumberColumn("Teams", format="%d"),
            "teams_per_1000": st.column_config.NumberColumn(
                "Teams/1000 Pop",
                format="%.2f",
                help="Teams per 1000 residents (population normalized)"
            ),
            "wins": st.column_config.NumberColumn("W", format="%d"),
            "losses": st.column_config.NumberColumn("L", format="%d"),
            "ties": st.column_config.NumberColumn("T", format="%d"),
            "win_pct": st.column_config.ProgressColumn(
                "Win %",
                format="%.1f%%",
                min_value=0,
                max_value=100,
            ),
            "wins_per_team": st.column_config.NumberColumn("W/Team", format="%.2f"),
            "goal_diff": st.column_config.NumberColumn("Goal Diff", format="%+d"),
            "goals_per_team": st.column_config.NumberColumn("Goals/Team", format="%.1f"),
        },
        hide_index=True,
        use_container_width=True
    )

    # Foxboro vs Peers comparison
    st.subheader(f"🎯 Foxboro vs. Peer Average (Level {level})")

    comparison = MetricsCalculator.calculate_foxboro_vs_peers(df, level)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Win % Difference",
            f"{comparison['foxboro_vs_peer_win_pct']:.1%}",
            delta=f"{comparison['foxboro_vs_peer_win_pct']:.1%}",
            delta_color="normal"
        )

    with col2:
        st.metric(
            "Goal Diff vs Peers",
            f"{comparison['foxboro_vs_peer_goal_diff']:+.1f}",
            delta=f"{comparison['foxboro_vs_peer_goal_diff']:+.1f}",
            delta_color="normal"
        )

    with col3:
        st.metric(
            "Teams per 1000 vs Peers",
            f"{comparison['foxboro_teams_per_1000'] - comparison['peer_avg_teams_per_1000']:+.2f}",
            delta=f"{comparison['foxboro_teams_per_1000'] - comparison['peer_avg_teams_per_1000']:+.2f}",
            delta_color="normal"
        )

    # Summary text
    st.markdown(f"""
    **Summary:**
    - Foxboro ranks **#{int(comparison['foxboro_rank'])}** out of {comparison['total_towns']} towns in Level {level}
    - Foxboro fields **{comparison['foxboro_teams']:.0f} teams** vs peer average of **{comparison['peer_avg_teams']:.1f}**
    - Foxboro win rate: **{comparison['foxboro_win_pct']:.1%}** vs peer average **{comparison['peer_avg_win_pct']:.1%}**
    """)
```

#### Chunk 6.4: Head-to-Head Comparison
**File:** `streamlit_pages/head_to_head.py`
```python
import streamlit as st
import plotly.graph_objects as go

def show_head_to_head():
    """Head-to-head comparison tool"""

    st.subheader("⚔️ Head-to-Head Comparison")

    col1, col2 = st.columns(2)

    with col1:
        town1 = st.selectbox("Select Town 1", towns, index=0)

    with col2:
        town2 = st.selectbox("Select Town 2", towns, index=1)

    if town1 != town2:
        # Load head-to-head data
        h2h_data = get_head_to_head_data(town1, town2)

        # Display record
        st.metric(f"{town1} Wins", h2h_data['town1_wins'])
        st.metric(f"{town2} Wins", h2h_data['town2_wins'])
        st.metric("Ties", h2h_data['ties'])

        # Radar chart comparing metrics
        fig = create_comparison_radar(town1, town2)
        st.plotly_chart(fig, use_container_width=True)

        # Game history table
        st.subheader("Game History")
        st.dataframe(h2h_data['games'])
```

#### Chunk 6.5: Trends Analysis
**File:** `streamlit_pages/trends.py`
```python
import streamlit as st
import plotly.express as px

def show_trends_over_time():
    """Analyze trends across seasons"""

    st.subheader("📈 Performance Trends Over Time")

    # Multi-line chart: win % by town over seasons
    trend_data = get_trend_data()

    fig = px.line(
        trend_data,
        x='season',
        y='win_pct',
        color='town',
        title='Win Percentage Trend by Town',
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

    # Goals scored trend
    fig2 = px.area(
        trend_data,
        x='season',
        y='total_goals',
        color='town',
        title='Total Goals by Season'
    )
    st.plotly_chart(fig2, use_container_width=True)
```

---

### **PHASE 7: Testing & Documentation** (2 coding sessions)

#### Chunk 7.1: Unit Tests
**File:** `tests/test_scraper.py`
```python
import unittest
from src.scraper import BAYSScraper
from src.parser import BAYSParser

class TestScraper(unittest.TestCase):

    def test_url_builder(self):
        """Test URL construction"""
        from src.url_builder import URLBuilder
        url = URLBuilder.get_organization_url('FOX')
        self.assertEqual(url, 'https://bays.org/bays/organizations/view/FOX')

    def test_parser(self):
        """Test HTML parsing"""
        # Load sample HTML
        # Test parser output
        pass

    def test_rate_limiting(self):
        """Test crawl delay is enforced"""
        import time
        client = BAYSClient(crawl_delay=2)

        start = time.time()
        client.get('https://bays.org')
        client.get('https://bays.org')
        elapsed = time.time() - start

        self.assertGreaterEqual(elapsed, 2)
```

#### Chunk 7.2: Documentation
**Files:**
- `README.md` - Project overview, setup instructions
- `docs/USAGE.md` - How to run scraper, dashboard
- `docs/DATA_DICTIONARY.md` - Database schema documentation
- `docs/ANALYSIS_GUIDE.md` - How to interpret dashboard

---

## Execution Strategy

### Recommended Order
1. **Start with Phase 1** - Set up project and do reconnaissance
2. **Phase 3** - Set up CSV storage (simple, no database needed)
3. **Phase 1 Chunk 1.2** - Manual site exploration to understand data structure
4. **Data Collection** - Use Claude Code Agent to manually scrape each season/team
   - Start with 1 town, 1 season to test process
   - Then scale to all towns/seasons
5. **Gather population data** - Find population for all 11 towns
6. **Phase 5** - Data analysis and metrics calculation
7. **Phase 6** - Build Streamlit dashboard
8. **Phase 7** - Testing and documentation

### Updated Time Estimates
- **Phase 1 (Setup):** 1-2 hours
- **Phase 3 (CSV setup):** 1 hour
- **Manual scraping with Agent:** 10-20 hours (depends on site complexity)
  - Can run agents in parallel for different towns/seasons
- **Population data gathering:** 30 minutes
- **Phase 5 (Analysis code):** 2-3 hours
- **Phase 6 (Streamlit dashboard):** 4-6 hours
- **Phase 7 (Testing/docs):** 1-2 hours

**Total: ~20-35 hours** (more scraping, less coding)

---

## Key Technical Challenges & Solutions

### Challenge 1: No API - Manual Scraping Required
**Problem:** Site may not have accessible API, Cloudflare protection blocks automated scraping
**Solution:**
- **Use Claude Code Agent** to manually navigate and extract data
- Agent can handle JavaScript-heavy sites, Cloudflare, CAPTCHAs
- Process: For each town → each season → extract all team data
- Agent outputs structured data that gets written to CSV

### Challenge 2: Large Data Volume
**Problem:** 11 towns × 10 seasons × ~20-50 teams each = 2,200-5,500 team records
**Solutions:**
- **Run agents in parallel** - separate agent per town or season
- Checkpoint progress (track which towns/seasons completed)
- Incremental CSV appends (don't lose data if interrupted)
- Start small: test with 1 town, 1 season before scaling

### Challenge 3: Extracting Division Level (2, 3, 4)
**Problem:** Need to reliably extract which level each team is in
**Solution:**
- Division names typically include level: "U12 Boys Division 2"
- Parse division string to extract level number
- Validate: levels should only be 2, 3, or 4
- Manual review of first few extractions to ensure accuracy

### Challenge 4: Population Data Collection
**Problem:** Need current population for all 11 towns
**Solution:**
- Use Wikipedia or US Census data
- Record source and date for transparency
- Store in `config/towns_config.py` as constants
- Use 2020 Census or latest estimate

### Challenge 5: Ensuring Data Quality
**Problem:** Manual scraping prone to errors
**Solutions:**
- Validation rules: wins + losses + ties > 0, goals >= 0
- Duplicate detection: same team/season/town
- Completeness check: all towns have similar number of teams
- Spot check: manually verify random sample of 20-30 records

---

## Alternative BI Tool Comparison

| Tool | Cost | Pros | Cons | Recommendation |
|------|------|------|------|----------------|
| **Streamlit** | FREE | Python-native, you already use it, fast dev | Less polished than commercial tools | ✅ **BEST CHOICE** |
| **Apache Superset** | FREE | Sigma-like UI, powerful, beautiful | Heavier setup, overkill for this | Good if you want enterprise feel |
| **Metabase** | FREE | Easiest setup, beautiful UI | Limited customization | Great for non-technical users |
| **Plotly Dash** | FREE | Python-native, highly customizable | More code than Streamlit | Good alternative to Streamlit |
| **Sigma (Free)** | N/A | No free tier for individuals | Not applicable | ❌ Not available |

**Final Recommendation: Streamlit**
- You're already familiar with it (mmolb-stats)
- Python-native (easy to integrate with scraper)
- Fast iteration
- Can host for free on Streamlit Cloud
- Reuse patterns from your existing project

---

## Data Points to Track

### Organization Level
- Organization name
- Organization code
- Town
- **Population** (for normalization)

### Team Level (Row-Level CSV)
Each row = one team-season combination:
- `town_code` - Town code (FOX, HOP, etc.)
- `town_name` - Full town name
- `town_population` - Town population (for normalization)
- `season_year` - Year (2024, 2023, etc.)
- `season_period` - Fall or Spring
- `team_name` - Full team name
- `division_level` - **Level 1, 2, 3, or 4** (CRITICAL for analysis)
- `division_tier` - **A, B, C, etc.** (within-division tier - 2A is stronger than 2B)
- `division_full` - Full division string (e.g., "U12 Boys Division 2A")
- `age_group` - U8, U10, U12, etc.
- `gender` - Boys, Girls, or Coed
- `wins` - Total wins
- `losses` - Total losses
- `ties` - Total ties
- `goals_for` - Goals scored
- `goals_against` - Goals conceded
- `final_rank` - Rank in division (if available)
- `total_teams_in_division` - Number of teams in division
- `scrape_date` - Date data was collected

### Key Analysis Metrics (Calculated)
**PRIMARY FOCUS: Division Level Performance (1, 2, 3, 4)**
- Win percentage by town **controlling for division level**
- Goal differential by town **controlling for division level**
- Goals scored by town **controlling for division level**
- Number of teams each town fields **by division level**
- **Program strength indicator:** % of teams in higher divisions (1, 2A) vs lower (3, 4)
- Per-capita performance (normalized by population):
  - Teams per 1000 residents
  - Wins per team (normalized)
  - Goals per team (normalized)

**Foxboro vs. Peers Comparisons:**
- Win % vs. peer average (by level and by gender)
- Goal differential vs. peer average (by level and by gender)
- Total goals scored vs. peer average (by level and by gender)
- Team count vs. peer average (by level and by gender)
- **Division distribution:** Are Foxboro teams competing in higher or lower divisions than peers?
- **Lag indicators:** Creative metrics to show if Foxboro is falling behind
  - Trend lines: improving or declining win % over time
  - Participation rates: increasing or decreasing team counts
  - Division shifts: moving up or down in divisions over seasons
- Competitive depth: performance across all levels (not just top teams)

**Future Expansion (Not in Initial Scope):**
- Head-to-head game analysis between specific towns
- Individual game results and scoring patterns
- Home vs away performance
- Season-by-season progression tracking for individual teams

---

## Success Criteria

✅ **Data Collection:**
- Successfully scrape all 11 towns
- Collect data for **as many seasons as available** on site (not limited to 10)
- All age groups (U8-U19) and both genders
- Division levels 1, 2, 3, 4 (including tier letters: A, B, C, etc.)
- Skip any in-progress seasons
- < 5% data errors/missing values

✅ **Storage:**
- Clean CSV with all required columns
- No duplicate team-season records
- Data validation passing (>95% valid records)

✅ **Analysis:**
- Can rank towns by performance **by division level (1, 2, 3, 4) and gender**
- Can show Foxboro vs peer averages **with population normalization**
- Can show how many teams each town fields by level
- Can show **program strength:** % of teams in higher vs lower divisions
- Can show **lag indicators:** trends showing if Foxboro is improving/declining vs peers
- Can analyze by gender (Boys vs Girls performance)
- Can show trends over time (all available seasons)

✅ **Visualization:**
- Interactive Streamlit dashboard
- At least 4-5 different views/charts
- Responsive and fast (< 2 sec load time)

---

## Next Steps

1. **Review this plan** - Confirm approach makes sense
2. **Start with Phase 1, Chunk 1.1** - Set up project structure
3. **Manual site exploration** - Visit bays.org, inspect pages
4. **Test single page scrape** - Prove concept works
5. **Iterate and build** - Work through phases systematically

---

## Key Clarifications from User

1. ✅ **Data Collection Method:** Use Claude Code Agent for manual scraping (no automated API scraping)
2. ✅ **Storage:** Single row-level CSV file (no database)
3. ✅ **Primary Analysis:** Performance by division level (2, 3, 4)
4. ✅ **Normalization:** All stats normalized by town population
5. ✅ **Key Metrics:**
   - Win % by level
   - Goal differential by level
   - Number of teams fielded by level
   - Foxboro vs peer comparisons

## All Requirements Confirmed ✅

### Data Collection Scope:
1. ✅ **Seasons:** Collect as many seasons as available on site (not limited to 10)
2. ✅ **Age groups:** All age groups (U8, U10, U12, U14, U16, U19)
3. ✅ **Gender:** Both Boys and Girls (keep as separate variable for analysis)
4. ✅ **Historical range:** As far back as site has data
5. ✅ **Update frequency:** One-time analysis (with note for possible yearly incremental updates)
6. ✅ **In-progress seasons:** Skip any season currently in progress

### Division Level Details:
6. ✅ **Division naming:** Teams listed by number + letter (2A, 2B, 3A, 3B, etc.)
   - 2A = highest level of Division 2
   - 2B, 2C, etc. = lower tiers within Division 2
   - Same pattern for Divisions 3, 4
7. ✅ **Division 1:** Also exists for older kids - **COLLECT THIS TOO** (levels 1, 2, 3, 4)
8. ✅ **Missing data:** For levels 2-4, towns will always have data

### Population & Normalization:
8. ✅ **Population source:** Use estimates (latest available)
9. ✅ **Population type:** Total town population (not just youth)

### Analysis Priorities:
12. ✅ **Comparison focus:** Both individual comparisons AND peer average + creative lag indicators
13. ✅ **Success metrics (in priority order):**
    - High win percentage (compared to peers)
    - High goals scored (compared to peers)
    - Performance in each division level
    - **Fielding teams in higher vs lower divisions** (program strength indicator)
14. ✅ **Data granularity:** Season totals only (not individual games)
15. ✅ **Future expansion:** Add head-to-head game analysis as possible enhancement

---

**IMPORTANT REMINDERS:**
- ⚠️ Respect robots.txt 10-second crawl delay
- ⚠️ Do NOT use data for AI training (robots.txt restriction)
- ⚠️ Implement proper error handling and logging
- ⚠️ Test on small subset before full scrape
- ⚠️ Keep raw data backup before processing

Good luck with the project! Start with reconnaissance and testing, then build incrementally.
