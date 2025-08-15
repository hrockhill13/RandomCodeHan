# Recipe Suggestion Generator
# Han Rockhill
# 02.29.2024 (leap day) happy birthday grandpa! love ya
# 42° degrees / MoonRockMeads
from random import randint, sample, choice

def generate_recipe_list():
    recipeList = []

    honey_types = ['wildflower honey', 'clover honey', 'orange blossom honey', 'ollieberry honey', 'NorCal honey', 'mesquite honey', 'sage honey', 'agave honey', 'maple syrup']
    spice_types = ['cinnamon', 'vanilla', 'basil', 'juniper', 'chai', 'hops', 'rosemary', 'cilantro', 'pumpkin','nutmeg', 'ginger', 'cloves', 'oak', 'cayenne', 'lavender', '', '','']
    fruit_types = ['apple', 'banana', 'pear', 'mango', 'peach', 'grape', 'pineapple', 'apricot', 'blackberry', 'strawberry', 'blueberry', 'raspberry', 'cranberry', 'lemon', 'orange', 'tangerine', 'papaya', 'fig', 'plum', 'cherry', 'coconut', '', '', '']
    pepper_types = ['habanero', 'jalapeno', 'red-chili', '', '', '', '', '', '', '', '']
    nut_types = ['macadamia', 'pecan', 'cashew', '', '', '', '', '', '', '', '']

    honeyType = randint(1, 9)
    if honeyType <= 9:
        recipeList.append(choice(honey_types))

    spiceType = randint(1, 18)
    if spiceType >= 15:
        recipeList.extend(sample(spice_types, 2))
    else:
        recipeList.append(choice(spice_types))

    fruitType = randint(1, 24)
    if fruitType >= 21:
        recipeList.extend(sample(fruit_types, 2))
    else:
        recipeList.append(choice(fruit_types))

    pepperType = randint(1, 11)
    if pepperType < 4:
        recipeList.append(choice(pepper_types))

    nutType = randint(1, 11)
    if nutType < 4:
        recipeList.append(choice(nut_types))

    return [item for item in recipeList if item]  # Remove empty strings

print("\nRecipe Suggestion:", generate_recipe_list())