#if you want to change the original dataframe
#use the inplace = true argument

#remove all rows with null values


import pandas as pd
df = pd.read_csv('data1.csv')
df.dropna(inplace= True,ignore_index=True)
print(df.to_string())

#note: now the dropna(inplace = true)
#will not return a new data frame
#but it will remove all rows containing null values
#from the original dataframe
