import numpy as np 
import random 
list1=np.asarray(random.sample(range(1, 1000), 10))
print(list1)
sortedarray=np.argsort(list1)
print(sortedarray)
# s=slice(-1,-6,-1)
print(sortedarray[slice(-1,-6,-1)],list1[sortedarray[slice(-1,-6,-1)]])  


