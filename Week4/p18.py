# p18.py
# Han Rockhill
# python version 3.12.2
# 02/20/2024 - 02/21/2024
# Write a program that displays the characters in the ASCII character table from ! to ~.
# Display ten characters per line.
# The characters are separated by exactly one space.

print('')
# while loop to print out the ascii character represented by the number value used
# starting at 33 (the value for !) and ending at 126 (the value for ~), starting count is 0
# using https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html as the source of truth
count = 0
asciiValue = 33     # starting value for the ascii character table
while asciiValue < 127:     # ending value for the ascii character table
# show characters on the same line
    print(chr(asciiValue), end=' ')     # this prints the characters and inserts the space on the same line
# count every character that is shown, we will use this later below
    count += 1
# Keep adding a new number to the output
    asciiValue += 1
    if count == 10:     # keep appending the same line until you have 10 characters showing
        print()     # show a new line
        # reset count to zero, and restart loop to complete each new line
        count = 0
print('')

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Downloads/p18.py =====================

! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 

'''