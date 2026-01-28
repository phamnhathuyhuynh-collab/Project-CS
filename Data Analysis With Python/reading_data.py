import pandas as pd

filePath = r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\btc-market-price.csv'
# with open(filePath, 'r') as reader: 
#     for index, line in enumerate(reader.readlines()):
#         if index < 10:
#             print(index, line)

csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
pd.read_csv(csv_url).head()

df =pd.read_csv(filePath)

df = pd.read_csv(filePath, 
                 header=None)

df = pd.read_csv(filePath,
                 header=None,
                 na_values=['', '?', '-'])

df = pd.read_csv(filePath,
                 header=None,
                 na_values=['', '?', '-'],
                 names=['Timestamp','Price']
                 )

df = pd.read_csv(filePath,
                 header=None, 
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'}
                 )

# df['Timestamp'] = pd.to_datetime(df['Timestamp'])



df = pd.read_csv(filePath, 
                 header=None, 
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'}
                # parse_dates=[0]
)

df['Timestamp'] = pd.to_datetime(
    df['Timestamp'],
    format='%d/%m/%y %H:%M', 
    errors='coerce'
)

df = pd.read_csv(filePath, 
                 header=None, 
                 na_values=['','?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price':'float'}
                 )

df['Timestamp'] = pd.to_datetime(
    df['Timestamp'],
    format='%d/%m/%y %H:%M', 
    errors='coerce'
)

df.set_index('Timestamp', inplace=True)

# df.reset_index(inplace=True)
df.head()



#More challenging parsing 

filePathCSV = r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\exam_review.csv'
    # with open(filePathCSV) as reading: 
    #     print(reading)

exam_df = pd.read_csv(filePathCSV)
exam_df = pd.read_csv(filePathCSV,
                      sep='>')


exam_df = pd.read_csv(filePathCSV, 
                      sep='>', 
                      decimal=',')
pd.read_csv(filePathCSV,
            sep='>',
            thousands=',')

(pd.read_csv(filePathCSV, 
                      sep='>',
                      decimal=',',
                      skiprows=[1, 3]))            

(pd.read_csv(filePathCSV,
            sep='>', 
            skip_blank_lines=False))

(pd.read_csv(filePathCSV,
             usecols=['first_name', 'last_name', 'age'], 
             sep='>' 
             ))

(pd.read_csv(filePathCSV,
             usecols=[0, 1, 2], 
             sep='>'))


exam_test1 = pd.read_csv(filePathCSV, 
                         sep='>'
                         )['last_name']
(type(exam_test1))


(exam_df.head())
exam_df.to_csv(r'exam.csv',
               index=None)
df1 = pd.read_csv(r'exam.csv')
df1.head()

