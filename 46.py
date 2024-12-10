import pandas as pd
a =pd.read_csv("Temperature.unknown",header=None,sep=" ")
a.columns=['year','temp']

#syntax
#newfname=olddfname.groupby('columnname') ['columnname'].sum()
b=a.groupby('year')['temp'].sum().sort_values(ascending=False)
print(b)
