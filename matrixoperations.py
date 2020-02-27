import numpy as np 
l1=[]
l2=[]
n,m=int(input("enter values of n (row in list)")),int(input("enter values of p(columns)"))
for i in range(n*m):
    l1.append(int(input("enter the values of matrix1")))
for j in range(n*m):
    l2.append(int(input("enter values of matrix2")))
# arr1=np.asarray(l1)
# arr2=np.asarray(l2)
# print(arr1)
# print(arr2)
# arr1=arr1.reshape(m,n)
# arr2=arr2.reshape(m,n)
sum1=np.add(l1,l2)
difference1 = np.subtract(l1,l2)
product1=np.multiply(l1,l2)
quotient=np.divide(l1,l2)
print(sum1)
print(difference1)
print(product1)
print(quotient)