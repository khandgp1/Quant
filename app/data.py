import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

# Stock Data 
def get_stock_data(tick):
    period = 'max'
    tick_data = yf.Ticker(tick)
    return tick_data.info, tick_data.history(period=period).reset_index()

# Stock Normalize Data
def normalize_data(df, col, limit=None):
    
    # Filter to Ceiling Limit
    if limit is not None:
        df = df.loc[:, [col]]
        df[df[col] > limit] = None
    
    # Normalize
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[[col]])
    return scaled

# Calculate Multiplier from Peak
def calc_peak_multiplier(df, col, ceiling, year_floor, year_ceiling):
    
    # Munge Data
    mult_col = 'Multiplier'
    multiplier = df.loc[:, ['Date', col]]
    multiplier.rename(columns={col: mult_col}, inplace=True)
    
    # Apply Filter
    multiplier = multiplier[multiplier['Date'] >= pd.Timestamp(year_floor, 1, 1)]
    multiplier = multiplier[multiplier['Date'] <= pd.Timestamp(year_ceiling, 1, 1)]
    
    # Calculate Multiplier
    multiplier[mult_col] = multiplier[mult_col].max() / multiplier[mult_col]
    
    multiplier[mult_col + '_Norm'] = normalize_data(multiplier, mult_col, limit=ceiling)
    return multiplier.drop(columns=['Date'])

def get_close_price(df, date):
    return df.loc[df['Date'] == date, 'Close'].iloc[0]