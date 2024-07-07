import streamlit as st
import pandas as pd
import data_loader as dlr
import charts
import plotly.express as px
import numpy as np

# Sidebar configuration
st.set_page_config(page_title="CPI Analysis", layout="wide", page_icon="📈", initial_sidebar_state="expanded",
                   menu_items={
                       'Get Help': 'https://www.google.com',
                       'Report a Bug': 'https://www.google.com'
                   })

# Content for CPI and its relationship with AD and BOP
cpi_content = """
# Consumer Price Index (CPI)

**CPI measures the average change over time in the prices paid by urban consumers for a basket of consumer goods and services. It is a key indicator of inflation and purchasing power in an economy.**

CPI includes various categories such as:
- Food and beverages
- Housing
- Apparel
- Transportation
- Medical care
- Recreation
- Education
- Other goods and services

## Relationship to AD = C + G + I + X - M

**CPI indirectly influences components of aggregate demand (AD) through its impact on consumer spending (C). Changes in CPI can affect consumer behavior, influencing their spending patterns on goods and services.**

- **Consumer Spending (C):** Inflation, as measured by CPI, affects the purchasing power of consumers, thereby influencing their spending on goods and services.
- **Investment (I):** Inflation also influences investment decisions by affecting interest rates and the cost of capital.
- **Imports (M) and Exports (X):** Changes in relative price levels due to inflation impact international competitiveness, thereby affecting imports and exports.

## BOP and CPI Interaction

**While CPI itself is not directly a part of BOP calculations, changes in CPI can influence the BOP indirectly. For example, higher inflation (as indicated by CPI) may affect the cost structure of exports and imports, thereby influencing the trade balance (X - M) in the BOP.**

- **Trade Balance (X - M):** Inflation impacts the prices of goods and services, influencing the competitiveness of exports and the cost of imports.
- **Primary Income:** Inflation affects the real value of income flows in the BOP, as nominal values may change due to price adjustments.

**In summary, while CPI and the components of AD = C + G + I + X - M are distinct concepts, CPI serves as a critical economic indicator that influences consumer behavior, economic policy decisions, and indirectly impacts the components of aggregate demand and the Balance of Payments through its effects on prices and purchasing power.**
"""

import streamlit as st

# Content for CPI, AD, and BOP
content_hypo = """
# Exploring the Relationship Between CPI, AD, and BOP

## Hypothesis

We hypothesize that changes in the Consumer Price Index (CPI) significantly influence the Balance of Payments (BOP) and, consequently, Aggregate Demand (AD). Specifically, we aim to explore how inflation (as measured by CPI) impacts the trade balance, investment flows, and overall economic stability.

## Understanding Key Concepts

### What is the Consumer Price Index (CPI)?

CPI measures the average change over time in the prices paid by urban consumers for a basket of consumer goods and services. It is a key indicator of inflation and purchasing power in an economy. 

### What is the Balance of Payments (BOP)?

BOP is a comprehensive record of a country’s economic transactions with the rest of the world over a specific period. It includes:
- **Current Account:** Records trade in goods and services, income from abroad, and current transfers.
- **Capital Account:** Records capital transfers and the acquisition/disposal of non-produced, non-financial assets.
- **Financial Account:** Records investments in foreign assets and liabilities.

### What is Aggregate Demand (AD)?

Aggregate Demand represents the total demand for goods and services within an economy. It is composed of:
- **C (Consumer Spending):** Total spending by households on goods and services.
- **G (Government Spending):** Total government expenditures on goods and services.
- **I (Investment):** Spending on capital goods that will be used for future production.
- **X (Exports):** Goods and services produced domestically and sold abroad.
- **M (Imports):** Goods and services bought from other countries.

**Formula: AD = C + I + G + (X - M)**

### Relationship Between CPI, AD, and BOP

- **CPI and Consumer Spending (C):** Higher inflation (CPI) reduces purchasing power, affecting how much consumers can buy.
- **CPI and Investment (I):** Inflation influences interest rates, impacting borrowing costs and investment decisions.
- **CPI and Trade Balance (X - M):** Inflation affects the prices of goods and services, influencing exports and imports.

### BOP and AD Interaction

- The **current account** of the BOP directly relates to the net exports component (X - M) of AD.
- Changes in net exports affect AD because net exports are part of the AD formula: **AD = C + I + G + (X - M)**.
- Inflation (CPI) influences both AD components and BOP components. For instance, higher inflation can reduce exports and increase imports, impacting the current account balance and thus affecting AD.

## Example to Illustrate

Consider a country experiencing high inflation:
- **Consumer Impact:** Higher prices mean consumers can buy less, reducing overall spending (C).
- **Investment Impact:** Rising costs and uncertainty might deter investment (I).
- **Trade Impact:** Domestic goods become more expensive relative to foreign goods, potentially reducing exports (X) and increasing imports (M), thereby worsening the trade balance and affecting the BOP.

## Summary

While CPI and the components of AD = C + I + G + (X - M) are distinct concepts, CPI serves as a critical economic indicator that influences consumer behavior, economic policy decisions, and indirectly impacts the components of aggregate demand and the Balance of Payments through its effects on prices and purchasing power.
"""

data = dlr.load_bop_cpi_merged()

# Convert all columns to numeric, if possible
data = data.apply(pd.to_numeric, errors='coerce')

# Drop columns with all NaN values (if any)
data.dropna(axis=1, how='all', inplace=True)

# Correlation heatmap
st.header("Correlation Heatmap")
corr = data.corr()
fig_heatmap = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="Viridis")
st.plotly_chart(fig_heatmap)

# Scatter plot: Example with Imports of Goods vs CPI (Food)
st.header("Scatter Plot: Imports of Goods vs CPI (Food)")
fig_scatter = px.scatter(data, x="Imports Of Goods", y="Food", labels={
    "Imports Of Goods": "Imports Of Goods",
    "Food": "CPI - Food"
})
st.plotly_chart(fig_scatter)

# Box plot: Distribution of CPI Categories
st.header("Box Plot: Distribution of CPI Categories")
cpi_columns = ["Food", "Housing & Utilities", "Health Care", "Transport_y"]  # adjust based on your actual column names
fig_box = px.box(data, y=cpi_columns, labels={
    "variable": "CPI Category",
    "value": "CPI Value"
})
st.plotly_chart(fig_box)

# Pair plot: Relationships between multiple variables
st.header("Pair Plot: Relationships between multiple variables")
pair_plot_columns = ["Current Account Balance", "Exports Of Goods", "Imports Of Goods", "Food"]
fig_pair = px.scatter_matrix(data, dimensions=pair_plot_columns)
st.plotly_chart(fig_pair)

# Bar chart: Average CPI for different categories
st.header("Bar Chart: Average CPI for different categories")
avg_cpi = data[cpi_columns].mean().reset_index()
avg_cpi.columns = ["CPI Category", "Average CPI"]
fig_bar = px.bar(avg_cpi, x="CPI Category", y="Average CPI")
st.plotly_chart(fig_bar)

# Histogram: Frequency distribution of Current Account Balance
st.header("Histogram: Frequency distribution of Current Account Balance")
fig_hist = px.histogram(data, x="Current Account Balance", nbins=50, marginal="kde")
st.plotly_chart(fig_hist)