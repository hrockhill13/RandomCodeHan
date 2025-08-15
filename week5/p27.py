# p26.py
# Han Rockhill
# python version 3.12.2
# 02/27/2024 - 03/01/2024
# Write a program that generates a random list of letters.
# # start with an empty_list = [ ] and use
# empty_list.append(Letter) # to add letters to the list
# The length of the list of letters changes every time you run the program.
# There can be a random number of X  letters on the list, where X is a random number between 50 to 75.
# Each of the letters on the list is a random letter between A to F (uppercase).
# Use a loop to generate the list and then Show the generated list of letters to the user.
# Count and then show to the user how many times the letter B appears.
# In order to receive credit, you may not use python built-in function "count()" !

from random import randint

print("\n> Lets generate some random letters <")

empty_listL = []        # start at empty list
ranQty = randint(50, 75)        # how many random letters to generate
print("  Randomly generating %i" % ranQty, "letters\n")       # show user

# generate our random numbers for the list (empty_listL)
ranNum =0

for i in range(0, ranQty, 1):
    ranNum = randint(65,70)     # using ascii char table instead of building own key (pre-mapped)
    # :note to self: this works in this case since all values returned are int
    # and maps to a valid str
    empty_listL.append(chr(ranNum))

    '''
    # I started with this solution before I looked at your hint and realized I could use ascii
    # left it here as a reference
    # build a key to map the randint to str (A-F)
    ranNum = randint(1, 6)     # using standard int
    if ranNum == 1:
        ranLet = 'A'
    elif ranNum == 2:
        ranLet = 'B'
    elif ranNum == 3:
        ranLet = 'C'
    elif ranNum == 4:
        ranLet = 'D'
    elif ranNum == 5:
        ranLet = 'E'
    elif ranNum == 6:
        ranLet = 'F'
    empty_listL.append(ranLet)     # add them to list (empty_listL)
    '''
print(empty_listL)      # show list
pickLet = chr(66)       # search value for the chr(int)
letTotal = 0        # start at zero found letter in list

# our search letter value (B)
print("\nSearching for how many times '%s'" % pickLet, "appears in our list.")

for i in range(0, ranQty, 1):
    if empty_listL[i] == pickLet:       # count the letters that match the search
        letTotal += 1       # add them to the total
print("The letter 'B' appears in the list %i" % letTotal, "times.")

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p27.py =====================

> Lets generate some random letters <
  Randomly generating 50 letters

['E', 'A', 'A', 'A', 'F', 'B', 'F', 'F', 'E', 'A', 'B', 'C', 'A', 'D', 'A', 'C', 'C', 'E', 'A', 'A', 'B', 'A', 'B', 'F', 'D', 'D', 'D', 'D', 'C', 'E', 'D', 'E', 'B', 'C', 'B', 'D', 'A', 'C', 'B', 'A', 'B', 'F', 'A', 'F', 'A', 'A', 'F', 'F', 'B', 'A']

Searching for how many times 'B' appears in our list.
The letter 'B' appears in the list 9 times.
'''