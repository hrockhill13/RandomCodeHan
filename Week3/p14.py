# p14.py
# Han Rockhill
# Python version 3.12.1
# 02/08/2024 - 02/15/2024
# Program requesting the users birthday and responding with their zodiac sign
print('')
print("Lets determine your zodiac sign")
# have user enter month and day (#)s
month = int(input("Enter the month you were born (1-12): "))
day = int(input("Enter the 'birth' day of that month (1-31): "))

# convert the month (#) input by user into the months name and display that instead
nMonth = int(month)  # align month name string and month number
if month == 1:  # check to see what month number is input
    nMonth = str("January")  # set the month name to the static number
elif month == 2:
    nMonth = str("February")
elif month == 3:
    nMonth = str("March")
elif month == 4:
    nMonth = str("April")
elif month == 5:
    nMonth = str("May")
elif month == 6:
    nMonth = str("June")
elif month == 7:
    nMonth = str("July")
elif month == 8:
    nMonth = str("August")
elif month == 9:
    nMonth = str("September")
elif month == 10:
    nMonth = str("October")
elif month == 11:
    nMonth = str("November")
elif month == 12:
    nMonth = str("December")
print("")

# show user the results
if (month == 3 and day >= 21) or (month == 4 and 0 != day <= 19):  # verify month/day range against zodiac
    print("So, since your birthday is %s -" % nMonth, "%i" % day)  # display month/day
    print("That would make you an Aries aka 'The Ram'")  # display zodiac output
elif (month == 4 and day >= 20) or (month == 5 and 0 != day <= 20):  # rinse, repeat
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Taurus aka 'The Bull'")
elif (month == 5 and day >= 21) or (month == 6 and 0 != day <= 21):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Gemini aka 'The Twins'")
elif (month == 6 and day >= 22) or (month == 7 and 0 != day <= 22):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Cancer aka 'The Crab'")
elif (month == 7 and day >= 23) or (month == 8 and 0 != day <= 22):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Leo aka 'The Lion'")
elif (month == 8 and day >= 23) or (month == 9 and 0 != day <= 22):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Virgo aka 'The Virgin'")
elif (month == 9 and day >= 23) or (month == 10 and 0 != day <= 23):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Libra aka 'The Balance'")
elif (month == 10 and day >= 24) or (month == 11 and 0 != day <= 21):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Scorpio aka 'The Scorpion'")
elif (month == 11 and day >= 22) or (month == 12 and 0 != day <= 21):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Sagittarius aka 'The Archer'")
elif (month == 12 and day >= 22) or (month == 1 and 0 != day <= 19):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Capricorn aka 'The Goat'")
elif (month == 1 and day >= 20) or (month == 2 and 0 != day <= 18):
    print("That would make you an Aquarius aka 'The Water Bearer'")
elif (month == 2 and day >= 19) or (month == 3 and 0 != day <= 20):
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("That would make you a Pisces aka 'The Fishes'")

# this is what is shown in the case of invalid values
else:
    print("So, since your birthday is %s -" % nMonth, "%i" % day)
    print("I cannot determine your zodiac. ")

'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p12.py =====================

Lets determine your zodiac sign
Enter the month you were born (1-12): 1
Enter the 'birth' day of that month (1-31): 6

So, since your birthday is January - 6
That would make you a Capricorn aka 'The Goat'
'''
