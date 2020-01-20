import momoslibrary as momo

number = input("Enter an year\n")
if momo.OddEven(number):
    print("Its leap year\n")
else:
    print("This aint no leap year.\n")