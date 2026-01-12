#!/usr/bin/env python3
"""
BAYS Soccer Analysis Dashboard
Interactive Streamlit dashboard for visualizing core metrics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page config
st.set_page_config(
    page_title="BAYS Soccer Analysis",
    page_icon="⚽",
    layout="wide"
)

# Load data
@st.cache_data(ttl=600, show_spinner=False)
def load_data():
    """Load team and enrollment data. Cache expires after 10 minutes."""
    df = pd.read_csv('data/bays_teams.csv')
    enrollment_df = pd.read_csv('data/school_enrollment.csv')
    return df, enrollment_df

df, enrollment_df = load_data()

# Create enrollment lookup
enrollment_map = dict(zip(enrollment_df['town_code'], enrollment_df['enrollment']))

# Town configuration
towns = ['FOX', 'ASH', 'BEL', 'HOP', 'HOL', 'MAN', 'WAL', 'MDY']
town_names = {
    'FOX': 'Foxborough',
    'ASH': 'Ashland',
    'BEL': 'Bellingham',
    'HOP': 'Hopkinton',
    'HOL': 'Holliston',
    'MAN': 'Mansfield',
    'WAL': 'Walpole',
    'MDY': 'Medway'
}

# Calculate all metrics
@st.cache_data(show_spinner=False)
def calculate_metrics(filtered_metrics_input, towns_list):
    """Calculate metrics for all configured towns"""
    metrics = {}

    for town in towns_list:
        town_df = filtered_metrics_input[filtered_metrics_input['town_code'] == town]
        enrollment = enrollment_map[town]
        total = len(town_df)

        if total == 0:
            continue

        # Participation Rate
        teams_per_100 = (total / 10) / enrollment * 100

        # Win Percentage
        total_games = town_df['wins'].sum() + town_df['losses'].sum() + town_df['ties'].sum()
        win_pct = (town_df['wins'].sum() + 0.5 * town_df['ties'].sum()) / total_games * 100 if total_games > 0 else 0

        # Goal Differential per Team
        avg_gd = round(town_df['goal_differential'].sum() / total, 1)

        # Spring Retention Rate
        fall_teams = len(town_df[town_df['season_period'] == 'Fall']) / 5
        spring_teams = len(town_df[town_df['season_period'] == 'Spring']) / 5
        retention = (spring_teams / fall_teams * 100) if fall_teams > 0 else 0

        # Goals For/Against per Team
        avg_gf = town_df['goals_for'].sum() / total
        avg_ga = town_df['goals_against'].sum() / total

        # Division Distribution
        avg_division = town_df['division_level'].mean()

        # Gender Balance (% girls, 50 is perfect)
        boys = len(town_df[town_df['gender'] == 'Boys'])
        girls = len(town_df[town_df['gender'] == 'Girls'])
        girls_pct = (girls / total * 100) if total > 0 else 50

        # Growth Rate (Fall 2021 → Fall 2025)
        fall2021 = len(town_df[(town_df['season_year'] == 2021) & (town_df['season_period'] == 'Fall')])
        fall2025 = len(town_df[(town_df['season_year'] == 2025) & (town_df['season_period'] == 'Fall')])
        growth_pct = round(((fall2025 - fall2021) / fall2021) * 100, 1) if fall2021 > 0 else 0

        metrics[town] = {
            'Town': town_names[town],
            'Participation Rate': float(teams_per_100),
            'Win %': float(win_pct),
            'Goal Diff': float(avg_gd),
            'Retention %': float(retention),
            'Goals For': float(avg_gf),
            'Goals Against': float(avg_ga),
            'Avg Division': float(avg_division),
            'Gender Balance': float(girls_pct),
            'Growth %': float(growth_pct),
            'Enrollment': int(enrollment)
        }

    df_result = pd.DataFrame(metrics).T

    # Ensure all numeric columns are properly typed
    numeric_columns = ['Participation Rate', 'Win %', 'Goal Diff', 'Retention %',
                      'Goals For', 'Goals Against', 'Avg Division', 'Gender Balance',
                      'Growth %', 'Enrollment']
    for col in numeric_columns:
        df_result[col] = pd.to_numeric(df_result[col], errors='coerce')

    return df_result

# Title and intro
st.markdown("<h1 style='margin-bottom: 5px;'>⚽ Foxboro Soccer Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top: 0px; margin-bottom: 10px;'>Compared to 7 Comparable Massachusetts Towns</h3>", unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["📊 Dashboard", "📖 Definitions & Assumptions"])

with tab2:
    st.markdown("## 📖 Definitions & Assumptions")
    st.markdown("---")

    st.markdown("### 🏘️ Comparable Towns")
    st.markdown("""
    Foxborough is compared to **7 similar Massachusetts towns** selected based on:
    - **Population size** (13,000 - 25,000 residents)
    - **Demographics** (suburban communities, similar socioeconomic profiles)
    - **Geographic proximity** (all within BAYS league)
    - **School enrollment** (1,990 - 4,187 students in K-12)

    **Towns included:**
    - Ashland (18,832 population, 2,909 students)
    - Bellingham (16,945 population, 1,990 students)
    - Hopkinton (18,758 population, 4,187 students)
    - Holliston (15,494 population, 2,810 students)
    - Mansfield (25,067 population, 3,243 students)
    - Walpole (24,070 population, 3,565 students)
    - Medway (13,115 population, 2,040 students)

    **Note on Data Normalization:**
    All participation-related metrics are **normalized by school enrollment** (teams per 100 students) to enable fair comparison between towns of different sizes. This ensures that differences in participation reflect program engagement rather than simply town size. Competitive performance metrics (Win %, Goal Differential, etc.) measure quality of play and are intentionally not size-normalized.

    **Important Finding:**
    Analysis of the data shows that **town/school size has no correlation to competitive performance**. Win %, Goal Differential, and Average Division show near-zero correlation with enrollment, meaning smaller towns compete just as effectively as larger towns. <b><span style='color: #1E90FF;'>Success is driven by program quality, not town size.</span></b>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📊 Metric Definitions")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Competitive Performance")
        st.markdown("""
        **Win %**: Percentage of games won
        - Formula: `(Wins + 0.5 × Ties) / Total Games × 100`
        - Ties count as half a win
        - 50% represents break-even performance

        **Goal Differential**: Average goal difference per team
        - Formula: `Total (Goals For - Goals Against) / Number of Teams`
        - Positive values indicate teams score more than they concede
        - Negative values indicate defensive struggles

        **Goals For**: Average goals scored per team per season
        - Formula: `Total Goals For / Number of Teams`
        - Indicates offensive strength and scoring ability

        **Goals Against**: Average goals conceded per team per season
        - Formula: `Total Goals Against / Number of Teams`
        - Lower is better - indicates defensive quality
        """)

        st.markdown("#### Program Structure")
        st.markdown("""
        **Average Division**: Mean BAYS division level across all teams
        - Scale: 1 (highest/most competitive) to 4 (recreational)
        - Lower average indicates teams compete at higher levels
        - Reflects overall program competitiveness

        **Gender Balance**: Percentage of teams that are girls teams
        - Formula: `Girls Teams / Total Teams × 100`
        - 50% represents perfect gender balance
        - Measures program inclusivity and appeal to all genders
        """)

    with col2:
        st.markdown("#### Participation & Growth")
        st.markdown("""
        **Participation Rate**: Teams per 100 students
        - Formula: `(Total Teams / 10 seasons) / School Enrollment × 100`
        - Divided by 10 to get average teams per year
        - Measures program reach relative to town size
        - Higher values indicate stronger community engagement

        **Retention %**: Teams returning from Fall to Spring
        - Formula: `(Average Spring Teams / Average Fall Teams) × 100`
        - Averaged across all years (2021-2025)
        - High retention (>80%) suggests program satisfaction
        - Low retention (<70%) may indicate issues with experience

        **Growth %**: Change in Fall teams from 2021 to 2025
        - Formula: `((Fall 2025 Teams - Fall 2021 Teams) / Fall 2021 Teams) × 100`
        - Positive values indicate program expansion
        - Negative values indicate declining enrollment
        """)

        st.markdown("#### Overall Grades")
        st.markdown("""
        **Letter Grade Calculation**: Based on average rank across metrics
        - **A**: Average rank ≤ 1.5 (Top 2 consistently)
        - **B**: Average rank ≤ 2.5 (Top 3 consistently)
        - **C**: Average rank ≤ 4.0 (Middle of pack)
        - **D**: Average rank ≤ 5.5 (Below average)
        - **F**: Average rank > 5.5 (Bottom performers)

        **Three Grade Categories:**
        1. **Competitive Performance**: Win %, Goal Diff, Goals For, Goals Against
        2. **Participation & Growth**: Participation Rate, Retention %, Growth %
        3. **Program Balance**: Gender Balance, Avg Division
        """)

    st.markdown("---")
    st.markdown("### 🔢 Key Assumptions")
    st.markdown("""
    1. **Data Period**: Analysis covers 10 seasons from Spring 2021 through Fall 2025
    2. **Teams Counted**: All BAYS-registered teams (recreational and competitive) for the 8 comparable towns
    3. **Enrollment Data**: K-12 public school enrollment from 2024-25 school year (does not include private school students)
    4. **Season Division**: Each year has Fall and Spring seasons
    5. **Ranking Method**: Lower rank number is better (1 is best, 8 is worst)
    6. **League Average**: Calculated as mean of the 7 comparison towns (excludes Foxborough)
    7. **Population Data**: Based on 2020 U.S. Census
    8. **Ties in Win %**: Ties count as 0.5 wins (standard soccer convention)
    9. **Division Levels**: BAYS assigns teams to divisions 1-4, with 1 being most competitive
    10. **Growth Baseline**: Fall 2021 used as baseline for calculating growth percentage
    """)

    st.markdown("---")
    st.markdown("### ⚠️ Limitations & Considerations")
    st.markdown("""
    - **Competition Quality**: Win % and Goal Diff affected by strength of opponents faced
    - **Team Size Variations**: Some towns may have larger or smaller team rosters
    - **Age Group Differences**: Some age groups may be more competitive than others
    - **Participation Factors**: Enrollment doesn't capture private school students or homeschoolers (estimated 6-10% of students in these communities based on state averages)
    - **Seasonal Variations**: Spring seasons typically have lower participation than Fall
    """)

    st.markdown("---")
    st.markdown("### 📊 Data Sources")
    st.markdown("""
    - **Team Performance Data**: BAYS (Bay State Youth Soccer League) records, 2021-2025
    - **School Enrollment**: Massachusetts Department of Elementary and Secondary Education, 2024-25
    - **Population Data**: U.S. Census Bureau, 2020 Census
    """)

# Sidebar - Filters (outside tabs, always visible)
st.sidebar.header("Filter Options")

# Season filter
st.sidebar.subheader("📅 Season Filter")
all_years = sorted(df['season_year'].unique())
selected_years = st.sidebar.multiselect(
    "Select Years",
    options=all_years,
    default=all_years
)

all_periods = ['Fall', 'Spring']
selected_periods = st.sidebar.multiselect(
    "Select Seasons",
    options=all_periods,
    default=all_periods
)

# Apply season filters to dataframe
filtered_metrics_data = df[
    (df['season_year'].isin(selected_years)) &
    (df['season_period'].isin(selected_periods))
]

# Town selector
st.sidebar.subheader("🏘️ Town Filter")
selected_towns = st.sidebar.multiselect(
    "Select Towns to Compare",
    options=list(town_names.values()),
    default=list(town_names.values())
)

# Calculate metrics with filtered data (pass towns list to avoid cache issues)
metrics_df = calculate_metrics(filtered_metrics_data, towns)

# Filter metrics by selected towns
filtered_metrics = metrics_df[metrics_df['Town'].isin(selected_towns)]

# Show filter summary
st.sidebar.markdown("---")
st.sidebar.markdown("**Active Filters:**")
st.sidebar.markdown(f"Years: {', '.join(map(str, selected_years))}")
st.sidebar.markdown(f"Seasons: {', '.join(selected_periods)}")
st.sidebar.markdown(f"Towns: {len(selected_towns)} selected")

# Tab 1: Dashboard content
with tab1:
    # Calculate all ranks for Overall Program Assessment (displayed at top)
    fox_metrics = metrics_df.loc['FOX']
    win_rank = (metrics_df['Win %'] >= fox_metrics['Win %']).sum()
    gd_rank = (metrics_df['Goal Diff'] >= fox_metrics['Goal Diff']).sum()
    gf_rank = (metrics_df['Goals For'] >= fox_metrics['Goals For']).sum()
    ga_rank = (metrics_df['Goals Against'] <= fox_metrics['Goals Against']).sum()
    part_rank = (metrics_df['Participation Rate'] >= fox_metrics['Participation Rate']).sum()
    ret_rank = (metrics_df['Retention %'] >= fox_metrics['Retention %']).sum()
    growth_rank = (metrics_df['Growth %'] >= fox_metrics['Growth %']).sum()
    gb_rank = (metrics_df['Gender Balance'].apply(lambda x: abs(x - 50)) <= abs(fox_metrics['Gender Balance'] - 50)).sum()
    div_rank = (metrics_df['Avg Division'] <= fox_metrics['Avg Division']).sum()
    
    # Calculate letter grades for the 3 main categories
    competitive_avg_rank = (win_rank + gd_rank + gf_rank + ga_rank) / 4
    participation_avg_rank = (part_rank + ret_rank + growth_rank) / 3
    balance_avg_rank = (gb_rank + div_rank) / 2
    
    def get_letter_grade(avg_rank):
        if avg_rank <= 1.5:
            return "A"
        elif avg_rank <= 2.5:
            return "B"
        elif avg_rank <= 4.0:
            return "C"
        elif avg_rank <= 5.5:
            return "D"
        else:
            return "F"
    
    def get_grade_color(grade):
        if grade == "A":
            return "#28a745"  # Green
        elif grade == "B":
            return "#5cb85c"  # Light green
        elif grade == "C":
            return "#ffc107"  # Yellow/Gold
        elif grade == "D":
            return "#fd7e14"  # Orange
        else:
            return "#dc3545"  # Red
    
    competitive_grade = get_letter_grade(competitive_avg_rank)
    participation_grade = get_letter_grade(participation_avg_rank)
    balance_grade = get_letter_grade(balance_avg_rank)
    
    # Display Overall Program Assessment at the top
    st.markdown("---")
    st.markdown("<h2 style='margin-bottom: 10px;'>📊 Overall Program Assessment</h2>", unsafe_allow_html=True)
    
    grade_col1, grade_col2, grade_col3 = st.columns(3)
    
    with grade_col1:
        color = get_grade_color(competitive_grade)
        st.markdown(f"""
        <div style='border: 3px solid {color}; padding: 10px; border-radius: 10px; text-align: center; background-color: rgba{tuple(list(bytes.fromhex(color[1:])) + [0.1])};'>
            <h4 style='margin: 0; margin-bottom: 3px;'>Competitive Performance</h4>
            <h1 style='margin: 0; color: {color}; font-size: 64px; font-weight: bold;'>{competitive_grade}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with grade_col2:
        color = get_grade_color(participation_grade)
        st.markdown(f"""
        <div style='border: 3px solid {color}; padding: 10px; border-radius: 10px; text-align: center; background-color: rgba{tuple(list(bytes.fromhex(color[1:])) + [0.1])};'>
            <h4 style='margin: 0; margin-bottom: 3px;'>Participation & Growth</h4>
            <h1 style='margin: 0; color: {color}; font-size: 64px; font-weight: bold;'>{participation_grade}</h1>
        </div>
        """, unsafe_allow_html=True)

    with grade_col3:
        color = get_grade_color(balance_grade)
        st.markdown(f"""
        <div style='border: 3px solid {color}; padding: 10px; border-radius: 10px; text-align: center; background-color: rgba{tuple(list(bytes.fromhex(color[1:])) + [0.1])};'>
            <h4 style='margin: 0; margin-bottom: 3px;'>Program Balance</h4>
            <h1 style='margin: 0; color: {color}; font-size: 64px; font-weight: bold;'>{balance_grade}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Color coding function
    def get_bar_colors(df, town_col='Town'):
        colors = []
        fox_rank = df[df[town_col] == 'Foxborough']['rank'].values[0] if 'Foxborough' in df[town_col].values else None
    
        for _, row in df.iterrows():
            if row[town_col] == 'Foxborough':
                if fox_rank <= 2:
                    colors.append('green')  # Top 2
                elif fox_rank >= len(df) - 2:
                    colors.append('red')  # Bottom 3
                else:
                    colors.append('gold')  # Middle
            else:
                colors.append('lightgray')
        return colors
    
    # Main metrics overview - organized by the three key questions
    st.markdown("<h3 style='margin-bottom: 10px; margin-top: 5px;'>📊 Key Performance Indicators - Foxborough</h3>", unsafe_allow_html=True)
    
    # Calculate metrics and comparisons
    fox_metrics = metrics_df.loc['FOX']
    numeric_cols = ['Participation Rate', 'Win %', 'Goal Diff', 'Retention %',
                    'Goals For', 'Goals Against', 'Avg Division', 'Gender Balance',
                    'Growth %']
    avg_metrics = metrics_df.drop('FOX')[numeric_cols].mean()
    
    # Helper function to get rank color
    def get_rank_color(rank):
        if rank <= 2:
            return "green"
        elif rank <= 5:
            return "orange"
        else:
            return "red"
    
    # Competitive Performance Section
    st.markdown("<h4 style='margin-bottom: 5px;'>🏆 Competitive Performance</h4>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        win_pct = fox_metrics['Win %']
        fox_rank = (metrics_df['Win %'] >= win_pct).sum()
        rank_color = get_rank_color(fox_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Win % <span style='color: {rank_color};'>#{fox_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{win_pct:.1f}%</h2>
        </div>""", unsafe_allow_html=True)
    
    with col2:
        gd = fox_metrics['Goal Diff']
        gd_rank = (metrics_df['Goal Diff'] >= gd).sum()
        rank_color = get_rank_color(gd_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Goal Diff <span style='color: {rank_color};'>#{gd_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{gd:+.1f}</h2>
        </div>""", unsafe_allow_html=True)
    
    with col3:
        gf = fox_metrics['Goals For']
        gf_rank = (metrics_df['Goals For'] >= gf).sum()
        rank_color = get_rank_color(gf_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Goals For <span style='color: {rank_color};'>#{gf_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{gf:.1f}</h2>
        </div>""", unsafe_allow_html=True)
    
    with col4:
        ga = fox_metrics['Goals Against']
        ga_rank = (metrics_df['Goals Against'] <= ga).sum()  # Lower is better
        rank_color = get_rank_color(ga_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Goals Against <span style='color: {rank_color};'>#{ga_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{ga:.1f}</h2>
        </div>""", unsafe_allow_html=True)
    
    # Participation & Growth Section
    st.markdown("<h4 style='margin-top: 10px; margin-bottom: 5px;'>👥 Participation & Growth</h4>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        part_rate = fox_metrics['Participation Rate']
        part_rank = (metrics_df['Participation Rate'] >= part_rate).sum()
        rank_color = get_rank_color(part_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Participation <span style='color: {rank_color};'>#{part_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{part_rate:.1f}</h2>
        </div>""", unsafe_allow_html=True)
    
    with col2:
        retention = fox_metrics['Retention %']
        ret_rank = (metrics_df['Retention %'] >= retention).sum()
        rank_color = get_rank_color(ret_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Retention <span style='color: {rank_color};'>#{ret_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{retention:.1f}%</h2>
        </div>""", unsafe_allow_html=True)
    
    with col3:
        growth = fox_metrics['Growth %']
        growth_rank = (metrics_df['Growth %'] >= growth).sum()
        rank_color = get_rank_color(growth_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Growth <span style='color: {rank_color};'>#{growth_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{growth:+.1f}%</h2>
        </div>""", unsafe_allow_html=True)
    
    with col4:
        enrollment = fox_metrics['Enrollment']
        enroll_rank = (metrics_df['Enrollment'] >= enrollment).sum()
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>School Enrollment <span style='color: gray;'>#{enroll_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{int(enrollment)}</h2>
        </div>""", unsafe_allow_html=True)
    
    # Program Balance Section
    st.markdown("<h4 style='margin-top: 10px; margin-bottom: 5px;'>⚖️ Program Balance</h4>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        gb = fox_metrics['Gender Balance']
        def distance_from_50(val):
            return abs(val - 50)
        fox_dist = distance_from_50(gb)
        gb_rank = (metrics_df['Gender Balance'].apply(distance_from_50) <= fox_dist).sum()
        rank_color = get_rank_color(gb_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>% Girls <span style='color: {rank_color};'>#{gb_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{gb:.1f}%</h2>
        </div>""", unsafe_allow_html=True)
    
    with col2:
        div = fox_metrics['Avg Division']
        div_rank = (metrics_df['Avg Division'] <= div).sum()  # Lower is better
        rank_color = get_rank_color(div_rank)
        st.markdown(f"""<div style='border: 1px solid lightgray; padding: 8px; border-radius: 5px;'>
        <p style='margin-bottom: 0px;'><strong>Avg Division <span style='color: {rank_color};'>#{div_rank}</span></strong></p>
        <h2 style='margin-top: 0; margin-bottom: 0;'>{div:.1f}</h2>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # SECTION 1: Are kids participating and having fun?
    st.markdown("<h2 style='margin-top: 10px; margin-bottom: 10px;'>🎉 Are Kids Participating and Having Fun?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Participation Rate")
    
        part_sorted = filtered_metrics.sort_values('Participation Rate', ascending=False).reset_index(drop=True)
        part_sorted['rank'] = range(1, len(part_sorted) + 1)
        part_sorted['colors'] = get_bar_colors(part_sorted)
    
        fig_part = go.Figure()
        fig_part.add_trace(go.Bar(
            x=part_sorted['Town'],
            y=part_sorted['Participation Rate'],
            marker_color=part_sorted['colors'],
            text=part_sorted['Participation Rate'],
            textposition='outside',
            texttemplate='%{text:.1f}',
            hovertemplate='%{x}<br>%{y:.1f}<extra></extra>',
            cliponaxis=False
        ))
    
        fig_part.update_layout(
            height=350,
            showlegend=False,
            yaxis=dict(title='Teams per 100 Students'),
            xaxis=dict(title=''),
            margin=dict(t=30, b=30, l=40, r=40),
            font=dict(size=14)
        )
        st.plotly_chart(fig_part, use_container_width=True)
    
    with col2:
        st.subheader("🔄 Spring Retention Rate")
    
        ret_sorted = filtered_metrics.sort_values('Retention %', ascending=False).reset_index(drop=True)
        ret_sorted['rank'] = range(1, len(ret_sorted) + 1)
        ret_sorted['colors'] = get_bar_colors(ret_sorted)
    
        fig_ret = go.Figure()
        fig_ret.add_trace(go.Bar(
            x=ret_sorted['Town'],
            y=ret_sorted['Retention %'],
            marker_color=ret_sorted['colors'],
            text=ret_sorted['Retention %'],
            textposition='outside',
            texttemplate='%{text:.1f}%',
            hovertemplate='%{x}<br>%{y:.1f}%<extra></extra>',
            cliponaxis=False
        ))
    
        fig_ret.update_layout(
            height=350,
            showlegend=False,
            yaxis=dict(title='Retention %'),
            xaxis=dict(title=''),
            margin=dict(t=30, b=30, l=40, r=40),
            font=dict(size=14)
        )
        st.plotly_chart(fig_ret, use_container_width=True)
    
    # Growth chart spanning full width
    st.subheader("📊 Growth Rate (2021 → 2025)")
    
    growth_sorted = filtered_metrics.sort_values('Growth %', ascending=False).reset_index(drop=True)
    growth_sorted['rank'] = range(1, len(growth_sorted) + 1)
    growth_sorted['colors'] = get_bar_colors(growth_sorted)
    
    fig_growth = go.Figure()
    fig_growth.add_trace(go.Bar(
        x=growth_sorted['Town'],
        y=growth_sorted['Growth %'],
        marker_color=growth_sorted['colors'],
        text=[f"{val:+.1f}%" for val in growth_sorted['Growth %']],
        textposition='outside',
        hovertemplate='%{x}<br>%{y:+.1f}%<extra></extra>',
        cliponaxis=False
    ))
    
    fig_growth.update_layout(
        height=350,
        showlegend=False,
        yaxis=dict(title='Growth %'),
        xaxis=dict(title=''),
        margin=dict(t=30, b=30, l=40, r=40),
        font=dict(size=14)
    )
    fig_growth.add_hline(y=0, line_dash="dash", line_color="black")
    st.plotly_chart(fig_growth, use_container_width=True)
    
    st.markdown("---")
    
    # SECTION 2: Is the program competitive? Are kids learning soccer?
    st.markdown("<h2 style='margin-top: 10px; margin-bottom: 10px;'>🏆 Is the Program Competitive? Are Kids Learning Soccer?</h2>", unsafe_allow_html=True)
    
    # Win Percentage - full width
    st.subheader("🏅 Win Percentage by Town")
    
    win_sorted = filtered_metrics.sort_values('Win %', ascending=False).reset_index(drop=True)
    win_sorted['rank'] = range(1, len(win_sorted) + 1)
    win_sorted['colors'] = get_bar_colors(win_sorted)
    
    fig_win = go.Figure()
    fig_win.add_trace(go.Bar(
        x=win_sorted['Town'],
        y=win_sorted['Win %'],
        marker_color=win_sorted['colors'],
        text=win_sorted['Win %'],
        textposition='outside',
        texttemplate='%{text:.1f}%',
        hovertemplate='%{x}<br>%{y:.1f}%<extra></extra>',
        cliponaxis=False
    ))
    
    fig_win.update_layout(
        height=350,
        showlegend=False,
        yaxis=dict(range=[25, 70], title='Win %'),
        xaxis=dict(title=''),
        margin=dict(t=30, b=30, l=40, r=40),
        font=dict(size=14)
    )
    fig_win.add_hline(y=50, line_dash="dash", line_color="gray", annotation_text="50% (Break Even)")
    st.plotly_chart(fig_win, use_container_width=True)
    
    # Three columns for competitive metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("⚡ Goal Differential")
    
        gd_sorted = filtered_metrics.sort_values('Goal Diff', ascending=False).reset_index(drop=True)
        gd_sorted['rank'] = range(1, len(gd_sorted) + 1)
        gd_sorted['colors'] = get_bar_colors(gd_sorted)
    
        fig_gd = go.Figure()
        fig_gd.add_trace(go.Bar(
            x=gd_sorted['Town'],
            y=gd_sorted['Goal Diff'],
            marker_color=gd_sorted['colors'],
            text=[f"{val:+.1f}" for val in gd_sorted['Goal Diff']],
            textposition='outside',
            hovertemplate='%{x}<br>%{y:+.1f}<extra></extra>',
            cliponaxis=False
        ))
    
        fig_gd.update_layout(
            height=350,
            showlegend=False,
            yaxis=dict(title='Goal Diff'),
            xaxis=dict(title=''),
            margin=dict(t=30, b=30, l=40, r=40),
            font=dict(size=14)
        )
        fig_gd.add_hline(y=0, line_dash="dash", line_color="black")
        st.plotly_chart(fig_gd, use_container_width=True)
    
    with col2:
        st.subheader("⚽ Goals For")
    
        gf_sorted = filtered_metrics.sort_values('Goals For', ascending=False).reset_index(drop=True)
        gf_sorted['rank'] = range(1, len(gf_sorted) + 1)
        gf_sorted['colors'] = get_bar_colors(gf_sorted)
    
        fig_gf = go.Figure()
        fig_gf.add_trace(go.Bar(
            x=gf_sorted['Town'],
            y=gf_sorted['Goals For'],
            marker_color=gf_sorted['colors'],
            text=gf_sorted['Goals For'],
            textposition='outside',
            texttemplate='%{text:.1f}',
            hovertemplate='%{x}<br>%{y:.1f}<extra></extra>',
            cliponaxis=False
        ))
    
        fig_gf.update_layout(
            height=350,
            showlegend=False,
            yaxis=dict(title='Goals For'),
            xaxis=dict(title=''),
            margin=dict(t=30, b=30, l=40, r=40),
            font=dict(size=14)
        )
        st.plotly_chart(fig_gf, use_container_width=True)
    
    with col3:
        st.subheader("🛡️ Goals Against")
    
        # For goals against, LOWER is BETTER
        ga_sorted = filtered_metrics.sort_values('Goals Against', ascending=True).reset_index(drop=True)
        ga_sorted['rank'] = range(1, len(ga_sorted) + 1)
        ga_sorted['colors'] = get_bar_colors(ga_sorted)
    
        fig_ga = go.Figure()
        fig_ga.add_trace(go.Bar(
            x=ga_sorted['Town'],
            y=ga_sorted['Goals Against'],
            marker_color=ga_sorted['colors'],
            text=ga_sorted['Goals Against'],
            textposition='outside',
            texttemplate='%{text:.1f}',
            hovertemplate='%{x}<br>%{y:.1f}<extra></extra>',
            cliponaxis=False
        ))
    
        fig_ga.update_layout(
            height=350,
            showlegend=False,
            yaxis=dict(title='Goals Against'),
            xaxis=dict(title=''),
            margin=dict(t=30, b=30, l=40, r=40),
            font=dict(size=14)
        )
        st.plotly_chart(fig_ga, use_container_width=True)
    
    st.markdown("---")
    
    # SECTION 3: Other Metrics (Gender, Division)
    st.markdown("<h2 style='margin-top: 10px; margin-bottom: 10px;'>📋 Other Program Metrics</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚖️ Gender Balance (% Girls)")
    
        # For gender balance, rank by closeness to 50%
        gb_sorted = filtered_metrics.copy()
        gb_sorted['distance_from_50'] = abs(gb_sorted['Gender Balance'] - 50)
        gb_sorted = gb_sorted.sort_values('distance_from_50', ascending=True).reset_index(drop=True)
        gb_sorted['rank'] = range(1, len(gb_sorted) + 1)
        gb_sorted['colors'] = get_bar_colors(gb_sorted)
    
        fig_gb = go.Figure()
        fig_gb.add_trace(go.Bar(
            x=gb_sorted['Town'],
            y=gb_sorted['Gender Balance'],
            marker_color=gb_sorted['colors'],
            text=gb_sorted['Gender Balance'],
            textposition='outside',
            texttemplate='%{text:.1f}%',
            hovertemplate='%{x}<br>%{y:.1f}%<extra></extra>',
            cliponaxis=False
        ))
    
        fig_gb.update_layout(
            height=350,
            showlegend=False,
            yaxis=dict(range=[0, 100], title='% Girls (50% = Perfect)'),
            xaxis=dict(title=''),
            margin=dict(t=30, b=30, l=40, r=40),
            font=dict(size=14)
        )
        fig_gb.add_hline(y=50, line_dash="dash", line_color="gray", annotation_text="50% (Perfect Balance)")
        st.plotly_chart(fig_gb, use_container_width=True)
    
    with col2:
        st.subheader("🏅 Average Division Level")
    
        # For division, LOWER is BETTER (1 is highest division)
        div_sorted = filtered_metrics.sort_values('Avg Division', ascending=True).reset_index(drop=True)
        div_sorted['rank'] = range(1, len(div_sorted) + 1)
        div_sorted['colors'] = get_bar_colors(div_sorted)
    
        fig_div = go.Figure()
        fig_div.add_trace(go.Bar(
            x=div_sorted['Town'],
            y=div_sorted['Avg Division'],
            marker_color=div_sorted['colors'],
            text=div_sorted['Avg Division'],
            textposition='outside',
            texttemplate='%{text:.1f}',
            hovertemplate='%{x}<br>%{y:.1f}<extra></extra>',
            cliponaxis=False
        ))
    
        fig_div.update_layout(
            height=350,
            showlegend=False,
            yaxis=dict(title='Division (1=Highest, 4=Lowest)'),
            xaxis=dict(title=''),
            margin=dict(t=30, b=30, l=40, r=40),
            font=dict(size=14)
        )
        st.plotly_chart(fig_div, use_container_width=True)
    
    st.markdown("---")
    
    # Multi-metric time series
    st.markdown("<h2 style='margin-top: 10px; margin-bottom: 10px;'>🎯 Performance Trends Over Time</h2>", unsafe_allow_html=True)
    st.caption("Foxborough vs League Average (7 Comparable Towns)")
    
    # Calculate metrics by year
    years = sorted(filtered_metrics_data['season_year'].unique())
    
    # Data structure for time series - 6 most relevant metrics
    time_series_data = {
        'Win %': {'Fox': [], 'Avg': []},
        'Goal Diff': {'Fox': [], 'Avg': []},
        'Goals For': {'Fox': [], 'Avg': []},
        'Goals Against': {'Fox': [], 'Avg': []},
        'Participation Rate': {'Fox': [], 'Avg': []},
        'Retention %': {'Fox': [], 'Avg': []}
        }
    
    for year in years:
        year_data = filtered_metrics_data[filtered_metrics_data['season_year'] == year]
    
        # Calculate Foxborough metrics for this year
        fox_year = year_data[year_data['town_code'] == 'FOX']
        if len(fox_year) > 0:
            total_games = fox_year['wins'].sum() + fox_year['losses'].sum() + fox_year['ties'].sum()
            fox_win_pct = (fox_year['wins'].sum() + 0.5 * fox_year['ties'].sum()) / total_games * 100 if total_games > 0 else 0
            fox_gd = fox_year['goal_differential'].sum() / len(fox_year)
            fox_gf = fox_year['goals_for'].sum() / len(fox_year)
            fox_ga = fox_year['goals_against'].sum() / len(fox_year)
    
            # Participation rate for this year
            fox_enrollment = enrollment_map.get('FOX', 2485)
            fox_part = (len(fox_year) / 10) / fox_enrollment * 100
    
            # Retention for this year (Fall to Spring)
            fox_fall = len(year_data[(year_data['town_code'] == 'FOX') & (year_data['season_period'] == 'Fall')])
            fox_spring = len(year_data[(year_data['town_code'] == 'FOX') & (year_data['season_period'] == 'Spring')])
            fox_ret = (fox_spring / fox_fall * 100) if fox_fall > 0 else None
        else:
            fox_win_pct = fox_gd = fox_gf = fox_ga = fox_part = fox_ret = None
    
        # Calculate league average for this year (excluding Foxborough)
        other_year = year_data[year_data['town_code'] != 'FOX']
        if len(other_year) > 0:
            avg_win_pct = 0
            avg_gd = 0
            avg_gf = 0
            avg_ga = 0
            avg_part = 0
            avg_ret = 0
            town_count = 0
    
            for town in [t for t in towns if t != 'FOX']:
                town_year = other_year[other_year['town_code'] == town]
                if len(town_year) > 0:
                    total_games = town_year['wins'].sum() + town_year['losses'].sum() + town_year['ties'].sum()
                    if total_games > 0:
                        avg_win_pct += (town_year['wins'].sum() + 0.5 * town_year['ties'].sum()) / total_games * 100
                        avg_gd += town_year['goal_differential'].sum() / len(town_year)
                        avg_gf += town_year['goals_for'].sum() / len(town_year)
                        avg_ga += town_year['goals_against'].sum() / len(town_year)
    
                        # Participation and retention
                        town_enrollment = enrollment_map.get(town, 2500)
                        avg_part += (len(town_year) / 10) / town_enrollment * 100
    
                        town_fall = len(year_data[(year_data['town_code'] == town) & (year_data['season_period'] == 'Fall')])
                        town_spring = len(year_data[(year_data['town_code'] == town) & (year_data['season_period'] == 'Spring')])
                        if town_fall > 0:
                            avg_ret += (town_spring / town_fall * 100)
    
                        town_count += 1
    
            if town_count > 0:
                avg_win_pct /= town_count
                avg_gd /= town_count
                avg_gf /= town_count
                avg_ga /= town_count
                avg_part /= town_count
                avg_ret /= town_count
            else:
                avg_win_pct = avg_gd = avg_gf = avg_ga = avg_part = avg_ret = None
        else:
            avg_win_pct = avg_gd = avg_gf = avg_ga = avg_part = avg_ret = None
    
        time_series_data['Win %']['Fox'].append(fox_win_pct)
        time_series_data['Win %']['Avg'].append(avg_win_pct)
        time_series_data['Goal Diff']['Fox'].append(fox_gd)
        time_series_data['Goal Diff']['Avg'].append(avg_gd)
        time_series_data['Goals For']['Fox'].append(fox_gf)
        time_series_data['Goals For']['Avg'].append(avg_gf)
        time_series_data['Goals Against']['Fox'].append(fox_ga)
        time_series_data['Goals Against']['Avg'].append(avg_ga)
        time_series_data['Participation Rate']['Fox'].append(fox_part)
        time_series_data['Participation Rate']['Avg'].append(avg_part)
        time_series_data['Retention %']['Fox'].append(fox_ret)
        time_series_data['Retention %']['Avg'].append(avg_ret)
    
    # Create subplots for 6 metrics
    from plotly.subplots import make_subplots
    
    fig_time = make_subplots(
        rows=3, cols=2,
        subplot_titles=('Win %', 'Goal Differential', 'Goals For', 'Goals Against (Lower is Better)',
                        'Participation Rate', 'Spring Retention Rate'),
        vertical_spacing=0.10,
        horizontal_spacing=0.12
    )
    
    # Win %
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Win %']['Fox'],
                                   name='Foxborough', mode='lines+markers',
                                   line=dict(color='rgba(155, 89, 230, 0.9)', width=3),
                                   showlegend=True), row=1, col=1)
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Win %']['Avg'],
                                   name='League Avg', mode='lines+markers',
                                   line=dict(color='lightgray', width=2, dash='dash'),
                                   showlegend=True), row=1, col=1)
    
    # Goal Diff
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Goal Diff']['Fox'],
                                   name='Foxborough', mode='lines+markers',
                                   line=dict(color='rgba(155, 89, 230, 0.9)', width=3),
                                   showlegend=False), row=1, col=2)
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Goal Diff']['Avg'],
                                   name='League Avg', mode='lines+markers',
                                   line=dict(color='lightgray', width=2, dash='dash'),
                                   showlegend=False), row=1, col=2)
    
    # Goals For
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Goals For']['Fox'],
                                   name='Foxborough', mode='lines+markers',
                                   line=dict(color='rgba(155, 89, 230, 0.9)', width=3),
                                   showlegend=False), row=2, col=1)
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Goals For']['Avg'],
                                   name='League Avg', mode='lines+markers',
                                   line=dict(color='lightgray', width=2, dash='dash'),
                                   showlegend=False), row=2, col=1)
    
    # Goals Against (inverted - lower is better)
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Goals Against']['Fox'],
                                   name='Foxborough', mode='lines+markers',
                                   line=dict(color='rgba(155, 89, 230, 0.9)', width=3),
                                   showlegend=False), row=2, col=2)
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Goals Against']['Avg'],
                                   name='League Avg', mode='lines+markers',
                                   line=dict(color='lightgray', width=2, dash='dash'),
                                   showlegend=False), row=2, col=2)
    
    # Participation Rate
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Participation Rate']['Fox'],
                                   name='Foxborough', mode='lines+markers',
                                   line=dict(color='rgba(155, 89, 230, 0.9)', width=3),
                                   showlegend=False), row=3, col=1)
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Participation Rate']['Avg'],
                                   name='League Avg', mode='lines+markers',
                                   line=dict(color='lightgray', width=2, dash='dash'),
                                   showlegend=False), row=3, col=1)
    
    # Retention %
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Retention %']['Fox'],
                                   name='Foxborough', mode='lines+markers',
                                   line=dict(color='rgba(155, 89, 230, 0.9)', width=3),
                                   showlegend=False), row=3, col=2)
    fig_time.add_trace(go.Scatter(x=years, y=time_series_data['Retention %']['Avg'],
                                   name='League Avg', mode='lines+markers',
                                   line=dict(color='lightgray', width=2, dash='dash'),
                                   showlegend=False), row=3, col=2)
    
    fig_time.update_layout(
        height=800,
        margin=dict(t=40, b=10, l=10, r=10),
        font=dict(size=11),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    
    # Don't invert Goals Against axis - the subtitle explains lower is better
    # fig_time.update_yaxes(autorange="reversed", row=2, col=2)

    # Show only integer year labels (keep all data points, just control tick labels)
    fig_time.update_xaxes(
        title_text="Year",
        row=3,
        col=1,
        tickmode='array',
        tickvals=[2021, 2022, 2023, 2024, 2025],
        ticktext=['2021', '2022', '2023', '2024', '2025']
    )
    fig_time.update_xaxes(
        title_text="Year",
        row=3,
        col=2,
        tickmode='array',
        tickvals=[2021, 2022, 2023, 2024, 2025],
        ticktext=['2021', '2022', '2023', '2024', '2025']
    )
    # Apply to all other x-axes
    fig_time.update_xaxes(
        tickmode='array',
        tickvals=[2021, 2022, 2023, 2024, 2025],
        ticktext=['2021', '2022', '2023', '2024', '2025']
    )
    
    st.plotly_chart(fig_time, use_container_width=True)
    
    st.markdown("---")
    
    # Data table with heatmap styling
    st.markdown("<h2 style='margin-top: 10px; margin-bottom: 10px;'>📋 Complete Metrics Table</h2>", unsafe_allow_html=True)
    
    # Create a copy for display with proper formatting
    display_df = filtered_metrics.copy()
    # Remove any blank rows
    display_df = display_df.dropna(how='all')
    
    # Apply gradient styling (gentle heatmap based on average)
    def highlight_vs_avg(s, col_name):
        """Apply color gradient based on comparison to average"""
        avg = s.mean()
        styles = []
    
        for val in s:
            if col_name in ['Win %', 'Goal Diff', 'Participation Rate', 'Retention %',
                            'Goals For', 'Growth %']:
                # Higher is better - green if above avg, red if below
                if val > avg:
                    diff = (val - avg) / (s.max() - avg) if s.max() > avg else 0
                    intensity = min(diff * 0.5, 0.5)  # Cap at 0.5
                    color = f'background-color: rgba(0, 200, 0, {intensity})'
                elif val < avg:
                    diff = (avg - val) / (avg - s.min()) if avg > s.min() else 0
                    intensity = min(diff * 0.5, 0.5)  # Cap at 0.5
                    color = f'background-color: rgba(255, 100, 100, {intensity})'
                else:
                    color = ''
            elif col_name in ['Goals Against', 'Avg Division']:
                # Lower is better - green if below avg, red if above
                if val < avg:
                    diff = (avg - val) / (avg - s.min()) if avg > s.min() else 0
                    intensity = min(diff * 0.5, 0.5)
                    color = f'background-color: rgba(0, 200, 0, {intensity})'
                elif val > avg:
                    diff = (val - avg) / (s.max() - avg) if s.max() > avg else 0
                    intensity = min(diff * 0.5, 0.5)
                    color = f'background-color: rgba(255, 100, 100, {intensity})'
                else:
                    color = ''
            elif col_name == 'Gender Balance':
                # Closeness to 50 is better
                dist_from_50 = abs(val - 50)
                avg_dist = abs(s - 50).mean()
                if dist_from_50 < avg_dist:
                    diff = (avg_dist - dist_from_50) / avg_dist if avg_dist > 0 else 0
                    intensity = min(diff * 0.5, 0.5)
                    color = f'background-color: rgba(0, 200, 0, {intensity})'
                elif dist_from_50 > avg_dist:
                    diff = (dist_from_50 - avg_dist) / (abs(s - 50).max() - avg_dist) if abs(s - 50).max() > avg_dist else 0
                    intensity = min(diff * 0.5, 0.5)
                    color = f'background-color: rgba(255, 100, 100, {intensity})'
                else:
                    color = ''
            else:
                color = ''
            styles.append(color)
    
        return styles
    
    # Apply styling and formatting
    styled_df = display_df.style.format({
        'Win %': '{:.1f}',
        'Goal Diff': '{:+.1f}',
        'Participation Rate': '{:.1f}',
        'Retention %': '{:.1f}',
        'Goals For': '{:.1f}',
        'Goals Against': '{:.1f}',
        'Avg Division': '{:.1f}',
        'Gender Balance': '{:.1f}',
        'Growth %': '{:+.1f}',
        'Enrollment': '{:.0f}'
    })
    
    # Apply heat map to each numeric column
    for col in display_df.select_dtypes(include=['float64', 'int64']).columns:
        if col != 'Enrollment':  # Skip enrollment
            styled_df = styled_df.apply(highlight_vs_avg, col_name=col, subset=[col])
    
    st.dataframe(styled_df, use_container_width=True, height=350)
    
    st.markdown("---")
    
    # Key findings with detailed analysis
    st.markdown("<h2 style='margin-top: 10px; margin-bottom: 10px;'>🔍 Key Findings & Recommendations</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: grey; font-size: 0.9em;'>(AI Generated)</p>", unsafe_allow_html=True)
    
    fox_metrics = metrics_df.loc['FOX']
    # Calculate average excluding FOX and only for numeric columns
    numeric_cols = ['Participation Rate', 'Win %', 'Goal Diff', 'Retention %',
                    'Goals For', 'Goals Against', 'Avg Division', 'Gender Balance',
                    'Growth %', 'Enrollment']
    avg_metrics = metrics_df.drop('FOX')[numeric_cols].mean()
    
    # Calculate ranks for context
    win_rank = (metrics_df['Win %'] >= fox_metrics['Win %']).sum()
    gd_rank = (metrics_df['Goal Diff'] >= fox_metrics['Goal Diff']).sum()
    part_rank = (metrics_df['Participation Rate'] >= fox_metrics['Participation Rate']).sum()
    ret_rank = (metrics_df['Retention %'] >= fox_metrics['Retention %']).sum()
    growth_rank = (metrics_df['Growth %'] >= fox_metrics['Growth %']).sum()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 style='margin-top: 5px; margin-bottom: 10px;'>⚠️ Areas Needing Attention</h3>", unsafe_allow_html=True)
    
        concerns = []
    
        # Competitive Performance Analysis
        if fox_metrics['Win %'] < 50:
            rank_txt = f"ranks #{win_rank} of 8 towns"
            diff = 50 - fox_metrics['Win %']
            concerns.append({
                'title': '🏆 Win Percentage Below 50%',
                'detail': f"Foxborough's {fox_metrics['Win %']:.1f}% win rate {rank_txt}. Teams are losing more than winning by {diff:.1f} percentage points. This suggests competitive struggles that may impact player confidence and retention."
            })
        elif fox_metrics['Win %'] < avg_metrics['Win %']:
            concerns.append({
                'title': '🏆 Win % Below Average',
                'detail': f"At {fox_metrics['Win %']:.1f}%, Foxborough is {avg_metrics['Win %'] - fox_metrics['Win %']:.1f}% below the league average and ranks #{win_rank} of 8. Consider reviewing coaching strategies and player development programs."
            })
    
        # Goal Differential Analysis
        if fox_metrics['Goal Diff'] < -2:
            concerns.append({
                'title': '⚽ Significant Negative Goal Differential',
                'detail': f"Teams are being outscored by {abs(fox_metrics['Goal Diff']):.1f} goals per season on average (rank #{gd_rank}). This indicates both offensive and defensive challenges. Focus on fundamental skills training and defensive organization."
            })
        elif fox_metrics['Goal Diff'] < 0:
            concerns.append({
                'title': '⚽ Negative Goal Differential',
                'detail': f"Teams average {fox_metrics['Goal Diff']:+.1f} goal differential per season. While modest, addressing this could improve competitive outcomes. Review both offensive creation and defensive positioning."
            })
    
        # Retention Analysis
        if fox_metrics['Retention %'] < 70:
            concerns.append({
                'title': '🔄 Low Spring Retention',
                'detail': f"Only {fox_metrics['Retention %']:.1f}% of Fall teams return in Spring (rank #{ret_rank}). This suggests families may be choosing other activities or experiencing dissatisfaction. Consider surveying families about barriers to participation."
            })
        elif fox_metrics['Retention %'] < avg_metrics['Retention %']:
            diff = avg_metrics['Retention %'] - fox_metrics['Retention %']
            concerns.append({
                'title': '🔄 Below-Average Retention',
                'detail': f"Spring retention of {fox_metrics['Retention %']:.1f}% is {diff:.1f}% below average. Understanding why families leave between seasons could help improve program satisfaction."
            })
    
        # Participation Analysis
        if fox_metrics['Participation Rate'] < avg_metrics['Participation Rate']:
            diff = avg_metrics['Participation Rate'] - fox_metrics['Participation Rate']
            concerns.append({
                'title': '📈 Below-Average Participation',
                'detail': f"At {fox_metrics['Participation Rate']:.1f} teams per 100 students, Foxborough trails the average by {diff:.1f}. Marketing efforts and community outreach could help increase awareness and enrollment."
            })
    
        # Growth Analysis
        if fox_metrics['Growth %'] < -10:
            concerns.append({
                'title': '📉 Significant Program Decline',
                'detail': f"Program has shrunk by {abs(fox_metrics['Growth %']):.1f}% since 2021 (rank #{growth_rank}). This declining trend requires immediate attention. Consider focus groups with current and former families to understand root causes."
            })
        elif fox_metrics['Growth %'] < 0:
            concerns.append({
                'title': '📉 Program Decline',
                'detail': f"Program decreased by {abs(fox_metrics['Growth %']):.1f}% from 2021-2025. Reversing this trend should be a priority. Analyze competitor programs and consider new initiatives to attract families."
            })
    
        if concerns:
            for concern in concerns:
                with st.expander(concern['title'], expanded=True):
                    st.markdown(concern['detail'])
        else:
            st.success("✅ No major concerns identified. Program is performing well across key metrics.")
    
    with col2:
        st.markdown("<h3 style='margin-top: 5px; margin-bottom: 10px;'>✅ Strengths & Positive Indicators</h3>", unsafe_allow_html=True)
    
        strengths = []
    
        # Gender Balance Strength
        gender_dist = abs(fox_metrics['Gender Balance'] - 50)
        if gender_dist <= 5:
            strengths.append({
                'title': '⚖️ Excellent Gender Balance',
                'detail': f"With {fox_metrics['Gender Balance']:.1f}% girls, Foxborough has nearly perfect 50/50 gender balance. This diversity creates a welcoming environment for all players and demonstrates broad community appeal."
            })
        elif gender_dist <= 10:
            strengths.append({
                'title': '⚖️ Good Gender Balance',
                'detail': f"At {fox_metrics['Gender Balance']:.1f}% girls, the program maintains healthy gender diversity. Continue promoting inclusivity to maintain this balance."
            })
    
        # Growth Strength
        if fox_metrics['Growth %'] > 10:
            strengths.append({
                'title': '📈 Strong Program Growth',
                'detail': f"Program grew by {fox_metrics['Growth %']:+.1f}% since 2021 (rank #{growth_rank}). This momentum indicates strong community interest and program satisfaction. Document what's working to sustain this trajectory."
            })
        elif fox_metrics['Growth %'] > 0:
            strengths.append({
                'title': '📈 Positive Growth Trend',
                'detail': f"Program expanded by {fox_metrics['Growth %']:+.1f}% from 2021-2025. Modest but positive growth shows program stability. Build on this foundation to accelerate growth."
            })
    
        # Participation Strength
        if fox_metrics['Participation Rate'] > avg_metrics['Participation Rate']:
            diff = fox_metrics['Participation Rate'] - avg_metrics['Participation Rate']
            strengths.append({
                'title': '📈 Above-Average Participation',
                'detail': f"At {fox_metrics['Participation Rate']:.1f} teams per 100 students (rank #{part_rank}), Foxborough exceeds the average by {diff:.1f}. Strong community engagement with soccer demonstrates effective outreach and program appeal."
            })
    
        # Win % Strength
        if fox_metrics['Win %'] >= 55:
            strengths.append({
                'title': '🏆 Strong Competitive Performance',
                'detail': f"Teams win {fox_metrics['Win %']:.1f}% of games (rank #{win_rank}), well above break-even. Competitive success enhances player confidence and program reputation. Share coaching best practices across all teams."
            })
        elif fox_metrics['Win %'] >= 50:
            strengths.append({
                'title': '🏆 Competitive Performance',
                'detail': f"With a {fox_metrics['Win %']:.1f}% win rate, teams are winning more than losing. Maintaining competitiveness helps retain players and attract new families."
            })
    
        # Retention Strength
        if fox_metrics['Retention %'] >= 90:
            strengths.append({
                'title': '🔄 Excellent Retention',
                'detail': f"With {fox_metrics['Retention %']:.1f}% Spring retention (rank #{ret_rank}), nearly all Fall teams return. This loyalty indicates high program satisfaction and strong community commitment."
            })
        elif fox_metrics['Retention %'] >= avg_metrics['Retention %']:
            diff = fox_metrics['Retention %'] - avg_metrics['Retention %']
            strengths.append({
                'title': '🔄 Above-Average Retention',
                'detail': f"Spring retention of {fox_metrics['Retention %']:.1f}% exceeds average by {diff:.1f}%. Good retention suggests families are satisfied with the program experience."
            })
    
        # Goal Differential Strength
        if fox_metrics['Goal Diff'] > 5:
            strengths.append({
                'title': '⚽ Strong Offensive/Defensive Balance',
                'detail': f"Average goal differential of {fox_metrics['Goal Diff']:+.1f} per season (rank #{gd_rank}) shows teams are both scoring well and playing solid defense. Continue current coaching approaches."
            })
        elif fox_metrics['Goal Diff'] > 0:
            strengths.append({
                'title': '⚽ Positive Goal Differential',
                'detail': f"Teams average {fox_metrics['Goal Diff']:+.1f} goal differential, indicating balanced competitive performance. Small improvements in either offense or defense could significantly boost results."
            })
    
        if strengths:
            for strength in strengths:
                with st.expander(strength['title'], expanded=True):
                    st.markdown(strength['detail'])
        else:
            st.info("💡 Building program strengths should be a focus area. Current performance provides opportunities for improvement across multiple metrics.")
    
    
    # Strategic Recommendations based on research
    st.markdown("---")
    st.markdown("### 🎯 Evidence-Based Recommendations")
    st.markdown("<p style='color: grey; font-size: 0.9em;'>(AI Generated)</p>", unsafe_allow_html=True)
    
    st.markdown("""
    Based on industry best practices and 2025 youth soccer development trends, consider these strategic initiatives:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Program Leadership & Development**")
        st.markdown("""
        - **Director of Coaching**: Hire a dedicated Director of Coaching to oversee player development curriculum, coach training, and program quality standards across all age groups
        - **Coach Education**: Provide ongoing training for volunteer and paid coaches in age-appropriate coaching methods and player-centered approaches
        - **Player Assessment**: Move beyond win-loss records to evaluate player growth using observable skills and development milestones
        - **Training Quality**: Increase training-to-match ratio (recommended 3:1) with structured practice plans focused on ball skills and tactical understanding
        """)
    
        st.markdown("#### **Community Accessibility**")
        st.markdown("""
        - **Financial Support**: Work with town officials to explore scholarship programs, equipment lending, and fee assistance to reduce cost barriers for families
        - **Local Facilities**: Partner with school district and parks department for field access and facility-sharing agreements
        - **Family Engagement**: Conduct annual satisfaction surveys to understand family experience and identify improvement opportunities
        - **Marketing & Outreach**: Strengthen presence at community events, schools, and social media to increase program awareness and enrollment
        """)
    
    with col2:
        st.markdown("#### **Player-Centered Programming**")
        st.markdown("""
        - **Age-Appropriate Focus**: Prioritize fun and skill development in younger ages (U8-U10) before introducing competitive pressure in older divisions
        - **Development Pathways**: Create clear progression from recreational to travel teams with transparent criteria and supportive transitions
        - **Positive Environment**: Emphasize sportsmanship, teamwork, and personal growth alongside competitive results
        - **Retention Strategies**: Survey families who don't return between seasons to understand barriers and implement targeted improvements
        """)
    
        st.markdown("#### **Data & Continuous Improvement**")
        st.markdown("""
        - **Regular Reporting**: Share program metrics with town leadership and families to demonstrate value and identify trends
        - **Benchmarking**: Compare performance against BAYS league averages to set realistic goals and celebrate achievements
        - **Feedback Loops**: Create channels for coaches, parents, and players to share input on program improvements
        - **Goal Setting**: Establish annual targets for participation, retention, and player development aligned with town resources
        """)
    
    # Implementation priorities
    st.markdown("---")
    st.markdown("### 📋 Priority Action Items")
    st.markdown("<p style='color: grey; font-size: 0.9em;'>(AI Generated)</p>", unsafe_allow_html=True)
    
    # Generate priorities based on actual metrics
    immediate_priorities = []
    short_term_priorities = []
    ongoing_priorities = []
    
    if fox_metrics['Win %'] < 48:
        immediate_priorities.append("Review coaching strategies and player development curriculum to address competitive performance")
    if fox_metrics['Retention %'] < 70:
        immediate_priorities.append("Survey families to identify retention barriers and implement targeted improvements")
    if fox_metrics['Growth %'] < -5:
        immediate_priorities.append("Conduct focus groups with current and former families to understand declining enrollment")
    
    # Short-term priorities
    short_term_priorities.append("Hire a dedicated Director of Coaching to oversee player development, coach training, and program quality standards")
    if fox_metrics['Participation Rate'] < avg_metrics['Participation Rate'] - 0.5:
        short_term_priorities.append("Enhance marketing efforts and community outreach to increase program awareness")
    if abs(fox_metrics['Gender Balance'] - 50) > 15:
        short_term_priorities.append("Develop targeted recruitment for underrepresented gender to improve balance")
    if fox_metrics['Win %'] >= 48 and fox_metrics['Win %'] < 52:
        short_term_priorities.append("Invest in coach education and tactical training to improve competitive outcomes")
    
    # Ongoing priorities
    ongoing_priorities.append("Implement regular player assessment using Quality of Play metrics beyond wins/losses")
    ongoing_priorities.append("Build partnerships with schools and community organizations to reduce access barriers")
    
    # Combine and display in time order
    priorities = []
    for p in immediate_priorities:
        priorities.append(f"**Immediate:** {p}")
    for p in short_term_priorities:
        priorities.append(f"**Short-term:** {p}")
    for p in ongoing_priorities:
        priorities.append(f"**Ongoing:** {p}")
    
    for i, priority in enumerate(priorities, 1):
        st.markdown(f"{i}. {priority}")
    
    st.markdown("---")
    st.markdown("### 📚 Research Sources")
    st.markdown("""
    This assessment incorporates best practices from leading youth soccer organizations and 2025 industry trends:
    - [MLS NEXT's Revolutionary Approach to Youth Soccer Development](https://youthsportsbusinessreport.com/mls-nexts-revolutionary-approach-to-youth-soccer-development-beyond-wins-and-losses/)
    - [KPIs: Unlocking Success in Youth Soccer](https://skillshark.com/soccer-kpis/)
    - [Youth Soccer Trends 2025: Lower Costs, Better Pathways](https://ussoccerparent.com/blog-youth-soccer-trends-2025/)
    - [State of Play 2025: Annual Report on Trends in Youth Sports](https://projectplay.org/state-of-play-2025/introduction)
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("### 📊 Data Sources")
    st.markdown("""
    - **Team Performance Data**: BAYS (Bay State Youth Soccer League) records, 2021-2025
    - **School Enrollment**: Massachusetts Department of Elementary and Secondary Education, 2024-25
    - **Population Data**: U.S. Census Bureau, 2020 Census
    """)
