import pandas as pd
import streamlit as st

from data import get_stock_data, normalize_data, calc_peak_multiplier, filter_date
from notes import get_notes
from sidebar import sidebar
from viz import plot_stock_data, plot_volume_data, plot_multiplier_data

# Config
st.set_page_config(layout="wide")

# Initialize
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'time_step' not in st.session_state:
    st.session_state.time_step = 'Day'

# Sidebar
ticker, end_date, start_date, ceiling, year_floor, year_ceiling, vol_ceiling, options = sidebar()

# Get Data
stock_info, stock_data = get_stock_data(ticker)
stock_data = filter_date(stock_data, end_date, start_date)

# Munge Stock Data
stock_data['Close_Norm'] = normalize_data(stock_data, 'Close')
stock_data['Volume_Norm'] = normalize_data(stock_data, 'Volume', limit=vol_ceiling)

# Calculate Multiplier from Peak Data
multiplier = calc_peak_multiplier(stock_data, 'Close', ceiling, year_floor, year_ceiling)
stock_data = stock_data.join(multiplier)

# Stock Viz
st.header(stock_info['longName'])
fig = plot_stock_data(stock_data)
fig = plot_volume_data(fig, stock_data, options)
fig = plot_multiplier_data(fig, stock_data, options)
st.plotly_chart(fig, theme=None, use_container_width=True)    

# Notes
# st.write(get_notes(stock_data))
if 'Notes' in options:
    st.dataframe(get_notes(stock_data), use_container_width=True)

# Stock Table
if 'Stock Data' in options:
    st.dataframe(stock_data, use_container_width=True)
