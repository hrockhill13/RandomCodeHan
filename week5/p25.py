# p25.py
# Han Rockhill
# python version 3.12.2
# 02/27/2024 - 03/01/2024
# Write a program that asks the user to input a sentence.
# The program will ask the user what two letters are to be counted.
# You must use a “for” loop to go through the sentence & count how many times the chosen letter appears in the sentence.
# You are not allowed to use python built-in function "count()" or you'll get a Zero!
# Output will show the sentence, the letter, and the number of times the letter appears in the sentence.

sentence = input("Enter your favorite song lyrics:\n-> ")

sentIndex = []  # creates open list for the sentence input
for i in range(0, len(sentence), 1):     # goes through the string from first element 0 to last element len()
    sentIndex += sentence[i]     # adds the element count to itself
    #sentIndex.append(sentence[i])
print("The Lyrics you selected, \n'%s' " % str(sentence))
print("has a total of %i" % len(sentence), "characters in it.")   # prints the number of elements in the song lyric string

# loop to search and count first letter selected by user
input_1 =[]     # setting up empty list for first input
search_1 = input('\n Search for 1st character:\n > ')
while True:
    for i in range(0, len(sentence), 1):
        if sentence[i] == search_1:     # if it finds the item as an element
            input_1 += sentence[i]  # add to the list
    break
print(" Result: [ %i ]" % len(input_1), "instances of the character [ %s ]." % search_1)      # show result

# loop to search and count second letter selected by user
input_2 =[]  # setting up an empty list for second input
search_2 = input('\n Search for 2nd character:\n > ')
while True:
    for i in range(0, len(sentence), 1):
        if sentence[i] == search_2:     # if it finds the item as an element
            input_2 += sentence[i]  # add to the list
    break
print(" Result: [ %i ]" % len(input_2), "instances of the character [ %s ]." % search_2)     # show result

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p25.py =====================
Enter your favorite song lyrics:
-> Roxanne, you don't have to put on the red light
The Lyrics you selected, 
'Roxanne, you don't have to put on the red light' 
has a total of 47 characters in it.

 Search for 1st character:
 > o
 Result: [ 5 ] instances of the character [ o ].

 Search for 2nd character:
 > a
 Result: [ 2 ] instances of the character [ a ].
'''