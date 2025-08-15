# p43.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
# The function returns the sorted list in ascending order if parameter 'reverse' is False.
# The function returns the sorted list in descending order if parameter 'reverse' is True.
# Function Name:
# def sort(alist, reverse)


from random import randint
def sort(aList, reverse):
    for allnumbers in aList:
        # if reverse is False
        if reverse == False:
            for number in range(0, len(aList) - 1, 1):
                if aList[number] > aList[number + 1]:
                    temp = aList[number]
                    aList[number] = aList[number + 1]
                    aList[number + 1] = temp
        # if Reverse is True
        if reverse == True:
            for number in range(0, len(aList) - 1, 1):
                if aList[number] < aList[number + 1]:
                    temp = aList[number]
                    aList[number] = aList[number + 1]
                    aList[number + 1] = temp
    return print(aList)
# generate a randomish list to work with
aList = [randint(1, 100) for _ in range(randint(3,10))]
# proofs
print('Here is the list is ascending order (Reverse = False)')
sort(aList, False)
print('Here is the list is descending order (Reverse = True)')
sort(aList, True)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p43.py ======================
Here is the list is ascending order (Reverse = False)
[6, 20, 40, 53, 62, 90, 95]
Here is the list is descending order (Reverse = True)
[95, 90, 62, 53, 40, 20, 6]
'''