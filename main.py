#moving average crossovertrading algo
#generates buy signal when short term moving av crosses
#above longer term moving avergae
#sells signals when shorter term moving av cross below longer term movoing av

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#generate sample data
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', end='2022-12-31')
prices = np.random.normal(loc = 100, scale = 10, size = len(dates))
df = pd.DataFrame({'Date':dates, 'Price':prices})
df.set_index('Date', inplace = True)

#calc moving av
short_window = 20
long_window = 50
df['Short_MA'] = df['Price'].rolling(window = short_window, min_periods = 1).mean()
df['Long_MA'] = df['Price'].rolling(window = long_window, min_periods = 1).mean()

#generate buy/sell signals
df['Signal'] = 0
df['Signal'][short_window:] = np.where(df['Short_MA'][short_window:] > df['Long_MA'][short_window:], 1, 0)
df['Position'] = df['Signal'].diff()

#plotting
plt.figure(figsize = (12, 6))
plt.plot(df['Price'], label = 'Price')
plt.plot(df['Short_MA'], label = f'Short MA ({short_window} days)')
plt.plot(df['Long_MA'], label = f'Long MA ({long_window} days)')
plt.plot(df[df['Position'] == 1].index, df['Short_MA'][df['Position'] == 1], '^', markersize = 10, color = 'g', lw = 0, label = 'Buy Signals')
plt.plot(df[df['Position'] == -1].index, df['Short_MA'][df['Position'] == -1], 'v', markersize = 10, color = 'r', lw = 0, label ='Sell Signal')
plt.title('Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
