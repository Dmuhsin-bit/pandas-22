import pandas as pd
data=[[100,'ali','khan',23,'python','kannur',2000],
     [101,'rahul','h',34,'python','kozhikode',3000],
     [102,'anu','k',36,'python','kannur',3000],
     [103,'das','1',45, 'bigdata','thrissur',2000],
     [104,'elna','shaji',30,'python','palakkad',2500]]

a=pd.DataFrame(data,columns=['id','fname','Lname','age','prof','place','salary'])

a['dpt']=['AHN','SHG','DFG','RTY','TOE']

print(a)
