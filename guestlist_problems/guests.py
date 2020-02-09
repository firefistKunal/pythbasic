names=[]
ages=[]
phonenum=[]
n=int(input("enter number of guests"))
for i in range(n):
    names.append(input("enter name of guest {} ".format(i+1)))
    ages.append(input("enter ages of guest {} ".format(i+1)))
    phonenum.append(input("enter phone number of guest {} ".format(i+1)))
# print(names)
# print(ages)
# print(phonenum)
# No iterables are passed
result = zip()
# Converting itertor to list
result_list = list(result)
print(result_list)
# Two iterables are passed
result = zip(names,ages,phonenum)
# Converting itertor to set
result_set = set(result)
final1=sorted(result_set)

file1 = open(r"myfile.txt","w") 


for i in range(len(final1)):
    mylist = final1[i]
    for j in range(len(mylist)):
        if(j<len(mylist)-1):
            file1.write(mylist[j]+",")
        else:
            file1.write(mylist[j])
    file1.write("\n")        
#file1.write("Hello \n") 
#file1.write(final1[0])
#file1.writelines(final1) 
file1.close() #to change file access modes 
  
file1 = open(r"myfile.txt","r") 
print(file1.read())


  
# print("Output of Read function is ")
# print(file1.read()) 
