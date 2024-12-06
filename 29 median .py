#calculate the median, and replace any empty values with it ?


#median = the value in the middle,
#after you have sorted all values ascending.


import pandas as pd

df= pd.read_csv('techiifayis.csv')

x =df["Calories"].median()

df["Calories"].fillna(x,inplace = True)
print(df.to_string())

#as you can see in row 18 and 28
#the empty values from calories was replaced with the median 409.1
