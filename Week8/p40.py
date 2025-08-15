# p40.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
#
# Ask the user to enter X numbers into a list.
# Calculate and show the sum, average, min, max of those numbers.
#
# Note: You are not allowed to use any pre-existing python functions such as
# sample(), sum(), min(), max(), average(), sort(), sorted()!!!...unless you write them yourself.
from random import randint
# START WITH A BLANK LIST
myList = []

# ASK USER HOW MANY NUMBERS SHOULD BE IN THE LIST
X = int(input("How many numbers do you want in your list?: "))
# for each index in range (the number of numbers selected by user)
for number in range(X):
    # generate a random number
    number = randint(1,100)
    # append the list (myList) with a new number (if not doing random it will start at 0 then 1,2,3, etc..)
    myList.append(number)
# show me the list
print('Here is your list: ', myList)

# GET THE SUM OF THE NUMBERS
# set sum start to 0
sum = 0
# iterate through the array
# for number in range(0,len(myList),1): -> could also be used but I like the simpler version in this case
for number in myList:
    # don't count 0, this line isn't needed
    if number != 0:
        # add each number to the sum
        sum += number
# show the sum
print('Here is the sum of that list of numbers: ', sum)

# GET THE AVERAGE OF THE NUMBERS
# set the sum to 0
sum = 0
# iterate through the array
for number in myList:
    # add each number to the sum
    sum += number
# find the average by taking the total and dividing by the length of list
average = sum / len(myList)
# show average
print ('Here is the average of that list of numbers: ', int(average))

# FIND THE MIN
# set the smallest number to first number in list
smallest = myList[0]
# iterate through the numbers in myList
for number in myList:
    # check if the number[i] is smaller than smallest
    if number < smallest:
        # if so make it the new smallest
        smallest = number
# show the smallest number
print('The smallest (min) number in that list is: ', smallest)

# FIND THE MAX
# set largest number to first number in list
largest = myList[0]
# iterate through the numbers in myList
for number in myList:
    # check to see if number[i] is larger than largest
    if number > largest:
        # if so make it the new largest
        largest = number
# show largest number
print('The largest (max) number in that list is: ', largest)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p40.py ======================
How many numbers do you want in your list?: 10
Here is your list:  [11, 72, 67, 96, 84, 22, 13, 74, 39, 73]
Here is the sum of that list of numbers:  551
Here is the average of that list of numbers:  55
The smallest (min) number in that list is:  11
The largest (max) number in that list is:  96
'''