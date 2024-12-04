#create labels

#with the index argument, you can name your own labels.
#create your own labels ?

import pandas as pd

a = [1,7,2]

myvar = pd.Series(a, index = ['x','y','z'])

print(myvar)

#return the value of 'y' ?
print(myvar['y'])

