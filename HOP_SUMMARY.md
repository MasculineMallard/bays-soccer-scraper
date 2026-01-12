# Hopkinton (HOP) - Data Collection Complete

**Collection Date:** 2026-01-10
**Status:** ✅ COMPLETE - 10 seasons imported

---

## Overview

**Total Teams:** 351 teams across 10 seasons
**Time Period:** Fall 2025 → Spring 2021 (5 years)
**School Enrollment:** 4,187 students (LARGEST district in study)

---

## Season-by-Season Breakdown

| Season | Teams | Notes |
|--------|-------|-------|
| Fall 2025 | 39 | Most recent |
| Spring 2025 | 34 | -12.8% drop |
| Fall 2024 | 41 | Peak season |
| Spring 2024 | 31 | -24.4% drop |
| Fall 2023 | 46 | **Highest** |
| Spring 2023 | 32 | -30.4% drop |
| Fall 2022 | 39 | |
| Spring 2022 | 31 | -20.5% drop |
| Fall 2021 | 36 | |
| Spring 2021 | 22 | **Lowest**, -38.9% drop |

**Average:** 35.1 teams per season
**Fall Average:** 40.2 teams
**Spring Average:** 30.0 teams
**Spring Participation Drop:** 25.4% average

---

## Gender Distribution

- **Boys:** 185 teams (52.7%)
- **Girls:** 166 teams (47.3%)

**Gender Balance:** Nearly equal, slight male skew (+5.4%)

---

## Division Distribution

| Division | Teams | Percentage |
|----------|-------|------------|
| Division 1 | 4 | 1.1% |
| Division 2 | 55 | 15.7% |
| Division 3 | 157 | 44.7% |
| Division 4 | 135 | 38.5% |

**Primary Placement:** Division 3 (44.7%) - Competitive mid-tier

---

## Competitive Performance

**Overall Record:** 1,329 W - 1,368 L - 395 T
**Win Rate:** 43.0%
**Goal Differential:** -88 total (-0.3 per team)

**Status:** Slightly negative performance, similar to FOX

---

## Participation Metrics

**Teams per 100 School-Age Children:** 0.84

**Comparison to Other Towns:**
- HOP: 0.84 (BASELINE for large districts)
- FOX: 0.78 (-7.1% vs HOP)
- ASH: 0.76 (-9.5% vs HOP)
- BEL: 0.51 (-39.3% vs HOP)

**Insight:** HOP has the HIGHEST participation rate of all 4 towns collected so far.

---

## Key Findings

### 1. Largest Program Collected
- 351 teams is the most of any town so far
- 46% more teams than FOX (193), 59% more than ASH (220)
- Largest school enrollment (4,187 students)

### 2. Strong Participation Rate
- 0.84 teams per 100 students (highest so far)
- 35.1 teams per season average
- Consistent Fall participation (40+ teams)

### 3. Spring Retention Challenge
- Average 25.4% drop from Fall to Spring
- Better than FOX (44.3%) but worse than BEL (2.0%)
- Similar to ASH (15.7%)

### 4. Competitive Performance
- 43.0% win rate (slightly below .500)
- -88 total goal differential (losing by 0.3 goals per team)
- Similar to FOX's competitive challenges

### 5. Division Placement
- Heavily concentrated in Division 3 (44.7%)
- Very few Division 1 teams (1.1%)
- Balanced between Division 3 and 4

---

## Files Created

### Import Scripts
- `import_hop_batch.py` - Fall 2025, Spring 2025, Fall 2024
- `import_hop_remaining.py` - Spring 2024 through Spring 2022
- `import_hop_final2.py` - Fall 2021, Spring 2021

### Data Files
- `data/pastes/HOP_Fall2025_raw.txt` - Original Fall 2025 paste
- `data/pastes/paste_dump.txt` - All 10 seasons backed up
- Individual paste files for each season (10 files)

### Database
- All 351 teams added to `data/bays_teams.csv`
- No duplicates, clean import

---

## Comparison to FOX (Baseline)

| Metric | HOP | FOX | Difference |
|--------|-----|-----|------------|
| School Enrollment | 4,187 | 2,485 | +68.5% |
| Teams per 100 Students | 0.84 | 0.78 | +7.7% |
| Spring Drop | 25.4% | 44.3% | -18.9% BETTER |
| Win Rate | 43.0% | TBD | TBD |
| Goal Differential | -0.3/team | -2.1/team | +1.8 BETTER |
| Gender Balance | 52.7% Boys | 50.8% Boys | +1.9% more boys |

**Key Insight:** Despite being 68% larger, HOP only has 7.7% higher participation rate when normalized. However, HOP has much better Spring retention and slightly better competitive performance than FOX.

---

## Next Steps

1. **Collect remaining 4 towns:** HOL, SUD, WAL, WSB
2. **Run full 5-town analysis** when next town is complete
3. **Compare large districts:** HOP (4,187) vs WAL (3,565) vs WSB (3,887)

---

**Data Quality:** ✅ Excellent
**Completeness:** ✅ 10/10 seasons
**Ready for Analysis:** ✅ Yes
