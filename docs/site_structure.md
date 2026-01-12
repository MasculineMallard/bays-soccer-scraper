# BAYS.org Website Structure - Reconnaissance Report

**Date:** 2026-01-10
**Purpose:** Document site structure for scraping team data

---

## Executive Summary

BAYS.org provides complete historical data from **Fall 2015 to present** (11 years, 22 seasons). The site uses Drupal 7 with POST-based season selection and has public access to all team records, standings, and schedules without authentication.

**Key Finding:** All required data is accessible and well-structured. The site supports both organization-based and division-based scraping approaches.

---

## 1. URL Patterns

### Organization Pages
**Pattern:** `/bays/organizations/view/{TOWN_CODE}`
**Example:** https://bays.org/bays/organizations/view/FOX

**Our Target Town Codes:**
- FOX - Foxborough Youth Soccer ✓
- HOP - Hopkinton Youth Soccer ✓
- WAL - Walpole Youth Soccer Association ✓
- WES - Westborough Youth Soccer Association ✓
- SUD - Sudbury Youth Soccer ✓
- ASH - Ashland Youth Soccer ✓
- HOL - Holliston Youth Soccer Association ✓
- BEL - Bellingham Soccer Association ✓
- NOR - Northborough Youth Soccer Association ✓
- MED - Medway Youth Soccer Association ✓
- WEF - Westford Youth Soccer Association ✓

### Team Pages
**Pattern:** `/bays/team/view/{TEAM_ID}`
**Example:** https://bays.org/bays/team/view/175572

### Section/Division Pages
**Pattern:** `/bays/section/view/{SECTION_ID}`
**Example:** https://bays.org/bays/section/view/8325

### Lookup Pages
- **Standings:** `/bays/standings_by_placement_lookup`
- **Schedule:** `/bays/schedule_by_placement_lookup`
- **Organizations List:** `/bays/organizations/select`

---

## 2. Available Seasons

**Historical Range:** Fall 2015 - Spring 2025 (11 years, 22 seasons)

**⚠️ IMPORTANT DATA COMPLETENESS NOTE:**
- Site lists seasons back to Fall 2015, but **data may not be complete** for all seasons
- Older seasons (2015-2017) may have:
  - Incomplete team rosters
  - Missing standings for some divisions
  - Teams without full W-L-T records
  - Missing goal data
- **Expected reality:** Likely 7-9 seasons of complete data (2018-2024), not full 10+
- Some towns may have joined BAYS later, so their historical data may start mid-range
- Must validate data completeness during scraping and note gaps in final analysis

**Season List:**
- Fall 2025, Spring 2025 *(may be in progress, skip per requirements)*
- Fall 2024, Spring 2024 ✓ (Expected complete)
- Fall 2023, Spring 2023 ✓ (Expected complete)
- Fall 2022, Spring 2022 ✓ (Expected complete)
- Fall 2021, Spring 2021 ✓ (Expected complete)
- Fall 2020, Spring 2020 ⚠️ (COVID season - may have data issues)
- Fall 2019, Spring 2019 ✓ (Expected complete)
- Fall 2018, Spring 2018 ⚠️ (May have some gaps)
- Fall 2017, Spring 2017 ⚠️ (May have gaps)
- Fall 2016, Spring 2016 ⚠️ (May have gaps)
- Fall 2015, Spring 2015 ⚠️ (May have significant gaps)

**Season Access:** POST-based form submission with season parameter

**Recommendation:** Start with Fall 2024 and work backwards. Stop when data quality drops significantly.

---

## 3. Data Structure

### Organization Page Data
**URL:** `/bays/organizations/view/{TOWN_CODE}`

**Available Data:**
- Table of all teams for selected season
- Columns: Gender/Grade/Division, Team Name, Field, Coach, Assistant Coach
- Each team links to individual team page

### Team Page Data
**URL:** `/bays/team/view/{TEAM_ID}`

**Available Data:**

**Team Identification:**
- Team Name
- Division (e.g., "3/B" = Division 3, Section B)
- Gender (Boys/Girls)
- Age Group (U8, U10, U12, U14, U16, U19)
- Organization/Town
- Field(s)
- Coach and Assistant Coach names

**Standings Data:**
- W (Wins)
- L (Losses)
- T (Ties)
- F (Forfeits)
- PTS (Points - typically 3 for win, 1 for tie)
- GF (Goals For)
- GA (Goals Against)
- +/- (Goal Differential)
- Home/Away splits for all above

**Schedule Data:**
- Game-by-game results with dates
- Home/Away designation
- Opponent (with link)
- Final score
- Field location

### Section Standings Data
**URL:** `/bays/section/view/{SECTION_ID}`

**Available Data:**
- Full standings table for all teams in section
- Team rankings (row order = rank)
- W-L-T records for all teams
- Goals For/Against for all teams
- Points totals
- Coach information

---

## 4. Division Structure

### Age Groups Available
- U3, U4, U5, U6, U8
- U9-12 (combined)
- U14, U16, U19

### Division Levels
- **Division 1** - Highest level (typically older age groups)
- **Division 2** - Second tier
- **Division 3** - Third tier
- **Division 4** - Fourth tier

### Division Tiers (Sections)
Within each division, teams are split into sections: A, B, C, D, E, etc.
- **Example:** "Division 3/B" = Division 3, Section B
- **Hierarchy:** 2A is stronger than 2B, 2B stronger than 2C, etc.

### Gender Categories
- Boys
- Girls
- (Coed may exist in younger age groups)

---

## 5. Scraping Strategies

### Strategy 1: Organization-Based (Recommended for complete town data)

**Approach:**
1. For each town code (FOX, HOP, WAL, etc.)
2. For each season (Fall 2015 - Fall 2024)
3. Access `/bays/organizations/view/{TOWN_CODE}` with season POST
4. Extract all team IDs from the table
5. For each team: access `/bays/team/view/{TEAM_ID}` with season POST
6. Parse team page for complete data

**Pros:**
- Comprehensive coverage of all teams from target towns
- Easy to track progress by town
- Can run parallel agents per town

**Cons:**
- Many individual team page requests
- Need to handle POST requests for season selection

### Strategy 2: Division/Section-Based (Recommended for structured data)

**Approach:**
1. Use `/bays/standings_by_placement_lookup` form
2. For each Season → Gender → Age → Division → Section
3. Scrape section standings table
4. Extract W-L-T, Goals, Rankings for all teams in section

**Pros:**
- Get multiple teams at once (6-8 per section)
- Data already formatted in standings table
- Fewer total requests

**Cons:**
- Need to enumerate all division/section combinations
- May miss teams not in standard divisions

### Strategy 3: Hybrid (RECOMMENDED - Best for accuracy and completeness)

**Approach:**
1. **Phase A - Discover all teams:** Use Strategy 1 (Organization-based)
   - For each town: `/bays/organizations/view/{TOWN_CODE}` with season POST
   - Extract all team names, IDs, and division info from organization table
   - Build master list of teams per town per season

2. **Phase B - Batch collect standings:** Use Strategy 2 (Division/Section-based)
   - For each Season → Gender → Age → Division → Section combo
   - Use `/bays/standings_by_placement_lookup` or `/bays/section/view/{SECTION_ID}`
   - Collect W-L-T, Goals, Rankings for all teams in section at once
   - This gets 6-8 teams per request (much more efficient)

3. **Phase C - Cross-reference and validate:**
   - Compare Phase A team list with Phase B standings data
   - Identify any teams in Phase A that didn't appear in Phase B standings
   - Check for mismatches or missing data

4. **Phase D - Fill gaps with individual team pages:**
   - For any teams missing standings data, scrape `/bays/team/view/{TEAM_ID}`
   - Parse individual team page for complete W-L-T and goals data
   - This ensures 100% data completeness

**Pros:**
- Most complete and accurate data collection
- Efficient batch collection where possible
- Validates data from multiple sources
- Catches edge cases (teams that moved divisions, incomplete rosters, etc.)

**Cons:**
- More complex implementation
- Requires coordination between multiple data sources
- Slightly longer execution time

**Recommended for:** Production data collection (after initial testing)

---

## 6. Data Extraction Points

### For CSV Schema Requirements

**From Organization Page:**
- Team name
- Division (parse to get level and tier)
- Age group
- Gender

**From Team Page:**
- Wins, Losses, Ties
- Goals For, Goals Against
- (Can calculate goal differential)

**From Section Standings:**
- Final rank in division
- Total teams in division (count rows)
- Points total

**Parsing Division String:**
Example: "3/B" or "Division 3/B"
- `division_level` = 3
- `division_tier` = "B"
- `division_full` = "Division 3/B" or construct as "U{age} {gender} Division {level}{tier}"

---

## 7. Technical Considerations

### Form Handling
- **Method:** POST requests required for season selection
- **Form Field:** Typically `season` parameter
- **Values:** "Fall 2024", "Spring 2024", etc.

### Page Structure
- **Platform:** Drupal 7 CMS
- **Tables:** jQuery "footable" plugin for responsive tables
- **Data Format:** HTML tables with data in standard td/th elements
- **No Auth Required:** All pages publicly accessible

### Rate Limiting
- **robots.txt:** 10-second crawl delay required
- **Cloudflare:** Present, may require proper headers
- **Best Practice:** Use agents with delays between requests

---

## 8. Sample Data Flow

**Example: Scraping Foxborough U12 Boys Division 2A for Fall 2024**

1. **Step 1:** GET/POST to `/bays/organizations/view/FOX` with season="Fall 2024"
2. **Step 2:** Find "U12 Boys Division 2/A" team in table
3. **Step 3:** Extract team_id from link (e.g., 175572)
4. **Step 4:** GET/POST to `/bays/team/view/175572` with season="Fall 2024"
5. **Step 5:** Parse standings section:
   - W: 8, L: 2, T: 1 (example)
   - GF: 32, GA: 15
   - PTS: 25
6. **Step 6:** Parse division string "2/A" → level=2, tier="A"
7. **Step 7:** Write row to CSV:
   ```csv
   FOX,Foxborough Youth Soccer,18618,2024,Fall,Foxboro Warriors U12B,2,A,U12 Boys Division 2A,U12,Boys,8,2,1,32,15,NULL,8,2026-01-10
   ```

---

## 9. Data Validation Checkpoints

### Required Fields
- ✅ Town code and name (from config)
- ✅ Season year and period (from season string)
- ✅ Team name (from team page or org table)
- ✅ Division level (1-4, parsed from division string)
- ✅ Division tier (A, B, C, etc., parsed from division string)
- ✅ Age group (U8-U19, from team info or division string)
- ✅ Gender (Boys/Girls, from team info or division string)
- ✅ W-L-T record (from standings)
- ✅ Goals for/against (from standings)
- ⚠️ Final rank (from section standings - may need separate lookup)
- ⚠️ Total teams in division (from section standings - may need count)
- ✅ Scrape date (current date)

### Validation Rules
- Wins + Losses + Ties should be > 0 (teams must have played games)
- Goals should be >= 0
- Division level should be 1, 2, 3, or 4
- Division tier should be A-E (or single letter)
- Age group should match U8, U10, U12, U14, U16, U19
- Gender should be Boys, Girls, or Coed

---

## 10. Recommended Scraping Workflow

### Phase 1: Test Single Town, Single Season
1. Scrape FOX for Fall 2024
2. Extract all teams
3. Parse and validate data
4. Write to CSV
5. Verify data quality

### Phase 2: Scale to All Seasons for FOX
1. Loop through all 20 seasons (Fall 2015 - Fall 2024)
2. For each season, scrape all FOX teams
3. Validate no duplicates
4. Track progress with checkpoints

### Phase 3: Scale to All Towns
1. For each of 11 towns
2. For each of 20 seasons
3. Scrape all teams
4. Estimate: 11 towns × 20 seasons × 30 teams avg = ~6,600 team-season records
5. Can parallelize by town (11 parallel agents)

### Phase 4: Gather Population Data
1. Lookup 2020 Census or latest estimates for all 11 towns
2. Update `config/towns_config.py` with population values

### Phase 5: Data Quality Check
1. Validate all required fields present
2. Check for duplicates
3. Verify reasonable team counts per town (should be similar)
4. Spot check 20-30 records manually

---

## 11. Next Steps

✅ **Completed:**
- Site structure documented
- URL patterns identified
- Data availability confirmed
- Scraping strategies outlined

⏭️ **Next:**
- Set up CSV storage and manager (Phase 3)
- Create data collection script templates
- Begin test scrape with FOX Fall 2024
- Gather population data for all 11 towns

---

**Sources:**
- [Foxboro Soccer Association on BAYS](https://bays.org/bays/organizations/view/FOX)
- [BAYS Standings Lookup](https://bays.org/bays/standings_by_placement_lookup)
- [Boston Area Youth Soccer Home](https://bays.org/)
