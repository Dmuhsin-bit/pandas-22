#pandas - cleaning data
# data cleaning
# data cleaning means fixing your bad data in your data set
#bad data could be :

# empty cells
#data in wrong format
# wrong data
# duplicates

import  pandas as pd

df = pd.read_csv('data1.csv')

print(df.to_string())

# the data set contains some empty cells ("data" in row 22 , and "calories" in row 18
# and 28).

#the data set contains wrong format ("data" in row 26).

#the data set contains wrong data ("duration in row 7).

#the data set contains duplicates (row 11 and 12).
