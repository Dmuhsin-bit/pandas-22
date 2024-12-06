#replace empty values
#another way of dealing with empty cells is to insert a new value instead.

#this wa you do not have to delete entire rows just because of some empty cells.

#the fillna() method allows us to replace empty cells with a value ?

#replace null values with the number 130

import pandas as pd

df = pd.read_csv('techiifayis.csv')

df.fillna(130,inplace=True)
print(df.to_string())

#notice in the result: empty cells got the value 130 (in row 18,28).