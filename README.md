# BAYS Soccer Scraper & Analysis

Compare Foxborough Youth Soccer performance against 10 peer towns over multiple seasons.

## Project Overview

This project scrapes historical soccer data from bays.org to analyze:
- Win percentages by division level (1, 2, 3, 4)
- Goal differential and goals scored
- Program strength (% of teams in higher vs lower divisions)
- Lag indicators (trends showing improvement/decline vs peers)
- Population-normalized metrics for fair comparison

**Target Towns:** 11 total (Foxborough + 10 peer towns)
**Data Scope:** All available seasons, all age groups (U8-U19), both genders

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Project Structure

```
bays-soccer-scraper/
├── config/              # Configuration files
│   ├── towns_config.py  # Town codes and population data
│   └── csv_schema.py    # CSV schema definition
├── src/                 # Source code
├── data/                # Data storage
│   ├── raw/            # Raw scraped data
│   ├── processed/      # Processed/aggregated data
│   └── bays_teams.csv  # Main data file
├── logs/                # Scraping logs
├── docs/                # Documentation
└── requirements.txt     # Python dependencies
```

## Data Collection

See [REQUIREMENTS_SUMMARY.md](REQUIREMENTS_SUMMARY.md) for detailed requirements.

Data collection will be done using Claude Code Agents due to Cloudflare protection on bays.org.

## Analysis

Population-normalized metrics include:
- Teams per 1000 residents
- Win % controlling for division level
- Program strength indicator
- Trend analysis and lag indicators

## Dashboard

Interactive Streamlit dashboard with:
- Division level rankings
- Foxboro vs peers comparison
- Program strength visualization
- Lag indicators and alerts
- Gender-specific breakdowns
- Historical trends

## License

Personal use only. Data from bays.org - respect robots.txt.
