import pandas as pd
import matplotlib.pyplot as plt
import statistics
data=pd.read_csv(r'C:\Users\madhura.anand\Desktop\pybasic\city1.csv')
xc1=data["X"]
yc1=data["Y"]
print(xc1)
print(yc1)
xc1sd=statistics.stdev(xc1)
yc1sd=statistics.stdev(yc1)
data=pd.read_csv(r'C:\Users\madhura.anand\Desktop\pybasic\city2.csv')
xc2=data["X"]
yc2=data["Y"]
print(xc2)
print(yc2)
xc2sd=statistics.stdev(xc2)
yc2sd=statistics.stdev(yc2)
print("sd of x coord city1 = ",xc1sd,"sd of y coord city1 =",yc1sd)
print("sd of x coord city2 = ",xc2sd,"sd of y coord city2 =",yc2sd)
plt.plot(xc1,yc1,'ro')
plt.plot(xc2,yc2,'ro')