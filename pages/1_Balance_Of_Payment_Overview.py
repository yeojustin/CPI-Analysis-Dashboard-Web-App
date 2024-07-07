# pages/1_correlation_analysis
import streamlit as st
import pandas as pd
import data_loader as dlr
import charts

def get_top_category():
    return st.selectbox(
        "Select the BOP category you wish to analyse",
        ('D Overall Balance (A-B+C)', 'A Current Account Balance', 'B Capital & Financial Account Balance', 'C Net Errors & Omissions')
    )

def get_selected_years(df):
    return st.select_slider(
        "Select the range of years you wish to analyse", 
        options=df['Year'].unique().tolist(),
        value=(df['Year'].min(), df['Year'].max())
    )

def get_avg_values(df, category):
    avg_values = df.groupby('Year').mean().loc[:, category]
    return avg_values.mean()

def get_latest_values(df, category):
    latest_year = df['Year'].max()
    latest_values = df[df['Year'] == latest_year].loc[:, category].values[0]
    return latest_values

# Load the data
df = dlr.load_bop_cpi_merged()

st.title('Balance of Payments (BOP)')
st.write("""<h6>
         Statistics on the Balance of Payments (BOP) and Inward Direct Investment Flows (FDI Inflows) are gathered by the Singapore Department of Statistics.
         The BOP provides a summary of economic transactions between the residents of Singapore and those of other countries. Singapore’s FDI inflows capture the 
         net value of investments made by foreign direct investors in local enterprises, accounting for both increases and decreases in investment over a specified period.
         </h6>""", unsafe_allow_html=True)

# Calculate the overall averages for the entire dataset
overall_avg_values = df[['A Current Account Balance', 'B Capital & Financial Account Balance', 'C Net Errors & Omissions']].mean()

# Sidebar controls
with st.sidebar:
    st.write('<p>Customise the Dashboard</p>', unsafe_allow_html=True)
    sel_yr_range = get_selected_years(df)

# Filter the dataset based on selected years
df_filtered = df[(df['Year'] >= sel_yr_range[0]) & (df['Year'] <= sel_yr_range[1])]

# Main screen chart
sel_cat = get_top_category()
charts.make_overall_bop_time_series(df_filtered, sel_cat)

col1, col2 = st.columns(2)
with col1:
    charts.make_goods_balance_over_time_chart(df,sel_yr_range)
with col2:
    charts.make_services_balance_over_time_chart(df,sel_yr_range)

charts.make_combined_balance_over_time_chart(df,sel_yr_range,balance_type='Services')
charts.make_combined_balance_over_time_chart(df,sel_yr_range,balance_type='Goods')
charts.make_combined_goods_services_balance_chart(df,sel_yr_range)