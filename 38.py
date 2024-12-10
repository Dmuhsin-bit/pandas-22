import pandas as pd
a=pd.Series([2,3,4,5,6])
b=pd.Series([4,5,6,7])

c=a.subtract(b)
print(c)