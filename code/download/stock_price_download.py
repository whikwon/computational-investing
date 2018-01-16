"""
1. download stock price
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# 네이버 : 035420
# 한전 : 015760


KOSPI_URL = 'http://finance.daum.net/quote/kospi_yyyymmdd.daum?'
STOCK_URL = 'http://finance.daum.net/item/foreign_yyyymmdd.daum?'

class LoadStockData(object):
    def __init__(self):
        pass


def _get_soup(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    return soup


def _organize_data(soup, kospi=False):
    _organized_data = []
    date = soup.find_all(name='td', attrs={'class': 'datetime2'})
    num = soup.find_all(name='td', attrs={'class': 'num'})
    if kospi:
        num2 = soup.find_all(name='td', attrs={'class': 'num2'})
    num_data = len(date)
    for i in range(num_data):
        if kospi:
            data_row = [date[i].text] + [i.text for i in num[6 * i:6 * (i + 1)]] \
                + [i.text for i in num2[2 * i:2 * (i + 1)]]
        else:
            data_row = [date[i].text] + [i.text for i in num[7 * i:7 * (i + 1)]]
        _organized_data.append(data_row)
    return _organized_data



# 일단 페이지 수로 받을 수 있게 만들어보자
def _collect_data(num_pages=10, code='015760', kospi=False):
    if kospi:
        url = KOSPI_URL
    else:
        url = STOCK_URL
    collection = []
    for i in range(1, num_pages+1):
        if kospi:
            url_page = url + 'page={}'.format(i)
        else:
            url_page = url + 'page={}&code={}'.format(i, code)
        soup = _get_soup(url_page)
        data = _organize_data(soup, kospi=kospi)
        collection.extend(data)
    return collection


# pandas 형태로 데이터 변환
def to_pandas_format(collection, kospi=False):
    if kospi:
        columns = ['date', 'change', 'change_per', 'trade_qty', 'trade_money',
                   'foreign_money', 'agency', 'end_price', 'domestic_money']
    else:
        columns = ['date', 'foreign_stock_qty', 'foreign_stock_ratio',
                   'foreign_bid', 'agency_bid', 'end_price', 'change', 'change_per']

    data_pd = pd.DataFrame(collection, columns=columns)
    data_pd['date'] = data_pd['date'].apply(lambda x: datetime.strptime('20' + x, '%Y.%m.%d'))
    data_pd['change_per'] = data_pd['change_per'].apply(lambda x:float(x[:-1]))
    data_pd['change'] = data_pd['change'].apply(lambda x: float(x.replace(',','').\
                        replace('-','').replace('▲', '+').replace('▼','-')))
    data_pd['end_price'] = data_pd['end_price'].apply(lambda x: float(x.replace(',', '')))
    if kospi:
        data_pd['trade_qty'] = data_pd['trade_qty'].apply(lambda x: int(x.replace(',', '')))
        data_pd['trade_money'] = data_pd['trade_money'].apply(lambda x: int(x.replace(',', '')))
        data_pd['agency'] = data_pd['agency'].apply(lambda x: int(x.replace(',', '')))
        data_pd['foreign_money'] = data_pd['foreign_money'].apply(lambda x: int(x.replace(',', '')))
        data_pd['domestic_money'] = data_pd['domestic_money'].apply(lambda x: int(x.replace(',','')))
    else:
        data_pd['foreign_stock_ratio'] = data_pd['foreign_stock_ratio'].apply(lambda x:float(x[:-1]))
        data_pd['foreign_stock_qty'] = data_pd['foreign_stock_qty'].apply(lambda x: int(x.replace(',', '')))
        data_pd['foreign_bid'] = data_pd['foreign_bid'].apply(lambda x: int(x.replace(',', '')))
        data_pd['agency_bid'] = data_pd['agency_bid'].apply(lambda x: int(x.replace(',', '')))

    return data_pd


def main():
    kospi = _collect_data(num_pages=180
                        ,kospi=True)
    kospi = to_pandas_format(kospi, kospi=True)
    kospi.to_csv('kospi_downloaded_data.csv', index=False)

    stock = _collect_data(num_pages=60)
    stock = to_pandas_format(stock)
    stock.to_csv('stock_download_data.csv', index=False)

if __name__ == '__main__':
    main()
