#pandas - duplicates

#the duplicated() method returnsa boolean values for each row

#returns true for every row that i  duplicate otherwise false

import pandas as pd

df=pd.read_csv("data.csv")

print(df.duplicated())