import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
from scipy import stats

# 1달 단위로 데이터를 사용해야 yahoo에 있는 beta랑 같아진다. 왜?
# assets = ['FB', '^GSPC']
#
# fb = wb.DataReader(assets[0], 'yahoo', '2014-01-01', '2017-01-01')
# gspc = wb.DataReader(assets[1], 'yahoo', '2014-01-01', '2017-01-01')
#
# monthly_prices = pd.concat([fb['Close'], gspc['Close']], axis=1)
# monthly_prices.columns = ['FB', '^GSPC']
# monthly_returns = monthly_prices.pct_change(1)
# clean_monthly_returns = monthly_returns.dropna(axis=0)  # drop first missing row
#
# X = clean_monthly_returns['^GSPC']
# y = clean_monthly_returns['FB']
#
# slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)
# print(slope)

assets = ['FB', '^GSPC']
portfolio=pd.DataFrame()
for t in assets:
	portfolio[t] = wb.DataReader(t, data_source='yahoo',start='2015-1-1',end='2017-12-31')['Adj Close']

set_ret = portfolio.asfreq('M', method='ffill')
sec_ret = set_ret.pct_change(1)
# We assume that there are 250 working days in one year.
covariance=sec_ret.cov()*250
print(covariance)
marketcov=covariance.iloc[0, 1]
print(marketcov)
market_var=sec_ret['^GSPC'].var()*250
print(market_var)
market_beta=marketcov/market_var
print(market_beta)
# Expected Return
Exp_ret= 0.025+market_beta*0.05
print(Exp_ret)
# Calculation os Sharpe ratio
sharpe=(Exp_ret-0.025)/(sec_ret['FB'].std()*250**0.5)
print(sharpe)

# pyfolio 보면서 공부하면 도움 될 듯.
import pyfolio as pf
stock_rets = pf.utils.get_symbol_rets('FB')
pf.create_returns_tear_sheet(stock_rets, live_start_date='2015-12-1')
