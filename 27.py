#repalce only for specified colums

#the example above replaces all empty cells in the whole data frame.

#to only replace empty values for one column,
#specify the column name for the dataframe :
#replace null values in the "calories" columns with the number 130: ?

import pandas as pd

df = pd.read_csv('techiifayis.csv')

df["Calories"].fillna(130,inplace = True)

print(df.to_string())

#this operation inserts 130 in empty cells in the "calories" column (row 18 and 28).
