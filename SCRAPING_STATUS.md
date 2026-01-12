# BAYS Soccer Scraping Status

**Last Updated:** 2026-01-10

## Fall 2024 - Complete ✅

Successfully scraped **255 teams from 10 towns**.

### Town Codes (Verified)

| Code | Town | Teams | Status | Notes |
|------|------|-------|--------|-------|
| ASH | Ashland Youth Soccer | 25 | ✅ Complete | Sample: "Barracuda" |
| BEL | Bellingham Soccer Association | 10 | ✅ Complete | Sample: "Hawks Gr8 Girls" |
| FOX | Foxborough Youth Soccer | 25 | ✅ Complete | Sample: "Warriors 7/8G-Blue" |
| HOL | Holliston Youth Soccer Association | 29 | ✅ Complete | Sample: "G7/8 Panthers Black" |
| HOP | Hopkinton Youth Soccer | 37 | ✅ Complete | Sample: "Fire" |
| MDY | Medway Youth Soccer Association | 16 | ✅ Complete | All teams named "Mustangs" |
| NOB | Northborough Youth Soccer Association | 22 | ✅ Complete | Sample: "Girls 7/8 Maroon" |
| SUD | Sudbury Youth Soccer | 23 | ✅ Complete | Sample: "United" |
| WAL | Walpole Youth Soccer Association | 41 | ✅ Complete | Sample: "Lightning" |
| WSB | Westborough Youth Soccer Association | 27 | ✅ Complete | Sample: "United - G7/8" |
| WSF | Westford Youth Soccer Association | 0 | ❌ No Data | No teams registered for Fall 2024 |

### Data Quality

- **Total Teams:** 255
- **Age Groups:** U8, U10, U12, U14, U16
- **Genders:** 141 Boys, 99 Girls, 15 Coed teams
- **Division Levels:** 1, 2, 3, 4
- **Complete Stats:** W/L/T, GF/GA, Points, Goal Differential, Coaches

### Key Findings

1. **Code Corrections Made:**
   - Westborough: WES → WSB ✓
   - Northborough: NOR → NOB ✓
   - Medway: MED → MDY ✓
   - Westford: WEF → WSF ✓

2. **Duplicate Detection Fixed:**
   - Updated to use `(town, season, team_name, age_group, gender, division_level, division_tier)` as unique key
   - Necessary because some towns (e.g., Medway) have multiple teams per age/gender in different divisions

3. **Westford (WSF):**
   - Organization page exists on BAYS.org
   - "Standings" section loads but contains no teams
   - Likely has no teams registered for Fall 2024 season

## Next Steps

1. ✅ **Verified all town codes are correct**
2. ⏳ **Scrape historical seasons** (Fall 2023, 2022, 2021, etc.) for all 10 working towns
3. ⏳ **Add population data** for normalization
4. ⏳ **Build analysis dashboard**

## Technical Notes

### CSV Schema (23 columns)
```
town_code, town_name, town_population, season_year, season_period,
team_name, division_level, division_tier, division_full, age_group,
gender, wins, losses, ties, goals_for, goals_against, goal_differential,
points, final_rank, total_teams_in_division, head_coach, assistant_coach,
scrape_date
```

### Scraper Features
- Selenium + BeautifulSoup for Cloudflare bypass
- Automatic "Standings" link clicking
- 10-second crawl delay (robots.txt compliance)
- Division parsing (handles "2/A", "3/B1", etc.)
- Age group mapping (Grade 8 → U8, Grade 5 → U12, etc.)
- Coach information extraction
- HTML backup for debugging

### Files
- **Data:** `data/bays_teams.csv` (255 rows)
- **Config:** `config/towns_config.py`, `config/csv_schema.py`
- **Scrapers:** `src/full_scraper.py`, `src/csv_manager.py`
- **HTML Backups:** `data/raw/{TOWN_CODE}_fall2024.html`

## Historical Seasons Available

Based on site_structure.md: **22 seasons available** (Fall 2015 - Spring 2025)

Expected complete data: **Fall 2018 - Fall 2024** (7 seasons)

---

**Status:** Ready to proceed with historical season scraping
