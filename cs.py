import pandas as pd
import statistics
DX=[]
DY=[]
HX=[]
HY=[]
CX=[]
CY=[]
BX=[]
BY=[]
df=pd.read_csv(r'C:\Users\madhura.anand\Desktop\pybasic\citysprawl.csv')
DX.append(df.loc[df['City']=="Delhi"]["X"])
DY.append(df.loc[df['City']=="Delhi"]["Y"])
print(DX)
print(DY)


SDDX=statistics.stdev(DX)
SDDY=statistics.stdev(DY)

BX.append(df.loc[df['City']=="Bengaluru"]["X"])
BY.append(df.loc[df['City']=="Bengaluru"]["Y"])
print(BX)
print(BY)
# SDBX=statistics.stdev(BX)
# SDBY=statistics.stdev(BY)


CX.append(df.loc[df['City']=="Chennai"]["X"])
CY.append(df.loc[df['City']=="Chennai"]["Y"])
print(CX)
print(CY)
# SDCX=statistics.stdev(CX)
# SDCY=statistics.stdev(CY)

HX.append(df.loc[df['City']=="Hyderabad"]["X"])
HY.append(df.loc[df['City']=="Hyderabad"]["Y"])
print(HX)
print(HY)
# SDHX=statistics.stdev(HX)
# SDHY=statistics.stdev(HY)

# print("STD DEV OF X CO-ORDINATE OF HYDERABAD",SDHX)
# print("STD DEV OF Y CO-ORDINATE OF HYDERABAD",SDHY)
print("STD DEV OF X CO-ORDINATE OF DELHI",SDDX)
print("STD DEV OF Y CO-ORDINATE OF DELHI",SDDY)
# print("STD DEV OF X CO-ORDINATE OF CHENNAI",SDCX)
# print("STD DEV OF Y CO-ORDINATE OF CHENNAI",SDCY)
# print("STD DEV OF X CO-ORDINATE OF BENGALURU",SDBX)
# print("STD DEV OF Y CO-ORDINATE OF BENGALURU",SDBY)

