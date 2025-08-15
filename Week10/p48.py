# p48.py
# Han Rockhill
# python 3.12.2
# 04/13/2024
# Write a program which reads the data from file sunspots.txt:
# ...and computes the average for each year,
# writing them one per line to a file averages.txt
#
# looks like the below sample
#
# Year   Avg
# 1945   32.29
# 1946   99.88


# Open the File to Read
myFile = open('/Users/42o/PycharmProjects/Week10/sunspots.txt', 'r')

# Read the data from file into a list
listOfLines = myFile.read().splitlines()
#print('listOfLines= \n ', listOfLines)
#print('Year    Average')
myFile.close()
sunSpotAv = open('averages.txt', 'w')
# create the table header
sunSpotAv.write('Year   Avg\n')
for j in range(0,len(listOfLines), 1):
    # show me oneline only
    aLine = listOfLines[j]
    #print('\n aLine= ', aLine)
    # split each line by spaces
    lineData = aLine.split()
    # shows list of strings ['1945','18.5','11.8',...,'28.4']
    # print('lineData= ', lineData)
    # pull out the year only
    year = lineData[0]
    # print('year= ', year)
    sumData = 0
    for i in range (1, len(lineData), 1):
        # add the number strings and convert them to floats
        sumData += float(lineData[i])
    # print('sumData= ', sumData)
    avg = round((sumData/12),2)
    # print('average= ' , average)
    # print(year, '  ', avg)
    # write using only one element
    sunSpotAv.write("%s   %.2f\n" % (year, avg))
sunSpotAv.close()

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: /Users/42o/Documents/p48.py =====================

'''

