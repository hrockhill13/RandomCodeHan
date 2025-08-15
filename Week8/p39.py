# p39.py
# Han Rockhill
# Python 3.12.2
# 03/22/2024
# Write a program that asks the user to enter a sentence.
# Your program will:
#     Show how many words are in the sentence
#     Show the last word of the sentence
#     Ask the user to enter their own word, and count how many times their word appears in the sentence
# Note: you can't use the built-in python function count() to do this!

#create a sentence
sentence = str(input("please enter a sentence: "))
#split the sentence into words
words = sentence.split()
# print the number of words
print('There are', len(words), 'words in this sentence.')
print('Dont believe me?, Here they are\n', words)
#print the first word
print("This is the first word: ", words[0])
# print the last word
print("This is the last word: ", words[-1])
# select any word to search for
selection = str(input("select any word: "))
# set the number of times we see that word initially to 0
wordCount = 0
# search the array for
for i in range(0, len(words),1):
# ^index^      ^len of array^ -- make it go through the list for each value in array

    # if we find the match count it
    if selection == words[i]:
        wordCount += 1
# show the user how many times the word showed up
print("The chosen word appears", wordCount, 'times')

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p39.py ======================
please enter a sentence: star light star bright first star I see tonight
There are 9 words in this sentence.
Dont believe me?, Here they are
 ['star', 'light', 'star', 'bright', 'first', 'star', 'I', 'see', 'tonight']
This is the first word:  star
This is the last word:  tonight
select any word: star
The chosen word appears 3 times
'''