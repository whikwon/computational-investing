"""
1. download list of kospi 200
"""

import csv
import requests
import re
from bs4 import BeautifulSoup

BASE_URL = 'http://finance.naver.com/sise/entryJongmok.nhn?&page='

for i in range(1, 22):
    try:
        url = BASE_URL + str(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        items = soup.find_all('td', {'class': 'ctg'})

        for item in items:
            txt = item.a.get('href')
            k = re.search('[\d]+', txt)
            if k:
                code = k.group()
                name = item.text
                data = code, name

                with open('kospi200.csv', 'a') as f:
                    writer=csv.writer(f)
                    writer.writerow(data)
    except:
        pass
    finally:
        temp_for_sort = []
        with open('kospi200.csv', 'r') as in_file:
            for sort_line in in_file:
                temp_for_sort.append(sort_line)
        with open('kospi200.csv', 'w') as out_file:
            seen = set()
            for line in temp_for_sort:
                if line in seen:
                    continue
                seen.add(line)
                out_file.write(line)
