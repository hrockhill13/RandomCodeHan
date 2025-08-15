# p15.py
# Han Rockhill
# Python version 3.12.1
# 02/08/2024 - 02/15/2024
# Write a program that asks the user to enter 4 numbers (positive or negative).
# The program shows:
#    the sum of all numbers (sumAll)
#    the sum of positive numbers (sumPos),
#    the sum of negative numbers (sumNeg)
print('')
n1 = float(input("Enter your first number in range (-x to x): "))
n2 = float(input("Enter your second number in range (-x to x): "))
n3 = float(input("Enter your third number in range (-x to x): "))
n4 = float(input("Enter your fourth number in range (-x to x): "))

# add all values together and show result
sumAll = n1 + n2 + n3 + n4
print('')
print("The sum of all the values entered = ", float(sumAll))   # result display

# Look for and add the positive numbers together and show result
sumPos = 0          # set value to 0
if n1 > 0:          # check to see if number is positive
    sumPos += n1    # add the number to sumPos
if n2 > 0:
    sumPos += n2    # alt sumPos = sumPos + n2
if n3 > 0:
    sumPos += n3    # alt sumPos = sumPos + n3
if n4 > 0:
    sumPos += n4    # alt sumPos = sumPos + n4
print("The sum of all the POSITIVE values = ", float(sumPos))  # result display

# Look for and add the Negative numbers together and show result
sumNeg = 0          # set value to 0
if n1 < 0:          # check to see if number is negative
    sumNeg += n1    # add number to sumNeg
if n2 < 0:
    sumNeg += n2    # alt sumNeg = sumNeg + n2
if n3 < 0:
    sumNeg += n3    # alt sumNeg = sumNeg + n3
if n4 < 0:
    sumNeg += n4    # alt sumNeg = sumNeg + n4
print("The sum of the all the NEGATIVE values = ", float(sumNeg))   # result display

'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p12.py =====================

Enter your first number in range (-x to x): -100
Enter your second number in range (-x to x): 34
Enter your third number in range (-x to x): 21
Enter your fourth number in range (-x to x): 2.1

The sum of all the values entered =  -42.9
The sum of all the POSITIVE values =  57.1
The sum of the all the NEGATIVE values =  -100.0
'''

