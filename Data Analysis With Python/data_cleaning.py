import numpy as np
import pandas as pd

#Missing Data
a = np.array([1, 2, 3, np.nan, np.nan, 4])
a.sum(), a.mean()
a = np.array([1, 2, 3, np.nan, None, 4], dtype='float')
a
a = np.array([1, 2, 3, np.nan, np.nan, 4])
a.sum()
a.mean()
3 + np.inf
np.inf / 3
np.inf/ np.inf

b = np.array([1, 2, 3, np.inf, np.nan, 4], dtype='float')
b.sum()

(np.isnan(np.nan))
(np.isinf(np.inf))
(np.isfinite(np.nan), np.isfinite(np.inf))

(np.isnan(np.array([1, 2, 3, np.nan, np.inf, 4])))
(np.isinf(np.array([1, 2, 3, np.nan, np.inf, 4])))
(np.isfinite(np.array([1, 2, 3, np.nan, np.inf, 4])))

a = np.array([1, 2, 3, np.nan, np.nan, 4])
a[~np.isnan(a)].sum()
a[np.isfinite(a)].mean()

#Handling missing data with pandas 
(pd.isnull(np.nan), pd.isnull(None), pd.isna(np.nan), pd.isna(None))
(pd.notnull(np.nan), pd.notnull(None), pd.notna(np.nan), pd.notna(None))
(pd.isnull(pd.Series([1, np.nan, 7])))
(pd.notnull(pd.Series([1, np.nan, 7])))

(pd.isnull(pd.DataFrame({
    'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
})))

(pd.Series([1, 2, np.nan]).sum())

s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
(pd.notnull(s))
(pd.isnull(s))
(pd.notnull(s).sum())
(pd.isnull(s).sum())

(s.isnull())
(s.notnull())
(s.isnull().sum())
(s.notnull().sum())
(s[s.notnull()])
(s[s.isnull()])


(s.dropna())
(s)



df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})

(df)
(df.shape)
#(df.info())
(df.isnull())
(df.isnull().sum())
(df.dropna())
(df.dropna(axis=1))


df2 = pd.DataFrame({
    'Column A': [1, np.nan, 30],
    'Column B': [2, np.nan, 31],
    'Column C': [np.nan, np.nan, 100]
})

df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})

(df)
(df.dropna(how='any'))
(df.dropna(how='all'))

(df)
(df.dropna(thresh=3))
(df.dropna(thresh=3, axis='columns'))

(s)
(s.fillna(0))
(s.fillna(s.mean()))
(s)


#(s.fillna(method='ffill'))
#(s.fillna(method='bfill'))
(s)
(s.ffill())
(s.bfill())

(pd.Series([np.nan, 3, np.nan, 9]).ffill())
(pd.Series([np.nan, 3, np.nan, 9]).bfill())

(pd.Series([1, np.nan, 3, np.nan, np.nan]).ffill())
(pd.Series([1, np.nan, 3, np.nan, np.nan]).bfill())

(df)
(df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()}))
(df.ffill(axis=0))
(df.ffill(axis=1))

(s.dropna().count())
missing_values = len(s.dropna()) != len(s)
(missing_values)

missing_values1 = s.count() != len(s)
(missing_values1)

(pd.Series([True, False, False]).any())
(pd.Series([True, False, False]).all())

(s.isnull())
(pd.Series([1, np.nan]).isnull().any())
(pd.Series([1, 3]).isnull().any())

(s.isnull().values)
(s.isnull().values.any())

#Cleaning not null values
df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})
(df['Sex'].unique())
(df['Sex'].value_counts())
(df['Sex'].replace({'D': 'F', '?': 'M'}))
(df.replace({
    'Sex': {
        'D': 'F',
        'N': 'F'
    },
    'Age': {
        290 : 29
    }
}))


df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10
(df)


ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])
(ambassadors.duplicated())
('\n')
(ambassadors.duplicated(keep='last'))
('\n')
(ambassadors.duplicated(keep=False))
(ambassadors.drop_duplicates())
(ambassadors.drop_duplicates(keep='last'))
(ambassadors.drop_duplicates(keep=False))

players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})

(players)
(players.duplicated(subset=['Name'], keep='last'))
(players.drop_duplicates(subset=['Name']))
(players.drop_duplicates(subset=['Name'], keep='last'))

#TEXT HANDLING 

df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

(df)
(df['Data'].str.split('_'))
(df['Data'].str.split('_', expand=True))

df = df['Data'].str.split('_', expand=True)
df.columns = ['Year', 'Sex', 'Country', 'No Children']

(df['Year'].str.contains(r'\?')) #(df['Year]).str.contains('\\?')
(df['Country'].str.contains('U'))
(df['Country'].str.strip())
(df['Country'].str.replace(' ', ''))


(df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'), regex=True))

#Visualizations
import matplotlib.pyplot as plt 
x = np.arange(-10, 11)
plt.figure(figsize=(12, 6))
plt.title('My nice plot')
plt.plot(x, x**2)
plt.plot(x, -1*(x**2))

plt.subplot(1,2,1)
plt.plot(x, x**2, label="X^2")
plt.plot([0, 0, 0], [-10, 0, 100], label="Vertical Line")
plt.xlabel('X')
plt.ylabel('X Squared')
plt.legend()

plt.subplot(1,2,2)
plt.plot(x, -1*(x**2), label="-X^2")
plt.plot([-10, 0, 10], [-50, -50, -50], label="Horizontal Line")
plt.xlabel('X')
plt.ylabel('X Squared')
plt.legend()

plt.close()
#OOP interface 
fig, axes = plt.subplots(figsize=(12, 6))

axes.plot(x, x**2, color='red', linewidth=3, marker='o', markersize=8, label='X^2')
axes.plot(x, -1*(x**2), 'b--', label='-X^2')

axes.set_xlabel('X')
axes.set_ylabel('X squared')

axes.set_title('My Nice Plot')
axes.legend()
plt.close()

fig, axes = plt.subplots(figsize=(12, 6))
axes.plot(x, x+0, linestyle='solid')
axes.plot(x, x+1, linestyle='dashed')
axes.plot(x, x+2, linestyle='dashdot')
axes.plot(x, x+3, linestyle='dotted')

axes.set_title("My Nice Plot")
plt.close(fig)

#fig.show()

fig, axes = plt.subplots(figsize=(12, 6))

axes.plot(x, x+0, '-og', label="solid green")
axes.plot(x, x+1, '--c', label="dashed cyan")
axes.plot(x, x+2, '-.b', label="dashdot blue")
axes.plot(x, x+3, ':r', label="dotted red")

axes.set_title("My Nice Plot")
axes.legend()
plt.close(fig)

#fig.show()
('Marker: {}'.format([m for m in plt.Line2D.markers]))
linestyles = ['_', '-', '--', ':']
('Line styles: {}'.format(linestyles))

plot_objects = plt.subplots()
fig, ax = plot_objects
ax.plot([1,2,3], [1,2,3])
plot_objects
plt.close()

plot_objects = plt.subplots(ncols=2, nrows=2, figsize=(12, 6))
fig, ((ax1, ax2), (ax3, ax4)) = plot_objects

ax4.plot(np.random.randn(50), c='yellow')
ax1.plot(np.random.randn(50), c='red', linestyle='--')
ax2.plot(np.random.randn(50), c='green', linestyle=':')
ax3.plot(np.random.randn(50), c='blue', marker='o', linewidth=3)
plt.close()

plt.figure(figsize=(14, 6))

ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
plt.close()

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi*(20*np.random.rand(N))**2

plt.figure(figsize=(14, 6))

plt.scatter(x, y, s=area, c=colors, cmap='Spectral')
plt.colorbar()
plt.close()


fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(1,2,1)
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel1')
plt.colorbar()


ax2 = fig.add_subplot(1,2,2)
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel2')
plt.colorbar()
plt.close()


values = np.random.randn(1000)

plt.subplots(figsize=(12, 6))
plt.hist(values, bins=100, alpha=0.8, histtype='bar', color='steelblue', edgecolor='green')
plt.xlim(xmin=-5, xmax=5)
plt.close()




from scipy import stats 
from scipy.stats import gaussian_kde
density = stats._kde.gaussian_kde(values)

plt.subplots(figsize=(12, 6))
values2 = np.linspace(min(values)-10, max(values)+10, 100)

plt.plot(values2, density(values2), color='#FF7F00')
plt.fill_between(values2, 0, density(values2), alpha=0.5, color='#FF7F00')
plt.xlim(xmin=-5, xmax=5)
plt.close()


plt.subplots(figsize=(12, 6))

plt.hist(values, bins=100, alpha=0.8, density=1, histtype='bar', color='steelblue', edgecolor='green')
plt.plot(values2, density(values2), color='#FF7F00')
plt.xlim(xmin = -5, xmax= 5)
plt.close()


Y = np.random.rand(1, 5)[0]
Y2 = np.random.rand(1, 5)[0]

plt.subplots(figsize=(12, 6))
barWidth = 0.5
plt.bar(np.arange(len(Y)), Y, width=barWidth, color='#00b894', label='Label Y')
plt.bar(np.arange(len(Y2)), Y2, width=barWidth, color='#e17055', bottom=Y, label='Label Y2')
plt.legend()
plt.close()

values = np.concatenate([np.random.randn(10), np.array([10, 15, -10, -15])])
plt.figure(figsize=(12, 4))
plt.hist(values)
plt.close()

plt.figure(figsize=(12, 4))
plt.boxplot(values)
plt.close()

import seaborn as sns 

df = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\freeCodeCamp project\Data Analysis With Python\eth-price.csv',
                 index_col=0,
                 parse_dates=True)

df.head()


