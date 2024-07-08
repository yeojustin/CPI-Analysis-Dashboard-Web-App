import streamlit as st
import pandas as pd
import data_loader as dlr
import charts
import plotly.express as px

def get_bop_category():
    return st.selectbox(
        "Select the BOP category you wish to analyze",
        ('D Overall Balance (A-B+C)', 'A Current Account Balance', 'B Capital & Financial Account Balance', 'C Net Errors & Omissions')
    )

def get_cpi_category():
    return st.selectbox(
        "Select the CPI category you wish to analyze",
        (dlr.get_L1_keys())
    )

def get_selected_years(df):
    return st.select_slider(
        "Select the range of years you wish to analyze", 
        options=df['Year'].unique().tolist(),
        value=(df['Year'].min(), df['Year'].max())
    )

def get_3d_categories():
    return st.multiselect(
        "Select up to 3 categories for 3D plotting",
        options=dlr.get_all_keys(),
        default=dlr.get_all_keys()[:3]  # Default to the first three categories
    )

df = dlr.load_bop_cpi_merged()

# Sidebar controls
with st.sidebar:
    st.write('<p style="font-size: 1em; font-weight: normal;">Customize the chart</p>', unsafe_allow_html=True)
    bop_cat = get_bop_category()
    cpi_cat = get_cpi_category()
    sel_yr = get_selected_years(df)
    
    chart_type = st.radio(
        "Select the time interval",
        options=["Yearly", "Quarterly", "Half-yearly"],
        index=0  # Default to the first option
    )
    st.session_state.selected_chart = chart_type

    # 3D chart category selection
    st.write('<p style="font-size: 1em; font-weight: normal;">3D Chart Settings</p>', unsafe_allow_html=True)
    three_d_cats = get_3d_categories()

#### START PAGE ####

st.title('Relationship between BOP and CPI 🔎')
st.write("""
    <p style="font-size: 1em; font-weight: normal;">
        A positive BOP, indicating more exports than imports, can strengthen the local currency, potentially lowering the CPI by making 
        imports cheaper. Conversely, a negative BOP can weaken the local currency, leading to higher import costs and an increase in the 
        CPI. Understanding the interplay between BOP and CPI helps in analyzing the economic stability and inflationary pressures within 
        an economy.
        <br/><br/>
        To understand how these two critical economic indicators interact, we present a scatter plot showing the relationship between BOP and CPI. Each point on the scatter plot represents a specific time period, allowing us to visually inspect any patterns or correlations between these variables.
        Additionally, we provide a correlation matrix that quantifies the strength and direction of the relationship between BOP and CPI. This matrix helps in identifying whether a significant correlation exists, which can offer insights into how changes in the BOP might be associated with fluctuations in the CPI.
    </p>
    """, unsafe_allow_html=True)

# 2D Scatter Plot
charts.make_2d_scatter(df, sel_yr, bop_cat, cpi_cat)

# 3D Scatter Plot
if len(three_d_cats) == 3:
    fig = px.scatter_3d(df, x=three_d_cats[0], y=three_d_cats[1], z=three_d_cats[2], color='Year')
    fig.update_layout(title='3D Scatter Plot of Selected Categories', scene=dict(
        xaxis_title=three_d_cats[0],
        yaxis_title=three_d_cats[1],
        zaxis_title=three_d_cats[2]
    ))
    st.plotly_chart(fig)
else:
    st.warning("Please select exactly 3 categories for the 3D plot.")
