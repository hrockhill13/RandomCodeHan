# myFunctions.py
# Han Rockhill
# python 3.12.2
# 04/21/2024
# You will create a file myFunctions.py , where you will define/write the functions below:
#
#     min(list) # returns min of a list
#     max(list) # returns max of a list
#     avg(list) # returns average of a list
#     sum(list) # returns sum of a list
#     abs(num) # returns absolute value of num
#     find(item,list)# returns true if item value is found in a list
#     isEven(number) # returns true/false if number is even

def min(list): #min(list) # returns min of a list
    minValue = list[0]
    for num in list:
        if num < minValue:
            minValue = num
    return print(minValue)

def max(list): # max(list) # returns max of a list
    maxValue = list[0]
    for num in list:
        if num > maxValue:
            maxValue = num
    return print(maxValue)

def avg(list): # avg(list) # returns average of a list
    count = 0
    total = 0
    for num in list:
        total += num
        count += 1
    avgValue = total / count
    return print(avgValue)

def sum(list): # sum(list) # returns sum of a list
    sum = 0
    total = 0
    for num in list:
        total += num
    sumValue = total
    return (print(sumValue))

def abs(number): # abs(num) # returns absolute value of num
    if number >= 0:
        return number
    else:
        return -number

def find(item, list):
    if item in list:
        return print(True)
    else:
        return print(False)


def isEven(number): # isEven(number) # returns true/false if number is even
    if number %2 == 0:
        print(True)
    else:
        print(False)
    return