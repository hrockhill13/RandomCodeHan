# 29.py
# Han Rockhill
# python 3.12.2
# 03/02/24 -03/06/2024
# Write a function that calculates the absolute value
# and returns the absolute value of a number.
# Do not just use the built-in python function abs()!
# You must write the definition yourself!

# print ( 'The absolute value of -1 is', absolute(-1) )
# print ( 'The absolute value of 1 is', absolute(1) )

# define a function that returns absolute value for an integer
def showAbs(num):
    if num < 0:     # if number is negative, multiply by a negative to ensure a positive
        numb = -1*(num)
        return numb
    numb = (num)
    return numb

# show results for a negative and a positive integer and ensure they both come back with absolute value
print('Absolute value of -1 is: ', showAbs(-1))
print('Absolute value of 1 is: ', showAbs(1))

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

======================= RESTART: /Users/42o/Desktop/29.py ======================
Absolute value of -1 is:  1
Absolute value of 1 is:  1
'''