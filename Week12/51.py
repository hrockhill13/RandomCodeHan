# 51.py
# Han Rockhill
# Python 3.12.2
# 04/21/2024

# Write a date Class with three variables (mm(month), dd(day), yyyy(year))
# allow user to enter date in 00/00/00 format
# 2 functions setDate(), showDate()

class Date:
    def __init__(self, newDate='01/01/01'):
        newMM, newDD, newYY = newDate.split('/') # create an object to use the functions on
        self.month = newMM
        self.day = newDD
        self.year = newYY


    def setDate(self, newDate):
        newMM, newDD, newYY = newDate.split('/') # set a new date value
        self.month = newMM
        self.day = newDD
        self.year = newYY

    def showDate(self):
        print(f'{self.month}/{self.day}/{self.year}') # survey says... show me the date



anyDate = Date()    # create anyDate
anyDate.showDate()  # show date
anyDate.setDate('12/21/25') # change the date
anyDate.showDate()  # show date
aDate1 = Date() # create aDate1
aDate1.setDate('05/06/70') # change the date
aDate1.showDate() # show the date
anotherDate = Date('11/27/35') # create anotherDate with non default values
anotherDate.showDate()  # show the date

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: /Users/42o/PycharmProjects/Week11/51.py ============
01/01/01
12/21/25
05/06/70
11/27/35
'''