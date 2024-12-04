#locate row

#pandas use the loc attribute to return one or more specified row(S)

import pandas as pd

data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
#load data into a data frame object:
df = pd.DataFrame(data)
print(df)
print(df.loc[0])




