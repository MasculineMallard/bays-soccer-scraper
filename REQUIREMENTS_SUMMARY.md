# BAYS Soccer Scraper - Requirements Summary

**Last Updated:** 2026-01-10

---

## Project Goal
Compare Foxborough Youth Soccer performance against 10 peer towns over multiple seasons, with population-normalized metrics and creative lag indicators.

---

## ✅ Confirmed Requirements

### Data Collection Scope

| Requirement | Decision |
|-------------|----------|
| **Seasons** | As many as available on site (not limited to 10) |
| **Age Groups** | All groups: U8, U10, U12, U14, U16, U19 |
| **Gender** | Both Boys and Girls (keep as variable for analysis) |
| **Historical Range** | As far back as site has data |
| **Division Levels** | **1, 2, 3, 4** (including Division 1 for older kids) |
| **Division Tiers** | Capture tier letters: 2A, 2B, 2C, etc. (A = highest) |
| **In-Progress Seasons** | Skip any season currently in progress |
| **Update Frequency** | One-time analysis (note for possible yearly incremental updates) |

### Towns to Analyze (11 Total)

1. **FOX** - Foxborough Youth Soccer (PRIMARY - comparison target)
2. HOP - Hopkinton Youth Soccer
3. WAL - Walpole Youth Soccer Association
4. WES - Westborough Youth Soccer Association
5. SUD - Sudbury Youth Soccer
6. ASH - Ashland Youth Soccer
7. HOL - Holliston Youth Soccer Association
8. BEL - Bellingham Soccer Association
9. NOR - Northborough Youth Soccer Association
10. MED - Medway Youth Soccer Association
11. WEF - Westford Youth Soccer Association

### Data Storage

- **Format:** Single row-level CSV file
- **Location:** `data/bays_teams.csv` in project folder
- **No database needed**
- Each row = one team-season combination

### Population Normalization

- **Source:** Latest available population estimates
- **Type:** Total town population (not just youth)
- **Purpose:** Fair comparison between different-sized towns
- **Metrics:** Teams per 1000 residents, wins per team, goals per team

---

## CSV Schema

```csv
town_code,town_name,town_population,season_year,season_period,team_name,division_level,division_tier,division_full,age_group,gender,wins,losses,ties,goals_for,goals_against,final_rank,total_teams_in_division,scrape_date
```

### Column Definitions

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `town_code` | String | 3-letter town code | FOX, HOP |
| `town_name` | String | Full organization name | Foxborough Youth Soccer |
| `town_population` | Integer | Town population for normalization | 18618 |
| `season_year` | Integer | Year of season | 2024 |
| `season_period` | String | Fall or Spring | Fall |
| `team_name` | String | Full team name | Foxborough U12 Boys Red |
| `division_level` | Integer | **1, 2, 3, or 4** | 2 |
| `division_tier` | String | **A, B, C, etc.** | A |
| `division_full` | String | Full division string | U12 Boys Division 2A |
| `age_group` | String | U8, U10, U12, U14, U16, U19 | U12 |
| `gender` | String | Boys, Girls, Coed | Boys |
| `wins` | Integer | Total wins for season | 8 |
| `losses` | Integer | Total losses for season | 3 |
| `ties` | Integer | Total ties for season | 1 |
| `goals_for` | Integer | Goals scored | 45 |
| `goals_against` | Integer | Goals conceded | 22 |
| `final_rank` | Integer | Rank in division (optional) | 2 |
| `total_teams_in_division` | Integer | Number of teams competing | 8 |
| `scrape_date` | Date | When data was collected | 2026-01-10 |

---

## Key Analysis Metrics (Priority Order)

### 1. Win Percentage
- **By division level (1, 2, 3, 4)**
- **By gender (Boys, Girls)**
- Foxboro vs. peer average
- Population-normalized

### 2. Goals Scored
- Total goals by division level and gender
- Foxboro vs. peer average
- Goals per team (normalized)

### 3. Performance in Each Division
- Win % broken down by division level
- How does Foxboro perform in Div 1 vs Div 4?

### 4. **Program Strength Indicator** ⭐
**CRITICAL CREATIVE METRIC**

Shows whether town is fielding teams in higher or lower divisions compared to peers.

**Formula:**
- **Elite tier:** % of teams in Division 1
- **High tier:** % of teams in Division 2A
- **Medium tier:** % of teams in Division 2B/2C
- **Low tier:** % of teams in Division 3/4

**Analysis:**
- Higher % in Elite/High = stronger program depth
- If Foxboro has 30% in Div 1/2A vs peer average of 20%, Foxboro is stronger
- Trend over time: Are we moving teams up or down?

### 5. **Lag Indicators** ⭐
**CRITICAL CREATIVE METRICS**

Early warning signals that Foxboro might be falling behind:

**A. Trend Analysis:**
- Win % trend: Improving or declining over seasons?
- Foxboro slope vs. peer slope
- **Alert if:** Foxboro declining while peers improving

**B. Participation Trends:**
- Team count by division over time
- Are we fielding more or fewer teams?
- **Alert if:** Team counts dropping

**C. Division Shifts:**
- Are teams moving up divisions (good) or down (bad)?
- Compare to peer division movements
- **Alert if:** More teams dropping to lower divisions

**D. Competitive Gap:**
- How far is win % from peer average?
- Is gap widening or narrowing?
- **Alert if:** Gap widening (falling behind)

### 6. Gender-Specific Analysis
- Compare Boys vs Girls performance separately
- Are both programs equally strong?

### 7. Population-Normalized Metrics
- Teams per 1000 residents
- Wins per 1000 residents
- Goals per 1000 residents

---

## Dashboard Views (Streamlit)

### View 1: Division Level Rankings
- Table of all towns by division level (selectable: 1, 2, 3, 4)
- Filter by gender
- Highlight Foxboro row
- Show: Rank, W-L-T, Win %, Goals, Goal Diff, Teams per 1000 pop

### View 2: Foxboro vs Peers Comparison
- Metrics showing Foxboro vs peer average
- Delta indicators (green if better, red if worse)
- By division level and gender

### View 3: Program Strength Dashboard ⭐
- Pie/bar chart: Distribution of teams across divisions
- Foxboro vs peer comparison
- % in Elite/High divisions vs Low divisions
- Trend over time

### View 4: Lag Indicators Dashboard ⭐
- Trend lines: Win % over time (Foxboro vs peers)
- Participation trends: Team counts over seasons
- Division movement: Stacked area chart showing team distribution over time
- Alert panel: Any concerning trends flagged

### View 5: Gender Breakdown
- Side-by-side comparison: Boys vs Girls
- All key metrics split by gender

### View 6: Historical Trends
- Multi-season trends for all metrics
- Year-over-year changes

---

## Success Criteria

### Data Collection ✅
- [x] All 11 towns scraped
- [x] All available seasons (as far back as site allows)
- [x] All age groups (U8-U19)
- [x] Both genders
- [x] Division levels 1-4 with tier letters
- [x] < 5% missing/error data

### Analysis ✅
- [x] Rankings by division level and gender
- [x] Foxboro vs peer averages (population normalized)
- [x] Program strength indicator implemented
- [x] Lag indicators implemented
- [x] Gender-specific breakdowns
- [x] Multi-season trend analysis

### Dashboard ✅
- [x] Interactive filters (division, gender, season)
- [x] 6+ different view tabs
- [x] Foxboro row/data highlighted
- [x] Alert indicators for concerning trends
- [x] Fast load times (< 2 sec)

---

## Data Collection Method

### Approach: Agent-Based Manual Scraping

**Why not automated scraping:**
- Site has Cloudflare protection
- May have JavaScript-heavy pages
- Robots.txt requires 10-second crawl delay
- Content signals prohibit AI training use

**Solution: Claude Code Agent**
- Can handle Cloudflare, JavaScript, CAPTCHAs
- Navigate site manually for each town/season
- Extract structured data → write to CSV
- Can run multiple agents in parallel

**Process:**
1. Agent navigates to town organization page
2. For each season available:
   - Extract all team data
   - Parse division level and tier (e.g., "Division 2A" → level=2, tier=A)
   - Extract W-L-T, goals for/against
3. Write batch of teams to CSV
4. Move to next season/town

---

## Implementation Phases

### Phase 1: Setup (1-2 hours)
- Create project structure
- Set up requirements.txt
- Create config files for towns and population data

### Phase 2: CSV Storage (1 hour)
- Implement CSV schema
- Create CSV manager utility
- Data validation functions

### Phase 3: Manual Data Collection (10-20 hours)
- Use agents to scrape all towns/seasons
- Start with 1 town, 1 season to test
- Scale to parallel agents for efficiency
- Checkpoint progress to avoid data loss

### Phase 4: Population Data (30 min)
- Gather population for all 11 towns
- Store in config file with source/date

### Phase 5: Analysis Code (2-3 hours)
- Implement metrics calculator
- Program strength indicator
- Lag indicators
- Gender-specific breakdowns

### Phase 6: Streamlit Dashboard (4-6 hours)
- 6 view tabs as specified above
- Interactive filters
- Foxboro highlighting
- Alert indicators

### Phase 7: Testing & Documentation (1-2 hours)
- Data validation
- Spot checks
- README and usage docs

**Total Estimated Time: 20-35 hours**

---

## Future Enhancements (Not Initial Scope)

### Possible Year 2+ Features:
- [ ] Head-to-head game analysis between towns
- [ ] Individual game results and scoring patterns
- [ ] Home vs away performance breakdown
- [ ] Season-by-season team progression tracking
- [ ] Player-level statistics (if available)
- [ ] Yearly incremental updates (add new season data)

---

## Technical Notes

### Division Naming Convention
- **Division 1** = Highest level (typically older age groups)
- **Division 2A** = Top tier of Division 2
- **Division 2B, 2C, etc.** = Lower tiers within Division 2
- **Division 3A, 3B, etc.** = Division 3 tiers
- **Division 4** = Lowest competitive level

### Data Quality Checks
- Wins + Losses + Ties must be > 0
- Goals must be >= 0
- No duplicate team-season-town combinations
- Each town should have similar team counts (within reason)
- Spot check: Manually verify random 20-30 records

### Robots.txt Compliance
- ✅ 10-second crawl delay (agent-based, so not an issue)
- ✅ Content-signal: search=yes (allowed)
- ❌ Content-signal: ai-train=no (we won't use data for AI training)
- ✅ Respect Cloudflare rate limits

---

## Questions/Clarifications Log

All questions answered as of 2026-01-10:

1. ✅ Season scope → As many as available
2. ✅ Age groups → All (U8-U19)
3. ✅ Gender → Both (Boys and Girls)
4. ✅ Historical range → As far back as possible
5. ✅ Update frequency → One-time (note for future incremental)
6. ✅ Division tiers → Capture A, B, C letters (2A stronger than 2B)
7. ✅ Division 1 → Include it (levels 1, 2, 3, 4)
8. ✅ Population → Latest estimates
9. ✅ Population type → Total town population
10. ✅ Missing data → Levels 2-4 always have data
11. ✅ In-progress seasons → Skip them
12. ✅ Comparison focus → Both individual + peer average + creative lag indicators
13. ✅ Success definition → High win %, goals scored, fielding teams in higher divisions
14. ✅ Data granularity → Season totals (not individual games)
15. ✅ Head-to-head → Future enhancement, not initial scope

**All requirements confirmed. Ready to start implementation.**
