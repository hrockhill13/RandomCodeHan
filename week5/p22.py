# p22.py
# Han Rockhill
# python version 3.12.2
# 02/27/2024 - 03/01/24
# Write a Dice Game program that generates two random dice values between 1 and 6 for you, and 2 for the computer.
# You get to roll as many times as you like (if you don't like your 2 dice), while the computer only rolls once, after you have decided that you like your two dice.
# Determine who wins, you or the computer.

# this brings in the ability to use/generate random variables
from random import randint
# start program
print("\n> Roll off against the computer <")
while True:
    # generate 2 random numbers in range 1-6
    userDice = [randint(1, 6), randint(1, 6)]
    #            ^^^0^^^               ^^^1^^^
    diceSum = 0
    for diceValues in userDice:
            diceSum += diceValues

    # show player their rolls/score
    print('player, your rolls were [',userDice[0], "and", userDice[1],"]")
    print('your score: ',diceSum)

    # Check if user wants new dice
    print('')
    saveRoll = input("Press 'y' to accept, else any key to re-roll ")
    if saveRoll != 'y':
        print("okay re-rolling...")
    if saveRoll == 'y':
        break

# Now let computer roll their dice
# generate 2 random numbers in range 1-6
comDice = [randint(1, 6), randint(1, 6)]
#            ^^^0^^^               ^^^1^^^
comSum = 0
for diceValues in comDice:
    comSum += diceValues

print('computer rolls [', comDice[0], 'and', comDice[1], ']')
print("computer's score: ", comSum)

# compare to see who won and show player
if comSum > diceSum:
    print("\n> The Computer is obviously better at this than you.")
elif comSum < diceSum:
    print("\n> Looks like all that rolling paid off, you win!")
elif comSum == diceSum:
    print("\n> you tied")

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p22.py =====================

> Roll off against the computer <
player, your rolls were [ 6 and 4 ]
your score:  10

Press 'y' to accept, else any key to re-roll y
computer rolls [ 4 and 6 ]
computer's score:  10

> you tied

===================== RESTART: /Users/42o/Documents/p22.py =====================

> Roll off against the computer <
player, your rolls were [ 1 and 3 ]
your score:  4

Press 'y' to accept, else any key to re-roll y
computer rolls [ 3 and 4 ]
computer's score:  7

> The Computer is obviously better at this than you.

===================== RESTART: /Users/42o/Documents/p22.py =====================

> Roll off against the computer <
player, your rolls were [ 2 and 6 ]
your score:  8

Press 'y' to accept, else any key to re-roll y
computer rolls [ 6 and 4 ]
computer's score:  10

> The Computer is obviously better at this than you.

===================== RESTART: /Users/42o/Documents/p22.py =====================

> Roll off against the computer <
player, your rolls were [ 5 and 4 ]
your score:  9

Press 'y' to accept, else any key to re-roll y
computer rolls [ 2 and 1 ]
computer's score:  3

> Looks like all that rolling paid off, you win!
'''
