# p26.py
# Han Rockhill
# python version 3.12.2
# 02/27/2024 - 03/01/2024
# Write a program that generates a random list of numbers.
# (start with an empty list and use append() )
# The length of the list X can be a random number between 15 to 20.
# Each of the random numbers on the list can be between 2 to 5.
# Count how many times the number 3 appears.
#  You are not allowed to use python built-in function "count()" or you'll get a Zero!

from random import randint

print("\n> Lets generate some random numbers <")

empty_listX = []        # start at empty list
ranQty = randint(15, 20)        # how many random letters to generate
print("  Randomly generating %i" % ranQty, "numbers\n")       # show user

# generate our random numbers for the list (empty_listX)
for i in range(0, ranQty, 1):
    ranNum = randint(2, 5)
    empty_listX.append(ranNum)      # add them to list (empty_listX)
print(empty_listX)      # show list

numTotal = 0        # start at zero found numbers in list
#pickNum = int(input("\nPick a number to search for:\n > "))     # pick an int to search for (not used)
pickNum = 3         # our search number value (3)
print("\nSearching for how many times %i" % pickNum, "appears in our list.")

for i in range(0, ranQty, 1):
    if empty_listX[i] == pickNum:       # count the numbers that match the search
        numTotal += 1       # add them to the total
print("That number appears in the list %i" % numTotal, "times.")        # show user total

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p26.py =====================

> Lets generate some random numbers <
  Randomly generating 17 numbers

[4, 2, 2, 3, 3, 2, 3, 5, 2, 2, 5, 4, 4, 4, 3, 2, 4]

Searching for how many times 3 appears in our list.
That number appears in the list 4 times.
'''