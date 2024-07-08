import streamlit as st
import pandas as pd
import data_loader as dlr
import charts
import plotly.express as px
import numpy as np

st.set_page_config(page_title="CPI Analysis", layout="wide", page_icon="📈", initial_sidebar_state="expanded")