import numpy as np 
import random 
from random import randint
#print(np.random(size=4))
# array=np.arange(random.randrange(0, 500,))
# print(array)
# for i in range(10):
#     val=randint(0,1000)
#     print(val)

list1=random.sample(range(1, 1000), 10)
out_arr = np.asarray(list1) 
# print(list1)
print(out_arr)
sortedarray=-np.sort(-out_arr)
print(sortedarray)
print("top 5 elements are")
for i in range(5):
    print(sortedarray[i])
    itemindex = np.where(out_arr==sortedarray[i])
    print(itemindex)