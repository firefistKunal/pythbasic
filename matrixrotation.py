import random 
import numpy as np

n=int(input("Size of the matrix?? ")) #size of matrix from user

array=np.random.randint(n*n, size=(n,n)) #create random matrix of given size
print(array)#display generated matrix

t_array=np.transpose(array)# take transpose of the matrix

for i in range (0, n): #repeatdly swap the rows
    if i>n/2:
        break #only need to repeat once index reaches middle column otherwise loop will swap it back to original matrix
    
    t_array[:,[i,-i-1]]=t_array[:,[-1-i,i]] #swap first "column index 0" with "last column index -1"
                                            # "second column index 1" with second last column index -2" and so on
                                            
print(t_array)#display the now rotated array
