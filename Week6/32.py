# 32.py
# Han Rockhill
# python 3.12.2
# 03/02/24 - 03/06/2024
# Write a function multAdd(a,b,c)  that Returns a*b+c.
# Write a main() function which calls the multAdd(a,b,c) function.
# Pass the three arguments such as 1, 2, 3 from the call in the main()

# define multiAdd function
def multiAdd(a,b,c):
    print(a,'*', b, '+', c,'=')
    #total = a*b+c      # here its formatted to be more readable
    #print('total =', total)
    #return ''
    return a*b+c
def main():
    print(multiAdd(10,2,3))  # print our result from calling into multiAdd with the arguments we passed in main

# our call into the main function
main()

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

======================= RESTART: /Users/42o/Desktop/32.py ======================
10 * 2 + 3 =
23
'''