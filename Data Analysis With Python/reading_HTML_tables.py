import pandas as pd
from io import StringIO
import requests
html_string = """
<table>
    <thead>
      <tr>
        <th>Order date</th>
        <th>Region</th> 
        <th>Item</th>
        <th>Units</th>
        <th>Unit cost</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1/6/2018</td>
        <td>East</td> 
        <td>Pencil</td>
        <td>95</td>
        <td>1.99</td>
      </tr>
      <tr>
        <td>1/23/2018</td>
        <td>Central</td> 
        <td>Binder</td>
        <td>50</td>
        <td>19.99</td>
      </tr>
      <tr>
        <td>2/9/2018</td>
        <td>Central</td> 
        <td>Pencil</td>
        <td>36</td>
        <td>4.99</td>
      </tr>
      <tr>
        <td>3/15/2018</td>
        <td>West</td> 
        <td>Pen</td>
        <td>27</td>
        <td>19.99</td>
      </tr>
    </tbody>
</table>
"""

dfs = pd.read_html(StringIO(html_string))

(len(dfs))

df = dfs[0]
(df.shape)
(df.loc[df['Region'] == 'Central'])
(df.loc[df['Units'] > 35])

(pd.read_html(StringIO(html_string), header=0)[0])


#parsing HTML tables from the web

html_url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
nba_tables = pd.read_html((html_url))
(len(nba_tables))

nba = nba_tables[0]
(nba.head())

html_url1 = "https://en.wikipedia.org/wiki/The_Simpsons"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
r = requests.get((html_url1), headers=headers)
wiki_tables = pd.read_html(StringIO(r.text), header=0)
print(len(wiki_tables))



