import numpy
import matplotlib.pyplot as plt
def calcslope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
x1,y1=input("enter x1 and y1 values of point 1").split()
x2,y2=input("enter x2 and y2 values of point 2").split()
x3,y3=input("enter x3 and y3 values of point 3").split()
x1=int(x1)
x2=int(x2)
x3=int(x3)
y1=int(y1)
y2=int(y2)
y3=int(y3)

plt.plot([x1,x2,x3],[y1,y2,y3],'ro-')
plt.ylabel('Y AXIS')
plt.xlabel('X AXIS')
plt.show()


s1=calcslope(x1,y1,x2,y2)
s2=calcslope(x1,y1,x3,y3)
s3=calcslope(x2,y2,x3,y3)
print(s1)
print(s2)
print(s3)
if s1==s2 and s2==s3:
    print("yes collinear")
    plt.plot([x1,x2,x3],[y1,y2,y3])
    plt.plot([x1,x2,x3],[y1,y2,y3],'ro')
    plt.ylabel('Y AXIS')
    plt.xlabel('X AXIS')
    plt.show()

else:
    print("no not collinear")

