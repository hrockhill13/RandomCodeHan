# p57.py
# Han Rockhill
# Python 3.12.2
# 05/10/24
# brute force password hack
count = 0
alist = []

lista = "This is a test list"
print(alist)
alist = lista.split(' ')
print(alist)
for i in lista:
    alist.append(i)
print(alist)
for a in alist:
    if a == 'a':
        count += 1
print(count)






'''string = input('Enter test string: ')  # this is the string itself
# search for characters in a string
characters = [] # this is character list from the string
for i in range(0, len(string), 1):
    characters +=string[i] # adds the element to itself
print('The string is: %s' % string)
print ('number of characters is %s: '% len(string), 'items')
'''
string = str("US District Judge Aileen Cannon will hear arguments from defense attorneys on two separate bids to throw out charges in the case. In the first motion, Trump’s valet and co-defendant Walt Nauta alleges he is being vindictively prosecuted, and in the second, Trump and his co-defendants argue the indictment suffers technical flaws requiring its dismissal.")
characters = list(string)  # Convert the string directly into a list of characters
print('The string is:', string)
print('Number of characters:', len(characters))


# look for a specific item
char_count = []
search_1 = input('which character are we looking for?: ')
while True:
    for i in range(0, len(string), 1):
        if string[i] == search_1:
            char_count += string[i]
    break

print("found [%i]" % len(char_count))


search_items = str('US District Judge Aileen Cannon will hear arguments from defense attorneys on two separate bids to throw out charges in the case. In the first motion, Trump’s valet and co-defendant Walt Nauta alleges he is being vindictively prosecuted, and in the second, Trump and his co-defendants argue the indictment suffers technical flaws requiring its dismissal.').split()
char_counts = {}

# Count occurrences of each search item
for search_item in search_items:
    char_counts[search_item] = string.count(search_item)

# Find the word with the highest count
max_count = max(char_counts.values())
max_word = [word for word, count in char_counts.items() if count == max_count]

print("Search item(s) with the highest count:", max_word)
print("Count:", max_count)


# introduce the string
the_string = 'US District Judge Aileen Cannon will hear arguments from defense attorneys on two separate bids to throw out charges in the case. In the first motion, Trump’s valet and co-defendant Walt Nauta alleges he is being vindictively prosecuted, and in the second, Trump and his co-defendants argue the indictment suffers technical flaws requiring its dismissal.'
char_counts = {}

# count occurrences of each word
for words in the_string:
    char_counts[words] = string.count(words)

# find the three words with the highest count in order
max_count = max(char_counts.values())
max_word = [word for word, count in char_counts.items() if count == max_count]

# show the result
print ('items with the highests count(s)', max_word)
print('count:', max_count)





