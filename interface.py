import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user
data=momo.dataInput()
max=0
for city, value in data.items():
    # result.append(momo.standardDeviation2D(city[0], city[1]))
    dispersion=momo.standardDeviation2D(value[0], value[1])
    if dispersion>max:
        max=dispersion
        ans=city
print(ans+" Is the most spread out city based upon the dispersion of the coordinates of the houses.")









# data_x = list(map(int, input("Enter the X separated by space: ").split()))
# data_y = list(map(int, input("Enter the Y separated by space: ").split()))

# city1= momo.standardDeviation2D(data_x, data_y)

# # data_x = list(map(int, input("Enter the X separated by space: ").split()))
# # data_y = list(map(int, input("Enter the Y separated by space: ").split()))

# data_x = list(int(x) for x in input("Enter the X separated by space: ").split())
# data_y = list(int (y) for y in input("Enter the Y separated by space: ").split())

# city2= momo.standardDeviation2D(data_x, data_y)

# if city1>city2:
#     print("city 1 is more dispersed\n")
# else:
#     print(" city 2 is more dispersed\n")




