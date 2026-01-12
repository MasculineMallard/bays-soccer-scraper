# School Enrollment Data for BAYS Towns

**Source:** Massachusetts Department of Education
**School Year:** 2024-25 (unless noted)
**Last Updated:** 2026-01-10

## Overview

This document contains K-12 public school enrollment data for all 8 BAYS soccer comparison towns. This data is used for **Metric 1: Teams Per 100 School-Age Children** to accurately measure youth soccer participation rates normalized to the school-age population.

---

## Complete Town Data

| Code | Town Name | Enrollment | Schools | Source |
|------|-----------|------------|---------|--------|
| **FOX** | Foxborough | 2,485 | 5 | [U.S. News](https://www.usnews.com/education/k12/massachusetts/districts/foxborough-108068) |
| **ASH** | Ashland | 2,909 | 5 | [MA DOE](https://profiles.doe.mass.edu/profiles/student.aspx?orgtypecode=5&fycode=2025&orgcode=00140000) |
| **BEL** | Bellingham | 1,990 | 6 | [MA DOE](https://profiles.doe.mass.edu/profiles/student.aspx?orgtypecode=5&fycode=2024&orgcode=00250000) |
| **HOL** | Holliston | 2,810 | 4 | [U.S. News](https://www.usnews.com/education/k12/massachusetts/districts/holliston-102638) |
| **HOP** | Hopkinton | 4,187 | 6 | [MA DOE](https://profiles.doe.mass.edu/profiles/student.aspx?orgtypecode=5&fycode=2024&orgcode=01390000) |
| **SUD** | Sudbury | 2,529 | 5 | [MA DOE](https://profiles.doe.mass.edu/profiles/student.aspx?orgtypecode=5&fycode=2025&orgcode=02880000) |
| **WAL** | Walpole | 3,565 | 8 | [MA DOE](https://profiles.doe.mass.edu/profiles/student.aspx?orgtypecode=5&fycode=2025&orgcode=03070000) |
| **WSB** | Westborough | 3,887 | 6 | [MA DOE](https://profiles.doe.mass.edu/profiles/student.aspx?orgtypecode=5&fycode=2025&orgcode=03210000) |

**Total:** 24,362 students across 8 towns

---

## District Size Categories

### Large Districts (3,500+ students)
- **HOP** - Hopkinton: 4,187 students (largest)
- **WSB** - Westborough: 3,887 students
- **WAL** - Walpole: 3,565 students

### Medium Districts (2,500-3,500 students)
- **ASH** - Ashland: 2,909 students
- **HOL** - Holliston: 2,810 students
- **SUD** - Sudbury: 2,529 students
- **FOX** - Foxborough: 2,485 students

### Small Districts (<2,500 students)
- **BEL** - Bellingham: 1,990 students (smallest)

---

## Key Statistics

**Average Enrollment:** 3,045 students per town
**Median Enrollment:** 2,820 students
**Range:** 1,990 - 4,187 students
**Standard Deviation:** 726 students

---

## Why School Enrollment Matters for Soccer Analysis

### Problem with Total Population Metric

Using total population (all ages) to measure youth soccer participation is misleading because:
- Towns vary in age demographics (retirees vs young families)
- Soccer is exclusively for school-age children (K-12)
- Total population includes adults who cannot participate

**Example:**
- FOX total population: 18,618 → 1.04 teams/1,000 residents
- ASH total population: 18,832 → 1.17 teams/1,000 residents (+12.7%)

This suggested ASH has much higher participation, but...

### Corrected with School Enrollment

When normalized to school-age children:
- FOX: 0.78 teams/100 students (BASELINE)
- ASH: 0.76 teams/100 students (-2.6% vs FOX)

**Insight:** FOX and ASH have nearly identical participation rates! The difference in total population metric was due to Ashland having more families with school-age children relative to total population.

---

## Important Notes

### Sudbury Special Case
**SUD enrollment (2,529) does NOT include Lincoln-Sudbury Regional High School**, which is a separate regional district serving both Sudbury and Lincoln students.

For accurate comparison:
- If Sudbury soccer teams include LSRHS students, we should add LSRHS enrollment
- If Sudbury soccer is only for Sudbury Public Schools (K-8), current figure is correct
- **Need to verify:** Do SUD BAYS teams include high school students?

### Data Year Variations
Most data is from 2024-25 school year, except:
- BEL: 2023-24 data (most recent available)
- All data within 1 year, acceptable for comparison

---

## Data Files

### JSON Format
`data/school_enrollment.json` - Full metadata with sources and notes

### CSV Format
`data/school_enrollment.csv` - Simple table for analysis scripts

### Usage in Analysis
Both `compare_to_fox.py` and future analysis scripts load from these files to calculate:
- Teams per 100 school-age children
- Participation rate comparisons
- District size correlations

---

## Source Documentation

All data sourced from:
1. **Massachusetts Department of Education** - Official enrollment data
2. **U.S. News Education** - Verified district enrollment figures

See individual source URLs in the data files for specific references.

---

**Next Steps:**
1. Verify Sudbury LSRHS participation question
2. Update analysis scripts to use school enrollment data
3. Recalculate all participation metrics with corrected baseline
