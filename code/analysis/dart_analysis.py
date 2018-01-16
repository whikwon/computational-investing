"""
1. Check whether right issues(유상증자) occurred
"""
import pandas as pd

DATA_DIR = './data/'

dart = pd.read_csv('./data/dart.csv')
rights_issue = dart['rpt_nm'][dart['rpt_nm'].str.contains('유상')]
