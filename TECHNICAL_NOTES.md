# Technical Notes - Foxboro Youth Soccer Analytics

## Data Collection Notes

### Teams Switching Divisions Mid-Season

During data collection, it was observed that some teams switch divisions mid-season. This can result in:

1. **Missing Data**: When a team moves from one division to another during the season, there may be incomplete records for that team's performance in each division.

2. **Duplicated Team Entries**: A team that switches divisions may appear in the dataset twice for the same season - once for each division they participated in.

3. **Impact on Metrics**: This affects primarily:
   - Average Division calculations (teams contribute to multiple division averages)
   - Win/Loss records (split across divisions)
   - Goals For/Against totals (split across divisions)

### Handling Approach

For the purposes of this analysis:
- Teams that switched divisions are counted in both divisions they participated in
- Their statistics are reported as recorded in each division
- The overall metrics aggregate all records, regardless of mid-season switches
- This represents a small percentage of teams (<5%) and does not materially impact the overall analysis

### Future Improvements

Consider implementing:
1. A flag to identify teams that switched divisions
2. Logic to aggregate their full-season statistics under a single record
3. Tracking of the timing of division switches within the season

## Data Quality Notes

### Private School Enrollment

Private school enrollment data was investigated for all 8 comparable towns. Analysis showed:
- Private school enrollment ranges from 6-10% of total K-12 students in these communities
- No statistically significant correlation found between private school enrollment percentage and BAYS participation rates
- Public school enrollment alone provides an adequate normalization baseline for participation metrics

### Grade Level Coverage

The BAYS league data analyzed includes:
- **Grades 3-8** only
- Does **not include** town recreational programs (typically grades K-2)
- This aligns with BAYS league structure which focuses on competitive travel soccer for older elementary and middle school ages

### Enrollment Data Sources

School enrollment data sourced from:
- Massachusetts Department of Elementary and Secondary Education (DESE)
- U.S. News & World Report
- School year: 2024-25 (most recent available)
- Represents K-12 public school enrollment only

## Metric Definitions

### Spring Retention Rate

Calculated as:
```
Spring Retention % = (Average Spring Teams / Average Fall Teams) × 100
```

Where:
- Average Spring Teams = Total spring teams across all years / Number of years
- Average Fall Teams = Total fall teams across all years / Number of years

This metric measures how many teams return from Fall to Spring seasons, which is an indicator of:
- Program satisfaction
- Family commitment
- Competitive balance (teams not getting discouraged)

### Participation Rate Normalization

Participation Rate is normalized by school enrollment to enable fair comparison:
```
Participation Rate = (Total Teams / 10 seasons) / School Enrollment × 100
```

This gives "teams per 100 students" which accounts for:
- Different town sizes
- Different school enrollment levels
- Enables apples-to-apples comparison

## Known Limitations

1. **Competition Quality**: Win % and Goal Differential are influenced by the strength of opponents faced, which can vary by division and season
2. **Team Size**: Roster sizes may vary between towns, affecting per-team statistics
3. **Homeschool Population**: Not captured in enrollment data (estimated <2% in these communities)
4. **Private/Parochial Programs**: Some towns may have separate Catholic Youth Organization (CYO) or private school leagues not reflected in BAYS data
5. **Seasonal Variations**: Spring seasons consistently show lower participation than Fall across all towns (weather, competing spring sports)

## Change Log

### 2025-01-12
- Removed Competition Quality from Limitations section (per user request)
- Updated private school notes to reflect investigation results
- Added Grade Level coverage clarification
- Reorganized dashboard into 4 tabs for better UX
- Reduced trends chart from 6 metrics to 4 (removed Goals For/Against)
