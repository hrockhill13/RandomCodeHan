# p47.py
# Han Rockhill
# python 3.12.2
# 04/13/2024
#
# Write a program which :
#
#     Writes a random number (50 to 55) of numbers (0 to 100) in a file
#     Opens the file and reads the numbers from it into a list
#     Sorts the list and Shows it.
#     Calculates the median.
#
# Note: You may NOT use the Python built in functions: sort(), sorted(), sum(), median()


from random import randint

# number of random numbers
qtyNumbers = randint(50,55)
#print(qtyNumbers)

# create a file I can append
aNumber = open("numbers.txt", 'a')

# number of random numbers equal to qtyNumbers
for i in range(qtyNumbers):
   aNumber.write(str(randint(1,100)) + "\n")

# close the file
aNumber.close()
theFileList = open("numbers.txt", 'r')

# add the numbers to a list in the file one line each
fileAsStrs = theFileList.read().splitlines()
theFileList.close()
# change the str values to ints before sorting
fileAsInts = []
for number in fileAsStrs:
   fileAsInts.append(int(number))

# show me the unsorted strings and ints (should match)
#print('unsorted strings = ', fileAsStrs)
#print('unsorted integers = ', fileAsInts)

# sort the list from low to high with bubble sort
n = len(fileAsInts)
for i in range(n):
    for j in range(0, n - i - 1):
        if fileAsInts[j] > fileAsInts[j + 1]:
            temp = fileAsInts[j]
            fileAsInts[j] = fileAsInts[j + 1]
            fileAsInts[j + 1] = temp

# show me the sorted list of integers
print('Sorted List: ', fileAsInts)

# calculate the median of the fileAsInts[]
n = len(fileAsInts)
if n % 2 != 0:
    median = fileAsInts[n // 2]
else:
    # If the length of the list is even, the median is the average of the two middle elements
    median = (fileAsInts[n // 2 - 1] + fileAsInts[n // 2]) / 2

print("Median:", median)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p47.py =====================
Sorted List:  [2, 3, 3, 7, 7, 8, 9, 10, 13, 14, 17, 19, 25, 29, 30, 32, 38, 39, 39, 41, 42, 44, 45, 49, 52, 57, 58, 61, 62, 63, 64, 64, 67, 71, 72, 72, 74, 74, 74, 74, 79, 79, 80, 80, 81, 86, 86, 91, 93, 94, 95, 98, 98, 99]
Median: 59.5

'''


