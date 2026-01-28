import pandas as pd 
import sqlite3
from sqlalchemy import create_engine


conn = sqlite3.connect(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\chinook.db')

cur = conn.cursor()
cur.execute('SELECT * FROM employees LIMIT 5;')
results = cur.fetchall()
(results)

df = pd.DataFrame(results)
df.head()
cur.close() 
conn.close() 

conn = sqlite3.connect(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\chinook.db')
df = pd.read_sql('SELECT * FROM employees LIMIT 5;', conn,
                 index_col='EmployeeId', 
                 parse_dates=['BirthDate', 'HireDate'])

# (df.info())
# (df.head())

(df['ReportsTo'].isna().sum())
(df['ReportsTo'].mean())
(df['ReportsTo'] > 1.75)

df['City'] = df['City'].astype('category')




conn = sqlite3.connect(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\chinook.db')
df = pd.read_sql_query('SELECT * FROM employees LIMIT 5;', conn,
                       index_col='EmployeeId', 
                       parse_dates=['BirthDate', 'HireDate'])


engine = create_engine(r'sqlite:///C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\chinook.db')
connection = engine.connect()

df = pd.read_sql_table('employees', con=connection,
                       index_col='EmployeeId',
                       parse_dates=['BirthDate', 'HireDate'])
connection.close()

# conn = sqlite3.connect(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\chinook.db')
# df.to_sql('employees3', conn)

print((pd.read_sql_query('SELECT * FROM employees3;', conn).head()))

pd.DataFrame().to_sql('employees3',
                      conn,
                      if_exists='replace')

(pd.read_sql_query('SELECT * FROM employees3;', conn).head())

df.to_sql('employees3',
          conn, 
          if_exists='replace')

(pd.read_sql_query('SELECT * FROM employees3;', conn).head())
conn.close()

