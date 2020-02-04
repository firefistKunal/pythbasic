class xyz():
    def __init__(self, a, b):
         self.a = a
         self.b = b
         print("self a",self.a)
         print("self b",self.b)
    def sum(self,a,b):
        return a+b
    def difference(self,a,b):
        return a-b
    #def main():
obj1 = xyz(6,1)
a=obj1.sum(6,1)
b=obj1.difference(6,1)

print(a)
print(b)

obj2=xyz(2,2)
c=obj2.sum(2,3)
d=obj2.difference(2,3)
print("c value",c,"d value",d)

         
    

    