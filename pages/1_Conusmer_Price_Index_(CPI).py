import streamlit as st
import pandas as pd
import data_loader as dlr
import charts

# Load the data
df_yearly = dlr.load_cpi_yearly()
df_quarterly = dlr.load_cpi_quarterly()
df_halfyearly = dlr.load_cpi_halfyearly()
df_yearly_pct = dlr.load_cpi_yearly_pct()
df_quarterly_pct = dlr.load_cpi_quarterly_pct()
df_halfyearly_pct = dlr.load_cpi_halfyearly_pct()

def get_selected_category():
    return st.multiselect(
        "Select the CPI category you wish to analyze",
        options=dlr.get_L1_keys(), 
        default=['All Items', 'Food', 'Transport', 'Communication']
    )

def get_selected_years(df):
    return st.select_slider(
        "Select the range of years you wish to analyze", 
        options=df.index.tolist(),
        value=(df.index[0], df.index[-1])
    )

# Initialize session state for chart selection
if 'selected_chart' not in st.session_state:
    st.session_state.selected_chart = "Yearly"  # Default chart

# Sidebar controls
with st.sidebar:
    st.write('<p style="font-size: 1em; font-weight: normal;">Customize the Dashboard</p>', unsafe_allow_html=True)
    sel_cat = get_selected_category()
    sel_yr = get_selected_years(df_yearly)
    
    chart_type = st.radio(
        "Select the time interval",
        options=["Yearly", "Quarterly", "Half-yearly"],
        index=0  # Default to the first option
    )
    st.session_state.selected_chart = chart_type

# Title of the app
st.markdown("# Consumer Price Index (CPI) 📈")
st.write("""
    <p style="font-size: 1em; font-weight: normal;">
        The Consumer Price Index (CPI) tracks the average changes in prices over time for a fixed basket of goods and services typically purchased by resident households. 
        It indicates price trends (i.e., how prices change) rather than the actual price level at a given time. The CPI is compiled monthly and is commonly used to measure 
        consumer inflation. The weighting pattern for the 2019-based CPI was developed from expenditure data collected during the Household Expenditure Survey conducted from 
        October 2017 to September 2018. These values were updated to reflect 2019 prices by accounting for price changes between 2017/18 and 2019.
    </p><br/>
    """, unsafe_allow_html=True)

# Display metrics at the top
metrics = None
if st.session_state.selected_chart == "Yearly":
    charts.make_time_series_chart(df_yearly, "Yearly CPI Index", sel_cat, sel_yr)
    charts.make_percentage_change_time_series_chart(df_yearly_pct, "Yearly CPI Percentage Change", sel_cat, sel_yr)
    charts.make_box_plot_cpi(df_yearly, sel_cat)
    metrics = charts.calculate_metrics(df_yearly, sel_cat, sel_yr)

elif st.session_state.selected_chart == "Quarterly":
    charts.make_time_series_chart(df_quarterly, "Quarterly CPI Index", sel_cat, sel_yr)  
    charts.make_percentage_change_time_series_chart(df_quarterly_pct, "Quarterly CPI Percentage Change", sel_cat, sel_yr)
    charts.make_box_plot_cpi(df_quarterly, sel_cat)
    metrics = charts.calculate_metrics(df_quarterly, sel_cat, sel_yr)

elif st.session_state.selected_chart == "Half-yearly":
    charts.make_time_series_chart(df_halfyearly, "Half-yearly CPI Index", sel_cat, sel_yr)
    charts.make_percentage_change_time_series_chart(df_halfyearly_pct, "Half-yearly CPI Percentage Change", sel_cat, sel_yr)
    charts.make_box_plot_cpi(df_halfyearly, sel_cat)
    metrics = charts.calculate_metrics(df_halfyearly, sel_cat, sel_yr)

# Display metrics at the top if they exist
if metrics:
    with st.container(border=True):
        st.write("<h4>Key Metrics</h4>", unsafe_allow_html=True)
        cols = st.columns(len(sel_cat))
        for idx, category in enumerate(sel_cat):
            if category in metrics:
                with cols[idx]:
                    st.metric(
                        label=f"Latest {category} Value",
                        value=f"{metrics[category]['latest']:.2f}" if metrics[category]['latest'] is not None else "N/A"
                    )
                    st.metric(
                        label=f"Average {category} Value",
                        value=f"{metrics[category]['average']:.2f}" if metrics[category]['average'] is not None else "N/A"
                    )
