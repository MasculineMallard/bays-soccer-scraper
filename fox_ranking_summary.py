#!/usr/bin/env python3
"""
Visual summary of Foxborough's rankings across key metrics
"""

print("=" * 70)
print("FOXBOROUGH PERFORMANCE SUMMARY")
print("Rankings out of 7 towns (FOX, ASH, BEL, HOP, HOL, MAN, WAL)")
print("=" * 70)
print()

# Define metrics and FOX rankings
metrics = [
    ("Win Percentage", 7, "LAST", "46.4%"),
    ("Goal Differential", 7, "LAST", "-2.13 goals/team"),
    ("Offensive Strength", 6, "2nd to LAST", "19.53 goals/team"),
    ("Competitive Level", 4, "MIDDLE", "Division 3.08"),
]

# Print header
print("METRIC                    RANK    STATUS           VALUE")
print("-" * 70)

# Print each metric with visual indicator
for metric, rank, status, value in metrics:
    # Create visual ranking bar
    if rank == 7:
        bar = "[" + "X" * rank + " " * (7-rank) + "]"
        color = "CRITICAL"
    elif rank == 6:
        bar = "[" + "X" * rank + " " * (7-rank) + "]"
        color = "POOR"
    elif rank == 4:
        bar = "[" + "X" * rank + " " * (7-rank) + "]"
        color = "AVERAGE"
    else:
        bar = "[" + "X" * rank + " " * (7-rank) + "]"
        color = "GOOD"

    print(f"{metric:25s} #{rank}/7   {status:15s}  {value}")

print()
print("=" * 70)
print("VISUAL RANKING CHART")
print("=" * 70)
print()
print("                          1st  2nd  3rd  4th  5th  6th  7th")
print("                          ---  ---  ---  ---  ---  ---  ---")
print(f"Win Percentage            [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [X]  LAST")
print(f"Goal Differential         [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [X]  LAST")
print(f"Offensive Strength        [ ]  [ ]  [ ]  [ ]  [ ]  [X]  [ ]  2nd to LAST")
print(f"Competitive Level         [ ]  [ ]  [ ]  [X]  [ ]  [ ]  [ ]  MIDDLE")
print()
print("=" * 70)
print("KEY FINDINGS")
print("=" * 70)
print()
print("CRITICAL ISSUES:")
print("  [!] LAST in Win Percentage (46.4%)")
print("      - Only town with a losing record (<50%)")
print("      - 6-20% below all other towns")
print()
print("  [!] LAST in Goal Differential (-2.13 per team)")
print("      - Losing by an average of 2 goals per game")
print("      - All other towns have better GD by 1.2-5.1 goals")
print()
print("  [!] 2nd to LAST in Offensive Strength (19.53 goals/team)")
print("      - Scoring 4-19% fewer goals than other towns")
print("      - Only Holliston scores less (18.75)")
print()
print("BELOW AVERAGE:")
print("  [+] MIDDLE in Competitive Level (Div 3.08)")
print("      - Competing at reasonable division levels")
print("      - Suggests losses are due to performance, not overscheduling")
print()
print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print()
print("Foxborough is underperforming in WINNING and SCORING despite competing")
print("at middle-tier division levels. This indicates systemic issues with:")
print()
print("  1. Player development / coaching quality")
print("  2. Team preparation and strategy")
print("  3. Offensive tactics and finishing")
print("  4. Overall program effectiveness")
print()
print("Foxborough should investigate what successful towns (MAN, ASH, BEL)")
print("are doing differently in coaching, training, and player development.")
print()
print("=" * 70)
