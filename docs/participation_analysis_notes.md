# Participation Rate Analysis - Key Metrics

## Overview
This document tracks key participation metrics to compare Foxborough against peer towns with similar populations.

---

## Metric 1: Teams Per 1,000 Residents

### Definition
Total teams per season divided by town population, expressed as teams per 1,000 residents.

### Baseline: Foxborough
- **Population**: 18,618
- **Average teams/season**: 19.4 (across 8 seasons: Fall 2021 - Spring 2025, excluding Fall 2023)
- **Participation rate**: 1.04 teams per 1,000 residents

### Comparison Format
For each peer town, calculate:
- `(Town teams/1000) / (FOX teams/1000) - 1 = +/- % compared to Foxborough`

### Current Data: Ashland vs Foxborough

| Town | Population | Avg Teams/Season | Teams/1,000 | vs FOX |
|------|-----------|------------------|-------------|--------|
| FOX  | 18,618    | 19.4             | 1.04        | baseline |
| ASH  | 18,832    | 22.0             | 1.17        | **+12.5%** |

**Finding**: Ashland has 12.5% higher participation rate than Foxborough despite nearly identical populations.

---

## Metric 2: Spring Participation Drop (Consistency)

### Definition
Measures the average percentage of teams lost from Fall to Spring season. Lower percentage indicates better Spring retention.

**Formula**: `((Fall teams - Spring teams) / Spring teams) * 100`

### Interpretation
- **Lower %**: Better Spring retention (more consistent year-round)
- **Higher %**: Poor Spring retention (significant seasonal drop-off)

### Current Data

| Town | Avg Fall Teams | Avg Spring Teams | Spring Drop % |
|------|---------------|------------------|---------------|
| ASH  | 23.2          | 20.0             | **16.1%**     |
| FOX  | 22.5          | 16.0             | **44.2%**     |

#### Year-by-Year Data

| Year | ASH Fall | ASH Spring | ASH Drop | FOX Fall | FOX Spring | FOX Drop |
|------|----------|------------|----------|----------|------------|----------|
| 2021 | 20       | 18         | 11.1%    | 23       | 14         | 64.3%    |
| 2022 | 23       | 21         | 9.5%     | 22       | 17         | 29.4%    |
| 2023 | 25       | 20         | 25.0%    | N/A*     | 14         | N/A      |
| 2025 | 25       | 21         | 19.0%    | 25       | 18         | 38.9%    |

*Fall 2023 Foxborough data not collected

### Key Finding

**Foxborough loses 44% of teams in Spring on average**, compared to Ashland's 16% drop. This represents significantly worse Spring retention and less consistent year-round participation.

---

## Future Analysis Checklist

When peer town data is collected, calculate:

- [ ] **BEL** (Bellingham): Teams/1,000 vs FOX (+/- %) | Spring Drop %
- [ ] **HOL** (Holliston): Teams/1,000 vs FOX (+/- %) | Spring Drop %
- [ ] **HOP** (Hopkinton): Teams/1,000 vs FOX (+/- %) | Spring Drop %
- [ ] **SUD** (Sudbury): Teams/1,000 vs FOX (+/- %) | Spring Drop %
- [ ] **WAL** (Walpole): Teams/1,000 vs FOX (+/- %) | Spring Drop %
- [ ] **WSB** (Westborough): Teams/1,000 vs FOX (+/- %) | Spring Drop %

---

## Analysis Questions to Answer

1. **Participation Rate**: Which peer towns have higher/lower participation than Foxborough?
2. **Seasonal Stability**: Which towns maintain consistent participation Fall-to-Spring?
3. **Population Efficiency**: Do smaller/larger towns have better participation rates?
4. **Growth Trends**: Are participation rates increasing or decreasing over time?
5. **Spring Retention**: Which towns retain the most teams from Fall to Spring?

---

## Data Quality Notes

- Foxborough Fall 2023 data missing (need to collect or mark as N/A)
- All other seasons complete for both FOX and ASH (Fall 2021 - Spring 2025)
- Population data accurate as of 2024

---

**Last Updated**: 2026-01-10
**Data Source**: Manual BAYS website data collection
**Analysis Tool**: `bays-soccer-scraper/batch_import_*.py`
