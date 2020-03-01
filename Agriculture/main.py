import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

original=pd.read_csv('apy.csv')

cg_data=original[original['State_Name']=='Chhattisgarh']
data=cg_data.groupby(['Crop_Year','Crop'])['Area'].agg(np.sum).reset_index().pivot(index='Crop', columns='Crop_Year')
# print(data.drop('Rice').columns)
# data.drop('Rice').sort_values(by=('Area', 2014)).plot.barh()
# plt.show()
plt.bar(data.loc['Rice',:].reset_index()['Crop_Year'], data.loc['Rice',:].reset_index()['Rice'])
plt.show()
print(data.index)
crop=input("\nWhat crop you want?")
data.loc[crop,:].plot(kind='line', subplots=True) 
plt.show()



