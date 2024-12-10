import numpy as np
import pandas as pd
a=pd.read_csv("sample4.txt",header=None)
a.columns=['id','fname','lname','age','phn_no','loc']
print(a)

#where are 5 evaluating functions
#1.count      3.min
#2.max        4.sum       5.average

b=a.groupby('loc') ['loc'].count()
print(b)
