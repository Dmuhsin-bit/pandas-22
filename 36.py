#removing duplicates

#to remove duplicates, use the drop_duplicates() ,method

#remove all duplicates

import pandas as pd

df=pd.read_csv("data.csv")

df.drop_duplicates(inplace=True)

print(df)