import pandas as pd
a =pd.read_csv("Temperature.unknown",header=None,sep=" ")
a.columns=['year','temp']

#syntax
#newfname=olddfname.groupby('columnname') ['columnname'].min()
b=a.groupby('year')['temp'].min().sort_values(ascending=False)
print(b)
