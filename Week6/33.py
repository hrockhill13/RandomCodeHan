# 33.py
# Han Rockhill
# python 3.12.2
# 03/02/24 - 03/06/2024
# “If any of the three sticks is greater than the sum of the other two,
# then you cannot form a triangle. Otherwise, you can.”
# Write a function named isTriangle(a,b,c) that has three sides a,b,c
# as parameters.
# The function returns either True or False, depending on whether you can
# form a triangle from the sides with the given lengths.

# import randint so we can use random numbers to generate sides
from random import randint
def isTriangle(a,b,c):
    Num = (a,b,c) # variables for the values input during the call of the function
    X = 3   # since we are doing a triangle only use three sides
    print("\nComputer,you have", X, "sticks")

# find the largest
    largest = Num[0]
    for i in range(1, X):
        if Num[i] > largest:
            largest = Num[i] # call out the largest

# show user the largest stick
    print('The longest stick is', largest, 'feet long')
# find the smallest
    smallest = Num[0]
    for i in range(1, X):
        if Num[i] < smallest:
            smallest = Num[i] # call out the smallest
# find the one left over
    middle = Num[0]
    for i in range(1, X):
        if Num[i] != smallest and Num[i] != largest:
            middle = Num[i] # call out the middle

# show user the two smallest sticks
    print('The two smallest sticks are', middle, 'and', smallest, 'feet long')
    print('Using these three sticks, do you have a triangle?')

# the sum of 2 smallest sides must be greater than the third
    if smallest+middle>largest:
        return True
    return False


# show three examples by calling function with random variables
print(isTriangle(randint(1,10), randint(1,10), randint(1,10)))
print(isTriangle(randint(1,10), randint(1,10), randint(1,10)))
print(isTriangle(randint(1,10), randint(1,10), randint(1,10)))

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

======================= RESTART: /Users/42o/Desktop/33.py ======================

Computer,you have 3 sticks
The longest stick is 8 feet long
The two smallest sticks are 7 and 7 feet long
Using these three sticks, do you have a triangle?
True

Computer,you have 3 sticks
The longest stick is 10 feet long
The two smallest sticks are 2 and 2 feet long
Using these three sticks, do you have a triangle?
False

Computer,you have 3 sticks
The longest stick is 10 feet long
The two smallest sticks are 8 and 4 feet long
Using these three sticks, do you have a triangle?
True
'''