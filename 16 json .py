#pandas read json

#load the json file into a dataframe

import pandas as pd

df=pd.read_json('jhai.json')

print(df.to_string())

#tip: use to_string() to print the entire dataframe