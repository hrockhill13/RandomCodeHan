# p9.py
# Han Rockhill
# 02/05/24 -  02/07/24
# Python 3.12.1
# Create program to check the users height and provide feedback message
print("Let's find out just how tall you are...")
feet = float(input('Enter a value for your height in feet: '))    # Here we will enter our value for feet
while feet < 0:    # validate the number is a whole number or zero
    print("You cannot enter a negative number.")   # notify of incorrect value
    feet = float(input('Enter a value for your height in feet: '))    # request new input
inches = float(input('Enter a value for your height inches: '))   # Here we will enter a value for inches
while inches < 0:    # validate the number is not a negative to avoid subtracting inches from total
    print("You cannot enter a negative number.")
    inches = float(input('Enter a value for your height inches: '))
totalInches = feet*12 + inches   # | the
totalFeet = feet + inches/12     # | calculations

if totalInches > 0:
    print("%.0f feet %.0f inch(es) = %.0f inches" % (feet, inches, totalInches))
    print("%.0f feet %.0f inch(es) = %.1f feet" % (feet, inches, totalFeet))

if totalInches < 48:
    print("You must be a hobbit.")
elif totalInches > 90:
    print("You might be a giant.")
else: print("Your around average height.")
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/p9.py =====================
Let's find out just how tall you are...
Enter a value for your height in feet: -4
You cannot enter a negative number.
Enter a value for your height in feet: 33
Enter a value for your height inches: -9
You cannot enter a negative number.
Enter a value for your height inches: 0
33 feet 0 inch(es) = 396 inches
33 feet 0 inch(es) = 33.0 feet
You might be a giant.
'''



