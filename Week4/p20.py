# p15.py
# Han Rockhill
# Python version 3.12.1
# 02/08/2024 - 02/15/2024
# Write a program that asks the user to enter a random qty of numbers in any order (positive or negative).
# The program shows:
#    the sum of all numbers (sumAll)
#    the sum of positive numbers (sumPos),
#    the sum of negative numbers (sumNeg)

# ask user how many numbers to add
qtyEnter = int(input("How many numbers do you want to add?: "))
# Initialize all the sums to zero
sumAll = 0
sumPos = 0
sumNeg = 0
# here is the loop we repeat n times
for qty in range(0, qtyEnter, 1):
    n = float(input("Enter a number in range (-x to x): "))
# when the number is positive we add it to sumPos
    if n > 0:
        sumPos += n
# when the number is negative we add it to sumNeg
    if n < 0:
        sumNeg += n
# We add all the values together
    sumAll += n
# show the output of all the values adding them together qtyEnter times
print('')
print("The sum of all numbers is:", sumAll)
print("The sum of positive numbers is:", sumPos)
print("The sum of negative numbers is:", sumNeg)

'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p20.py =====================
How many numbers do you want to add?: 5
Enter a number in range (-x to x): 2
Enter a number in range (-x to x): 5
Enter a number in range (-x to x): -9
Enter a number in range (-x to x): 8
Enter a number in range (-x to x): 2

The sum of all numbers is: 8.0
The sum of positive numbers is: 17.0
The sum of negative numbers is: -9.0
'''