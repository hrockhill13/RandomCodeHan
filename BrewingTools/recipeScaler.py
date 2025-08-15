# Recipe Scaler
# Han Rockhill
# 42° degrees / MoonRockMeads
# 02/10/2024
# A Program to scale ingredients depending on size of batch desired.
print('')
print("         >>>>>   RECIPE SCALER   <<<<<")

# Determine recipe size
origScale = float(input("          Original Batch Size(gal): "))
chooseScale = float(input("          New Batch Size(gal): "))

# how big or how small are we changing this recipe to
if chooseScale > origScale:
    newScale = chooseScale*origScale
    # show average conversion scale ballpark
    print("The new recipe will be ~%.1f x larger than the original size " % newScale)

elif chooseScale < origScale:
    newScale = 1/(origScale/chooseScale)
    # show average conversion scale ballpark
    print("The new recipe will be ~%.02f x smaller than the original size." % newScale)

# Lets start gathering some ingredient data
print('')
print('')
print("Lets get more specific......... ")
print("Enter the original recipe below")

print('-------------------------------')
waterLevel = float(input("(gal) of Water: "))

juiceLevel = input("(gal) of Juice: ")
if juiceLevel == '':
    juiceLevel = float(0)
else:
    juiceLevel = float(juiceLevel)
if juiceLevel != 0:
    juiceName = input("Juice Type: ")

honeyLevel = input("(lbs) of Honey: ")
if honeyLevel == '':
    honeyLevel = float(0)
else:
    honeyLevel = float(honeyLevel)
if honeyLevel != 0:
    honeyName = input("Honey Type: ")



fruitLevel = input("(lbs) of Fruit: ")
if fruitLevel == '':
    fruitLevel = float(0)
else:
    fruitLevel = float(fruitLevel)
if fruitLevel != 0:
    fruitName = input("Fruit Type: ")

# check to see if we entered anything and skip additional steps if not
if fruitLevel == 0:
    fruitLevel1 = 0
else:
    fruitLevel1 = input("(lbs) of Fruit 2: ")
if fruitLevel1 == '':
    fruitLevel1 = float(0)
else:
    fruitLevel1 = float(fruitLevel1)
if fruitLevel1 != 0 and fruitLevel != 0:
    fruitName1 = input("Fruit Type: ")


grainLevel = input("(lbs) of Grain: ")
if grainLevel == '':
    grainLevel = float(0)
else:
    grainLevel = float(grainLevel)
if grainLevel != 0:
    grainName = input("Grain Type: ")

# one line example of the below
# spiceLevel = float(0) if (spiceLevel := input("(oz) of Spice: ")) == '' else float(spiceLevel); spiceName = input("Spice Type: ")
spiceLevel = input("(oz) of Spice: ")
if spiceLevel == '':
    spiceLevel = float(0)
else:
    spiceLevel = float(spiceLevel)
if spiceLevel != 0:
    spiceName = input("Spice Type: ")
# end example block: NOTE: example doesnt work in the below because of the extra condition for original item

if spiceLevel == 0:
    spiceLevel1 = 0
else:
    spiceLevel1 = input("(oz) of Spice 2: ")
if spiceLevel1 == '':
    spiceLevel1 = float(0)
else:
    spiceLevel1 = float(spiceLevel1)
if spiceLevel1 != 0 and spiceLevel != 0:
    spiceName1 = input("Spice Type: ")

if spiceLevel1 == 0:
    spiceLevel2 = 0
else:
    spiceLevel2 = input("(oz) of Spice 3: ")
if spiceLevel2 == '':
    spiceLevel2 = float(0)
if spiceLevel2 != 0 and spiceLevel != 0:
    spiceName2 = input("Spice Type: ")

# Here we display the outputs of the scaler using the information the user added above,
# providing the recipe in an easy to read format that can be followed.
print("")
print("     >>>>> Here is the NEW RECIPE <<<<<")

waterLevel = waterLevel*newScale
print("           %.02f gal. of water." % waterLevel)

juiceLevel = juiceLevel*newScale
if juiceLevel < 1 and juiceLevel != 0:
    juiceLevel = juiceLevel*16
    print("           %.02f cups of %s juice." % (juiceLevel, juiceName))
elif juiceLevel >= 1:
    print("           %.02f gal. of %s juice." % (juiceLevel, juiceName))

honeyLevel = honeyLevel*newScale
if honeyLevel < 1 and honeyLevel != 0:
    honeyLevel = honeyLevel*16
    print("           %.02f oz. of %s honey." % (honeyLevel, honeyName))
elif honeyLevel >= 1:
    print("           %.02f lbs. of %s honey." % (honeyLevel, honeyName))

fruitLevel = fruitLevel*newScale
if fruitLevel < 1 and fruitLevel != 0:
    fruitLevel = fruitLevel*16
    print("           %.02f oz. of %s." % (fruitLevel, fruitName))
elif fruitLevel >= 1:
    print("           %.02f lbs. of %s." % (fruitLevel, fruitName))

fruitLevel1 = fruitLevel1*newScale
if fruitLevel1 < 1 and fruitLevel1 != 0 and fruitLevel != 0:
    fruitLevel1 = fruitLevel1*16
    print("           %.02f oz. of %s." % (fruitLevel1, fruitName1))
elif fruitLevel1 >= 1:
    print("           %.02f lbs. of %s." % (fruitLevel1, fruitName1))

grainLevel = grainLevel*newScale
if grainLevel < 1 and grainLevel != 0:
    grainLevel = grainLevel*16
    print("           %.02f oz. of %s." % (grainLevel, grainName))
elif grainLevel >= 1:
    print("           %.02f lbs. of %s." % (grainLevel, grainName))

spiceLevel = spiceLevel*newScale
if spiceLevel < 1 and spiceLevel != 0:
    spiceLevel = spiceLevel * 28.35
    print("           %.02f grams of %s." % (spiceLevel, spiceName))
elif spiceLevel >= 1:
    print("           %.02f oz. of %s." % (spiceLevel, spiceName))

spiceLevel1 = spiceLevel1*newScale
if spiceLevel1 < 1 and spiceLevel1 != 0:
    spiceLevel1 = spiceLevel1 * 28.35
    print("           %.02f oz. of %s." % (spiceLevel1, spiceName1))
elif spiceLevel1 >= 1:
    print("           %.02f oz. of %s." % (spiceLevel1, spiceName1))

spiceLevel2 = spiceLevel2*newScale
if spiceLevel2 < 1 and spiceLevel2 != 0:
    spiceLevel2 = spiceLevel2 * 28.35
    print("           %.02f oz. of %s." % (spiceLevel2, spiceName2))
elif spiceLevel2 >= 1:
    print("           %.02f oz. of %s." % (spiceLevel2, spiceName2))
