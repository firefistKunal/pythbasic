import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user



transpose_data=momo.csvListTranspose('guestlist')

age=momo.strToInt(transpose_data[1])

print(sum(age)/len(age))



