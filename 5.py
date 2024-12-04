#create a series using only data from "day1" and "day2" ?
from operator import index

import pandas as pd

calories = {"day1" : 459 ,"day2":380 , "day 3 ": 390}

myvar = pd.Series(calories,index=["day1","day2"])

print(myvar)
