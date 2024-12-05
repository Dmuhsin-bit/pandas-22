# create a csv file?


import pandas as pd
import numpy as np

data = {'duration': [60,60,60,60],
        'data': [np.nan,np.nan ,'2020/11/09','2020/12/10'],

         'pulse': [110,110,117,103,],
         'maxpulse':[130,130,145,13510,],
         'calories': [409.1,409.1,np.nan,230.0,]

       }

df = pd.DataFrame(data)
print(df)
df.to_csv('create.csv')