import csv
import statistics 
import math

with open(r'si.csv','rt')as f:
  data = csv.reader(f)
  er=[]
  ir=[]
  X=[]
  Y=[]
  X2=[]
  Y2=[]
  XY=[]
  
  for row in data:
        #print(row)
        ir.append(row[0])
        er.append(row[1])
er.remove(er[0])
ir.remove(ir[0])
print(ir)
print(er)
for i in range(len(ir)):
    ir[i]=int(ir[i])
for i in range(len(er)):
    er[i]=int(er[i])

x = statistics.mean(ir)
y = statistics.mean(er) 
print("x",x)
print("y",y)
for i in range(len(ir)):
    X.append(ir[i]-x)
for i in range(len(er)):
    Y.append(er[i]-y)
print(X)
print(Y)
for i in range(len(ir)):
    X2.append(X[i]*X[i])
for i in range(len(er)):
    Y2.append(Y[i]*Y[i])
print(X2)
print(Y2)
for i in range(len(ir)):
    XY.append(X[i]*Y[i])
print(XY)
sumxy=0
sumX2=0
sumY2=0
for i in range((len(ir))):
    sumxy+=XY[i]
    sumX2+=X2[i]
    sumY2+=Y2[i]
print(sumxy)
print(sumX2)
print(sumY2)
X2Y2=sumX2*sumY2
sqX2Y2=math.sqrt(X2Y2)
print(sqX2Y2)
r=sumxy/sqX2Y2
print(r)



  