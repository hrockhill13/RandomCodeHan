# brewCalc
# Han Rockhill
# 42° degrees / MoonRockMeads
# started 02/07/24
# small program to capture all the relevant data on fermentation
'''
from datetime import datetime

print("")
print(">>>     Brew Rate Calculator    <<<")

# capture some initial values
iGrav = float(input('Starting gravity: '))
str_d1 = str(input("Start Date YY/MM/DD: "))

# determine ABV expectation (max value)
pAbv = (iGrav - 1.00)*131.25
pAbv = round(pAbv, 2)
print('')
print('~All gravity > 1.000 = fermentable sugar')
print("Fully Dry projected ABV will = %.02f" % pAbv, "%")
print('')
# capture most recent values to compare against
print('CHECKPOINT')
fGrav = float(input('Current gravity: '))
end_d2 = input("Current Date YY/MM/DD: ")

# convert string to date object
d1 = datetime.strptime(str_d1, "%y/%m/%d")
d2 = datetime.strptime(end_d2, "%y/%m/%d")

# compare starting gravity with final gravity
abv = (iGrav - fGrav)*131.25
abv = round(abv, 2)

# output the calculated real ABV
print('')
print('Current ABV is: ', abv, '%')

# difference between dates in timedelta
delta = d2 - d1
print(f'It has been Fermenting for {delta.days} days')

# calculations for fermentation rate/%/time
fComplete = (abv / pAbv)*100
fRate = fComplete / delta.days
fLeft = (100 - fComplete)
fEnd = fLeft / fRate

# provide some fermentation data to the user
print('Fermentation completion = %.0f' % fComplete, '%')
if fRate >= 1:
    print('Fermentation rate = %.02f' % fRate, '% per day')
    print('To ferment completely dry it will take ~ %.0f more days' % fEnd)
elif fRate < 1:
    print('Fermentation rate = %.02f' % fRate, '% per day')
    print('Fermentation is either stalled or finished.')
'''
from datetime import datetime

print("")
print(">>>     Brew Rate Calculator    <<<")

# capture some initial values
iGrav = float(input('Starting gravity: '))
str_d1 = str(input("Start Date MM.DD.YY: "))

# determine ABV expectation (max value)
pAbv = (iGrav - 1.00) * 131.25
pAbv = round(pAbv, 2)
print('')
print('~All gravity > 1.000 = fermentable sugar')
print("Fully Dry projected ABV will = %.02f" % pAbv, "%")
print('')

while True:
    # capture most recent values to compare against
    print('')
    print('CHECKPOINT')
    fGrav_input = input('Current gravity: ')

    if not fGrav_input:
        break  # Exit the loop if the user presses Enter

    fGrav = float(fGrav_input)
    end_d2 = input("Current Date MM.DD.YY: ")

    # convert string to date object
    d1 = datetime.strptime(str_d1, "%m.%d.%y")
    d2 = datetime.strptime(end_d2, "%m.%d.%y")
    centered_d2 = f"{d2.strftime('%m-%d-%Y')}".center(34)

    # compare starting gravity with final gravity
    abv = (iGrav - fGrav) * 131.25
    abv = round(abv, 2)

    # output the calculated real ABV
    print('')
    print('Current ABV is: ', abv, '%')

    # difference between dates in timedelta
    delta = d2 - d1
    print(f'It has been Fermenting for {delta.days} days')

    # calculations for fermentation rate/%/time
    fComplete = (abv / pAbv) * 100
    fRate = fComplete / delta.days
    fLeft = (100 - fComplete)
    fEnd = fLeft / fRate

    # provide some fermentation data to the user
    print('Fermentation completion = %.0f' % fComplete, '%')
    if fRate >= 1:
        print('Fermentation rate = %.02f' % fRate, '% per day')
        print('To ferment completely dry it will take ~ %.0f more days' % fEnd)
    elif fRate < 1:
        print('Fermentation rate = %.02f' % fRate, '% per day')
        print('Fermentation is either stalled or finished.')
print("")

name = input("Recipe Name: ")
centered_name = f"{name.upper()}".center(34)

notes_list = []

while True:
    notes = input("Expected Notes: ")
    if not notes:
        break  # Exit the loop if the user enters an empty string
    notes_list.append(notes)

# moon dictionary
moon_types = {
    "fruit": "Gibbous Moon",
    "braggot": "Solar Eclipse",
    "pepper": "Crescent Moon",
    "session": "New Moon",
    "spiced": "Philodox Moon",
    "traditional": "Full Moon",
    "classic": "Full Moon",
    "wine": "Blood Moon",
    "sack": "Blue Moon",
    "great": "Blue Moon",
    "show": "Full Moon",
    "cider": "Lunar Eclipse",
    "beer": "Solar Eclipse"
}

moon = input("What type of brew is this?: ")
moon = moon_types.get(moon, "UNKNOWN MOON")
centered_moon = f"{moon.upper()}".center(34)

# brew dictionary
brew_types = {
    "Gibbous Moon": "melomel",
    "Crescent Moon": "capsicumel",
    "New Moon": "hydromel",
    "Philodox Moon": "metheglin",
    "Full Moon": "classic",
    "Blue Moon": "great",
    "Blood Moon": "wine",
    "Lunar Eclipse": "cider",
    "Solar Eclipse": "beer"
}

brew = brew_types.get(moon, "unknown brew")
centered_brew = f"{brew.lower()}".center(34)


print('')
print('==================================')
print('=============MOONROCK=============')
print('==================================')
print(centered_name)
print(centered_brew)
print("          ABV  = ", abv, "%")

# Print with 3 items per line
for i in range(0, len(notes_list), 3):
    line = " | ".join(notes_list[i:i + 3])
    centered_line = f"{line.lower()}".center(32)
    print("|",centered_line,"|")
print('----------------------------------')
print(centered_moon)
print(centered_d2)
print('==================================')
print('==============MEADS===============')
print('==================================')

# the SG of a honey = 0.035
# the SG of a sugar = 0.46
