import csv

r=[]
with open('ga2.txt', 'r') as file: #why the fuck are you reading a .txt file with csv reader? do you not know the difference between file types???

    reader = csv.reader(file) #this returns a list of rows which is a list in itself, its a list of list
    sum=0
    for row in reader:
         print(row)
         for i in range(len(row)):

             #print(row[i])
             if(str(row[i]).isnumeric()):

                 print(row[i], "is numeric")
                 print(type(row[i]))
                 r.append(int(row[i])) #append element instead of a list in list of list??????
print(r)
sum=0
for i in range(len(r)):
    sum+=r[i]
avg=sum/len(r)
print(avg)
