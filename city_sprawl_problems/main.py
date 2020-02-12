import math
import cmath
import csv
import pandas as pd
import matplotlib.pyplot as plt

def standardDeviation2D(x_values, y_values):
    x_mean=sum(x_values)/len(x_values)
    y_mean=sum(y_values)/len(y_values)
    variance_x=variance_y=0
    for x in x_values:
        
        variance_x =variance_x+(x-x_mean)**2

    for y in y_values:
        variance_y =variance_y+(y-y_mean)**2

    return ((variance_y + variance_x)/len(x_values))**0.5

def dataInput():
    dict={}
    while int(input("Add a city?\n0.No\n1.Yes\n"))!=0:
        key=input("city name\n")
        # dict[key+"_x"]=list(int(x) for x in input("Enter the X for "+key+" separated by space: ").split())
        # dict[key+"_y"]=list(int(y) for y in input("Enter the Y for " +key+" separated by space: ").split())
        dict[key]=list(int(x) for x in input("Enter the X for "+key+" separated by space: ").split()), list(int(y) for y in input("Enter the Y for " +key+" separated by space: ").split())
    return dict
    #the dictionary created and returned here is in the format {'cityname':[x cordinates],[y coordinates],
    #                                                           'cityname':[x cordinates],[y coordinates]}

def cityDataSet(): #this function reads the csv file and returns it as a dictionary of city and x, y coordinates.
    data=pd.read_csv('citysprawl.csv')
    dict={}
    for city in data['City'].unique():
    
        dict[city]= data[data['City'].isin([city])]['X'].tolist(), data[data['City'].isin([city])]['Y'].tolist()

    return dict

def citySprawl():
    data=cityDataSet()                  #we get the data from csv as a dictionary of city and corresponding x, y coordinates.
    max=0
    cities=[]
    for city, value in data.items():    #this loops through the keys which each city, one by one and the value[0] and value[1] are x and y coordinate list respectively
        
        plt.scatter(value[0], value[1]) #plot the coordinates
        cities.append(city)             #list of cities for the legend

        dispersion=standardDeviation2D(value[0], value[1]) #the value[0] and value[1] are x and y coordinate list respectively
        
        if dispersion>max:              #as loop iterates this compares the dispersion and stores the city with higher dispersion
            max=dispersion
            ans=city
    
    print(ans+" Is the most spread out city based upon the dispersion of the coordinates of the houses.")

    plt.legend(cities) #fromt the list created in above loop legend is shown
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show() #shows everything plotted at once in single window.


citySprawl()
