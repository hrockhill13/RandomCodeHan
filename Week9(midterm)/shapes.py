# shapes.py
# Han Rockhill
# python 3.12.2
# 03/24/2024
# A quadrilateral is a shape with 4 sides and 4 angles.
# Write a program that lets the user enter 4 sides and 4 angles into LISTS.
# The program checks if the type of quadrilateral is either:
# - Rhombus
# - Square
# - Rectangle

# create the empty lists to hold sides and angles
angles = []
sides = []

# enter the side values
print('Enter 4 side values')
for s in range(4):
    aSide = int(input('>> '))
    sides.append(aSide)


# sort the list to make comparison easier
for i in range(len(sides)):
    for number in range(0, len(sides)-i-1):
        if sides[number] > sides[number + 1]:
            temp = sides[number]
            sides[number] = sides[number + 1]
            sides[number + 1] = temp


# enter the angle values
print('Enter 4 angle values')
for a in range(4):
    aAngle = int(input('>> '))
    angles.append(aAngle)


# define the sum of all the angles
sumAngle = angles[0]+angles[1]+angles[2]+angles[3]

# define each shape we care about or call out invalid shape
if sumAngle != 360:
    print("Angles don't add up to 360°, not a valid quadrilateral")
else:
    if sides[0] == sides[1] == sides[2] == sides[3]:
        if angles[0] == angles[1] == angles[2] == angles[3] == 90:
            print('Quadrilateral type: a Square')
        else:
            print('Quadrilateral type: a Rhombus')
    elif sides[0] == sides[1] and sides[2] == sides[3]:
        if angles[0] == angles[1] == angles[2] == angles[3] == 90:
            print('Quadrilateral type: a Rectangle')
    else:
        print('Unrecognized quadrilateral')

print(sides)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Desktop/shapes.py =====================
Enter 4 side values
>> 5
>> 5
>> 5
>> 5
Enter 4 angle values
>> 90
>> 90
>> 90
>> 90
Quadrilateral type: a Square
[5, 5, 5, 5]

===================== RESTART: /Users/42o/Desktop/shapes.py =====================
Enter 4 side values
>> 5
>> 5
>> 5
>> 5
Enter 4 angle values
>> 135
>> 45
>> 135
>> 45
Quadrilateral type: a Rhombus
[5, 5, 5, 5]

===================== RESTART: /Users/42o/Desktop/shapes.py =====================
Enter 4 side values
>> 2
>> 2
>> 1
>> 2
Enter 4 angle values
>> 56
>> 76
>> 89
>> 76
Angles don't add up to 360°, not a valid quadrilateral
[1, 2, 2, 2]

===================== RESTART: /Users/42o/Desktop/shapes.py =====================
Enter 4 side values
>> 2
>> 10
>> 2
>> 10
Enter 4 angle values
>> 90
>> 90
>> 90
>> 90
Quadrilateral type: a Rectangle
[2, 2, 10, 10]

===================== RESTART: /Users/42o/Desktop/shapes.py =====================
Enter 4 side values
>> 12
>> 13
>> 14
>> 15
Enter 4 angle values
>> 45
>> 45
>> 135
>> 135
Unrecognized quadrilateral
[12, 13, 14, 15]
'''