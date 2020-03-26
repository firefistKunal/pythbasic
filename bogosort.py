import random

# numbers=list(int(x) for x in input("Enter the numbers to be sorted separated by space: ").split())
numbers=random.sample(range(0, 999), 900)

print(numbers)
def isSorted(list):
    for index in range(len(list)-1):
        if list[index] > list[index + 1]:
            return False
    return True

while not isSorted(numbers):
    random.shuffle(numbers)

print(numbers)
