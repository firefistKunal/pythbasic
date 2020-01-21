import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user

number=input("enter a number to verify its primality.\n")

if momo.isPrime(number):
    print("its a prime number.\n")

else:
    print("This ain't a prime number.\n")


