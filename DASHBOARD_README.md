# BAYS Soccer Analysis Dashboard

Interactive Streamlit dashboard for visualizing BAYS soccer performance metrics across 7 Massachusetts towns.

## Features

- **Key Performance Indicators**: Win percentage, goal differential, growth rate
- **Interactive Charts**: Bar charts, radar plots, comparative analysis
- **Town Filtering**: Select specific towns to compare
- **Multi-Metric Radar**: Visualize performance across 5 key dimensions
- **Offensive vs Defensive**: Compare scoring and defensive capabilities
- **Growth Trends**: Track program growth from 2021 to 2025
- **Key Findings**: Automated analysis of strengths and concerns

## Quick Start

### 1. Ensure Dependencies are Installed

```bash
pip install streamlit plotly pandas
```

### 2. Run the Dashboard

```bash
streamlit run streamlit_dashboard.py
```

The dashboard will open automatically in your default web browser at `http://localhost:8501`

## Dashboard Sections

### 📊 Key Performance Indicators
- Top-level metrics for Foxborough with comparisons to league average
- Quick view of win %, goal differential, rank, and growth

### 🏆 Win Percentage by Town
- Bar chart comparing win percentages across all towns
- Color-coded (red to green) to show performance
- 50% break-even line for reference

### ⚡ Goal Differential & Participation
- Side-by-side comparison of goal differential and participation rates
- Normalized per team and per 100 students respectively

### ⚔️ Offensive vs Defensive Performance
- Grouped bar chart showing goals for vs goals against
- Identifies offensive and defensive strengths/weaknesses

### 🎯 Multi-Metric Performance Radar
- Radar chart comparing 5 key metrics:
  - Win Percentage
  - Participation Rate
  - Retention Rate
  - Gender Balance
  - Growth Rate
- Foxborough highlighted by default

### 📊 Growth Rate Comparison
- Bar chart showing program growth (2021 → 2025)
- Positive/negative growth clearly indicated

### 📋 Complete Metrics Table
- Full data table with all calculated metrics
- Filterable by selected towns

### 🔍 Key Findings
- Automated analysis identifying areas of concern
- Highlights strengths of Foxborough program

## Customization

### Sidebar Filters
- **Select Towns**: Choose which towns to include in comparisons
- **Highlight Foxborough**: Toggle emphasis on Foxborough in charts

## Data Source

All data sourced from BAYS (Bay State Youth Soccer League) records covering seasons from 2021-2025.

Towns included:
- Foxborough (FOX)
- Ashland (ASH)
- Bellingham (BEL)
- Hopkinton (HOP)
- Holliston (HOL)
- Mansfield (MAN)
- Walpole (WAL)

## Metrics Calculated

1. **Participation Rate**: Teams per 100 students
2. **Win Percentage**: (Wins + 0.5 × Ties) / Total Games × 100
3. **Goal Differential**: Average goal diff per team
4. **Spring Retention**: % of fall teams that return in spring
5. **Offensive Strength**: Average goals scored per team
6. **Defensive Strength**: Average goals allowed per team
7. **Division Level**: Average division (1=highest, 4=lowest)
8. **Gender Balance**: Score based on 50/50 boys/girls split
9. **Growth Rate**: % change in teams (Fall 2021 → Fall 2025)

## Stopping the Dashboard

Press `Ctrl+C` in the terminal where the dashboard is running.
