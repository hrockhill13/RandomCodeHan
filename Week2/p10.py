# p10.py
# Han Rockhill
# 02/05/24 - 02/07/24
# Python 3.12.1
# Letter Grade output with input validation
print("")
score = float(input("Please enter the % score you got on your last test: "))
if score < 0 or score > 100:
    print("You need to enter a valid test score between 1% and 100%.")
    score = float(input("Please enter the % score you got on your last test: "))

if score >= 90 and score <= 100:
    print("Looks like you got an 'A' on that test.")
elif score < 90 and score >= 80:
    print("That would mean you got a 'B' on your test.")
elif score < 80 and score >= 70:
    print("Well a 'C' on that test isn't too bad try harder on the next one.")
elif score < 70 and score >= 60:
    print("Damn dude a 'D' on that test? You should have studied.")
elif score < 60:
    print("It's time to re-evaluate your education level, an 'F' is a horrible grade.")
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/p10.py =====================

Please enter the % score you got on your last test: -9
You need to enter a valid test score between 1% and 100%.
Please enter the % score you got on your last test: 9.9
It's time to re-evaluate your education level, an 'F' is a horrible grade.

'''