import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

import pandas as pd

data=pd.read_csv(r'C:\Users\madhura.anand\Documents\abc.csv','rt')

print(data['X'])
print(data['Y'])