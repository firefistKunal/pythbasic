import numpy as np 
import random 

#print(np.random(size=4))
# array=np.arange(random.randrange(0, 500,))
# print(array)
# for i in range(10):
#     val=randint(0,1000)
#     print(val)

list1=np.asarray(random.sample(range(1, 1000), 10))
#out_arr = np.asarray(list1) 
# print(list1)
print(list1)
sortedarray=np.argsort(list1)
print(sortedarray)

for i in range(-1,-6,-1):
    index1=print(sortedarray[i],list1[sortedarray[i]])
    # print(index1)
    # print(out_arr[index1])

    
#print("Output sorted array : ", list1[out_arr]) 
#print("top 5 elements are")
# for i in range(5):
#     print(sortedarray[i])
#     itemindex = np.where(out_arr==sortedarray[i])
#     print(itemindex)
# for i in range(5):
#     print(sortedarray[i])
#     print(np.argmax(out_arr))
