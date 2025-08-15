# p21.py
# Han Rockhill
# Python version 3.12.2
# 02/20/2024 - 02/21/2024
# Write a program which calculates exactly how much more (or less)
# you can make with the penny on day 30. A loop must be used.

print('')
pennies = 1  # set the initial value for pennies
for days in range(0, 31, 1):  # set the range from 0 - 31 (using 30 will make the loop never true, so go 1 higher)
    pennies = pennies * 2  # pennies double every day
    if days == 30:  # check to see what is more valuable your penny collection or 1 mil
        # {:,}'.format(pennies) means show pennies total, comma make it more legible
        print('By the 30th day your pennies will total ')
        print('${:,}'.format(pennies / 100, 'pennies'))  # convert the pennies total to $
print("I'd start saving your pennies... it will net far more than the 1 mil")

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Downloads/p21.py =====================

By the 30th day your pennies will total 
$21,474,836.48
I'd start saving your pennies... it will net far more than the 1 mil

'''
