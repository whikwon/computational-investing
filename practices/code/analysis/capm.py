from pandas_datareader import data
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# stock and market index tickers
stock_symbol = 'FB'
mrkt_symbol = '^GSPC'

# set time period for historical prices
end_time = time.strftime('%m/%d/%Y')
start_time = end_time[:6] + str(int(end_time[-4:]) - 20)

# retreive historical prices for stock
stock = data.DataReader(stock_symbol,
                        data_source='yahoo', start=start_time, end=end_time)

# retrieve historical prices for market index
mrkt = data.DataReader(mrkt_symbol,
                       data_source='yahoo', start=start_time, end=end_time)

# simplify data sets
stock_simple = stock.rename(columns={'Adj Close': 'Stock'})
mrkt_simple = mrkt.rename(columns={'Adj Close': 'Mrkt'})
# combine stock and market index closing prices
data_simple = pd.concat([mrkt_simple, stock_simple],
                        axis=1, join='inner')[['Mrkt', 'Stock']]

# keep only values by month
data_month = data_simple.asfreq('M', method='ffill')

# calculate percent change of closing prices
data_month['MrktPctChg'] = data_month.Mrkt.pct_change(1)
data_month['StockPctChg'] = data_month.Stock.pct_change(1)

# plot monthly returns
scat_data = data_month.tail(59)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
ax1.scatter(scat_data['MrktPctChg'],
            scat_data['StockPctChg'],
            label='Monthly Returns', color='blue',
            edgecolors='none', alpha=0.5)
ax1.grid(True)

# set x and y coordinate limits
x_corr = (-0.05, 0.05)
y_corr = (-0.05, 0.05)

# draw lines for x and y axes
ax1.plot(x_corr, (0, 0), color='black', alpha=0.4)
ax1.plot((0, 0), y_corr, color='black', alpha=0.4)

# reset x and y coordinate limits back to original
ax1.set_xlim(x_corr[0], x_corr[1])
ax1.set_ylim(y_corr[0], y_corr[1])

# set axis labels
ax1.set_xlabel('Market Index Monthly Returns')
ax1.set_ylabel(stock_symbol + ' Monthly Returns')

# create an array of x (i.e. market index) values
x = np.linspace(x_corr[0] + 0.005, x_corr[1] - 0.005)

from scipy import stats

# run regression to calculate beta
slope, intercept, r, _, _ = stats.linregress(y=scat_data['StockPctChg'], x=scat_data['MrktPctChg'])

# define function for regression equation


def month(x):
    return intercept + slope * x


# plot beta for monthly returns
ax1.plot(x, month(x), color='magenta', linestyle='-',
         linewidth=2, label='Beta', alpha=0.8)

# add legend
ax1.legend(loc='upper center',
           bbox_to_anchor=(0.5, -0.075), ncol=2, fontsize='large')

# add Beta and R2 stats to plot
ax1.text(-0.038, 0.042,
         'Beta: ' + str(np.round(slope, 3)),
         fontsize=12)
ax1.text(-0.038, 0.035,
         'R2: ' + str(np.round(r, 3)),
         fontsize=12)


# calculate rolling betas
period = 12
for date in data_month.index[1:]:
    data = data_month.loc[:date].tail(period - 1)
slope, incercept, r, _, _ = stats.linregress(y=data['StockPctChg'], x=data['MrktPctChg'])
data_month.loc[date, 'Beta'] = slope

# plot only betas with 60 data points
if len(data_month) > period:
    to_plot = data_month[data_month.index[period]:]
else:
    to_plot = data_month
ax2.plot(to_plot.index, to_plot.Beta, color='blue',
         linewidth=2, alpha=0.5, label='5-year Rolling Beta')
ax2.grid(True)

# get x coordinate limits
x_corr = ax2.get_xlim()

# draw lines for x axis
ax2.plot(x_corr, (1, 1), color='black', alpha=0.4)

# add y label
ax2.set_ylabel(stock_symbol + ' Beta')

# add legend
ax2.legend(loc='upper center',
           bbox_to_anchor=(0.5, -0.075), ncol=1, fontsize='large')

# display plot
fig.show()