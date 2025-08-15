# p12.py
# themed to Hitchhikers Guide to the Galaxy
# Han Rockhill
# Python version 3.12.1
# 02/08/2024 - 02/15/2024
# Build a program that can determines if a person can vote
print('')
print('>>>    Vogon Election Ballot Registry Form [VEB1d]      <<<')  # Header text giving instruction
print(">>> Please answer the questions below in order to vote. <<<")
print(">> Fill them out in order and in triplicate to proceed.  <<")
print('')

# start asking questions, starting with citizen
citizen = str(input(" Are you an Vogon citizen? (y/n): "))  # Expecting user to enter y or n
print(" Very well, lets see here... ")

# begin the age question
print('')
age = int(input(" How old, in years, are you as of today?: "))
print(" Hmm k uumm good, hmmm...")

# begin the registration question
print(" ")
register = str(input(" Have you registered to vote in your district? (y/n): "))

# declare what the success conditions are
if age >= 18 and citizen == 'y' and register == 'y':
    print('')
    print(" I see, seems like everything is in order...you can vote in the next Vogon election>")
    print("")
    print(">>>>>    VOGON VOTE APPROVAL CONFIRMATION    <<<<<<")
    print(">>>>>    VOGON VOTE APPROVAL CONFIRMATION    <<<<<<")
    print(">>>>>    VOGON VOTE APPROVAL CONFIRMATION    <<<<<<")
# call out the failure conditions and what is shown to user
# starting with age
else:
    if age < 18:
        print('')
        print(">>>>>     VOGON APPROVAL IS DENIED     <<<<<<")
        print("Oh too bad, you can't vote until...")
        print("You become old enough to vote, your too young.")
# then citizen
    if citizen != 'y':
        print('')
        print(">>>>>     VOGON APPROVAL IS DENIED     <<<<<<")
        print("Only Vogon citizens can vote, ")
        print("unless you completed a Non-Vogon Election Request Waiver form NVERW1a")
# then registered
    if register != 'y':
        print('')
        print(">>>>>     VOGON APPROVAL IS DENIED     <<<<<<")
        print("You will need to fill out a Registration to Vote form RV1b")

'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p12.py =====================

>>>    Vogon Election Ballot Registry Form [VEB1d]      <<<
>>> Please answer the questions below in order to vote. <<<
>> Fill them out in order and in triplicate to proceed.  <<

 Are you an Vogon citizen? (y/n): y
 Very well, lets see here... 

 How old, in years, are you as of today?: 45
 Hmm k uumm good, hmmm...
 
 Have you registered to vote in your district? (y/n): y

 I see, seems like everything is in order...you can vote in the next Vogon election>

>>>>>    VOGON VOTE APPROVAL CONFIRMATION    <<<<<<
>>>>>    VOGON VOTE APPROVAL CONFIRMATION    <<<<<<
>>>>>    VOGON VOTE APPROVAL CONFIRMATION    <<<<<<

===================== RESTART: /Users/42o/Documents/p12.py =====================

>>>    Vogon Election Ballot Registry Form [VEB1d]      <<<
>>> Please answer the questions below in order to vote. <<<
>> Fill them out in order and in triplicate to proceed.  <<

 Are you an Vogon citizen? (y/n): n
 Very well, lets see here... 

 How old, in years, are you as of today?: 61
 Hmm k uumm good, hmmm...
 
 Have you registered to vote in your district? (y/n): y

>>>>>     VOGON APPROVAL IS DENIED     <<<<<<
Only Vogon citizens can vote, 
unless you completed a Non-Vogon Election Request Waiver form NVERW1a

===================== RESTART: /Users/42o/Documents/p12.py =====================

>>>    Vogon Election Ballot Registry Form [VEB1d]      <<<
>>> Please answer the questions below in order to vote. <<<
>> Fill them out in order and in triplicate to proceed.  <<

 Are you an Vogon citizen? (y/n): y
 Very well, lets see here... 

 How old, in years, are you as of today?: 10
 Hmm k uumm good, hmmm...
 
 Have you registered to vote in your district? (y/n): y

>>>>>     VOGON APPROVAL IS DENIED     <<<<<<
Oh too bad, you can't vote until...
You become old enough to vote, your too young.

===================== RESTART: /Users/42o/Documents/p12.py =====================

>>>    Vogon Election Ballot Registry Form [VEB1d]      <<<
>>> Please answer the questions below in order to vote. <<<
>> Fill them out in order and in triplicate to proceed.  <<

 Are you an Vogon citizen? (y/n): y
 Very well, lets see here... 

 How old, in years, are you as of today?: 23
 Hmm k uumm good, hmmm...
 
 Have you registered to vote in your district? (y/n): n

>>>>>     VOGON APPROVAL IS DENIED     <<<<<<
You will need to fill out a Registration to Vote form RV1b
'''
