"""
1. dart information check
2. dart info url: http://dart.fss.or.kr/dsap001/guide.do
3. columns : 'crp_cd', 'crp_cls', 'crp_nm', 'flr_nm', 'rcp_dt', 'rcp_no', 'rmk', 'rpt_nm'
"""
import requests
import pandas as pd
from pandas.io.json import json_normalize

AUTH_KEY = '08b144ec6146d0be11a34ce672199eb8d89d53cb'
BASE_URL = 'http://dart.fss.or.kr/api/search.json?auth={}&page_set={}&crp_cd={}&start_dt={}&end_dt={}'
PAGE_SET = 100
START_DT = '20160101'
END_DT = '20171231'
kospi200_list_path = './data/kospi200.csv'

kospi200 = pd.read_csv(kospi200_list_path)
bucket = pd.DataFrame()
for c in kospi200.iloc[:, 0]:
    c_data = pd.DataFrame()
    crp_cd = '%06d' % (c)
    end_dt = END_DT
    while end_dt > START_DT:
        url = BASE_URL.format(AUTH_KEY, PAGE_SET, crp_cd, START_DT, end_dt)
        raw_json = requests.get(url).json()['list']
        c_data = c_data.append(json_normalize(raw_json))
        new_end_dt = c_data['rcp_dt'].min()
        if new_end_dt == end_dt:
            break
        else:
            end_dt = new_end_dt
    bucket = bucket.append(c_data)

# bucket.columns = ['종목코드', '법인구분', '회사명', '공시 제출인명', '공시 접수일자', '접수번호', '조합 문자', '공시구분+보고서명+기타정보']


bucket.to_csv('dart.csv')

