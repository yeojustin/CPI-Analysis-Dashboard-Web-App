import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

def make_time_series_chart(df, title, selected_category, selected_years): 

    # Ensure selected columns are in the dataframe
    selected_category = [cat for cat in selected_category if cat in df.columns]
    
    if not selected_category:
        st.error("No valid categories selected.")
        return

    # Convert relevant columns to numeric, handling errors by setting invalid parsing as na
    df[selected_category] = df[selected_category].apply(pd.to_numeric, errors='coerce')

    # Filter the dataframe based on the selected date range
    start_year, end_year = selected_years
    filtered_df = df.loc[start_year:end_year]

    if filtered_df.empty:
        st.error("No data available for the selected date range.")
        return

    # Main time series chart - top row
    fig_top = px.line(filtered_df, x=filtered_df.index, y=selected_category, height=600)
    fig_top.update_layout(
        title=title,
        xaxis=dict(
            title='Year',
            tickmode='array',
            ticktext=filtered_df.index,
        ),
        yaxis=dict(
            title='CPI Value'
        ),
        xaxis_title="Time Period (Year)",
        yaxis_title="CPI Index Value",
        legend_title="CPI Variable",
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14,
        hoverlabel_font_size=14
    )

    fig_top.update_traces(mode="lines", hovertemplate=None)
    fig_top.update_layout(hovermode="x unified")

    st.plotly_chart(fig_top, use_container_width=True)


def make_percentage_change_time_series_chart(df, title, selected_category, selected_years):
    # Ensure selected columns are in the dataframe
    selected_category = [cat for cat in selected_category if cat in df.columns]
    
    if not selected_category:
        st.error("No valid categories selected.")
        return

    # Convert relevant columns to numeric, handling errors by setting invalid parsing as na
    df[selected_category] = df[selected_category].apply(pd.to_numeric, errors='coerce')

    # Filter the dataframe based on the selected date range
    start_year, end_year = selected_years
    filtered_df = df.loc[start_year:end_year]

    if filtered_df.empty:
        st.error("No data available for the selected date range.")
        return

    # Create the bar chart
    fig = px.bar(filtered_df, x=filtered_df.index, y=selected_category, barmode='group', height=600)
    fig.update_layout(
        title=title,
        xaxis=dict(
            title='Year',
            tickmode='array',
            ticktext=filtered_df.index,
        ),
        yaxis=dict(
            title='Percentage Change (%)'
        ),
        xaxis_title="Time Period (Year)",
        yaxis_title="Percentage Change (%)",
        legend_title="CPI Category",
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14,
        hoverlabel_font_size=14
    )
    
    st.plotly_chart(fig, use_container_width=True)
    


def calculate_metrics(df, selected_category, selected_years):
    metrics = {}
    start_year, end_year = selected_years
    filtered_df = df.loc[start_year:end_year]

    for category in selected_category:
        if category in filtered_df.columns:
            latest_value = filtered_df[category].iloc[-1] if not filtered_df[category].empty else None
            average_value = filtered_df[category].mean() if not filtered_df[category].empty else None
            metrics[category] = {
                'latest': latest_value,
                'average': average_value
            }
    
    return metrics


def make_overall_bop_time_series(df, selected_category):
    fig = px.bar(df, x='Year', y=selected_category,
             title=f'Overall {selected_category} Over Time',
             labels={'Year': 'Year', selected_category: 'Overall Balance (in Million SGD)'})
    
    fig.update_layout(
        xaxis_title="Time Period (Year)",
        yaxis_title="Percentage Change (%)",
        legend_title="CPI Category",
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14,
        hoverlabel_font_size=14
    )
    
    st.plotly_chart(fig, use_container_width=True)


def get_avg_values(df, category):
    df_filtered = df[df['Category'] == category]
    avg_values = df_filtered[['A Current Account Balance', 'B Capital & Financial Account Balance', 'C Net Errors & Omissions']].mean()
    return avg_values


def make_goods_balance_over_time_chart(df, selected_years):
    """
    Create an area chart using Plotly Express showing Exports Of Goods and Imports Of Goods over time,
    with a line for Goods Balance.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    selected_years (tuple): A tuple containing the start and end years for filtering the data.
    
    Returns:
    fig (plotly.graph_objs._figure.Figure): The generated plotly figure.
    """
    # Calculate Goods Balance
    df['Goods Balance'] = df['Exports Of Goods'] - df['Imports Of Goods']

    # Filter the dataframe based on user input
    start_year, end_year = selected_years
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Melt the dataframe to long format for Plotly Express
    df_melted = filtered_df.melt(id_vars=['Year'], value_vars=['Exports Of Goods', 'Imports Of Goods'], 
                                 var_name='Category', value_name='Value')

    # Create the area chart
    fig = px.area(df_melted, 
                  x='Year', 
                  y='Value', 
                  color='Category',
                  labels={'Value': 'Value', 'Year': 'Year', 'Category': 'Category'},
                  title=f'Goods Balance Analysis from {start_year} to {end_year}')

    # Add line for Goods Balance
    fig.add_scatter(x=filtered_df['Year'], y=filtered_df['Goods Balance'], mode='lines', name='Goods Balance', line=dict(color='firebrick'))
    
    fig.update_layout(showlegend=True)       
    fig.update_layout(legend=dict(orientation="h", yanchor="top", y=-0.50, xanchor="right", x=1))

    fig.update_layout(
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14,
        hoverlabel_font_size=14
    )
       
    return st.plotly_chart(fig, use_container_width=True)


def make_services_balance_over_time_chart(df, selected_years):
    """
    Create an area chart using Plotly Express showing Exports Of Goods and Imports Of Goods over time,
    with a line for Goods Balance.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    selected_years (tuple): A tuple containing the start and end years for filtering the data.
    
    Returns:
    fig (plotly.graph_objs._figure.Figure): The generated plotly figure.
    """
    # Filter the dataframe based on user input
    start_year, end_year = selected_years
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Melt the dataframe to long format for Plotly Express
    df_melted = filtered_df.melt(id_vars=['Year'], value_vars=['Exports Of Services', 'Imports Of Services'], 
                                 var_name='Category', value_name='Value')

    # Create the area chart
    fig = px.area(df_melted, 
                  x='Year', 
                  y='Value', 
                  color='Category',
                  labels={'Value': 'Value', 'Year': 'Year', 'Category': 'Category'},
                  title=f'Services Balance Analysis from {start_year} to {end_year}')

    # Add line for Goods Balance
    fig.add_scatter(x=filtered_df['Year'], y=filtered_df['Services Balance'], mode='lines', name='Services Balance', line=dict(color='firebrick'))
    
    fig.update_layout(showlegend=True)       
    fig.update_layout(legend=dict(orientation="h", yanchor="top", y=-0.50, xanchor="right", x=1))   
    
    fig.update_layout(
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14,
        hoverlabel_font_size=14
    )
    
    return st.plotly_chart(fig, use_container_width=True)


def make_combined_balance_over_time_chart(df, selected_years, balance_type='Goods'):
    """
    Create a combined area and line chart using Plotly Express showing Exports and Imports over time,
    with a line for the corresponding balance (Goods or Services).
    
    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    selected_years (tuple): A tuple containing the start and end years for filtering the data.
    balance_type (str): The type of balance to analyze ('Goods' or 'Services').
    
    Returns:
    fig (plotly.graph_objs._figure.Figure): The generated plotly figure.
    """
    if balance_type not in ['Goods', 'Services']:
        raise ValueError("balance_type must be either 'Goods' or 'Services'")
    
    if balance_type == 'Goods':
        df['Balance'] = df['Exports Of Goods'] - df['Imports Of Goods']
        export_col = 'Exports Of Goods'
        import_col = 'Imports Of Goods'
        title = 'Goods Balance Analysis'
    else:
        df['Balance'] = df['Exports Of Services'] - df['Imports Of Services']
        export_col = 'Exports Of Services'
        import_col = 'Imports Of Services'
        title = 'Services Balance Analysis'

    # Filter the dataframe based on user input
    start_year, end_year = selected_years
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Melt the dataframe to long format for Plotly Express
    df_melted = filtered_df.melt(id_vars=['Year'], value_vars=[export_col, import_col], 
                                 var_name='Category', value_name='Value')

    # Create the area chart
    fig = px.area(df_melted, 
                  x='Year', 
                  y='Value', 
                  color='Category',
                  labels={'Value': 'Value', 'Year': 'Year', 'Category': 'Category'},
                  title=f'{title} from {start_year} to {end_year}')

    # Add line for Balance
    fig.add_scatter(x=filtered_df['Year'], y=filtered_df['Balance'], mode='lines', name='Balance', line=dict(color='firebrick'))
    
    # Update layout for legend and hover mode
    fig.update_layout(showlegend=True)
    fig.update_layout(legend=dict(orientation="h", yanchor="top", y=-0.20, xanchor="right", x=1))
    fig.update_traces(mode="lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")

    fig.update_layout(
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14,
        hoverlabel_font_size=14
    )
    

    return st.plotly_chart(fig, use_container_width=True)


def make_combined_goods_services_balance_chart(df, selected_years):
    """
    Create a combined area chart using Plotly Express showing Exports and Imports of Goods and Services over time,
    with lines for Goods Balance and Services Balance.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    selected_years (tuple): A tuple containing the start and end years for filtering the data.
    
    Returns:
    fig (plotly.graph_objs._figure.Figure): The generated plotly figure.
    """
    # Calculate Balances
    df['Goods Balance'] = df['Exports Of Goods'] - df['Imports Of Goods']
    df['Services Balance'] = df['Exports Of Services'] - df['Imports Of Services']

    # Filter the dataframe based on user input
    start_year, end_year = selected_years
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Melt the dataframe to long format for Plotly Express
    df_melted = filtered_df.melt(id_vars=['Year'], value_vars=['Exports Of Goods', 'Imports Of Goods', 
                                                               'Exports Of Services', 'Imports Of Services'], 
                                 var_name='Category', value_name='Value')

    # Create the area chart for Exports and Imports
    fig = px.area(df_melted, 
                  x='Year', 
                  y='Value', 
                  color='Category',
                  labels={'Value': 'Value', 'Year': 'Year', 'Category': 'Category'},
                  title=f'Goods and Services Balance Analysis from {start_year} to {end_year}')

    # Add lines for Goods Balance and Services Balance
    fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Goods Balance'], 
                             mode='lines', name='Goods Balance', line=dict(color='firebrick')))
    fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Services Balance'], 
                             mode='lines', name='Services Balance', line=dict(color='blue')))

    # Update layout for legend and hover mode
    fig.update_layout(showlegend=True)
    fig.update_layout(legend=dict(orientation="h", yanchor="top", y=-0.50, xanchor="right", x=1))
    fig.update_traces(mode="lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")

    fig.update_layout(
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14,
        hoverlabel_font_size=14
    )
           
    return st.plotly_chart(fig, use_container_width=True, height=800)

def make_box_plot_cpi(df, category):
    fig = px.box(df, y=category, labels={
        "variable": "CPI Categories",
        "value": "Index Value (2019 as base year)"}, 
        title="Distribution of CPI Categories",
        points="all")

    # fig.update_layout(hovermode="x unified")

    fig.update_layout(
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14
    )

    st.plotly_chart(fig)


def make_2d_scatter(df, selected_years, cat1, cat2):
    # Extract the start and end years from the selected range
    start_year, end_year = selected_years

    # Filter the DataFrame based on the selected year range
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Create the scatter plot using Plotly Express
    fig = px.scatter(
        filtered_df, 
        x=cat1, 
        y=cat2, 
        title=f'Scatter Plot of {cat1} vs {cat2} ({start_year}-{end_year})',
        labels={cat1: cat1, cat2: cat2}
    )

    # Update the layout of the figure
    fig.update_layout(
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        xaxis_title_font_size=16, 
        xaxis_tickfont_size=14, 
        yaxis_title_font_size=16, 
        yaxis_tickfont_size=14
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)

def make_3d_scatter(df, selected_years, cat1, cat2, cat3):
    # Extract the start and end years from the selected range
    start_year, end_year = selected_years

    # Filter the DataFrame based on the selected year range
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Create the 3D scatter plot using Plotly Express
    fig = px.scatter_3d(
        filtered_df,
        x=cat1,
        y=cat2,
        z=cat3,
        title=f'3D Scatter Plot of {cat1}, {cat2}, and {cat3} ({start_year}-{end_year})',
        labels={cat1: cat1, cat2: cat2, cat3: cat3}
    )

    # Update the layout of the figure
    fig.update_layout(
        title_font_size=16,
        legend_title_font_size=14,
        legend_font_size=14,
        scene=dict(
            xaxis_title_font_size=16,
            yaxis_title_font_size=16,
            zaxis_title_font_size=16,
            xaxis_tickfont_size=14,
            yaxis_tickfont_size=14,
            zaxis_tickfont_size=14
        )
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)