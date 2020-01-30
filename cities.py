m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
mat=[]
for i in range(m):
    mat.append([])
print(mat)
for i in range(m):
    for j in range(n):
        mat[i].append(j)
        mat[i][j]=0
print(mat)
for i in range(0,m):
    for j in range(0,n):                                               
        print ('entry in row: ',i+1,' column: ',j+1)
        mat[i][j]=int(input())
print (mat)

   
       



