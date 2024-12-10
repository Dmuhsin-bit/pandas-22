#pandas-fxing wrong data

#replacing values

#set "Duration" s 45 in row 1

import pandas as pd

df=pd.read_csv("wrong.csv")
print(df)
df.loc[1,"Duration"]=45

print(df.to_string())