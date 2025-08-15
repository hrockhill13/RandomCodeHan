# p56.py
# Han Rockhill
# Python 3.12.2
# 05/10/24
# Write  ceaser cypher

# create a loop to show the English Alphabet


alphabet = ''
for i in range(65, 91, 1):
    alphabet+= chr(i)

# show the English Alphabet
print('alphabet= ', alphabet)

shift = 13
# show the 'shift' key
print('shift=', shift, 'letters')

# create a loop to show the cypher alphabet
encrypted = ''
for i in range(65, 91, 1):
    if i+shift <91:
        encrypted+= chr(i+shift)
    if i+shift >=91:
        encrypted+= chr(65+(i+shift-91))
# show cypher alphabet
print('encrypted= ', encrypted)

# make empty dictionaries
encrypt = {}
decypher = {}

# Add to the dictionaries
encrypt [ ' ' ] = ' '
decypher [ ' ' ] = ' '
#          ^^Key  ^^value

for i in range(0, len(alphabet), 1):
    encrypt [alphabet[i]] =  encrypted [i]
    decypher [ encrypted[i]] = alphabet[i]

original_message = "CLGUBA VF TERNG"
encrypted_message = ''
for i in range(0, len(original_message)):
    if original_message[i] == ' ':
        encrypted_message += ' '
    else:
        encrypted_message+= encrypt [original_message[i]]

print('original sentence: ', original_message) # this is hello world
print('cypher sentence: ', encrypted_message)
print('...decyphered: ', end='')
for i in range(0,len(encrypted_message), 1):
    print (decypher [encrypted_message[i]], end='')
