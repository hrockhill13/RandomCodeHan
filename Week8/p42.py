# p42.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
#Write the below 5 functions according to the following requirements:
#    sum (list_parameter) : returns the sum of numbers inside a list
#    average (list_parameter) : returns the average of numbers inside a list
#    min (list_parameter) : returns the smallest of all numbers inside a list
#    max (list_parameter) : returns the largest of all numbers inside a list
#    main () : calls all the other functions above

# do imports first
from random import randint

# then define functions
# function name: sum
# function parameter: myList
# function return: sum of all numbers in a list
# function description: GET THE SUM OF THE NUMBERS
def sum(myList):
    # set sum start to 0
    sum = 0
    # iterate through the array
    for number in myList:
        # don't count 0, this line isn't needed
        if number != 0:
            # add each number to the sum
            sum += number
    # show the sum
    return print('Here is the sum of that list of numbers: ', sum)

# function name: average
# function parameter: myList
# function return: average of all numbers in a list
# function description: GET THE AVERAGE OF THE NUMBERS
def average(myList):
    # set the sum to 0
    sum = 0
    # iterate through the array
    for number in myList:
        # add each number to the sum
        sum += number
    # find the average by taking the total and dividing by the length of list
    average = sum / len(myList)
    # show average
    return print ('Here is the average of that list of numbers: ', int(average))

# function name: min
# function parameter: myList
# function return: smallest value from all numbers in a list
# function description: FIND THE MIN
def min(myList):
    # set the smallest number to first number in list
    smallest = myList[0]
    # iterate through the numbers in myList
    for number in myList:
        # check if the number[i] is smaller than smallest
        if number < smallest:
            # if so make it the new smallest
            smallest = number
    # show the smallest number
    return print('The smallest (min) number in that list is: ', smallest)

# function name: max
# function parameter: myList
# function return: largest value from all numbers in a list
# function description: FIND THE MAX
def max(myList):
    # set largest number to first number in list
    largest = myList[0]
# iterate through the numbers in myList
    for number in myList:
    # check to see if number[i] is larger than largest
        if number > largest:
        # if so make it the new largest
            largest = number
    # show largest number
    return print('The largest (max) number in that list is: ', largest)

# function name: main
# function parameter: none
# function return: none
# function description: calls all the other functions, starts the program
def main():
    myList = []
    # ASK USER HOW MANY NUMBERS SHOULD BE IN THE LIST
    X = int(input("How many numbers do you want in your list?: "))
    # for each index in range (the number of numbers selected by user)
    for number in range(X):
        # generate a random number
        number = randint(1, 100)
        # append the list (myList) with a new number (if not doing random it will start at 0 then 1,2,3, etc..)
        myList.append(number)
    # show me the list
    print('Here is the list: ', myList)
    # call the other functions with the contents of myList
    sum(myList)
    average(myList)
    min(myList)
    max(myList)
    return

# kick off the program
main() # call main(), thereby calling all the other functions included inside

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p42.py ======================
How many numbers do you want in your list?: 12
Here is the list:  [37, 100, 82, 40, 25, 24, 49, 89, 22, 48, 43, 89]
Here is the sum of that list of numbers:  648
Here is the average of that list of numbers:  54
The smallest (min) number in that list is:  22
The largest (max) number in that list is:  100
'''
