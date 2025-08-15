# p13.py
# Han Rockhill
# Python version 3.12.1
# 02/08/2024 - 02/15/2024
# Write a program to convert any given number of total cents (under 100)
# into the correct number of: quarters, dimes, nickels, pennies.
print('')
urCents = int(input("How many cents do you have? (1-100): "))
if urCents <= 0:
    print("You have no cents")
print("If you were to get change in order to end up with the least number of coins..")
quarters = int(urCents / 25)
if quarters > 0:
    print("U would have %.0f quarter(s)" % quarters)
    urCents = urCents - quarters*25

dimes = int(urCents / 10)
if dimes > 0:
    print("U would have %.0f dime(s)" % dimes)
    urCents = urCents - dimes*10

nickels = int(urCents / 5)
if nickels > 0:
    print("U would have %.0f nickel(s)" % nickels)
    urCents = urCents - nickels*5

pennies = int(urCents / 1)
if pennies > 0:
    print("and U would have %.0f pennie(s)" % pennies)

'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p13.py =====================

How many cents do you have? (1-100): 95
If you were to get change in order to end up with the least number of coins..
U would have 3 quarter(s)
U would have 2 dime(s)
'''