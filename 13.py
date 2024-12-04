#pandas read csv
# if you have a large dataframe with many rows,

#to_string()--used to print the entire dataframes.

import pandas as pd

df = pd.read_csv('big.csv')

print(df.to_string())

#print(df)--method
# will only retun the first 5 rows, and the last 5 rows:
