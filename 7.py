#pandas dataframes

#a pandas dataframes is a 2 dimensional data structure,
#like a 2 dimensional array, or a table with rows and columns.

#create a simple pandas dataframe ?

import pandas as pd

data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data)

print(myvar)

