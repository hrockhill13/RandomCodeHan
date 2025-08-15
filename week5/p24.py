# p24.py
# Han Rockhill
# python version 3.12.2
# 02/27/2024 - 03/01/2024
# Write a program that generates X random integers Num.
# Num is a random number between 20 to 50.
# X is a random number between 10 to 15.
# Calculate and show the Smallest, Largest, Sum, and Average of those numbers.
# You are not allowed to use the following Python functions;
# sample(), min(), max(), average(), sort(), sorted()!!

from random import randint

# set the variables
Num = [randint(20, 50) for _ in range(15)]
X = randint(10, 15)
value = Num[0]

# show the list of numbers
print("Here is a bunch of random numbers:")
for i in range(1, X):
    value += Num[i]
    print(Num[i])

# Calculate and show the smallest
smallest = Num[0]
for i in range(1, X):
    if Num[i] < smallest:
        smallest = Num[i]
print('The smallest number is', smallest)

# Calculate and show the largest
largest = Num[0]
for i in range(1, X):
    if Num[i] > largest:
        largest = Num[i]
print('The largest number is', largest)

# Calculate and show the sum
print("The sum of all the numbers is", value)

# Calculate and show the average
average = Num[0]
for i in range(1, X):
    average = value / X
print('The average (whole number) of the values is %i ' % (average))

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p24.py =====================
Here is a bunch of random numbers:
21
26
28
38
21
37
31
21
43
23
24
42
36
36
The smallest number is 21
The largest number is 43
The sum of all the numbers is 452
The average (whole number) of the values is 30 
'''