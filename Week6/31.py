# 31.py
# Han Rockhill
# python 3.12.2
# 03/02/24 - 03/06/2024
# Write a function that has an integer N as parameter and returns true if N is even.
# Hint: A number N is even if N % 2  == 0

# define isEven function
def isEven(N):
    if N %2 == 0:
        print('The value of N is', N)
        return True # if even return true out
    return False    # else return false out if not even

# show result of function using 4 as the test integer
print("This is an even number:", isEven(4))

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

======================= RESTART: /Users/42o/Desktop/31.py ======================
The value of N is 4
This is an even number: True
'''
