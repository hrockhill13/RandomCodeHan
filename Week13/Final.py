# Final.py
# Han Rockhill
# python 3.12.2
# 03/30/2024
# Final Exam Program:
# You may not use any built-in python functions such as:
# sum(), average(), sort(), sorted(), median() ...unless you define them yourself (as you did in p50)
#
# A) Use a loop to make 10 random numbers between 20 and 30, store them in a variable numList  .
#   ( Hint: use numList.append(number), where number is a randomint between 20 and 30 )
# B) Sort the list using the bubble sort you learned in this class.
# C) Show the sorted list and the unsorted list.
# D) Find the sum, and average of the numbers in numList .
# E) Find the median of the list.
#   ( Hint for 10 numbers the median is the average of the two numbers in the middle)
# F) Show how many numbers are evenly divisible by 2
# G) Copy/paste the Output of your program (A-F) as a multiline comment at the bottom of your program .
from random import randint

numList = []
# (A) create the random numbers using a loop
for num in range(0,10,1):
    numbers = (randint(20,30))
    numList.append(numbers)

# (C) show the unsorted list
print('Unsorted List: ', numList)

# variable for the length of numList (will be used in two sections - sort/median)
n = len(numList)
# (B) sort/organize the list of numbers using bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        if numList[j] > numList[j + 1]:
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp

# (C) show the sorted list
print('Sorted List: ', numList)

sum = 0
# (D) find the sum of the numbers in the list
for num in numList:
    sum += num
print('Sum = ', sum)


# (E) find the median of the numbers in the list
# If the length of the list is even, the median is the average of the two middle elements
median = (numList[4] + numList[5]) / 2
# OR median = (numList[n // 2 - 1] + numList[n // 2]) / 2

print('Median: ' , median)

# (F) show how many numbers are divisible by 2
numToTest = numList
# is the number divisible by anything besides itself and one
for numToTest in numList:
    for number in range(10,numToTest):
        if numToTest % number == 0:
            print(numToTest, 'is a number divisible by 2')
            break


# (G) show my work
'''Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Desktop/Final.py =====================
Unsorted List:  [25, 25, 24, 21, 22, 29, 25, 28, 22, 30]
Sorted List:  [21, 22, 22, 24, 25, 25, 25, 28, 29, 30]
Sum =  251
Median:  25.0
22 is a number divisible by 2
22 is a number divisible by 2
24 is a number divisible by 2
28 is a number divisible by 2
30 is a number divisible by 2
'''