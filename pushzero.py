l=[]
n=int(input("enter the no of elements you want to enter in a list"))
for i in range(n):
    l.append(int(input("enter the {}th element".format(i+1))))
print(l)
for i in range(n):
    if(l[i]==0):
        l.insert(n,l[i])
        l.remove(l[i])
print(l)