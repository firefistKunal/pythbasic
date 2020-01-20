def LeapYearCheck(year):
    year=int(year)
    if year%4==0 and year%100!=0 or year%400==0:
        return True

def OddEven(number):
    number=int(number)
    if number%2==0:
        return True
    