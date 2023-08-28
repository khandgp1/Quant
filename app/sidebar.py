import streamlit as st
import datetime

def sidebar():
    
    # Stock Ticker Options
    tickers = ('OXY', '^DJI', '^GSPC' ,'^IXIC' )

    # Market Analysis Title 
    st.sidebar.title('Market Analysis')

    # Selected Ticker
    ticker = st.sidebar.radio('Select Trading Symbol', tickers)
    
    # Multiplier Ceiling
    mult_ceiling = st.sidebar.number_input('Max Multiplier Filter', min_value=1, value=1000, step=1)
    
    # Date Floor
    current_year = datetime.date.today().year
    num_of_year_since_1900 = current_year-1900
    year_options =  [current_year - year for year in range(num_of_year_since_1900+1)] # starting from current year going in reverse to 1900
    year_floor = st.sidebar.selectbox('Min Year for Multiplier Filter', year_options, index=num_of_year_since_1900)
    
    # Date Ceiling
    year_ceiling = st.sidebar.selectbox('Max Year for Multiplier Filter', year_options, index=0)
    
    # Volume Ceiling
    vol_ceiling_help_txt = 'If 0 then volume ceiling is set to None'
    vol_ceiling = st.sidebar.number_input('Max Volume Filter (in thousands)', step=10_000, help=vol_ceiling_help_txt) * 1_000
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
    
    return ticker, mult_ceiling, year_floor, year_ceiling, vol_ceiling, options