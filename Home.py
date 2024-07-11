import streamlit as st
import pandas as pd
import data_loader as dlr
import charts
import plotly.express as px
import numpy as np

st.set_page_config(page_title="CPI Analysis", layout="wide", page_icon="📈")

st.markdown("# Understanding Key Concepts 🧠")

with st.container(border=True):
    st.write("""
            <h3>Hypothesis 🤔</h3>
            <p>We hypothesize that changes in the Consumer Price Index (CPI) significantly influence the Balance of Payments (BOP) and, consequently, Aggregate Demand (AD).
            Specifically, we aim to explore how inflation (as measured by CPI) impacts the trade balance, investment flows, and overall economic stability.</p>
    """, unsafe_allow_html=True)

with st.container(border=True):
    st.write("""
            <h4>What is the Consumer Price Index (CPI)? 📈</h4> 
            <p style="font-size: 1em; font-weight: normal;">
            CPI measures the average change over time in the prices paid by urban consumers for a basket of consumer goods and services. It is a key indicator of inflation 
            and purchasing power in an economy.</p>
        """, unsafe_allow_html=True)

with st.container(border=True):
    st.write("""
            <h4>What is the Balance of Payments (BOP)? 📊</h4>
            <p style="font-size: 1rem; font-weight: normal;">
            BOP is a comprehensive record of a country’s economic transactions with the rest of the world over a specific period. It includes:
            <ul>
                <li><b>Current Account:</b> Records trade in goods and services, income from abroad, and current transfers.</li>
                <li><b>Capital Account:</b> Records capital transfers and the acquisition/disposal of non-produced, non-financial assets.</li>
                <li><b>Financial Account:</b> Records investments in foreign assets and liabilities.</li>
            </ul>
            </p>
        """, unsafe_allow_html=True)

with st.container(border=True):
    st.write("""
            <h4>What is Aggregate Demand (AD)?</h4>
            <p style="font-size: 1rem; font-weight: normal;">
            Aggregate Demand represents the total demand for goods and services within an economy. It is composed of:
            <ul>
                <li><b>C (Consumer Spending):</b> Total spending by households on goods and services.</li>
                <li><b>G (Government Spending):</b> Total government expenditures on goods and services.</li>
                <li><b>I (Investment):</b> Spending on capital goods that will be used for future production.</li>
                <li><b>X (Exports):</b> Goods and services produced domestically and sold abroad.</li>
                <li><b>M (Imports):</b> Goods and services bought from other countries.</li>
            </ul>
            <p><b>Formula: AD = C + I + G + (X - M)</b></p>
            </p>
        """, unsafe_allow_html=True)

with st.container(border=True):
    st.write("""
            <h4>Relationship Between CPI, AD, and BOP</h4>
            <ul>
                <li><b>CPI and Consumer Spending (C):</b> Higher inflation (CPI) reduces purchasing power, affecting how much consumers can buy.</li>
                <li><b>CPI and Investment (I):</b> Inflation influences interest rates, impacting borrowing costs and investment decisions.</li>
                <li><b>CPI and Trade Balance (X - M):</b> Inflation affects the prices of goods and services, influencing exports and imports.</li>
            </ul>
            """,unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1, st.container(border=True, height=370):
    st.write("""
            <h4>BOP and AD Interaction</h4>
            <p>The <b>current account</b> of the BOP directly relates to the net exports component (X - M) of AD. Changes in net exports affect AD because net exports are part of the AD formula: <b>AD = C + I + G + (X - M)</b>. Inflation (CPI) influences both AD components and BOP components. For instance, higher inflation can reduce exports and increase imports, impacting the current account balance and thus affecting AD.</p></p>
            """, unsafe_allow_html=True)
    
with col2, st.container(border=True, height=370):
    st.write("""
            <h4>Example to Illustrate</h4>
            <p>Consider a country experiencing high inflation:
            <ul>
                <li><b>Consumer Impact:</b> Higher prices mean consumers can buy less, reducing overall spending (C).</li>
                <li><b>Investment Impact:</b> Rising costs and uncertainty might deter investment (I).</li>
                <li><b>Trade Impact:</b> Domestic goods become more expensive relative to foreign goods, potentially reducing exports (X) and increasing imports (M), thereby worsening the trade balance and affecting the BOP.</li>
            </ul></p>
            """, unsafe_allow_html=True)

# data = dlr.load_bop_cpi_merged()

# # Convert all columns to numeric, if possible
# data = data.apply(pd.to_numeric, errors='coerce')

# # Drop columns with all NaN values (if any)
# data.dropna(axis=1, how='all', inplace=True)

# # Correlation heatmap
# st.header("Correlation Heatmap")
# corr = data.corr()
# fig_heatmap = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="Viridis")
# st.plotly_chart(fig_heatmap)

# # Scatter plot: Example with Imports of Goods vs CPI (Food)
# st.header("Scatter Plot: Imports of Goods vs CPI (Food)")
# fig_scatter = px.scatter(data, x="Imports Of Goods", y="Food", labels={
#     "Imports Of Goods": "Imports Of Goods",
#     "Food": "CPI - Food"
# })
# st.plotly_chart(fig_scatter)

# # Box plot: Distribution of CPI Categories
# st.header("Box Plot: Distribution of CPI Categories")
# cpi_columns = ["Food", "Housing & Utilities", "Health Care", "Transport_y"]  # adjust based on your actual column names
# fig_box = px.box(data, y=cpi_columns, labels={
#     "variable": "CPI Category",
#     "value": "CPI Value"
# })
# st.plotly_chart(fig_box)

# # Pair plot: Relationships between multiple variables
# st.header("Pair Plot: Relationships between multiple variables")
# pair_plot_columns = ["Current Account Balance", "Exports Of Goods", "Imports Of Goods", "Food"]
# fig_pair = px.scatter_matrix(data, dimensions=pair_plot_columns)
# st.plotly_chart(fig_pair)

# # Bar chart: Average CPI for different categories
# st.header("Bar Chart: Average CPI for different categories")
# avg_cpi = data[cpi_columns].mean().reset_index()
# avg_cpi.columns = ["CPI Category", "Average CPI"]
# fig_bar = px.bar(avg_cpi, x="CPI Category", y="Average CPI")
# st.plotly_chart(fig_bar)

# # Histogram: Frequency distribution of Current Account Balance
# st.header("Histogram: Frequency distribution of Current Account Balance")
# fig_hist = px.histogram(data, x="Current Account Balance", nbins=50, marginal="kde")
# st.plotly_chart(fig_hist)