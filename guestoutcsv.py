import csv
sum=0
count=0

with open(r"C:\Users\madhura.anand\Documents\guestsss.csv",'r') as f:
    data = csv.reader(f)
    for row in data:
        print(row)
        count += 1
        for i in row:
            if(len(i)<=2 and i.isnumeric()):
                 sum=sum+int(i)
           

            #print(i)
            if(i.isalpha()==True):
                print("name is ",i)
            if(len(i)>2 and i.isnumeric()):
                print("phone num is",i)

        
                

                       
# print(sum)
# print(count)
avg=sum/count
print("avg age of all ppl is",avg)

        

