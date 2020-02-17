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

exercise2()

