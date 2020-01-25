import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user


data_x = list(map(int, input("Enter the X separated by space: ").split()))
data_y = list(map(int, input("Enter the Y separated by space: ").split()))

city1= momo.standardDeviation2D(data_x, data_y)

# data_x = list(map(int, input("Enter the X separated by space: ").split()))
# data_y = list(map(int, input("Enter the Y separated by space: ").split()))

data_x = list(int(x) for x in input("Enter the X separated by space: ").split())
data_y = list(int (y) for y in input("Enter the Y separated by space: ").split())

city2= momo.standardDeviation2D(data_x, data_y)

if city1>city2:
    print("city 1 is more dispersed\n")
else:
    print(" city 2 is more dispersed\n")




