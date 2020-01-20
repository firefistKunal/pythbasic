def LeapYearCheck(year):                          # function take the value and puts it in the variable "year"
    year=int(year)                                # year is formatted as integer datatype
    if year%4==0 and year%100!=0 or year%400==0:
        return True                               # funtions returns true or 1 if the year is a leap year

def OddEven(number):                              # function takes the value and stores it in the variable "number"
    number=int(number)                            # number is formatted as integer datatype
    if number%2==0:
        return True                               # funtion returns true or 1 if the number is an even number
