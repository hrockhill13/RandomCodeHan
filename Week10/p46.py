# p46.py
# Han Rockhill
# python 3.12.2
# 4/13/2024
# Write a Python program to do the following:
#
#     Let the user enter a file name (such as "myMovies.txt").
#     Let the user enter the titles of 4 of their favorite movies using a loop.
#     Write using a loop the 4 movie titles to a file, one per line, and closes the file.
#     Read the 4 movie titles from "myMovies.txt" using splitlines(), stores them in a list, and then shows the list.
#     Write the titles in reverse order into a file "reverseOrder.txt"

# user creates file
fileName = str(input("Enter a file name (no spaces): "))
#print(fileName + ".txt")
print("Enter your 4 favorite movies")
totalMovies = 4  # Set the total number of movies

# empty list to store the movies
favoriteMovies = []

# gather 4 movies
for i in range(totalMovies):
    movie = input(f"movie {i + 1}= ")
    favoriteMovies.append(movie)

# write the movies to a file one per line
userFile = open(fileName + ".txt", 'w')
for movie in favoriteMovies:
    userFile.write(movie + "\n")
userFile.close()

# read the movies from the file
theFile = open(fileName + ".txt", 'r')
fileAsStrs = theFile.read().splitlines()
theFile.close()

# show the list
print(fileAsStrs)

# write the list in reverse order to a file
fileAsStrs.reverse()
#print(fileAsStrs)

revOrd = open("reverseOrder.txt", 'w')
for movie in fileAsStrs:
    revOrd.write(movie + "\n")
revOrd.close()
'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p46.py =====================
Enter a file name (no spaces): myMOvies
Enter your 4 favorite movies
movie 1= Big trouble in Little China
movie 2= Aliens
movie 3= Ghostbusters
movie 4= Ted
['Big trouble in Little China', 'Aliens', 'Ghostbusters', 'Ted']

'''
