# CRITICAL BUG DISCOVERED - Historical Data is Invalid

## Date: 2026-01-10

## Summary

All historical season data in the CSV (Fall 2023 back to Fall 2018) is **INVALID**. The scraper was pulling the CURRENT season's data (Fall 2025) repeatedly for every historical season request.

## Evidence

Comparing Foxborough Fall 2025 vs Fall 2019 data:

```
Fall 2025: Warriors 7/8G-Blue: 7-1, GF=20, GA=13
Fall 2019: Warriors 7/8G-Blue: 7-1, GF=20, GA=13  ← IDENTICAL!
```

Every town shows exactly the same team count for all seasons:
- ASH: 25 teams for ALL 16 seasons
- BEL: 10 teams for ALL 16 seasons
- FOX: 25 teams for ALL 16 seasons
- etc.

This is statistically impossible. Team counts vary year-to-year.

## Root Cause

The scraper URL construction does NOT include season information:
```python
url = f"https://bays.org/bays/organizations/view/{town_code}"
```

This URL shows the CURRENT season by default. The scraper never selected a different season, so it scraped Fall 2025 data repeatedly.

## Fix Attempted

Added season selection code to:
1. Click "(Change)" checkbox
2. Select season from dropdown
3. Submit form
4. Wait for page reload
5. Click Standings

**Problem:** After submitting the form, Cloudflare triggers ANOTHER protection check ("Just a moment...") that never completes within 30 seconds.

## Valid Data

**ONLY Fall 2024 data is confirmed valid:**
- 273 teams across 10 towns
- Proper variation in stats
- See `data/fall2024_profile.json` for baseline

## Next Steps

### Immediate: Data Cleanup
1. **Clear Invalid Data:** Remove all seasons except Fall 2024 from CSV (keep the 273 valid teams)

### Technical Challenge: Cloudflare Blocking

**Problem:** BAYS.org has VERY aggressive Cloudflare protection that blocks:
- Standard Selenium (regular Chrome)
- Selenium with undetected-chromedriver
- Form submissions (triggers new Cloudflare challenge)

**What We Tried:**
1. ✓ Season selector implementation (works up to form submission)
2. ✗ Standard delays (not enough)
3. ✗ Undetected-chromedriver (Cloudflare still blocks for 60+ seconds)
4. ✗ JavaScript clicks (same result)

**Cloudflare Behavior:**
- Initial page load: Sometimes passes, sometimes stuck at "Just a moment..."
- Form submission: ALWAYS triggers new challenge that never completes

### Options Going Forward

**Option 1: Manual Data Entry** (Most Reliable)
- Visit BAYS.org manually
- Change season dropdown by hand
- Copy/paste data into CSV
- Pros: Works immediately, no Cloudflare issues
- Cons: Time-consuming (~20-30 min per season = 7-8 hours total)

**Option 2: Contact BAYS** (Best Long-term)
- Email BAYS asking for historical data export
- Or ask if they have an API
- Pros: Official data, complete/accurate
- Cons: May take time, they may not provide it

**Option 3: Advanced Cloudflare Bypass** (Complex)
- Try residential proxy services
- Use browser automation tools like Puppeteer with stealth plugins
- Add human-like mouse movements and delays
- Rotate user agents more aggressively
- Pros: Automated once working
- Cons: Expensive, still might fail, ethically questionable

**Option 4: Hybrid Approach** (Recommended)
- Manually collect 2-3 recent seasons (Fall 2023, Spring 2023, Fall 2022)
- Use that data for immediate analysis
- Continue investigating automated solutions in parallel
- Pros: Get usable data quickly, don't give up on automation
- Cons: Still some manual work

### Recommended Path

**Phase 1** (Now):
1. Clear invalid data from CSV
2. Validate Fall 2024 as baseline
3. Manually collect Fall 2023 data (test manual process)

**Phase 2** (If manual works):
4. Collect 2-3 more recent seasons manually
5. Begin analysis with available data

**Phase 3** (Parallel research):
6. Research BAYS contact/API
7. Try Puppeteer with stealth mode
8. Consider if full historical data is truly needed

## Files

- `data/fall2024_profile.json` - Baseline data profile
- `build_data_profile.py` - Profile builder
- `check_duplicates.py` - Analysis showing identical data
- `analyze_variance.py` - Shows zero variance across seasons (red flag)

## Impact

Current CSV contains:
- **Valid:** 273 Fall 2024 teams
- **Invalid:** ~3,677 teams from other seasons (actually duplicated Fall 2025 data)

**Total data collection must be redone after fixing the scraper.**
