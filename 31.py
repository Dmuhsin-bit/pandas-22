#pandas - cleaning data of wrong format
#data of wrong format
#cells with data of wrong format can  make it difficult ,
# for even impossible, to analyze data.

#to fix it, you have two options:
# remove the rows , or
#convert all cells in the columns into the same format.

# pandas has to_datetime() method for this:

#convert to data ?

import pandas as pd

df = pd.read_csv('dd.csv')
print(df)

df['Data'] = pd.to_datetime(df['Date'])

print(df.to_string())
