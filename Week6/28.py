# 28.py
# Han Rockhill
# python 3.12.2
# 03/02/24 - 03/06/2024
# Write a function which given two integer parameters Returns their sum...
# unless the two values are the same, then the function Returns their doubled sum.

# define the returnSum function
def returnSum(num1, num2):
    if num1 != num2:    # are the numbers different?
        sumNum = num1+num2
        print('Here the numbers (',num1, 'and', num2, '), we are using are not the same.')
        return sumNum   # if the values are the different show sum
    if num1 == num2:    # are the numbers the same?
        sumNum = (num1+num2)*2
        print('Here the numbers (',num1, 'and', num2, '), we are using are the same.')
        return sumNum    # if the values are the same double the shown sum

# calling the function with two sets of inputs to show both results
print('The sum of these numbers is', returnSum(1,4))   # if the values are the different show sum
print('The doubled sum of these numbers is',returnSum(4,4))   # if the values are the same double the shown sum

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

======================= RESTART: /Users/42o/Desktop/28.py ======================
Here the numbers ( 1 and 4 ), we are using are not the same.
The sum of these numbers is 5
Here the numbers ( 4 and 4 ), we are using are the same.
The doubled sum of these numbers is 16
'''
