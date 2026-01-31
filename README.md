# Foxboro Youth Soccer Analytics Dashboard

Interactive Streamlit dashboard comparing Foxborough Youth Soccer against 7 peer towns over 10 seasons.

## Data: COMPLETE

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

## Setup

```bash
pip install -r requirements.txt
streamlit run streamlit_dashboard.py
```

## Repo Contents

```
bays-soccer-scraper/
├── streamlit_dashboard.py   # Dashboard app
├── data/
│   ├── bays_teams.csv       # Primary database (1,846 teams)
│   └── school_enrollment.csv
├── fox-logo_3.png           # Dashboard logo
├── requirements.txt         # Python dependencies
└── README.md
```

## Analysis Highlights

- **Foxborough has the lowest participation rate** among peers (10.37 teams/1,000 residents)
- **Hopkinton leads** at 18.71 teams/1,000 (+80% vs Foxborough)
- **Foxborough has the worst Spring retention** — 30.7% drop vs Mansfield's -1.3%

## Data Source

Collected manually from bays.org. Personal use only — respect robots.txt.
