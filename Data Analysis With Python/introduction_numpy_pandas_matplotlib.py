import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook


def get_historic_price(symbol, after='2018-09-01'):
    
    url = 'https://api.kraken.com/0/public/OHLC'
    pair = f"{symbol.upper()}USD" # XBTUSD when symbol='xbt' for example
    
    resp = requests.get(url, params={
        "pair": pair,
        'interval': 60,
        'since': str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    
    data = resp.json()
    
    results_key = [k for k in data['result'].keys() if k != 'last'][0]
    results = [
        (close_time, float(open), float(high), float(low), float(close), float(volume))
        for (close_time, open, high, low, close, vwap, volume, count)
        in data['result'][results_key]
    ]
    df = pd.DataFrame(results, columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df

last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
btc = get_historic_price('btc', after=last_week)
eth = get_historic_price('eth', after=last_week)


with pd.ExcelWriter(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\crypto.xlsx') as writer:
    btc.to_excel(writer, sheet_name='BitCoin')
    eth.to_excel(writer, sheet_name='Ether')