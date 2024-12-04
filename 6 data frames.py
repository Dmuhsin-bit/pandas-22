#data frames

#data sets in pandas are usually multi-dimensional tables, called dataframes.

#series is like a column, a dataframe is the whole table.
#create a data frame from two series ?
import pandas as pd

data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data)

print(myvar)
