# p7.py
# Han Rockhill
# 02/04/24 - 02/07/24
# Python 3.12.1
# Determine the Circumference of a circle from user input values
radius = float(input("What is the radius (in inches) of the circle you want to draw? "))
while radius <= 0:  # validate the radius is a positive number
    print("The value has to be greater than 0 to work, try again")  # inform user the number isn't valid
    radius = float(input("What is the radius (in inches) of the circle you want to draw? "))  # ask for the input again
if radius > 0:  # if the input value is valid allow it to proceed
    print("A circle with radius %.02f inches has" % radius)  # begin returning the calculated values

# calculate the circumference of a circle using the input
circleCir = float(2*radius*3.1415)
print("circumference: %.02f " % circleCir, "inches")
#alculate the area of a circle using the input
areaCir = float(radius*radius*3.1415)
print("area: %.02f " % areaCir, "inches")
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/p7.py =====================
What is the radius (in inches) of the circle you want to draw? 0
The value has to be greater than 0 to work, try again
What is the radius (in inches) of the circle you want to draw? 0
The value has to be greater than 0 to work, try again
What is the radius (in inches) of the circle you want to draw? 0
The value has to be greater than 0 to work, try again
What is the radius (in inches) of the circle you want to draw? 45
A circle with radius 45.00 inches has
circumference: 282.74  inches
area: 6361.54  inches
'''