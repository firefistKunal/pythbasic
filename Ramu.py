def exercise1():
    sum =0
    for steps in range (5):
        sum += int(input("Enter the %d number" %steps))
    print (sum)
    return 0

def exercise2():
    dividend=int(input("What's the dividend? "))
    divisor = int(input("What's the divisor? "))
    if dividend%divisor==0:
        print("Oh yeah!!!")
    else:
        print("Not quite!!")
    return 0

def exercise3():

    numbers = list(int(x) for x in input("Enter 3 numbers separated by space to find lowest and highest among them: ").split())
    numbers.sort()
    print(numbers)
    print("\nhighest number is {}\nlowest number is {}" .format(numbers[-1],numbers[0]))

    return 0
def exercise4():
    count=10
    number=0
    list=[]
    while count:
        number+=1
        if number%2!=0:
            list.append(number)
            count-=1
    print(sum(list)/len(list))        

    return 0

def exercise5():
    fibonacci_series=[0,1]
    while fibonacci_series[-1]!=89:
        fibonacci_series.append(fibonacci_series[-1]+fibonacci_series[-2])
    print(fibonacci_series)

    return 0

def exercise6():

    count=20
    number=1
    list=1
    while count:
        number+=1
        if number%2==0:
            list=list*number
        count-=1
    print(list)        

    return 0

exercise6()

