import pandas as pd 


def cityDataSet():
    data=pd.read_csv('citysprawl.csv')
    dict={}
    for city in data['City'].unique():
    
        dict[city]= data[data['City'].isin([city])]['X'].tolist(), data[data['City'].isin([city])]['Y'].tolist()

    return dict

