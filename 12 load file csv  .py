#load files into a dataframe

#if your data sets are stored in a file, pandas can load them into a dataframes.

#load a coma separated file (csv file ) into a dataframe ?


import pandas as pd

df = pd.read_csv('data.csv')

print(df)
