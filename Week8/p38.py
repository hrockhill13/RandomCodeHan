# p38.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
# Write a program that asks the user to enter a sentence.
# The program then finds the longest word in the sentence, and shows it.
# Note: The use of python functions max() and sorted() is not permitted!

# enter a sentence
sentence = str(input("please enter a sentence here: "))
#  break it into a list
words = sentence.split()
# go through the list and find longest word
for index in range(0, len(words), 1):
    if index == 0 :
        longest = words[index]
    else:
        if len(words[index]) > len(longest):
            longest = words[index]
# show me the result
print("The longest word in the sentence you entered is: ", longest)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p38.py ======================
please enter a sentence here: This is a test of the code.
The longest word in the sentence you entered is:  code.
'''