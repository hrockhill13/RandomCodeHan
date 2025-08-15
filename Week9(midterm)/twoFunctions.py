# twoFunctions.py
# Han Rockhill
# python 3.12.2
# 03/24/2024
#
# Function 1:
# Write a function named "speed" which has 2 PARAMETERS: distance, time.
# The functions computes and PRINTS the speed = distance/ time .
# The value is shown rounded to 2 values to the right of the decimal point.
import time
def speed(distance, time):
    mySpeed = distance / time
    print ('The speed = %.2f' %mySpeed)
speed(100, 5)

# Function 2:
# Write a function named "middle" which has 3 PARAMETERS: num1, num2, num3.
# The function RETURNS the middle/median value of the 3 arguments.
# Assume 3 different values as parameters.
# Note: Median is not the same as Average!
# Show the value that the function returns after it was called.

def middle(num1, num2, num3):
    aList = [num1, num2, num3]
    for number in range(0, len(aList) - 1, 1):
        if aList[number] > aList[number + 1]:
            temp = aList[number]
            aList[number] = aList[number + 1]
            aList[number + 1] = temp
    # the median calculation (split the diff and add it to the start value)
    median = (((aList[-1] - aList[0]) / 2)) +aList[0]
    return print('The Median is:', median) # median of the three values

#middle(5,3,10)
middle(2,4,6)
#middle(0,1120,567)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Desktop/twoFunctions.py =====================
The speed = 20.00
The Median is: 4.0
'''