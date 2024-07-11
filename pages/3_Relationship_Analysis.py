import streamlit as st
import pandas as pd
import numpy as np
import data_loader as dlr
import charts
import plotly.express as px

def get_bop_category(key, index):
    return st.selectbox(
        "Select the BOP category to analyze",
        ('D Overall Balance (A-B+C)', 'A Current Account Balance', 'B Capital & Financial Account Balance', 'C Net Errors & Omissions'),
        index=index,
        key=key
    )

def get_cpi_category(key, index):
    return st.selectbox(
        "Select the CPI category to analyze",
        (dlr.get_L1_keys()),
        index=index,
        key=key
    )

def get_selected_years(df):
    return st.select_slider(
        "Select the range of years you wish to analyze", 
        options=df['Year'].unique().tolist(),
        value=(2000, 2023)
    )

def calculate_correlation(df, selected_years, cat1, cat2):
    # Extract the start and end years from the selected range
    start_year, end_year = selected_years
    # Filter the DataFrame based on the selected year range
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
    # Calculate the Pearson correlation coefficient
    correlation = filtered_df[cat1].corr(filtered_df[cat2])
    return correlation


def display_scatter_and_correlation(df, sel_yr, bop_key, cpi_key, bop_key_id, cpi_key_id, cpi_index, bop_index):
    col = st.columns(2)
    with col[0]: bop_cat = get_bop_category(bop_key_id, bop_index)
    with col[1]: cpi_cat = get_cpi_category(cpi_key_id, cpi_index)
    
    charts.make_2d_scatter(df, sel_yr, bop_cat, cpi_cat, None, True)
    
    correlation = calculate_correlation(df, sel_yr, bop_cat, cpi_cat)
    correlation_color = "green" if correlation > 0 else "red"
    
    st.markdown(f"<p style='text-align:center; color:{correlation_color}; font-size:1.2em;'>Correlation Coefficient: {correlation:.2f}</p>", unsafe_allow_html=True)

df = dlr.load_bop_cpi_merged()

# Sidebar controls
with st.sidebar:
    st.write('<p style="font-size: 1em; font-weight: normal;">Customise the year across all scatter plots</p>', unsafe_allow_html=True)
    sel_yr = get_selected_years(df)
    

#### START PAGE ####

st.title('Relationship between BOP and CPI 🔎')
st.write("""
    <p style="font-size: 1em; font-weight: normal;">
        A positive BOP, indicating more exports than imports, can strengthen the local currency, potentially lowering the CPI by making 
        imports cheaper. Conversely, a negative BOP can weaken the local currency, leading to higher import costs and an increase in the 
        CPI. Understanding the interplay between BOP and CPI helps in analyzing the economic stability and inflationary pressures within 
        an economy. To understand how these two critical economic indicators interact, we present a scatter plot showing the relationship between BOP and CPI. 
        Each point on the scatter plot represents a specific time period, allowing us to visually inspect any patterns or correlations between these variables.
    </p>
    """, unsafe_allow_html=True)

st.write(f"<h3>Analysing Data From {sel_yr[0]} - {sel_yr[1]}</h3>", unsafe_allow_html=True)

row_one = st.columns(2)
row_two = st.columns(2)

with row_one[0], st.container(border=True):
    display_scatter_and_correlation(df, sel_yr, "bop_cat_1", "cpi_cat_1", "11", "12", 0, 1)

with row_one[1], st.container(border=True):
    display_scatter_and_correlation(df, sel_yr, "bop_cat_2", "cpi_cat_2", "21", "22", 1, 1)

with row_two[0], st.container(border=True):
    display_scatter_and_correlation(df, sel_yr, "bop_cat_3", "cpi_cat_3", "31", "32", 4, 0)

with row_two[1], st.container(border=True):
    display_scatter_and_correlation(df, sel_yr, "bop_cat_4", "cpi_cat_4", "41", "42", 5, 0)
