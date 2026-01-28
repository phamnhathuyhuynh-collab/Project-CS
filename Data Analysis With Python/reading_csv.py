import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 



df = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\btc-market-price.csv', header=None)
df.columns = ['Timestamp', 'Price']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

df = pd.read_csv(
    r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\btc-market-price.csv',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
)



#df.plot() #plt.plot(df.index, df['Price'])


#More challenging parsing
eth = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\eth-price.csv')
eth = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\eth-price.csv', parse_dates=True)
eth.dtypes
pd.to_datetime(eth['UnixTimeStamp']).head()
pd.to_datetime(eth['Date(UTC)']).head()

pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\eth-price.csv', parse_dates=[0]).head()

eth = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\eth-price.csv', parse_dates=True, index_col = 0)


prices = pd.DataFrame(index=df.index)
prices['Bitcoin'] = df['Price']
prices['Ether'] = eth['Value']
prices.head()
prices.loc['2017-12-01':'2018-01-01'].plot(figsize=(12, 6))
plt.show()