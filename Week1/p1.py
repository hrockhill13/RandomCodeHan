# p1.py
# Han Rockhill
# 1/31/24
# Python 3.12.1
# sample of output to file (console)
bName = "42 Degrees Brewing Co."     # bname (brewer name) is a variable
fName = "Hank 'tank' Nepper"         # fname is full name variable
sDate = "2019"                       # sDate is founded on date variable
brews = ['mead', 'beer', 'wine', 'cider'] # list of brews
print("Welcome to", bName)          # begin welcome message
print("Founded in %s" % sDate)              # date
print("by %s" % fName)                      # name of founder
print("We make {}" % brews)         # end message with menu list
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: /Users/42o/Documents/p1.py ===================
Welcome to 42 Degrees Brewing Co.
Founded in 2019
by Hank 'tank' Nepper
We make ['mead', 'beer', 'wine', 'cider']
'''
