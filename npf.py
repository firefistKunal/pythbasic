import numpy as np 
import random 
list1=np.asarray(random.sample(range(1, 1000), 10))
print(list1)
print(np.argsort(list1)[-1:-6:-1],list1[np.argsort(list1)[-1:-6:-1]])  


