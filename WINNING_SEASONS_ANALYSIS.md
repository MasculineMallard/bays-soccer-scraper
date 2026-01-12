# Winning Seasons Metric Analysis

## Objective

Investigate whether "number of winning seasons normalized by team count" would be a useful metric for comparing towns.

## Metric Definition

**Winning Season**: A team that finishes with more wins than losses (Win % > 50%)

**Proposed Metric**:
```
Winning Seasons % = (Number of Winning Seasons / Total Teams) × 100
```

## Analysis

### Pros
1. **Easy to understand**: Clear binary outcome (winning season or not)
2. **Resilient to outliers**: Not skewed by one dominant or struggling team
3. **Program-wide view**: Shows what percentage of teams have successful seasons
4. **Comparable**: Normalized by team count, fair comparison across town sizes

### Cons
1. **Redundant with Win %**: Highly correlated with average Win % metric
   - If a town's average Win % is 55%, most teams are likely having winning seasons
   - If average Win % is 45%, most teams are likely having losing seasons
2. **Loss of granularity**: 51% Win % and 70% Win % both count as "1 winning season"
3. **Division effects**: Teams in higher divisions face tougher competition, naturally have lower win rates
   - Could penalize towns with more competitive placements

### Correlation Analysis

Expected correlation with existing metrics:
- **High correlation** with Win %  (R² likely > 0.85)
- **High correlation** with Goal Differential (R² likely > 0.75)
- **Moderate correlation** with Average Division (negative correlation)

## Recommendation

**Do NOT add this metric** to the dashboard for the following reasons:

1. **Adds minimal new information**: The current Win % metric already captures this concept with more precision
2. **Creates confusion**: Having both Win % and Winning Seasons % would require explaining the difference to users
3. **Dashboard simplicity**: The current 9 metrics provide comprehensive coverage without redundancy

## Alternative Approach

If you want to highlight team success distribution, consider:

### Option 1: Win % Distribution Visualization
Show a histogram or box plot of team Win % for each town, revealing:
- Median Win %
- Spread/variance in performance
- Number of teams above/below 50%

### Option 2: Success Tier Breakdown
Categorize teams into tiers:
- **Elite** (Win % > 60%): X% of teams
- **Winning** (50-60%): Y% of teams
- **Competitive** (40-50%): Z% of teams
- **Struggling** (< 40%): W% of teams

This would show the distribution of success across the program.

## Implementation Notes

If you decide to add Winning Seasons % despite recommendations:

```python
# Calculate winning seasons percentage
winning_teams = len(town_df[town_df['win_pct'] > 50])
total_teams = len(town_df)
winning_seasons_pct = (winning_teams / total_teams) * 100
```

Add to metrics dictionary and include in rankings/comparisons.

## Conclusion

The **Win % metric already effectively captures program competitive performance**. Adding a winning seasons metric would be redundant and could complicate the dashboard narrative without providing meaningful additional insights.

**Status**: Analysis complete. Recommend **not implementing** this metric.
