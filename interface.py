import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user
number = input("Enter an year\n")

# The relevant function is then called passing the input
if momo.OddEven(number): # the function "OddEven()"" is written as "momo.OddEven()" because its from "momoslibrary" which is imported as "momo"
    print("Its leap year\n")
else:
    print("This aint no leap year.\n")
#Based on the function response the neccessary output is given to the user
