"""
1. stock data download from yahoo finance
"""

from pandas_datareader import data, wb
import pandas as pd

START_DT = '20160101'
END_DT = '20171231'
kospi200_list_path = './data/kospi200.csv'
kospi200_price_path = 'kospi_price.csv'

kospi200 = pd.read_csv(kospi200_list_path)
bucket = pd.DataFrame()

for i, c in enumerate(kospi200.iloc[:, 0]):
    crp_cd = '{0:06d}.KS'.format(c)
    error_occurred_list = []
    try:
        df = data.DataReader(crp_cd, 'yahoo', start=START_DT, end=END_DT)
        df['crp_cd'] = crp_cd[:-3]
        bucket = bucket.append(df)
        print(i)
    except:
        error_occurred_list.append(crp_cd)
        continue

bucket.to_csv(kospi200_price_path)
