import csv


def guestInput():
    list=[]
    

    with open('guestlist.csv', 'a', newline='') as file:
        list.append(input("Enter guest name "))
        list.append(input("Enter age "))
        list.append(input("Enter Phone number "))
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(list)

    return 0

def csvListTranspose(filename):
    
    with open('%s.csv' % filename, newline='') as file:
        reader=csv.reader(file)
        guests=list(reader)

        names=list(map(list, zip(*guests)))
        

        return names
def guestDisplay(filename):
    with open('%s.csv' % filename, newline='') as file:
        reader=csv.reader(file)
        print(list(reader))
    return 0


def strToInt(str_list): #function to conver list datatype from string to integers, pass list with strings, as argument and returns same list with integers
        int_list = list(int(x) for x in str_list)
        return int_list

choice=1
while choice:
    choice=int(input("1.Enter guests\n2.Display guest List\n3.Average age of guest\n0.Exit\n"))
    if choice==1:
        guestInput()
    elif choice==2:
        guestDisplay('guestlist')
    elif choice==3:



        transpose_data=csvListTranspose('guestlist')

        age=strToInt(transpose_data[1])

        print("Average age of guests is {} " .format(sum(age)/len(age)))





