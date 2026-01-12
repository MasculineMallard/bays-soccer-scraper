# Manual Data Extraction Guide

Since BAYS.org has Cloudflare protection that blocks automated scraping, here's a simple manual extraction workflow.

---

## Quick Method: Browser Console JavaScript

### Step 1: Open the Page

1. Open your browser and navigate to: `https://bays.org/bays/organizations/view/FOX`
2. Select "Fall 2024" season from the dropdown (if not already selected)
3. Wait for the teams table to load

### Step 2: Extract Data Using Browser Console

1. Press `F12` to open Developer Tools
2. Click on the "Console" tab
3. Paste this JavaScript code and press Enter:

```javascript
// Extract all team data from the table
let table = document.querySelector('table');
let rows = Array.from(table.querySelectorAll('tr')).slice(1); // Skip header row

let data = rows.map(row => {
    let cells = Array.from(row.querySelectorAll('td')).map(cell => cell.innerText.trim());
    return cells.join('\t');
}).join('\n');

// Copy to clipboard
copy(data);
console.log('Data copied to clipboard!');
console.log('Rows extracted: ' + rows.length);
console.log('\nPreview:');
console.log(data.substring(0, 500) + '...');
```

### Step 3: Paste Data into Python Script

1. The data is now in your clipboard (tab-separated)
2. Open `src/manual_browser_extract.py`
3. Find the `MANUAL_DATA = """` section
4. Paste your clipboard data between the triple quotes
5. Run: `python src/manual_browser_extract.py`

---

## Alternative Method: Copy Table Directly

### Step 1: Select the Table

1. Open: `https://bays.org/bays/organizations/view/FOX`
2. Select Fall 2024 season
3. Click and drag to select the entire teams table
4. Press `Ctrl+C` to copy

### Step 2: Paste into Excel/Google Sheets

1. Open Excel or Google Sheets
2. Paste the table (`Ctrl+V`)
3. Clean up any extra columns/rows
4. Save as CSV: `foxborough_fall2024.csv`

### Step 3: Import CSV

```python
import pandas as pd
from csv_manager import CSVManager
from manual_data_entry import parse_division, create_team_record

# Load the CSV
df = pd.read_csv('foxborough_fall2024.csv')

# Convert to team records
teams = []
for _, row in df.iterrows():
    team = create_team_record(
        town_code='FOX',
        town_name='Foxborough Youth Soccer',
        town_population=None,  # Fill later
        season_year=2024,
        season_period='Fall',
        team_name=row['Team Name'],  # Adjust column names as needed
        division_string=row['Division'],
        age_group=row['Age Group'],  # or extract from team name
        gender=row['Gender'],  # or extract from team name
        wins=int(row['W']),
        losses=int(row['L']),
        ties=int(row['T']),
        goals_for=int(row['GF']),
        goals_against=int(row['GA'])
    )
    teams.append(team)

# Save to main CSV
manager = CSVManager()
manager.append_teams(teams)
```

---

## Expected Table Structure

The BAYS.org teams table typically has columns like:

- Team Name
- Division (e.g., "2/A", "3/B")
- Wins (W)
- Losses (L)
- Ties (T)
- Goals For (GF)
- Goals Against (GA)
- Possibly: Rank, Points, etc.

**Example row:**
```
Foxboro U12 Boys Blue    2/A    8    2    1    32    15    2    24
```

---

## Tips for Faster Data Collection

### For Multiple Towns/Seasons:

1. **Use the Browser Console Method** - Fastest for single-page extraction
2. **Create a simple loop** in browser console:

```javascript
// Save this as a bookmark/snippet for reuse
function extractBAYSTable() {
    let table = document.querySelector('table');
    if (!table) {
        alert('No table found!');
        return;
    }

    let rows = Array.from(table.querySelectorAll('tr')).slice(1);
    let data = rows.map(row => {
        let cells = Array.from(row.querySelectorAll('td')).map(cell => cell.innerText.trim());
        return cells.join('\t');
    }).join('\n');

    copy(data);
    alert('Copied ' + rows.length + ' rows to clipboard!');
}

extractBAYSTable();
```

3. **For each town:**
   - Navigate to organization page
   - Select season
   - Run `extractBAYSTable()` in console
   - Paste into a text file labeled with town and season
   - Repeat for next town

4. **Process all files at once** using a batch script

---

## Scaling to All 11 Towns

### Recommended Workflow:

**For Fall 2024** (start with most recent):

1. Create a folder: `data/manual_extracts/fall2024/`
2. For each town:
   - Extract data using browser console
   - Save as: `{TOWN_CODE}.txt` (e.g., `FOX.txt`, `HOP.txt`)
3. Run batch processor:

```python
# src/batch_process_manual.py
import os
import glob
from csv_manager import CSVManager
from manual_data_entry import parse_manual_data, save_to_csv

manager = CSVManager()

# Process all files in manual_extracts/fall2024/
files = glob.glob('data/manual_extracts/fall2024/*.txt')

for file in files:
    town_code = os.path.basename(file).replace('.txt', '')

    with open(file, 'r') as f:
        data = f.read()

    teams = parse_manual_data(data, town_code, TOWNS[town_code]['name'], 2024, 'Fall')

    added, skipped = manager.append_teams(teams)
    print(f"{town_code}: Added {added}, Skipped {skipped}")
```

**Time estimate per town:** 2-3 minutes
**Total time for 11 towns, 1 season:** ~30 minutes
**Total time for 11 towns, 8 seasons:** ~4 hours

---

## When to Use Which Method

| Method | Best For | Speed | Complexity |
|--------|----------|-------|------------|
| **Browser Console JS** | Single pages, quick extraction | Fastest | Easiest |
| **Copy to Excel** | Visual validation, complex tables | Medium | Easy |
| **Selenium (if working)** | Bulk automation, many seasons | Fastest (bulk) | Complex |

---

## Next Steps After Extraction

1. **Verify data quality**
   - Check for missing values
   - Validate division parsing worked correctly
   - Confirm win-loss records make sense

2. **Gather population data** for normalization

3. **Analyze the data** using the planned metrics

4. **Build the Streamlit dashboard**

---

## Troubleshooting

**Q: The JavaScript returns "No table found"**
- Make sure you're on the organizations view page with a season selected
- Try: `document.querySelectorAll('table')` to see all tables
- Adjust the selector to the correct table class/ID

**Q: Data format looks wrong**
- Check the column order in the table
- Adjust the parsing logic in `manual_data_entry.py`
- Print sample rows to debug: `console.log(rows[0])`

**Q: Some teams are missing data**
- Some teams may not have played any games yet
- Check if clicking the team name reveals more data
- Note incomplete records for later validation

---

## Summary

Given Cloudflare blocking, manual extraction is the most reliable method right now. The browser console JavaScript method takes ~2 minutes per page and is very reliable.

**Recommended approach:**
1. Start with Foxborough Fall 2024 to test the workflow
2. Validate the data looks correct in the CSV
3. Scale to all 11 towns for Fall 2024
4. Then work backwards through seasons (Fall 2023, 2022, etc.)

This approach is actually quite fast and avoids the complexities of Cloudflare bypass attempts.
