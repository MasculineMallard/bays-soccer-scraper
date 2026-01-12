# BAYS Soccer Scraper - Current Status

**Last Updated:** 2026-01-10
**Data Collection Method:** Manual import with auto-save to dump file
**Total Teams:** 514 teams across 30 seasons (3 complete towns)

---

## Data Collection Status

### ✅ COMPLETE - Foxborough (10 seasons)
- Fall 2025: 25 teams
- Spring 2025: 18 teams
- Fall 2024: 22 teams
- Spring 2024: 16 teams
- Fall 2023: 22 teams
- Spring 2023: 14 teams
- Fall 2022: 22 teams
- Spring 2022: 17 teams
- Fall 2021: 23 teams
- Spring 2021: 14 teams

**Total:** 193 teams across 10 complete seasons

### ✅ COMPLETE - Ashland (10 seasons)
- Fall 2025: 25 teams
- Spring 2025: 21 teams
- Fall 2024: 25 teams
- Spring 2024: 22 teams
- Fall 2023: 25 teams
- Spring 2023: 20 teams
- Fall 2022: 23 teams
- Spring 2022: 21 teams
- Fall 2021: 20 teams
- Spring 2021: 18 teams

**Total:** 220 teams across 10 complete seasons

### ✅ COMPLETE - Bellingham (10 seasons)
- Fall 2025: 10 teams
- Spring 2025: 11 teams
- Fall 2024: 17 teams
- Spring 2024: 11 teams
- Fall 2023: 8 teams
- Spring 2023: 10 teams
- Fall 2022: 8 teams
- Spring 2022: 10 teams
- Fall 2021: 8 teams
- Spring 2021: 8 teams

**Total:** 101 teams across 10 complete seasons

### ❌ TODO - Remaining 5 Towns
- [ ] HOL (Holliston)
- [ ] HOP (Hopkinton)
- [ ] SUD (Sudbury)
- [ ] WAL (Walpole)
- [ ] WSB (Westborough)

---

## Key Metrics Defined

### Metric 1: Teams Per 1,000 Residents

**Purpose:** Compare participation rates across towns with different populations

**Formula:** `(Total teams / Town population) * 1000`

**Current Results:**
- **Foxborough (FOX)**: 1.04 teams/1,000 (baseline)
- **Ashland (ASH)**: 1.17 teams/1,000 (+12.5% vs FOX)

**For Remaining Towns:** Calculate `+/- %` compared to Foxborough baseline

---

### Metric 2: Spring Participation Drop (Consistency)

**Purpose:** Measure year-round participation consistency

**Formula:** `((Fall teams - Spring teams) / Spring teams) * 100`

**Interpretation:**
- Lower % = Better Spring retention
- Higher % = Larger seasonal drop-off

**Current Results:**
| Town | Avg Fall | Avg Spring | Spring Drop % |
|------|----------|------------|---------------|
| ASH  | 23.2     | 20.0       | **16.1%**     |
| FOX  | 22.5     | 16.0       | **44.2%**     |

**Key Finding:** Foxborough loses 44% of teams in Spring vs Ashland's 16% drop

**For Remaining Towns:** Calculate Spring Drop % to compare consistency

---

## Data Files

### Primary Database
- `data/bays_teams.csv` - **514 teams** (FOX + ASH + BEL complete historical data)

### Paste Files (Raw Data Storage)
All pasted data saved to TWO locations:

1. **Dump File (Universal Backup):**
   - `data/pastes/paste_dump.txt` - Chronological backup of ALL pastes with timestamps
   - Auto-saved on every paste
   - Used to recover missing seasons

2. **Individual Paste Files:**
   - `data/pastes/{TOWN}_{SEASON}{YEAR}_raw.txt` - Clean season-specific files
   - FOX: 10 seasons (Fall 2025 - Spring 2021)
   - ASH: 10 seasons (Fall 2025 - Spring 2021)
   - BEL: 10 seasons (Fall 2025 - Spring 2021)

### Import Scripts
- `universal_import.py` - **HARDCODED STANDARD** for all imports (Ashland format)
  - Auto-saves to dump file
  - Auto-saves to individual paste file
  - Imports to CSV database
- `auto_save_pastes.py` - Dump file manager
  - Check for missing seasons
  - Import from dump file
  - List all pastes
- `check_complete.py` - Verify all towns have 10 seasons

### Analysis Documentation
- `docs/participation_analysis_notes.md` - Metric definitions and future analysis checklist
- `docs/PASTE_WORKFLOW.md` - Complete paste workflow documentation
- `KEY_METRICS.md` - All 7 key metrics with current data

---

## Data Quality

### Duplicates Cleaned
- Removed 8 duplicates (MDY and SUD Fall 2024)
- Removed 46 FOX Fall 2024 duplicates
- Re-imported FOX Fall 2024 cleanly: 22 teams
- **Final count:** 568 teams (clean)

### Data Standards (Ashland Format - Universal)
**Column Order (MANDATORY):**
1. Team name
2. Team number
3. GADS (Gender Age Division/Section)
4. Wins
5. Losses
6. Ties
7. Forfeits
8. Points
9. Goals For
10. Goals Against
11. Goal Differential (+/-)
12. Head Coach
13. Assistant Coach (optional)

**Grade Mapping:**
- Grades 7 and 8 → "Grade 7/8" (always mixed)
- Grades 1 and 2, 912 → "Grade 1/2"
- Other grades → "Grade {number}"

**Division Parsing:**
- "3/E" splits to:
  - `division_level` = 3
  - `division_tier` = E
  - `division_full` = "Division 3E"

---

## Important Rules

### Data Collection Rules
1. ✅ **Auto-save to dump file** - Every paste automatically saved to `paste_dump.txt`
2. ✅ **Always save to individual paste files** - Specific season files in `data/pastes/`
3. ✅ **Use Ashland format** for all imports (universal standard)
4. ✅ **Capture assistant coaches** (don't forget this field)
5. ✅ **Separate division level and tier** (not combined)
6. ✅ **Use actual school grades** (not age groups)
7. ✅ **Check dump for missing seasons** - Run `auto_save_pastes.py` regularly

### Automation Status
- ❌ **Web scraping BLOCKED** - Cloudflare protection too aggressive
- ✅ **Manual collection WORKING** - Using paste + import method
- ✅ **Universal import STANDARDIZED** - All towns use same format

---

## Next Steps

### Immediate (User Decision Required)
1. Decide on approach for collecting 6 remaining towns:
   - Manual collection (paste method like FOX/ASH)
   - Contact BAYS for data export
   - Other approach

### When Data Collection Complete
1. Run participation analysis for all 8 towns
2. Calculate Teams/1,000 vs FOX (+/- %) for each town
3. Calculate Spring Drop % for each town
4. Build comparative visualizations
5. Identify trends and insights

---

## Town Population Data

| Code | Town          | Population |
|------|---------------|------------|
| ASH  | Ashland       | 18,832     |
| BEL  | Bellingham    | TBD        |
| FOX  | Foxborough    | 18,618     |
| HOL  | Holliston     | TBD        |
| HOP  | Hopkinton     | TBD        |
| SUD  | Sudbury       | TBD        |
| WAL  | Walpole       | TBD        |
| WSB  | Westborough   | TBD        |

**Note:** Need to collect population data for 6 remaining towns

---

## Historical Context

### Previous Issues (Resolved)
1. ✅ Automated scraping blocked by Cloudflare
2. ✅ Wrong column parsing in initial imports
3. ✅ Missing assistant coach data
4. ✅ Division parsing combining level/tier incorrectly
5. ✅ Not saving data to files before processing
6. ✅ Wrong grade mapping (was using age groups)
7. ✅ Duplicate data in CSV

### Current Approach
**Manual collection with auto-save safety net:**
1. User pastes data from BAYS website
2. System auto-saves to `paste_dump.txt` with timestamp (BACKUP)
3. System saves to specific paste file (e.g., `ASH_Spring2024_raw.txt`)
4. `universal_import.py` parses using Ashland format
5. Data appended to `data/bays_teams.csv`
6. If season missed, recover from dump file using `auto_save_pastes.py`

**Benefits:**
- Never lose pasted data
- Can detect missing seasons automatically
- Chronological audit trail of all pastes
- Works reliably, no Cloudflare issues

---

**Status:** 3 towns complete (FOX, ASH, BEL). Ready to collect remaining 5 towns (HOL, HOP, SUD, WAL, WSB).
