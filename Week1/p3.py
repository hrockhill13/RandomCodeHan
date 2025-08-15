# p3.py
# Han Rockhill
# 1/31/2024
# Python 3.12.1
# Description: Program to take input in Python
btype = input("BrewType: ")                 # this is a string to label what your measuring
name = input("RecipeName: ")                # another string description denoting recipe
iGrav = float(input("InitialGravity#: "))   # this is float value
age = int(input("BrewDate (dd/mm/yy): "))   # this is a integer value (time not used for calc)
fGrav = float(input("FinalGravity#: "))     # this is a float value
abv = float(iGrav - fGrav)*131
abv = round(abv, 2)
label = "BREW LABEL"
print("")                                   # this is where I start building the label output
print("")
print("----------------------")
print(" >>>>", label, "<<<<")
print("|                    |")
print("|                    |")
print("   ", btype.upper())
print("   ", name.upper())
print("    Brewed: ", age)
print("       ABV: ", abv)
# print("       ABV: %.2f" % abv)     ...I preferred the legibility of the round() format -for now
print("|                    |")
print("|                    |")
print(" >>>>", label, "<<<<")
print("----------------------")
print("", end=' ')                          # adding a space at the end for looks and allow cropping
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: /Users/42o/Documents/p3.py ===================
BrewType: mead
RecipeName: chaichaichiapet
InitialGravity#: 1.080
BrewDate (dd/mm/yy): 013124
FinalGravity#: 1.040


----------------------
 >>>> BREW LABEL <<<<
|                    |
|                    |
    MEAD
    CHAICHAICHIAPET
    Brewed:  13124
       ABV:  5.24
|                    |
|                    |
 >>>> BREW LABEL <<<<
----------------------
 
'''
