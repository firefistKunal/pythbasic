import numpy

arr1=[]
arr = numpy.arange(10)
print(arr)
arr = (arr[::-1])
print(arr)
for i in range(0,len(arr)):
    arr1.append(float(arr[i]))
print(arr1)

    