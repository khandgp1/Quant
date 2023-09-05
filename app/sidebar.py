import pandas as pd
import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

def sidebar():
    
    # Stock Ticker Options
    tickers = ('OXY', 'ENPH', '^DJI', '^GSPC' ,'^IXIC' )

    # Market Analysis Title 
    st.sidebar.title('Market Analysis')

    # Selected Ticker
    ticker = st.sidebar.radio('Select Trading Symbol', tickers)

    with st.sidebar.expander('Date Selection'):

        placeholder_end_data = st.empty()

        # Date Step Options
        st.session_state.time_step = st.selectbox('End Date Time Step', ['Day', 'Week', 'Month', 'Year', '5 Year'], on_change=update_date_range_options)

        # Select Date
        if st.session_state.time_step == 'Day': step = datetime.timedelta(days=1)
        if st.session_state.time_step == 'Week': step = datetime.timedelta(days=7)
        if st.session_state.time_step == 'Month': step = datetime.timedelta(days=30)
        if st.session_state.time_step == 'Year': step = datetime.timedelta(days=365)
        if st.session_state.time_step == '5 Year': step = datetime.timedelta(days=365*5)
        st.session_state.end_date = placeholder_end_data.slider('End Date', min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today(), value=st.session_state.default_end_date, step=step)
        end_date = pd.to_datetime(st.session_state.end_date)

        # Range Selection
        date_range = st.selectbox('Date Range Selection', ['None', '20 Years', '10 Years', '5 Years', '50 Days'])
        if date_range == 'None':
            start_date = None
        else:
            if date_range == '20 Years': start_date = end_date - relativedelta(years=20)
            if date_range == '10 Years': start_date = end_date - relativedelta(years=10)
            if date_range == '5 Years': start_date = end_date - relativedelta(years=5)
            if date_range == '50 Days': start_date = end_date - relativedelta(days=50)
            start_date = pd.to_datetime(start_date)
    
    with st.sidebar.expander('Multiplier Options'):

        # Multiplier Ceiling
        mult_ceiling = st.number_input('Max Multiplier Filter', min_value=1, value=1000, step=1)
        
        # Date Floor
        current_year = datetime.date.today().year
        num_of_year_since_1900 = current_year-1900
        year_options =  [current_year - year for year in range(num_of_year_since_1900+1)] # starting from current year going in reverse to 1900
        year_floor = st.selectbox('Min Year for Multiplier Filter', year_options, index=num_of_year_since_1900)
        
        # Date Ceiling
        year_ceiling = st.selectbox('Max Year for Multiplier Filter', year_options, index=0)
    
    with st.sidebar.expander('Volume Options'):

        # Volume Ceiling
        vol_ceiling_help_txt = 'If 0 then volume ceiling is set to None'
        vol_ceiling = st.number_input('Max Volume Filter (in thousands)', step=10_000, help=vol_ceiling_help_txt) * 1_000
        if vol_ceiling == 0: vol_ceiling = None
    
    # Options
    options = st.sidebar.multiselect('Options', ['Multiplier', 'Volume', 'Stock Data', 'Chat', 'Notes'],
                                     placeholder='Addtional Stock Data')
    
    # Chat Input
    if 'Chat' in options:
        
        if prompt := st.chat_input("Notes"):
            st.session_state.messages.append(prompt)

        # Chat Display
        for message in st.session_state.messages:
            chat =  st.sidebar.chat_message(name='user', avatar='🦖')
            chat.write(message)
    
    return ticker, end_date, start_date, mult_ceiling, year_floor, year_ceiling, vol_ceiling, options

def update_date_range_options():
    st.session_state.default_end_date = st.session_state.end_date
