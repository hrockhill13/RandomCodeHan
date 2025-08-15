# p41.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
#
# Write a function which outputs as many crosses
# as the parameter 'numCrosses' indicates.
# For example, when parameter 'numCrosses' equals 5,
# the function displays the following:
#  +
#  + +
#  + + +
#  + + + +
#  + + + + +
# You are not allowed to use string "concatenation" or multiplication.
# Also the use of a list and appending to a list is not permitted.
# You must solve the problem using 2 loops (one 'for' loop nested in the other).

def cross(numCrosses):
    for row in range(0, numCrosses,1):
        print('+ ', end='')
        for column in range(0, row, 1):
            print('+ ', end ='')
        print()
cross(5)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p41.py ======================
+ 
+ + 
+ + + 
+ + + + 
+ + + + + 
+ + + + + + 
+ + + + + + + 
+ + + + + + + + 
+ + + + + + + + + 
+ + + + + + + + + + 
'''