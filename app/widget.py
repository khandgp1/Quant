import streamlit as st
from data import fetch_stock_data, filter_date, normalize_data, calc_peak_multiplier, normalize_dfs
from viz import plot_stock_data, plot_volume_data, plot_multiplier_data, plot_stock_subset_data

@st.cache_data
def get_stock_data(tick):
	return fetch_stock_data(tick)

def ticker_view(ticker, end_date, start_date, vol_ceiling, mult_ceiling, mult_year_floor, mult_year_ceiling, options):

	# Get Data
	stock_info, stock_data = get_stock_data(ticker)
	stock_data = filter_date(stock_data, end_date, start_date)

	# Munge Stock Data
	stock_data['Close_Norm'] = normalize_data(stock_data, 'Close')
	stock_data['Volume_Norm'] = normalize_data(stock_data, 'Volume', limit=vol_ceiling)

	# Calculate Multiplier from Peak Data
	multiplier = calc_peak_multiplier(stock_data, 'Close', mult_ceiling, mult_year_floor, mult_year_ceiling)
	stock_data = stock_data.join(multiplier)

	# Stock Viz
	st.header(stock_info['longName'])
	fig = plot_stock_data(stock_data)
	fig = plot_volume_data(fig, stock_data, options)
	fig = plot_multiplier_data(fig, stock_data, options)
	st.plotly_chart(fig, theme=None, use_container_width=True)

	return stock_data

def ticker_overview(ticker, end_date, start_date):

	# Get Data
	stock_info, stock_data = get_stock_data(ticker)
	stock_data_filtered = stock_data.copy()
	stock_data_filtered = filter_date(stock_data_filtered, end_date, start_date)

	# Normalize
	[stock_data, stock_data_filtered] = normalize_dfs([stock_data, stock_data_filtered], 'Close')

	# Stock Viz
	fig = plot_stock_data(stock_data)
	fig = plot_stock_subset_data(fig, stock_data_filtered)
	fig.update_layout({'uirevision': 'brass monkey'}, overwrite=True)
	st.plotly_chart(fig, theme=None, use_container_width=True)
