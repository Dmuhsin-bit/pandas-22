#removing rows

#the result  from the converting in the example above gave us a NaT value
#which can be handled as a NULL value
#and we can remove the row by using the dropna() method

#remove rows with a NULL value in the "Date" column

import pandas as pd

df=pd.read_csv("dd.csv")

df["Date"]=pd.to_datetime(df["Date"])

df.dropna(subset=["Date"],inplace=True)
print(df.to_string())
