"""
1. Choose stocks had right issues(유상증자) in 2 years
2. Draw 2-year date/price graphs for each stock
3. Draw vertical line in the graph to indicate occurrence of right issues
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

plt.rcParams["font.family"] = 'NanumGothicCoding'
plt.rcParams['font.size'] = 12.
plt.rcParams['xtick.labelsize'] = 12.
plt.rcParams['ytick.labelsize'] = 12.
plt.rcParams['axes.labelsize'] = 10.
plt.rcParams["figure.figsize"] = (14, 6)
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.unicode_minus'] = False

dart = pd.read_csv('./data/dart.csv')
stock_price = pd.read_csv('./data/kospi_price.csv')


rights_issue = dart[dart['rpt_nm'].str.contains('증자')][['crp_cd', 'rcp_dt', 'crp_nm']].drop_duplicates()
crp_cd_rights_issue = rights_issue['crp_cd'].drop_duplicates()

for c in crp_cd_rights_issue:
    crp_nm = dart[dart['crp_cd'] == c]['crp_nm'].iloc[0]
    crp_cd = '{0:06d}'.format(c)
    crp_cd_stock_price = stock_price[stock_price['crp_cd'] == c]
    crp_cd_stock_price = crp_cd_stock_price[['Date', 'Close']]
    rights_issue_dt = rights_issue[rights_issue['crp_cd'] == c]['rcp_dt'].apply(lambda x: dt.datetime.strptime(str(x), '%Y%m%d'))

    fig, ax = plt.subplots()
    ax.plot_date(crp_cd_stock_price['Date'], crp_cd_stock_price['Close'], linestyle='-', markersize=0, color='r', linewidth=1)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    fig.autofmt_xdate(rotation=30)
    for i in rights_issue_dt:
        plt.axvline(mdates.date2num(i), color='g', linewidth=1)
    plt.xlim(dt.datetime(2016, 1, 1), dt.datetime(2018, 1, 1))
    plt.title(crp_nm)
    plt.show()