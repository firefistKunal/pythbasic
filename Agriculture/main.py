import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('apy.csv')

Cgdata=df[df['State_Name']=='Chhattisgarh']
graph=Cgdata.groupby(['Crop_Year','Crop'])['Area'].agg(np.sum).reset_index().pivot(index='Crop', columns='Crop_Year')
# print(graph.drop('Rice').columns)
graph.drop('Rice').sort_values(by=('Area', 2014)).plot.barh()
plt.show()



