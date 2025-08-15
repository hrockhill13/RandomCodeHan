# p34.py
# Han Rockhill
# Python 3.12.2
# 03/09/2024
# Write a program that shows the entire song "99 beers on the wall" using recursion (not a loop!)
#
# The song is as follows:
#
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall...
#
# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down, pass it around, 97 bottles of beer on the wall...
# ...
# The same verse is repeated, each time with one bottle fewer, until there are none left.
# ...
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
#
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.


def numBott(beer):

    if beer >= 1:
        print('\n', beer, 'bottles of beer on the wall,', beer, 'bottles of beer...')
        print('\n Take one down, pass it around,', beer-1, ' bottles of beer on the wall.')
        numBott(beer-1)
    else:
        print('\n No more bottles of beer on the wall, no more bottles of beer...')
        print(' Go to the store and buy some more, 99 bottles of beer on the wall')


numBott(99)
