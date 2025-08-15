# p11.py
# Han Rockhill
# 02/05/24 - 02/07/24
# Python 3.12.1
# Build a Rock, Paper, Scissors Game (in this case rock, paper, scissors, lizard, spock)

import random
p1 = random.randint(1, 5)  # this is computers selection
print("")
print("           ROCK/PAPER/SCISSORS/LIZARD/SPOCK             ")
print("     You will play against the computer, good luck      ")
print("        Enter a number value shown below to play        ")
print("1 = Rock, 2 = Scissors, 3 = Paper, 4 = Lizard, 5 = Spock")
print("")
p2 = int(input("Make your selection: "))  # this is the players selection
#  print("Player throws = ", p2)   # this line isn't needed (just duplicates the selection, cleaner without)
print("Computer throws = ", p1)
# define the values for each selection
rock = 1
scissors = 2
paper = 3
lizard = 4
spock = 5

# Here we build the logic table for result.

# conditions where the computer will win
if p1 == rock and p2 == scissors:
    print("The computer wins, rock smashes scissors")
elif p1 == rock and p2 == lizard:
    print("The computer wins, rock crushes lizard")
elif p1 == paper and p1 == rock:
    print("The computer wins, paper covers rock")
elif p1 == paper and p2 == spock:
    print("The computer wins, paper disproves spock")
elif p1 == scissors and p2 == paper:
    print("The computer wins, scissors cuts paper")
elif p1 == scissors and p2 == lizard:
    print("The computer wins, scissors decapitates lizard")
elif p1 == lizard and p2 == paper:
    print("The computer wins, lizard eats paper")
elif p1 == lizard and p2 == spock:
    print("The computer wins, lizard poisons spock")
elif p1 == spock and p2 == rock:
    print("The computer wins, spock vaporizes rock")
elif p1 == spock and p2 == scissors:
    print("The computer wins, spock breaks scissors")

# conditions where the player will win
if p1 == rock and p2 == paper:
    print("The player wins, paper covers rock")
elif p1 == rock and p2 == spock:
    print("The player wins, spock vaporizes rock")
elif p1 == paper and p2 == scissors:
    print("The player wins, scissors cuts paper")
elif p1 == paper and p2 == lizard:
    print("The player wins, lizard eats paper")
elif p1 == scissors and p2 == rock:
    print("The player wins, rock smashes scissors")
elif p1 == scissors and p2 == spock:
    print("The player wins, spock breaks scissors")
elif p1 == lizard and p2 == rock:
    print("The player wins, rock crushes lizard")
elif p1 == lizard and p2 == scissors:
    print("The player wins, scissors decapitates lizard")
elif p1 == spock and p2 == paper:
    print("the player wins, paper disproves spock")
elif p1 == spock and p2 == lizard:
    print("The player wins, lizard poisons spock")

# conditions where player and computer will tie
if p1 == rock and p2 == rock:
    print("You tied the computer")
elif p1 == paper and p1 == paper:
    print("You tied the computer")
elif p1 == scissors and p2 == scissors:
    print("You tied the computer")
elif p1 == lizard and p2 == lizard:
    print("You tied the computer")
elif p1 == spock and p2 == spock:
    print("You tied the computer")
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/p11.py =====================

           ROCK/PAPER/SCISSORS/LIZARD/SPOCK             
     You will play against the computer, good luck      
1 = Rock, 2 = Scissors, 3 = Paper, 4 = Lizard, 5 = Spock

Make your selection: 5
Computer throws =  2
The player wins, spock breaks scissors

'''