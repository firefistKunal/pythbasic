import math
import numpy as np

import pandas as pd

# data1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# arr1 = np.array(data1)
# print(arr1)
# print(arr1.ndim)
# print(arr1.shape)
# print(np.zeros(10))
# array=([ 0, 1, 2, 3, 4, 12, 12, 12, 8, 9])

a = np.zeros((2, 3, 4))

# Using Random for same thing instead of zeros
# a=np.random.rand(2, 3, 4)

# Try to figure out what would this code do??
# a=np.random.randint(1,7,(2, 2, 2))

print(a)

#creating a dataframe from the above 3d array usimng panda to help you visualise

index = pd.MultiIndex.from_product([range(s)for s in a.shape], names=['x', 'y', 'z'])
df = pd.DataFrame({'a': a.flatten()}, index=index)['a']

df = df.unstack(level='x').swaplevel().sort_index()
df.columns = ['Column 1', 'Column 2']
df.index.names = ['Third argument index ', 'Second Argument index']

#google what each of the methods used above does and how you can interchange row with columns or with the height

print(df)
