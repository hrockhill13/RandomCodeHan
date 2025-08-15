# abvTable.py
# Han Rockhill
# python 3.12.2
# checks ABV level and can save to a scratch file for later use
def gravity():
    startGrav = float(input('what is the starting gravity?\n > '))
    currentGrav = float(input('what is the current gravity?\n > '))
    maxABV = round((startGrav - 1.000) * 131.25,3)
    realABV = round((startGrav - currentGrav) * 131.25,3)
    ABV = round((76.08 * (startGrav - currentGrav)/(1.775 - startGrav)) / 0.794,2)
    brix = round((((182.4601 * startGrav -775.6821) * startGrav +1262.7794) * startGrav -669.5622),3)
    print('Using OG-FG and multiplying by a factor of 131.25')
    print('The max projected ABV  >  %f' % maxABV)
    print('The absolete current ABV >  %f' % realABV)
    print('or')
    print('The precise current ABV  >>>>>>>>>>>  %f' %ABV)
    print('the brix value = %f' % brix)
    return ABV

sABV = gravity()
# Ask if I want to write it to the save file
saveBrew = str(input("Save to File (y/n)?: "))
if saveBrew == 'y':
    brewName = str(input("Enter the brew name: "))
    recipe = str(input("Enter ingredients: "))
    myFile = open("abvFile.txt", 'a')
    myFile.write('\n')
    myFile.write(brewName)
    myFile.write("\nBottle ABV is %s" % str(sABV))
    myFile.write('\n')
    myFile.write(recipe)
    myFile.write('\n')
    myFile.close()
