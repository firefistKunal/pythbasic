import momoslibrary as momo # import the file that contains our functions, individual functions can also be imported

# Code for the program to take neccessary  inputs from the user

x1=input("x1 ")
y1=input("y1 ")
x2=input("x2 ")
y2=input("y2 ")

line = momo.lineEquation(x1, y1, x2, y2)

print(" y = {}x + {}\n".format(line[0], line[1]))

std_line= momo.lineStdEquation(x1, y1, x2, y2)
print ("\nStandard equation of line is")
print(" {}x + {}y + {} = 0".format(std_line[0], std_line[1], std_line[2]))

