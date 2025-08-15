# p23.py
# Han Rockhill
# python version 3.12.2
# 02/27/2024 - 03/01/24
# Write a program to let a child practice arithmetic skills.
# The program should first ask for what kind of practice is wanted:
# addition(1), subtraction(2), or multiplicatio(3)... (no division).
# Then, the program will have a loop for each of the the desired operations that lets the user repeat the practice
# as many times as desired, Two random numbers will be generated (0 - 9), and the child will have to
# add, subtract or multiply them.
# If the child answers the question correctly, congratulate them, and give them two different numbers to try.
# If the child answers incorrectly, the problem should be repeated (with the two same numbers).
# Note: You are not allowed to use the eval() or sum() functions!

# start by asking what kind of testing
from random import randint
while True:
    testType = input("Select your practice problem type(1-3)? \n(1.) Addition \n(2.) Subtraction \n(3.) Multiplication \n >> ")
    # addition problem loop
    if testType == '1':
        print("okay, addition problems.")
        while True:
            addValue_1 = (randint(1,9))
            print(" ", addValue_1)
            # get the + sign and the value on the same line for looks
            print("+", end=' ')
            addValue_2 = (randint(1,9))
            print(addValue_2)
            # seperator
            print("--------")
            # get the real answer
            sumValue = addValue_1 + addValue_2
            # get the players answer
            playerValue = int(input("  "))
            # are they correct?
            if sumValue == playerValue:
                # congratulate
                print("excellent")
            else:
                # reprimand
                print("clearly you need practice")
            # see if they want to continue
            again = input("another? (y/n): ")
            if again == 'n':
                # exit out when no
                print("Exiting to menu.")
                break
            elif again == 'y':
                # go again if yes
                print("Okay, another round.")
            else:
                # handle the error and exit to menu
                print("Invalid input. Exiting to menu.")
                break

    # subtraction problem loop
    if testType == '2':
        print("okay, subtraction problems.")
        while True:
            subValue_1 = (randint(1, 9))
            print(" ", subValue_1)
            print("-", end=' ')
            subValue_2 = (randint(1, 9))
            print(subValue_2)
            print("--------")
            subValue = subValue_1 - subValue_2
            playerValue = int(input("  "))
            if subValue == playerValue:
                print("excellent")
            else:
                print("clearly you need practice")
            again = input("another? (y/n): ")
            if again == 'n':
                print("Exiting to menu.")
                break
            elif again == 'y':
                print("Okay, another round.")
            else:
                print("Invalid input. Exiting to menu.")
                break

    # multiplication problem loop
    if testType == '3':
        print("okay, multiplication problems.")
        while True:
            multValue_1 = (randint(1, 9))
            print(" ", multValue_1)
            print("x", end=' ')
            multValue_2 = (randint(1, 9))
            print(multValue_2)
            print("--------")
            multValue = multValue_1 * multValue_2
            playerValue = int(input("  "))
            if multValue == playerValue:
                print("excellent")
            else:
                print("clearly you need practice")
            again = input("another? (y/n): ")
            if again == 'n':
                print("Exiting to menu.")
                break
            elif again == 'y':
                print("Okay, another round.")
            else:
                print("Invalid input. Exiting to menu.")
                break

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p23.py =====================
Select your practice problem type(1-3)? 
(1.) Addition 
(2.) Subtraction 
(3.) Multiplication 
 >> 1
okay, addition problems.
  9
+ 3
--------
  12
excellent
another? (y/n): y
Okay, another round.
  3
+ 2
--------
  5
excellent
another? (y/n): n
Exiting to menu.
Select your practice problem type(1-3)? 
(1.) Addition 
(2.) Subtraction 
(3.) Multiplication 
 >> 2
okay, subtraction problems.
  2
- 5
--------
  3
clearly you need practice
another? (y/n): y
Okay, another round.
  2
- 8
--------
  -6
excellent
another? (y/n): n
Exiting to menu.
Select your practice problem type(1-3)? 
(1.) Addition 
(2.) Subtraction 
(3.) Multiplication 
 >> 3
okay, multiplication problems.
  3
x 6
--------
  18
excellent
another? (y/n): y
Okay, another round.
  9
x 9
--------
  3
clearly you need practice
another? (y/n): n
Exiting to menu.
Select your practice problem type(1-3)? 
(1.) Addition 
(2.) Subtraction 
(3.) Multiplication 
 >> 
 '''




