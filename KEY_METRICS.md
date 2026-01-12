# Key Metrics - BAYS Soccer Analysis

**Purpose:** Track important metrics discovered during data exploration
**Last Updated:** 2026-01-10

---

## Core Comparison Metrics

### 1. Teams Per 1,000 Residents
**What it measures:** Overall program participation normalized by population
**Formula:** `(Total teams / Town population) * 1000`
**Why it matters:** Fair comparison between towns of different sizes

**Current Data:**
| Town | Population | Avg Teams/Season | Teams/1,000 | vs FOX |
|------|-----------|------------------|-------------|--------|
| FOX  | 18,618    | 19.4             | 1.04        | baseline |
| ASH  | 18,832    | 22.0             | 1.17        | **+12.5%** ✅ |
| BEL  | TBD       | TBD              | TBD         | TBD    |
| HOL  | TBD       | TBD              | TBD         | TBD    |
| HOP  | TBD       | TBD              | TBD         | TBD    |
| SUD  | TBD       | TBD              | TBD         | TBD    |
| WAL  | TBD       | TBD              | TBD         | TBD    |
| WSB  | TBD       | TBD              | TBD         | TBD    |

**Interpretation:**
- ✅ Positive % = Higher participation than Foxborough
- ❌ Negative % = Lower participation than Foxborough

---

### 2. Spring Participation Drop (Consistency)
**What it measures:** Year-round program stability
**Formula:** `((Fall teams - Spring teams) / Spring teams) * 100`
**Why it matters:** Shows which towns retain players through both seasons

**Current Data:**
| Town | Avg Fall | Avg Spring | Spring Drop % | Rating |
|------|----------|------------|---------------|--------|
| ASH  | 23.2     | 20.0       | **16.1%**     | ✅ Excellent |
| FOX  | 22.5     | 16.0       | **44.2%**     | ⚠️ Poor |
| BEL  | TBD      | TBD        | TBD           | TBD    |
| HOL  | TBD      | TBD        | TBD           | TBD    |
| HOP  | TBD      | TBD        | TBD           | TBD    |
| SUD  | TBD      | TBD        | TBD           | TBD    |
| WAL  | TBD      | TBD        | TBD           | TBD    |
| WSB  | TBD      | TBD        | TBD           | TBD    |

**Rating Scale:**
- ✅ Excellent: < 20% drop
- 🟡 Good: 20-30% drop
- 🟠 Fair: 30-40% drop
- ⚠️ Poor: > 40% drop

**Interpretation:**
- Lower % = Better Spring retention
- Higher % = Significant seasonal volatility

---

## Additional Metrics

### 3. Win Rate by Division Level
**What it measures:** Competitive performance controlling for division strength
**Formula:** `(Wins + 0.5 × Ties) / Total Games × 100`
**Why it matters:** Shows if FOX performs differently at various competition levels

**Current Data:**
| Division | ASH Win % | FOX Win % | Difference |
|----------|-----------|-----------|------------|
| Division 1 | 40.0% (4 teams) | N/A (0 teams) | ASH only |
| Division 2 | 47.3% (42 teams) | 46.9% (40 teams) | -0.4% (tied) |
| Division 3 | 53.7% (63 teams) | 41.5% (68 teams) | **-12.2%** ⚠️ |
| Division 4 | 53.0% (89 teams) | 45.5% (47 teams) | **-7.5%** ⚠️ |

**Key Finding:**
- **FOX struggles in lower divisions** (3 & 4), performing 7-12% worse than ASH
- Division 2 performance is competitive (nearly equal)
- ASH has Division 1 representation, FOX has none

---

### 4. Program Depth (Division Distribution)
**What it measures:** Percentage of teams in higher vs lower divisions
**Why it matters:** Shows program strength - more Division 2 teams = stronger program

**Current Data:**
| Town | Div 1 | Div 2 | Div 3 | Div 4 | Program Rating |
|------|-------|-------|-------|-------|----------------|
| FOX  | 0.0% (0) | 25.8% (40) | 43.9% (68) | 30.3% (47) | DEVELOPING |
| ASH  | 2.0% (4) | 21.2% (42) | 31.8% (63) | 44.9% (89) | DEVELOPING |

**Rating Criteria:**
- **STRONG**: >40% in Division 2 or higher
- **MODERATE**: 30-40% in Division 2
- **DEVELOPING**: <30% in Division 2 (majority in 3/4)

**Key Finding:**
- Both towns are "DEVELOPING" programs (74-77% in Divisions 3/4)
- ASH has slight edge with Division 1 presence
- FOX has slightly more Division 2 representation (25.8% vs 21.2%)

---

### 5. Gender Balance
**What it measures:** Boys vs Girls program size
**Formula:** `Boys Teams / Girls Teams`
**Why it matters:** Shows equity and reach to all youth in community

**Current Data:**
| Town | Boys | Girls | Boys/Girls Ratio | Balance Rating |
|------|------|-------|------------------|----------------|
| FOX  | 79 (51.0%) | 76 (49.0%) | 1.04:1 | ✅ Well-balanced |
| ASH  | 121 (61.1%) | 77 (38.9%) | 1.57:1 | ⚠️ Boys-heavy |

**Rating Scale:**
- ✅ Well-balanced: 0.8-1.2 ratio
- 🟡 Slight imbalance: 0.6-0.8 or 1.2-1.5 ratio
- ⚠️ Heavy imbalance: <0.6 or >1.5 ratio

**Key Finding:**
- **FOX has excellent gender balance** (nearly 50/50)
- ASH is boys-heavy with 57% more boys teams than girls

---

### 6. Goals Per Game
**What it measures:** Offensive output
**Formula:** `Total Goals Scored / Total Games Played`
**Why it matters:** Shows attacking effectiveness and style of play

**Current Data - Overall:**
| Town | Goals/Game | Total Goals | Total Games |
|------|------------|-------------|-------------|
| ASH  | 2.46 | 4,461 | 1,816 |
| FOX  | 2.10 | 2,904 | 1,386 |
| **Difference** | **-0.36** | **-17% fewer** | |

**By Division Level:**
| Division | ASH Goals/Game | FOX Goals/Game | Difference |
|----------|----------------|----------------|------------|
| Division 1 | 2.73 | N/A | ASH only |
| Division 2 | 2.15 | 2.13 | -0.02 (tied) |
| Division 3 | 2.44 | 1.95 | **-0.49 (-25%)** ⚠️ |
| Division 4 | 2.59 | 2.28 | **-0.31 (-14%)** ⚠️ |

**Key Finding:**
- **FOX scores significantly fewer goals**, especially in Division 3
- Division 2 offense is competitive
- FOX averages 17% fewer goals overall

---

### 7. Goal Differential (CRITICAL METRIC)
**What it measures:** Overall team quality (offense + defense combined)
**Formula:** `Goals For - Goals Against`
**Why it matters:** Ultimate measure of winning - positive = good teams, negative = struggling

**Current Data - Overall:**
| Town | Total Diff | Diff/Team | Status |
|------|------------|-----------|--------|
| ASH  | +378 | +1.9 | ✅ **POSITIVE** |
| FOX  | -446 | -2.9 | ⚠️ **NEGATIVE** |
| **Gap** | **-824** | **-4.8 per team** | **Very concerning** |

**Breakdown:**
| Town | Goals For | Goals Against | Differential |
|------|-----------|---------------|--------------|
| ASH  | 4,461 | 4,083 | +378 |
| FOX  | 2,904 | 3,350 | -446 |

**By Division Level:**
| Division | ASH Diff/Team | FOX Diff/Team | Gap |
|----------|---------------|---------------|-----|
| Division 1 | -3.0 | N/A | ASH only |
| Division 2 | +0.7 | -1.2 | **-1.9** ⚠️ |
| Division 3 | +2.0 | **-5.1** | **-7.1** 🚨 |
| Division 4 | +2.7 | -1.1 | **-3.8** ⚠️ |

**Key Finding (MOST IMPORTANT):**
- 🚨 **FOX has negative goal differential across ALL divisions**
- 🚨 **Division 3 is catastrophic** (-5.1 per team)
- This indicates **systemic weakness in both offense AND defense**
- FOX teams are being consistently outscored by opponents

---

## Insights Discovered

### Finding 1: Ashland Has Higher Participation
- **Data:** ASH has 12.5% more teams per capita than FOX (1.17 vs 1.04 per 1,000)
- **Context:** Nearly identical populations (18,832 vs 18,618)
- **Implication:** Ashland attracts/retains more youth soccer players

### Finding 2: Foxborough Has Poor Spring Retention
- **Data:** FOX loses 44% of teams in Spring vs ASH losing only 16%
- **Context:** Both towns field similar Fall numbers (~22-25 teams)
- **Implication:** FOX struggles to maintain year-round participation
- **Questions:**
  - Why do FOX families drop out in Spring?
  - What does ASH do differently to retain players?
  - Is this a multi-sport conflict issue?
  - Weather/field availability?

### Finding 3: Foxborough Missing Fall 2023 Data
- **Data:** No FOX teams for Fall 2023 in database
- **Status:** Need to collect this season
- **Impact:** Affects trend analysis and averages

### Finding 4: Foxborough Has Negative Goal Differential (CRITICAL)
- **Data:** FOX is -446 total goal differential (-2.9 per team) vs ASH +378 (+1.9 per team)
- **Severity:** 824-goal gap between towns with similar populations
- **Implication:** FOX teams are systematically weaker in both offense and defense
- **Worst Area:** Division 3 (-5.1 goal diff per team) - catastrophic performance
- **Questions:**
  - Is FOX coaching/training quality lower than ASH?
  - Player development gaps?
  - Tryout/team formation issues?

### Finding 5: Foxborough Struggles in Lower Divisions
- **Data:**
  - Division 2: FOX 46.9% vs ASH 47.3% (competitive)
  - Division 3: FOX 41.5% vs ASH 53.7% (-12.2% worse)
  - Division 4: FOX 45.5% vs ASH 53.0% (-7.5% worse)
- **Context:** FOX performs similarly in Division 2 but significantly worse in 3 & 4
- **Implication:** FOX may have depth issues - top teams are competitive, but lower teams struggle
- **Questions:**
  - Does FOX concentrate best players on fewer teams?
  - Is ASH better at developing all skill levels?
  - Training/coaching quality for recreational players?

### Finding 6: Foxborough Has Excellent Gender Balance
- **Data:** FOX is 51% Boys / 49% Girls (1.04:1) vs ASH 61% Boys / 39% Girls (1.57:1)
- **Context:** This is the ONE metric where FOX outperforms ASH
- **Implication:** FOX successfully attracts girls to soccer
- **Positive:** Shows FOX does something right with gender equity

### Finding 7: Foxborough Scores Fewer Goals
- **Data:** FOX averages 2.10 goals/game vs ASH 2.46 goals/game (-17%)
- **Worst:** Division 3 where FOX scores 25% fewer goals
- **Context:** Lower scoring = weaker offense, fewer wins
- **Implication:** Offensive development or coaching may be lacking

---

## Questions to Investigate

### Immediate Questions (Once All Towns Collected)
1. ⏳ Which peer towns have participation rates higher than FOX?
2. ⏳ Which peer towns have better Spring retention than FOX?
3. ⏳ Is FOX an outlier or are other towns also struggling with Spring?
4. ⏳ Does participation rate correlate with Spring retention?

### Secondary Questions
5. ⏳ Do smaller towns have higher participation rates per capita?
6. ⏳ Is there a Boys vs Girls participation difference across towns?
7. ⏳ Are higher-participation towns also more competitive (win rates)?
8. ⏳ Has FOX participation been improving or declining over time?

### Deep Dive Questions (After Initial Analysis)
9. ⏳ What division levels do FOX teams compete in vs peers?
10. ⏳ Does FOX have more teams in lower divisions (program weakness)?
11. ⏳ Is FOX goal differential positive or negative vs peers?
12. ⏳ Are there specific age groups where FOX underperforms?

---

## Analysis Commands

### Quick Stats for a Town
```bash
python -c "
import pandas as pd
df = pd.read_csv('data/bays_teams.csv')
town_df = df[df['town_code'] == 'FOX']
print(f'Total teams: {len(town_df)}')
print(f'Avg wins: {town_df[\"wins\"].mean():.1f}')
print(f'Total seasons: {len(town_df.groupby([\"season_year\", \"season_period\"]))}')
"
```

### Compare Two Towns
```bash
python -c "
import pandas as pd
df = pd.read_csv('data/bays_teams.csv')

town1 = df[df['town_code'] == 'FOX']
town2 = df[df['town_code'] == 'ASH']

print(f'FOX: {len(town1)} teams')
print(f'ASH: {len(town2)} teams')
print(f'FOX avg wins: {town1[\"wins\"].mean():.1f}')
print(f'ASH avg wins: {town2[\"wins\"].mean():.1f}')
"
```

### Calculate Spring Drop for a Town
```bash
python -c "
import pandas as pd

df = pd.read_csv('data/bays_teams.csv')
town_df = df[df['town_code'] == 'FOX']

seasons = town_df.groupby(['season_year', 'season_period']).size().reset_index(name='teams')
pivot = seasons.pivot_table(index='season_year', columns='season_period', values='teams', fill_value=0)

if 'Fall' in pivot.columns and 'Spring' in pivot.columns:
    pivot['drop_pct'] = ((pivot['Fall'] - pivot['Spring']) / pivot['Spring'] * 100).round(1)
    print(pivot[['Fall', 'Spring', 'drop_pct']])
    print(f\"\\nAverage Spring Drop: {pivot['drop_pct'].mean():.1f}%\")
"
```

---

## Data Sources

- **Team Data:** Manual collection from BAYS.org standings pages
- **Population Data:** US Census estimates (2020+)
- **Import Tool:** `universal_import.py` (Ashland format standard)
- **Database:** `data/bays_teams.csv`

---

## Notes

- All metrics use season averages (not cumulative totals)
- Metrics are calculated from complete seasons only (no in-progress)
- Population normalization critical for fair comparisons
- FOX Fall 2023 missing - affects multi-year averages
- Spring Drop % calculated only for years with both Fall and Spring data

---

**Status:** 2 of 8 towns complete (FOX, ASH) | 6 towns remaining
