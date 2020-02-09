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

def strToInt(str_list): #function to conver list datatype from string to integers, pass list with strings, as argument and returns same list with integers
        int_list = list(int(x) for x in str_list)
        return int_list



transpose_data=csvListTranspose('guestlist')

age=strToInt(transpose_data[1])

print("Average age of guests is {} " .format(sum(age)/len(age)))