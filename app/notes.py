from datetime import date
import pandas as pd
from data import get_close_price

def get_notes(stock_data):
    
    stock_data = stock_data.copy()
    stock_data['Date'] = stock_data['Date'].dt.date
    
    # Build Peak-Trough Notes
    peak_trough_dates = [
        (date(2005, 10, 20),  date(2008, 5, 8)),
        (date(2008, 11, 20),  date(2010, 5, 3)),
        (date(2008, 11, 20),  date(2011, 5, 2)),
        (date(2011, 10, 3),   date(2014, 6, 23)),
        (date(2016, 1, 20),   date(2018, 6, 11)),
        (date(2020, 10, 28),  date(2022, 11, 7)),
    ]
    
    # Build Peak-Trough Dateframe
    notes = pd.DataFrame(
        [[trough_dt, peak_dt, get_close_price(stock_data, trough_dt), get_close_price(stock_data, peak_dt)]
         for trough_dt, peak_dt in peak_trough_dates],
        columns=['Buy Date', 'Sell Date', 'Buy Price', 'Sell Price']
    )

    # Calculate Multiplier / Format
    notes['Multiplier'] = notes['Sell Price'] / notes['Buy Price']
    notes['Multiplier'] = notes['Multiplier'].map('x{:.2f}'.format)
    
    # Hold Time
    notes['Hold'] = pd.to_timedelta(notes['Sell Date'] - notes['Buy Date']).dt.days / 365.2425
    notes['Hold'] = notes['Hold'].map('{:.2f} years'.format)

    # Format Currency
    notes['Buy Price'] = notes['Buy Price'].map('${:,.2f}'.format)
    notes['Sell Price'] = notes['Sell Price'].map('${:,.2f}'.format)
    
    return notes