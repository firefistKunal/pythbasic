import numpy as np
import random
from itertools import permutations
arr=[]
sum=[]
sumt=0
perm = permutations(random.sample(range(1, 100), 3))

for i in list(perm):
    print(i)
    for j in range(len(i)):
        sumt=sumt+i[j]
    sum.append(sumt)
print(sum)
print(max(sum))



