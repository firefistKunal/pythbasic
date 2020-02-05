import csv

r=[]
with open('ga2.txt', 'r') as file:
    reader = csv.reader(file)
    sum=0
    for row in reader:
         print(row)
         for i in range(len(row)):

             #print(row[i])
             if(str(row[i]).isnumeric()):

                 print(row[i], "is numeric")
                 print(type(row[i]))
                 r.append(int(row[i]))
print(r)
sum=0
for i in range(len(r)):
    sum+=r[i]
avg=sum/len(r)
print(avg)
