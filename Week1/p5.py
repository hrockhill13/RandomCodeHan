# p5.py
# Han Rockhill
# 02/01/2024
# Python 3.12.1
# Sum and Product of two numbers
print("Enter some values below to use calculator")
# Here the user will enter two values, I used float in case user tries decimals
num1 = float(input("Enter any number: "))
num2 = float(input("Enter any second number: "))
# the functions that can be calculated
difResult = num1 - num2 # subtraction
addResult = num1 + num2 # addition
prodResult = num1 * num2 # multiplication
divResult = num1 / num2 # division
# Here are the results as presented to the user once calculation is completed, I chose not to limit it to 2 decimals
print("The difference of those values is: ", num1, "-", num2, '=', difResult)   # subtraction print out
print("The sum of those values is: ", num1, "+", num2, '=', addResult)          # addition print out
print("The product of those values is: ", num1, "x", num2, '=', prodResult)     # multiplication print out
print("Dividing the first by the second is: ", num1, "/", num2, "=", divResult) # division print out
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: /Users/42o/Documents/p5.py ===================
Enter some values below to use calculator
Enter any number: 100
Enter any second number: 20.5
The difference of those values is:  100.0 - 20.5 = 79.5
The sum of those values is:  100.0 + 20.5 = 120.5
The product of those values is:  100.0 x 20.5 = 2050.0
Dividing the first by the second is:  100.0 / 20.5 = 4.878048780487805
'''
