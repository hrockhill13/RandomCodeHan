# p45.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
# Write a program that calculates and shows all prime numbers between 3 - 100.
# Prime numbers can only be evenly (remainder 0) divided by itself and 1.

#print('All the prime numbers from 3-100:')
numToTest = 100
# is the number divisible by anything besides itself and one
for numToTest in range(2, numToTest +1):
    for number in range(2,numToTest):
        if numToTest % number == 0:
            break
        else:
            # only divisible by self and 1
            if numToTest % number != 0 and number == numToTest-1:
                print(numToTest, 'is a prime number')


'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p45.py ======================
3 is a prime number
5 is a prime number
7 is a prime number
11 is a prime number
13 is a prime number
17 is a prime number
19 is a prime number
23 is a prime number
29 is a prime number
31 is a prime number
37 is a prime number
41 is a prime number
43 is a prime number
47 is a prime number
53 is a prime number
59 is a prime number
61 is a prime number
67 is a prime number
71 is a prime number
73 is a prime number
79 is a prime number
83 is a prime number
89 is a prime number
97 is a prime number
'''