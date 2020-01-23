import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user

input_string = input("Enter the data numbers separated by space: ")
data_string = list(map(int, input_string.split()))
print ("Standard deviation of the given data set is {} ".format( momo.populationStdDeviation(data_string)))


print ("Sample Standard deviation of the given data set is {} ".format( momo.sampleStdDeviation(data_string)))
