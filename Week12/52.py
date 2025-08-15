# 52.py
# Han Rockhill
# Python 3.12.2
# 04/21/2024

# Create a class Item which has
# - instance variables: itemName, itemCost
# - class variable: numberItems (gets increased every time a new Item is created)
# - a default constructor that allows the user to set itemName and itemCost
# ( the default constructor sets itemName="apple" itemCost=2.49 if the user does not specify them)
# - function to show() the item name and cost
# - function to get() and set() the item name and cost
#

class Item:
    numberItems = 0

    def __init__(self, newName='apple   ', newCost=2.49):
        self.itemName = newName
        self.itemCost = newCost
        # print(' %s' % newName, '$ %i' % newCost)
        Item.numberItems += 1
        groceryBag.append(self)

    def show(self):
        print('Item >>', self.itemName, '   price each = $', self.itemCost)

    def getName(self):
        return self.itemName

    def getCost(self):
        return self.itemCost

    def setName(self, newName):
        self.itemName = newName

    def setCost(self, newCost):
        self.itemCost = newCost

    def set(self, newName, newCost):
        self.itemName = newName
        self.itemCost = newCost

# create the shopping list and create the grocery bag
groceryBag = []
item0 = Item()
item1 = Item('beer', 20.12)
item2 = Item('burrito', 9.82)
item3 = Item('yogurt', 1.15)
item4 = Item('peanuts', 5.47)
item5 = Item('salmon', 26.36)

# count number of items in grocery bag
print('\nNumber of Items in the Bag=', Item.numberItems)

# get the sum of all items
totalCost = 0
for item in groceryBag:
    totalCost += item.getCost()
print('totalCost=      $', round(totalCost,2))

# Show everything in the bag
print('\n Contents of your grocery bag:')
for item in groceryBag:
    item.show()

item2.setName('taco')
item3.setCost(2.15)
item5.set('chicken', 18.43)


# check again after changes
print('\n  Are you sure, check again..')
print('\n Contents of your grocery bag:')
for item in groceryBag:
    item.show()

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: /Users/42o/PycharmProjects/Week11/52.py ============

Number of Items in the Bag= 6
totalCost=      $ 65.41

 Contents of your grocery bag:
Item >> apple       price each = $ 2.49
Item >> beer    price each = $ 20.12
Item >> burrito    price each = $ 9.82
Item >> yogurt    price each = $ 1.15
Item >> peanuts    price each = $ 5.47
Item >> salmon    price each = $ 26.36

  Are you sure, check again..

 Contents of your grocery bag:
Item >> apple       price each = $ 2.49
Item >> beer    price each = $ 20.12
Item >> taco    price each = $ 9.82
Item >> yogurt    price each = $ 2.15
Item >> peanuts    price each = $ 5.47
Item >> chicken    price each = $ 18.43
'''