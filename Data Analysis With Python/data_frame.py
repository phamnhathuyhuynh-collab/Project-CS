import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

#DATAFRAME CREATION 
#Create an empty pandas DataFrame
pd.DataFrame(data=[None],
             index=[None],
             columns=[None])

#Create a marvel_df pandas DataFrame with the given marvel data
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]

marvel_df = pd.DataFrame(data=marvel_data)

#Add column names to the marvel_df
col_names = ['name', 'sex', 'first_appearance']
marvel_df.columns = col_names
 
#Add index names to the marvel_df (use the character name as index)
marvel_df.index = marvel_df['name']

#Drop the name column as it's now the index
marvel_df = marvel_df.drop(columns=['name']) #marvel_df = marvel_df.drop(['name'], axis=1)

#Drop 'Namor' and 'Hank Pym' rows
marvel_df = marvel_df.drop(index=['Namor', 'Hank Pym']) #marvel_df = marvel_df.drop(['Namor', 'Hank Pym], axis=0)

#DATAFRAME SELECTION, SLICING AND INDEXATION 
#Show the first 5 elements on marvel_df
marvel_df.head()
marvel_df.loc['Spider-Man':'Thor', ]
marvel_df.iloc[:5, ]

#Show the last 5 elements on marvel_df
marvel_df.loc['Doctor Strange': 'Vision', ]
marvel_df.iloc[-5: , ]
marvel_df.tail()

#Show just the sex of the first 5 elements on marvel_df
marvel_df.iloc[: 5, 0]
marvel_df.loc['Spider-Man': 'Thor', 'sex']
marvel_df.iloc[:5,].sex.to_frame()

#Show the first_appearance of all middle elements on marvel_df
marvel_df.iloc[1:-1,].first_appearance.to_frame()

#Show the first and last elements on marvel_df
marvel_df.iloc[[0, -1],] #marvel_df.iloc[[0, -1]][['sex', 'first_appearance']]

#DATAFRAME MANIPULATION AND OPERATIONS
#Modify the first_appearance of 'Vision' to year 1964
marvel_df.loc['Vision', 'first_appearance'] = 1964

#Add a new column to marvel_df called 'years_since' with the years since first_appearance
marvel_df['years_since'] = 2018 - marvel_df['first_appearance']

#DATAFRAME BOOLEAN ARRAYS (ALSO CALLED MASKS)
#Given the marvel_df pandas DataFrame, make a mask showing the female characters
mask = marvel_df['sex'] == 'female'

#Given the marvel_df pandas DataFrame, get the male characters
marvel_df[marvel_df['sex'] == 'male']

#Given the marvel_df pandas DataFrame, get the characters with first_appearance after 1970
marvel_df[marvel_df['first_appearance'] > 1970]

#Given the marvel_df pandas DataFrame, get the female characters with first_appearance after 1970
marvel_df[(marvel_df['sex'] == 'female') & (marvel_df['first_appearance'] > 1970)]

#DATAFRAME SUMMARY STATISTICS
#Show basic statistics of marvel_df
marvel_df.describe()

#Given the marvel_df pandas DataFrame, show the mean value of first_appearance
marvel_df['first_appearance'].mean()

#Given the marvel_df pandas DataFrame, show the min value of first_appearance
marvel_df['first_appearance'].min()
np.min(marvel_df['first_appearance'])

#Given the marvel_df pandas DataFrame, get the characters with the min value of first_appearance
marvel_df[marvel_df['first_appearance'] == marvel_df['first_appearance'].min()]

#DATAFRAME BASIC PLOTTINGS
#Reset index names of marvel_df
marvel_df = marvel_df.reset_index()

#Plot the values of first_appearance
marvel_df.first_appearance.plot() #plt.plot(marvel_df.index, marvel_df.first_appearance)

#Plot a histogram (plot.hist) with values of first_appearance
plt.hist(marvel_df.first_appearance)

print(marvel_df)