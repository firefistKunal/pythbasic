import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user


input_x = input("Enter the data numbers separated by space: ")
data_x = list(map(int, input_x.split()))

input_y = input("Enter the data numbers separated by space: ")
data_y = list(map(int, input_y.split()))
city1= momo.standardDeviation2D(data_x, data_y)


input_x = input("Enter the data numbers separated by space: ")
data_x = list(map(int, input_x.split()))
input_y = input("Enter the data numbers separated by space: ")
data_y = list(map(int, input_y.split()))

city2= momo.standardDeviation2D(data_x, data_y)




if city1>city2:
    print("city 1 is more dispersed\n")
else:
    print(" city 2 is more dispersed\n")




