import math
import cmath



def leapYearCheck(year):                          # function take the value and puts it in the variable "year"
    year=int(year)                                # year is formatted as integer datatype
    if year%4==0 and year%100!=0 or year%400==0:
        return True                               # funtions returns true or 1 if the year is a leap year

def oddEven(number):                              # function takes the value and stores it in the variable "number"
    number=int(number)                            # number is formatted as integer datatype
    if number%2==0:
        return True                               # funtion returns true or 1 if the number is an even number


def quadraticEquation(a, b, c):
    a=float(a)
    b=float(b)
    c=float(c)

    ans = []
    ans.append(b**2 - 4*a*c)
    
    if ans[0]>0:
        ans.append((-b + math.sqrt(ans[0])/(2*a)))
        ans.append((-b - math.sqrt(ans[0])/(2*a)))

    elif ans[0]==0:
        ans.append(-b/(2*a))

    elif ans[0]<0:

        ans.append((-b + cmath.sqrt(ans[0])/(2*a)))
        ans.append((-b - cmath.sqrt(ans[0])/(2*a)))
    return ans

def isPrime(n):
    n=int(n)
    if n<2:
        return False
    elif n>2:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    else:
        return True

def lineEquation(x1, y1, x2, y2):
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)

    equation=[]
    equation.append((y2-y1)/(x2-x1))
    equation.append(y1-equation[0]*x1)
    return equation

def lineStdEquation(x1, y1, x2, y2):
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)

    equation = []

    equation.append(y2-y1)
    equation.append(x1-x2)
    equation.append((x2-x1)*y1 - (y2-y1)*x1)

    return equation

def populationStdDeviation(datalist):
    mean=sum(datalist)/len(datalist)
    variance=0
    for data in datalist:
        variance=variance+(data-mean)**2
    return (variance/len(datalist))**0.5

def sampleStdDeviation(datalist):
    mean=sum(datalist)/len(datalist)
    variance=0                                   
    for data in datalist:
        variance=variance+(data-mean)**2
    return (variance/(len(datalist)-1))**0.5


def standardDeviation2D(x_values, y_values):
    x_mean=sum(x_values)/len(x_values)
    y_mean=sum(y_values)/len(y_values)
    variance_x=variance_y=0
    for x in x_values:
        
        variance_x =variance_x+(x-x_mean)**2

    for y in y_values:
        variance_y =variance_y+(y-y_mean)**2

    return ((variance_y + variance_x)/len(x_values))**0.5


def dataInput():
    dict={}
    while int(input("Add a city?\n0.No\n1.Yes\n"))!=0:
        key=input("city name\n")
        # dict[key+"_x"]=list(int(x) for x in input("Enter the X for "+key+" separated by space: ").split())
        # dict[key+"_y"]=list(int(y) for y in input("Enter the Y for " +key+" separated by space: ").split())
        dict[key]=list(int(x) for x in input("Enter the X for "+key+" separated by space: ").split()), list(int(y) for y in input("Enter the Y for " +key+" separated by space: ").split())
    return dict
    
