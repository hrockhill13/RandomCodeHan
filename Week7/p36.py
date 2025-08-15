# p36.py (CodingBat.py)
# Han Rockhill
# Python 3.12.2
# 03/09/2024 - 03/15/2024

# string times
# Given a string and a non-negative int n,
# return a larger string that is n copies of the original string.
def string_times(str, times):
        fullString = str * times
        return fullString

# proofs
print(string_times('Hi', 2))   # → 'HiHi'
print(string_times('Hi', 3))   # → 'HiHiHi'
print(string_times('Hi', 1))   # → 'Hi'


# extra end
# Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
# The string length will be at least 2.

def extra_end(str):
        last2x3 = str[-2:]* 3
        return last2x3
# proofs
print(extra_end('Hello')) # → 'lololo'
print(extra_end('ab'))    # → 'ababab'
print(extra_end('Hi'))    # → 'HiHiHi'


# make tags
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
        strTag = '<' + tag + '>' + word + '</' + tag + '>'
        #strTag = f'<{tag}>{word}<{tag}/>'
        return strTag

# proofs
print(make_tags('i', 'Yay') )  # → '<i>Yay</i>'
print(make_tags('i', 'Hello'))     # → '<i>Hello</i>'
print(make_tags('cite', 'Yay'))    # → '<cite>Yay</cite>'


# combo strings
# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
        if len(a) > len(b):
                order = (b+a+b)
        else:
                order = (a+b+a)
        return order
# proofs
print(combo_string('Hello', 'hi'))     # → 'hiHellohi'
print(combo_string('hi', 'Hello'))     # → 'hiHellohi'
print(combo_string('aaa', 'b'))    # → 'baaab'
