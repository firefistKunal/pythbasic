import pandas as pd
import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data)
# print(s)

import pandas as pd

data=pd.read_csv('abc.csv')

# print(data.columns)

print(data['X'])
print(data['Y'])