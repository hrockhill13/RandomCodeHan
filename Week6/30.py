# 30.py
# Han Rockhill
# python 3.12.2
# 03/02/24 - 03/06/2024
# Write a function which has two parameters, N and M.
# The function returns True if N is evenly divisible by M, and False otherwise

def isDivisible(N,M):
    print('The function we will verify whether', N, 'is evenly divisible by', M, '.')
    if (N % M) == 0: # N is divisible by M:'
        return True
    return False


print('The statement is', isDivisible(4,4)) # expect it to be true
print('The statement is', isDivisible(5,7)) # expect it to be false

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

======================= RESTART: /Users/42o/Desktop/30.py ======================
The function we will verify whether 4 is evenly divisible by 4 .
The statement is True
The function we will verify whether 5 is evenly divisible by 7 .
The statement is False
'''