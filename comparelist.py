l1=[]
l2=[]
flag=0
n1=int(input("enter the no of elements you want to enter in a list"))
for i in range(n1):
    l1.append(int(input("enter the {}th element".format(i+1))))
print(l1)
n2=int(input("enter the no of elements you want to enter in a list"))
for i in range(n2):
    l2.append(int(input("enter the {}th element".format(i+1))))
print(l2)
if(n1==n2):
    for i in range(n1):
        if(l1[i]==l2[i]):
            flag=0
        else:
            flag=1
            break
    if (flag==1):print("list not equal")
    else:print("list equal")
else:
    print("both list not of same order")


    
        