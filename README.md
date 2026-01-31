# BAYS Soccer Scraper & Analysis

Compare Foxborough Youth Soccer performance against 7 peer towns over 10 seasons.

## Project Overview

This project collects and analyzes historical soccer data from bays.org to compare:
- Participation rates (teams per 1,000 residents)
- Spring participation retention
- Win percentages by division level (1, 2, 3, 4)
- Goal differential and goals scored
- Program strength (% of teams in higher vs lower divisions)
- Lag indicators (trends showing improvement/decline vs peers)

## Data Status: COMPLETE

**1,846 teams** across **8 towns × 10 seasons** (Spring 2021 – Fall 2025)

| Town | Code | Population | Teams |
|------|------|-----------|-------|
| Foxborough | FOX | 18,618 | 193 |
| Ashland | ASH | 18,832 | 220 |
| Bellingham | BEL | 16,945 | 101 |
| Holliston | HOL | 15,494 | 209 |
| Hopkinton | HOP | 18,758 | 351 |
| Mansfield | MAN | 25,067 | 302 |
| Medway | MDY | 13,115 | 158 |
| Walpole | WAL | 24,070 | 312 |

## Quick Start

### 1. Setup Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Project Structure

```
bays-soccer-scraper/
├── config/                # Configuration
│   ├── towns_config.py    # Town codes, names, populations
│   └── csv_schema.py      # CSV column definitions
├── src/                   # Core source code
│   └── csv_manager.py     # CSV operations (append, load, dedup)
├── data/
│   ├── bays_teams.csv     # Primary database (1,846 teams)
│   └── school_enrollment.csv
├── analysis/              # Analysis scripts
│   ├── analyze_9_metrics.py
│   ├── compare_to_fox.py
│   ├── fox_coach_rankings.py
│   └── ...
├── docs/                  # Reference documentation
│   ├── CORE_METRICS.md
│   ├── participation_analysis_notes.md
│   └── site_structure.md
├── archive/               # Historical data & retired code
│   ├── pastes/            # Raw paste data (all 80 seasons)
│   ├── raw_html/          # Scraped HTML backups
│   ├── import_scripts/    # One-off import scripts
│   ├── scrapers/          # Selenium/BS4 scrapers (blocked by CF)
│   ├── backups/           # CSV backups
│   └── docs/              # Old planning & status docs
├── streamlit_dashboard.py # Interactive dashboard
├── universal_import.py    # Standard data import tool
├── check_complete.py      # Data completeness checker
├── KEY_METRICS.md         # 7 key analysis metrics
├── CURRENT_STATUS.md      # Project status & data summary
└── requirements.txt       # Python dependencies
```

## Data Collection

Data was collected manually from bays.org using a paste + import workflow (automated scraping blocked by Cloudflare). All raw data is preserved in `archive/pastes/`.

See [CURRENT_STATUS.md](CURRENT_STATUS.md) for detailed per-town breakdowns and metrics.

## Key Findings (Preliminary)

- **Foxborough has the lowest participation rate** among similar-population peers (10.37 teams/1,000 residents)
- **Hopkinton leads** at 18.71 teams/1,000 (+80% vs Foxborough)
- **Foxborough has the worst Spring retention** — 30.7% drop vs Mansfield's -1.3% (Spring actually higher)

## Next Steps

1. Run full analysis across all 7 key metrics
2. Build Streamlit dashboard for interactive comparison
3. Generate final report for Foxborough Youth Soccer board

## License

Personal use only. Data from bays.org — respect robots.txt.
