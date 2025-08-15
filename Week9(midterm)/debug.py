# debug.py
# Han Rockhill
# python 3.12.2
# 03/24/2024

def  isEven(num): # should have a parameter
  if  num % 2 == 0:
      return True
  elif num % 2 != 0:
      return False

def  main(): # needs to be called first
    num = int(input("Please enter a number: "))
    print ("The number %i is even:" %num, isEven(num))
    return

main()

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Desktop/debug.py =====================
Please enter a number: 100
The number 100 is even: True

'''