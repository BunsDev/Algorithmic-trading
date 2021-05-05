import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as plt
from ta.trend import ADXIndicator


df = pd.read_csv("test.csv")
print(df)


"""df = pd.read_csv("test.csv")
#df['Date'] = df['Date']+ ' ' + df['Time'].str.slice(0,-3)
df = df.set_index(pd.DatetimeIndex(df['Date'].values))
print(df)
figure = go.Figure(
    data = [
        go.Candlestick(
            x = df.index,
            low = df['Low'],
            high = df['High'],
            close = df['Close'],
            open = df['Open'],
            increasing_line_color = 'green',
            decreasing_line_color = 'red'
        )
    ]
)
figure.show()"""
