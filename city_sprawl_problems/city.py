nofcity=int(input("enter no of cities"))                                            #nofcity=2
cities=[[]] 
house=[]
for i in range(0,nofcity-1):
    cities.append([])
print(cities)                                                                       #cities=[[[],[]],[[],[],[]]]
for i in range(0,nofcity):
    house.append(int(input("enter no houses in city{} ".format(i+1))))
print(house)                                                                        #house=[[],[]] 
# for i in range(0,nofcity):
#     for k in range(0,house[i]):                         
#         cities[i].append([])

#print(cities)

for i in range(0,nofcity):
     for k in range(0,house[i]):                         
         cities[i].append(raw_input("enter the x and y values of house ").split(","))
print(cities)
for city in cities:
    print(city)