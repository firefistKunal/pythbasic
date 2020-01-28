colm1=list(input("space separated list ").split())

colm2=list(input("space separated list again ").split())

colm3=list(input("space separated list one last time ").split())

colm4=list(input("one last ride ").split())

nested=[colm1, colm2, colm3, colm4]

print(nested)

print(list(map(list, zip(*nested))))
