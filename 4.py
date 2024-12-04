#key/value object as series

#you can also use a key/value object,
# like a dictionary, when creating a series.

#create a simple pandas series from a dictionary ?

import pandas as pd

calories = {"day1" : 459 ,"day2":380 , "day 3 ": 390}

myvar = pd.Series(calories)

print(myvar)
