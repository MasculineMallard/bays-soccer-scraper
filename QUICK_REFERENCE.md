# Quick Reference Guide

## Current Status
- **6 towns complete:** FOX (193 teams), ASH (220 teams), BEL (101 teams), HOP (351 teams), HOL (209 teams), MAN (302 teams)
- **1,376 total teams** across 60 seasons
- **2 towns remaining:** WAL, WSB

---

## When You Return to Collect More Towns

### Step 1: Paste Data
Just paste the data - it auto-saves to dump file and imports to CSV automatically.

### Step 2: Verify Completeness
```bash
python check_complete.py
```
Shows all seasons for all towns with checkboxes.

### Step 3: Check for Missing Seasons
```bash
python auto_save_pastes.py
# Choose option 2
```
Compares dump file to CSV, finds any gaps.

### Step 4: Run Analysis
```bash
python compare_to_fox.py
```
Shows all metrics normalized to FOX baseline.

---

## Key Files

### Data
- `data/bays_teams.csv` - Main database (1,074 teams)
- `data/school_enrollment.csv` - Enrollment for all 8 towns
- `data/pastes/paste_dump.txt` - Universal backup

### Scripts
- `universal_import.py` - Import any pasted data
- `auto_save_pastes.py` - Manage dump file, check gaps
- `check_complete.py` - Verify all seasons present
- `compare_to_fox.py` - FOX-normalized analysis

### Docs
- `SESSION_SUMMARY.md` - Complete session summary
- `CURRENT_STATUS.md` - Current project status
- `KEY_METRICS.md` - All 7 metrics definitions
- `docs/SCHOOL_ENROLLMENT_DATA.md` - School enrollment reference

---

## Critical Findings So Far

**FOX is underperforming:**
- Only town with NEGATIVE goal differential (-411 total)
- Loses 44% of teams in Spring (worst retention)
- Lower win rates across ALL divisions
- Similar participation rate to ASH when normalized

**ASH is strong:**
- +613 goal differential (winning consistently)
- Only 16% Spring drop (good retention)
- Higher win rates, more goals per game

**BEL is competitive:**
- +115 goal differential (winning)
- Only 2% Spring drop (excellent retention!)
- Strong win rates despite being smallest program

---

## School Enrollment Reference

| Town | Students | Size Category |
|------|----------|---------------|
| HOP | 4,187 | Large (largest) ✅ |
| WSB | 3,887 | Large |
| WAL | 3,565 | Large |
| MAN | 3,243 | Medium ✅ |
| ASH | 2,909 | Medium ✅ |
| HOL | 2,810 | Medium ✅ |
| FOX | 2,485 | Medium ✅ |
| BEL | 1,990 | Small ✅ |

✅ = Data collected

---

## Next 2 Towns to Collect

**Need 10 seasons each (Fall 2025 → Spring 2021):**

1. **WAL** (Walpole) - 3,565 students
2. **WSB** (Westborough) - 3,887 students

**Total needed:** 20 more seasons (10 × 2 towns)

---

## Safety Features

**Auto-save to dump file:** ✅ Every paste backed up with timestamp
**Gap detection:** ✅ Can find missing seasons automatically
**Duplicate prevention:** ✅ CSV deduplicates on import
**Recovery:** ✅ Can import from dump if season missed

---

## Quick Commands

```bash
# Check completeness
python check_complete.py

# Check for gaps
python auto_save_pastes.py
# Choose option 2

# Import missing seasons from dump
python auto_save_pastes.py
# Choose option 3

# Run full analysis
python compare_to_fox.py

# Calculate metrics 3-7
python calculate_metrics.py
```

---

**Last Updated:** 2026-01-10
**Ready for:** Remaining 3 towns (MAN, WAL, WSB)
