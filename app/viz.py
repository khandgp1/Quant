import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_stock_data(df):
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Stock Viz
    fig.add_trace(
        go.Scatter(x=df['Date'], y=df['Close_Norm'], customdata=df['Close'], hovertemplate='%{customdata:$.2f}', name='Price'),
        secondary_y=False, 
        )

    # Set Hoverlabels
    fig.update_traces(xhoverformat="%b %d, %Y")
    fig.update_layout(hovermode='x unified', showlegend=False)
    
    # Set axes
    fig.update_xaxes(title_text="Date")
    
    return fig

def plot_volume_data(fig, df, options):
    
    if 'Volume' in options:
        fig.add_trace(
                go.Scatter(x=df['Date'], y=df['Volume_Norm'], customdata=df['Volume']/1_000, hovertemplate='%{customdata:,d} K', name='Volume'),
                secondary_y=True
            )
    
    return fig

def plot_multiplier_data(fig, df, options):
    
    if 'Multiplier' in options:
        fig.add_trace(
            go.Scatter(x=df['Date'], y=df['Multiplier_Norm'], customdata=df['Multiplier'], hovertemplate='%{customdata:.4f}', name='Multiplier'),
            secondary_y=True
        )
    
    return fig