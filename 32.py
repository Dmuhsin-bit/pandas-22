#create csv with wrong date format

import pandas as pd
import numpy as np

data={"duration": [60,450,60,60,60],
      "Date":[np.nan,"2020/11/13" ,"2020/12/10","2020/12/10","2020/12/10"],
      "Pulse":[110,110,103,103,103],
      "Maxpuls":[130,130,145,145,145],
      "Calories":[409.1,409.1,230.0,230.0,230.0]}

df=pd.DataFrame(data)

df.to_csv("dup1.csv")

print(df)
