# Snake Water Gun Game

'''

        snake   water   gun

snake     0       1      -1

water    -1       0       1

gun       1      -1       0

-1 => Lose
 0 => Draw
 1 => Win

'''

import random

mat = [[0,1,-1],[-1,0,1],[1,-1,0]]

print("****** Welcome to the Snake Water and Gun Game ******")
print("Snake = 0")
print("Water = 1")
print("Gun = 2")

while(True):
    choice = int(input("Enter your Choice :- "))
    comp_choice = random.randint(0,2)

    print("Your Choice :- ",choice)
    print("Computer's Choice :- ",comp_choice)

    if(mat[choice][comp_choice] == 0):
        print("Draw")
    elif(mat[choice][comp_choice] == 1):
        print("You Won")
    else:
        print("You Lose")

    ch = str(input("Do you want to continue (y/n) :- "))
    if(ch=="n" or ch=="N"):
        break


print("Thank for playing our game")

