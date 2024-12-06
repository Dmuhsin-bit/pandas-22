#calculate the mode, and replace any empty values with it?

#mode = the value that appears most frequently.

import pandas as pd

df = pd.read_csv('techiifayis.csv')

x = df["Calories"].mode()[0]
print(x)
df["Calories"].fillna(x,inplace = True)
print(df.to_string())

#as you can see in row 18 and 28,
# the empty value from "calories" was replaced with the mode: 230.0
