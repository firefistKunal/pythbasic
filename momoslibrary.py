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

def primenum(n):
    c=0
    for i in range(1,n):
        if n%i==0:
          c=c+1
        
    if c>1:
        return "not a prime"
    else:
        return "prime"
#print(primenum(6))
#print(primenum(2))
