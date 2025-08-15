# p6.py
# Han Rockhill
# 02/04/24 - 02/07/24
# Python 3.12.1
# A small program to compute a users height including validation
print("")
feet = float(input('Please enter the number of feet: '))        # Here we will enter our value for feet
inches = float(input('Please enter the number of inches: '))    # enter inch value so we can do the final calculations2
totalInches = feet*12 + inches   # | the calculations

if totalInches > 0:
    print("%.0f feet %.0f inch(es) = %.0f inches" % (feet, inches, totalInches)) # calculate the total inches for the user
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/p6.py =====================

Please enter the number of feet: 5
Please enter the number of inches: 11
5 feet 11 inch(es) = 71 inches
'''
