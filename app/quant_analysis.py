import datetime
import streamlit as st

from notes import get_notes
from sidebar import sidebar
from widget import ticker_view, ticker_overview

# Config
st.set_page_config(layout="wide")

# Initialize
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'default_end_date' not in st.session_state:
    st.session_state.default_end_date = datetime.date.today()

if 'time_step' not in st.session_state:
    st.session_state.time_step = 'Day'

# Sidebar
ticker, end_date, start_date, ceiling, year_floor, year_ceiling, vol_ceiling, options = sidebar()

main_tab, energy_tab = st.tabs(['Main', 'Energy'])

# Main Tab Stock View
with main_tab:
	stock_data = ticker_view(ticker, end_date, start_date, vol_ceiling, ceiling, year_floor, year_ceiling, options)
	ticker_overview(ticker, end_date, start_date)

# Energy Tab Analysis
with energy_tab:

	col1, col2 = st.columns([1, 6])
	load_energy_tab = col1.toggle('Load')

	col2.title('Top 20 Winners in the 2022 Bear Market')
	st.divider()

	if load_energy_tab:
		for i_tick in ['OXY', 'HES', 'MPC', 'XOM', 'SLB', 'APA', 'HAL', 'FSLR', 'VLO', 'MRO', 'COP', 'STLD', 'EQT', 'CVX', 'MCK', 'CAH', 'EOG', 'ENPH', 'MRK', 'CI']:
			ticker_view(i_tick, end_date, start_date, vol_ceiling, ceiling, year_floor, year_ceiling, options)

# Notes
if 'Notes' in options:
    st.dataframe(get_notes(stock_data), use_container_width=True)

# Stock Table
if 'Stock Data' in options:
    st.dataframe(stock_data, use_container_width=True)

