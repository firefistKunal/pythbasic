import csv
sum=0
count=0

with open(r"C:\Users\madhura.anand\Documents\guestsss.csv",'r') as f:
    data = csv.reader(f)
    for row in data:
        #print(row)
        count += 1
        for i in row:
            #print(i)
            if(i.isalpha()==True):
                print(i)
            if(len(i)>2 and i.isnumeric()):
                print(i)

            if(len(i)<=2 and i.isnumeric()):
                sum=sum+int(i)

                       
# print(sum)
# print(count)
avg=sum/count
print("avg age is",avg)

        

