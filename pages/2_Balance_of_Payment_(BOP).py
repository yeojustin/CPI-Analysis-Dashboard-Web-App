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

#### CONTAINER CSS ####
container_style = """
    <style>
        .container1 {
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .container2 {
            /* Add styles for Container 2 if needed */
        }
    </style>
"""

# Display the CSS styles
st.markdown(container_style, unsafe_allow_html=True)

####
# Load the data
df = dlr.load_bop_cpi_merged()


#### START PAGE ####

st.title('Balance of Payments (BOP) 📊')
st.write("""
        <p style="font-size: 1.25em; font-weight: normal;">
            Statistics on the Balance of Payments (BOP) and Inward Direct Investment Flows (FDI Inflows) are gathered by the Singapore Department of Statistics.
            The BOP provides a summary of economic transactions between the residents of Singapore and those of other countries. Singapore’s FDI inflows capture the 
            net value of investments made by foreign direct investors in local enterprises, accounting for both increases and decreases in investment over a specified period.
        </p><br/>
        """, unsafe_allow_html=True)

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

# Container for both columns to ensure equal height
col1, col2 = st.columns([0.7, 0.3])
with col2, st.container(border=True, height=500):
    if sel_cat == "D Overall Balance (A-B+C)":
        st.write("""
                <p><b>Overall Balance (D)</b> reflects the net change in a country's foreign exchange reserves. It summarizes the combined 
                effect of the Current Account Balance (A), Capital & Financial Account Balance (B), and Net Errors & Omissions (C). 
                A positive overall balance indicates a surplus, leading to an increase in reserves, while a negative balance 
                indicates a deficit, resulting in a decrease in reserves.</p>
                """, unsafe_allow_html=True)

    elif sel_cat == "A Current Account Balance":
        st.write("""
                <p><b>Current Account Balance (A)</b> measures the difference between a nation's savings and its investment. It includes:</p>
                <ul>
                    <li><b>Goods Balance</b>: The net exports (Exports - Imports) of goods.</li>
                    <li><b>Services Balance</b>: The net exports (Exports - Imports) of services.</li>
                    <li><b>Primary Income Balance</b>: Earnings on investments and wages from abroad.</li>
                    <li><b>Secondary Income Balance</b>: Transfers such as remittances and foreign aid.</li>
                </ul>
                <p>A positive current account balance means a country is a net lender to the rest of the world, while a negative balance means it is a net borrower.</p>
                """, unsafe_allow_html=True)

    elif sel_cat == "B Capital & Financial Account Balance":
        st.write("""
                <p><b>Capital & Financial Account Balance (B)</b> records net changes in ownership of national assets. It includes:</p>
                <ul>
                    <li><b>Financial Account (Net)</b>: Financial transactions that involve foreign investments.</li>
                    <li><b>Direct Investment</b>: Investments in physical assets like factories and businesses.</li>
                    <li><b>Portfolio Investment</b>: Investments in financial assets like stocks and bonds.</li>
                    <li><b>Financial Derivatives</b>: Transactions involving complex financial instruments.</li>
                    <li><b>Other Investment</b>: Various other financial transactions, including loans and currency deposits.</li>
                </ul>
                <p>A positive balance indicates net capital inflow, while a negative balance indicates net capital outflow.</p>
                """, unsafe_allow_html=True)

    elif sel_cat == "C Net Errors & Omissions":
        st.write("""
                <p><b>Net Errors & Omissions (C)</b> account for discrepancies and errors in the Balance of Payments records. 
                This ensures that the Balance of Payments balances to zero.</p>
                """, unsafe_allow_html=True)

with col1, st.container(border=True, height=500):      
    charts.make_overall_bop_time_series(df_filtered, sel_cat)

col1, col2 = st.columns(2)
with col1, st.container(border=True):

    charts.make_goods_balance_over_time_chart(df,sel_yr_range)
    
    st.write("""
            <p><b>Goods Balance</b> represents the difference between the value of goods exported and imported. A positive goods balance, or surplus, 
            indicates that the value of exports exceeds that of imports, contributing positively to the overall trade balance. Conversely, 
            a negative goods balance, or deficit, indicates higher imports than exports, which can be a sign of strong domestic demand 
            or dependency on foreign products.
            </p>
            """, unsafe_allow_html=True)

with col2, st.container(border=True):

    charts.make_services_balance_over_time_chart(df,sel_yr_range)

    st.write("""
            <p><b>Goods Balance</b> represents the difference between the value of goods exported and imported. A positive goods balance, or surplus, 
            indicates that the value of exports exceeds that of imports, contributing positively to the overall trade balance. Conversely, 
            a negative goods balance, or deficit, indicates higher imports than exports, which can be a sign of strong domestic demand 
            or dependency on foreign products.
            </p>
            """, unsafe_allow_html=True)

with st.container(border=True):
    charts.make_combined_goods_services_balance_chart(df,sel_yr_range)