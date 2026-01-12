# Paste Workflow - Auto-Save System

## Overview

Every paste containing "youth soccer" is automatically saved to two locations:
1. **Dump file** (`data/pastes/paste_dump.txt`) - Chronological backup of ALL pastes
2. **Individual paste file** (`data/pastes/{TOWN}_{SEASON}_raw.txt`) - Specific season file
3. **CSV database** (`data/bays_teams.csv`) - Cleaned, structured data

This creates a safety net: if a season is accidentally missed during import, it can be recovered from the dump file.

## Files

### 1. `paste_dump.txt` - Universal Backup
Location: `data/pastes/paste_dump.txt`

Contains ALL pastes with timestamps and metadata. Format:
```
================================================================================
PASTE TIMESTAMP: 2026-01-10 17:15:45
TOWN: ASH | SEASON: Spring 2024
================================================================================
Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Storm	30389	Girls 8 3/D	8	1	1	0	25	35	8	27	William Curtis	Rob Piantedosi
...
```

### 2. Individual Paste Files
Location: `data/pastes/{TOWN}_{SEASON}{YEAR}_raw.txt`

Example: `data/pastes/ASH_Spring2024_raw.txt`

Clean copy of just the table data for a specific season.

### 3. CSV Database
Location: `data/bays_teams.csv`

Cleaned, structured data with columns:
- town_code, season_year, season_period, team_name
- gender, age_group, division_level, division_tier, division_full
- wins, losses, ties, forfeits, points
- goals_for, goals_against, goal_differential
- head_coach, assistant_coach, team_number

## How It Works

### Automatic Save (universal_import.py)

When you paste data using `universal_import.py`:

```python
from universal_import import save_and_import

save_and_import(raw_data, 'ASH', 2024, 'Spring')
```

This automatically:
1. ✅ Appends to `paste_dump.txt` with timestamp
2. ✅ Saves to `data/pastes/ASH_Spring2024_YYYYMMDD_HHMMSS.txt`
3. ✅ Parses data and adds to CSV
4. ✅ Skips duplicates

### Check for Missing Seasons

Use `auto_save_pastes.py` to find seasons in dump file that aren't in CSV:

```bash
python auto_save_pastes.py
# Choose option 2: Check for missing seasons
```

This compares:
- All seasons found in `paste_dump.txt`
- All seasons in `bays_teams.csv`
- Reports any gaps

### Import Missing Seasons

If you find missing seasons:

```bash
python auto_save_pastes.py
# Choose option 3: Import missing seasons from dump
```

This will:
1. List all missing seasons
2. Ask for confirmation
3. Import each one automatically
4. Update CSV

## Workflow Examples

### Example 1: Normal Paste
```
1. User pastes Ashland Spring 2024 data
2. Script saves to dump file automatically
3. Script saves to ASH_Spring2024_raw.txt
4. Script imports 22 teams to CSV
5. Done!
```

### Example 2: Recovering Lost Data
```
1. User realizes ASH Spring 2024 is missing from CSV
2. Run: python auto_save_pastes.py
3. Choose option 2 (check missing)
4. System shows: ASH Spring 2024 found in dump but not CSV
5. Choose option 3 (import missing)
6. System imports from dump file automatically
7. Done!
```

### Example 3: Viewing Paste History
```
1. Run: python auto_save_pastes.py
2. Choose option 1 (list all pastes)
3. See chronological list of every paste with timestamps
4. Can export specific entries if needed
```

## Benefits

### Safety Net
- Never lose pasted data
- Can always recover from dump file
- Timestamped for accountability

### Gap Detection
- Automatically find missing seasons
- Compare dump vs CSV
- Import missing data with one command

### Audit Trail
- See exactly when data was pasted
- Track which seasons have been collected
- Verify completeness across all towns

## Commands Reference

### Check Missing Seasons
```bash
python auto_save_pastes.py
# Choose 2
```

### Import Missing Seasons
```bash
python auto_save_pastes.py
# Choose 3
```

### View All Pastes
```bash
python auto_save_pastes.py
# Choose 1
```

### Manual Import from Dump
```bash
python auto_save_pastes.py
# Choose 4
# Enter entry number to extract
```

## Technical Details

### Dump File Format
- Separator: 80 equals signs
- Header: Timestamp + Town + Season
- Content: Raw pasted data
- Appended chronologically

### Town Code Detection
Automatically detects from paste content:
- "Ashland Youth Soccer" → ASH
- "Foxborough Youth Soccer" → FOX
- "Bellingham Youth Soccer" → BEL
- etc.

### Season Detection
Finds in paste header:
- "Fall 2024" → Fall, 2024
- "Spring 2024" → Spring, 2024

### Duplicate Handling
- CSV uses composite key: (town, year, period, team, division_level, division_tier)
- Duplicates are automatically skipped during import
- Dump file keeps ALL pastes (no deduplication)

## Maintenance

### Regular Checks
Run this weekly while collecting data:
```bash
python auto_save_pastes.py
# Option 2 - check for gaps
```

### After Bulk Collection
After collecting multiple towns:
```bash
python check_complete.py  # See what's collected
python auto_save_pastes.py  # Check dump for anything missed
```

### Before Final Analysis
Before running metrics:
```bash
# 1. Check for missing seasons
python auto_save_pastes.py  # Option 2

# 2. Verify all towns complete
python check_complete.py

# 3. Run metrics
python calculate_metrics.py
```

## Future Enhancements

Potential additions:
- Auto-detect paste from clipboard
- Email alerts for missing seasons
- Backup dump file to cloud
- Version control for CSV changes
- Web interface for paste management
