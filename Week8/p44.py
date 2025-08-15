# p44.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
# You have 1000 lockers and 1000 students. All lockers are initially locked.
# 1st student opens all lockers
# 2nd student closes every other locker
# 3rd student opens(if closed) or closes (if open) every 3rd locker
# 4th student opens(if closed) or closes (if open) every 4th locker
# .
# .
# .
# 1000th student opens(if closed) or closes (if open) every 1000th locker
# Write a program to determine which exact locker numbers are open, and total number that are open.
# You are not allowed to use Python function  count()!!

# basic starting info
# create a list to represent lockers
lockers = []
# lock areLocked = 1
# lock areOpen = 0
for lock in range(0,1000,1):
    lockers.append(1)
print('Total lockers', len(lockers))
print('After all 1000 students open or close all the lockers they are going to...')
#print(lockers)


# student 1 opens all the lockers
for lock in range(0,1000,1):
    lockers[lock] = 0
#print('student 1 opens all lockers')
#print(lockers)


# student 2 closes every other locker
for lock in range(1,1000,2):
    lockers[lock] = 1
#print('student 2 closes every other locker')
#print(lockers)


# students 3 through 11 either closes or opens every corresponding locker
for student in range(3,1001):
    for lock in range(student-1,1000,student):
        if lockers[lock] == 1:
            lockers[lock] = 0
        elif lockers[lock] == 0:
            lockers[lock] = 1
    #print('student', student, 'opens or closes every', student, 'locker')
    #print(lockers)



count = 0
for i in range(0,1000,1):
    if lockers[i] ==0:
        count+=1
        print('index [', i, '] aka locker', i+1, 'is open')
print('There are', count, 'open lockers')

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p44.py ======================
Total lockers 1000
After all 1000 students open or close all the lockers they are going to...
index [ 0 ] aka locker 1 is open
index [ 3 ] aka locker 4 is open
index [ 8 ] aka locker 9 is open
index [ 15 ] aka locker 16 is open
index [ 24 ] aka locker 25 is open
index [ 35 ] aka locker 36 is open
index [ 48 ] aka locker 49 is open
index [ 63 ] aka locker 64 is open
index [ 80 ] aka locker 81 is open
index [ 99 ] aka locker 100 is open
index [ 120 ] aka locker 121 is open
index [ 143 ] aka locker 144 is open
index [ 168 ] aka locker 169 is open
index [ 195 ] aka locker 196 is open
index [ 224 ] aka locker 225 is open
index [ 255 ] aka locker 256 is open
index [ 288 ] aka locker 289 is open
index [ 323 ] aka locker 324 is open
index [ 360 ] aka locker 361 is open
index [ 399 ] aka locker 400 is open
index [ 440 ] aka locker 441 is open
index [ 483 ] aka locker 484 is open
index [ 528 ] aka locker 529 is open
index [ 575 ] aka locker 576 is open
index [ 624 ] aka locker 625 is open
index [ 675 ] aka locker 676 is open
index [ 728 ] aka locker 729 is open
index [ 783 ] aka locker 784 is open
index [ 840 ] aka locker 841 is open
index [ 899 ] aka locker 900 is open
index [ 960 ] aka locker 961 is open
There are 31 open lockers
'''