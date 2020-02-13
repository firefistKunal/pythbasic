import random
import matplotlib.pyplot as plt

def part1(choice, doors): # on player's first pick a door not containing prize is revealed
    if choice=='empty':
        open_door='also_empty'
    elif choice=='also_empty':
        open_door='empty'
    else:
        open_door=random.choice(['empty', 'also_empty'])
    return open_door # since the host know which door has prize he will always reveal and empty door the first time

def noChange(choice):# player choses to stay with the original choice
    if choice=='prize': 
        return 1 # the original choice of the player contained prize
    else:
        return 0

def change(choice, doors):#player choses to switch the doors

    index=doors.index(choice)# I was unable to use doors.remove(choice) as it always returning NONE for some reason
    del doors[index]# the first choice is removed and 
                    # we see the remaining door that player switched to contains prize or not
    
    if doors==['prize']:
        return 1
    else:
        return 0    

iteration=10000

print("For {} trials each we get".format(iteration))
no_change_win = change_win = 0

for i in range(iteration):
    doors=['prize', 'empty', 'also_empty']
    random.shuffle(doors)

    first_choice=random.choice(doors)

    first_reveal=part1(first_choice, doors)
    doors.remove(first_reveal)# once host reveals an empty door there's only two doors remaining
    
    # players are given a choice to switch their first picked door or stay with their original choice
    no_change_win += noChange(first_choice)
    change_win += change(first_choice, doors)

no_switch_win=(no_change_win/iteration)*100
switch_win=(change_win/iteration)*100

print("No change win percentage is {}\nChanging Door win percent is {}". format(no_switch_win, switch_win))

# pie chart from the result
plt.title("Win Percentage for {} Simulations Each".format(iteration))
plt.pie([no_switch_win, switch_win], labels=('On Not Switching Doors', 'On Switching Doors'), autopct='%1.1f%%', startangle=90)
plt.show()