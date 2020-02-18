import pandas as pd
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt

data=pd.read_csv('Si.csv')
print(data['IR'])
print(pearsonr(data['IR'], data['ER']))

#To Visualize
plt.xlabel("Intelleigence Ratio")
plt.ylabel("Engineering ratio")
plt.scatter(data['IR'], data['ER'])
plt.show()
