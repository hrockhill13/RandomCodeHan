# AG_csm.py
# Han Rockhill
# python version 3.12.2
# 03/06/2025
# Write a program that creates a random CSM army based on some basic initial criteria
# current criteria :
#                   1 Character (to meet warlord criteria)
#                   1 Battle Line (to meet action monkey needs)
#                   # Chaos Allies  <= 25%
#                   TBA : if unit is Unique limit is 1 instead of 3

from random import randint

damned = str('d')
titanic = str('titanic')
vehicle = str('vehicle')

# Define unit types and their costs
unit_data = {
    'Characters': {
        1: ('Chaos Cerastus Knight Acheron', 420, titanic), 2: ('Chaos Cerastus Knight Atrapos', 420, titanic),
        3: ('Chaos Cerastus Knight Castigator', 445, titanic), 4: ('Chaos Cerastus Knight Lancer', 420, titanic),
        5: ('Chaos Questoris Knight Magaera', 435, titanic), 6: ('Chaos Questoris Knight Styrix ', 430, titanic),
        7: ('Knight Abominant', 365, titanic), 8: ('Knight Desecrator', 410, titanic), 9: ('Knight Despoiler', 415, titanic),
        10: ('Knight Rampager', 380, titanic), 11: ('Knight Tyrant', 510, titanic), 12: ('War Dog Stalker', 140, vehicle)
    },
    'Battle line': {1: ('War Dog Brigand', 165, vehicle), 2: ('War Dog Executioner', 130, vehicle),
                    3: ('War Dog Hunstman', 140, vehicle), 4: ('War Dog Karnivore', 140, vehicle),
                    5: ('War Dog Moirax', 160, vehicle), 6: ('War Dog Stalker', 140, vehicle)},
    'Other Datasheets': {
        1: ('Chaos Acastus Knight Asterius', 765, titanic), 2: ('Chaos Acastus Knight Porphyrion', 700, titanic)
    },
    'Chaos Allies': {1: ('Accursed Cultists', 90, damned), 2: ('Dark Commune', 80, damned),
                     3: ('Chaos Cultist', 50, damned), 4: ('Cultist Firebrand', 45, damned),
                     5: ('Fellgor Beastmen', 85, damned), 6: ('Traitor Enforcer', 65, damned),
                     7: ('Traitor Guardsmen Squad', 70, damned)}
}

# Define the battle sizes
battle_sizes = {
    1: ('Combat Patrol', 500),
    2: ('Incursion', 1000),
    3: ('Crusade 1.5', 1500),
    4: ('Strike Force', 2000),
    5: ('Crusade 2.5', 2500),
    6: ('Onslaught', 3000)
}

def generate_unit(max_points):
    csm_units = {'Characters': [], 'Battle line': [], 'Other Datasheets': [], 'Chaos Allies': []}
    army_points = 0  # Initialize army_points as an integer
    unit_counts = {'Characters': {}, 'Battle line': {}, 'Other Datasheets': {}, 'Chaos Allies': {}}
    battle_line_count = 0  # Track the number of battle line units for transport limit
    chaos_allies_count = 0  # Track the number of Chaos Allies units added
    total_units = 0  # Track the total number of units in the army

    # Helper function to track units and enforce the limit
    def add_unit(name, cost, unit_type, limit, unit_tag):
        nonlocal army_points, total_units, chaos_allies_count
        if army_points + cost <= max_points:
            if max_points == 500 and (unit_tag == titanic):  # Skip adding titanic units in Combat Patrol
                return False
            if unit_counts[unit_type].get(name, 0) < limit:
                unit_counts[unit_type][name] = unit_counts[unit_type].get(name, 0) + 1
                army_points += cost
                csm_units[unit_type].append((name, cost))  # Add the unit as a tuple (name, cost)
                total_units += 1  # Increment the total number of units
                if unit_type == 'Chaos Allies':
                    chaos_allies_count += 1  # Increment Chaos Allies count if added
                return True
        return False

    # Always add a character unit first
    char_name, char_cost, char_type = character()
    add_unit(char_name, char_cost, 'Characters', 3, char_type)  # Limit for characters is 3

    # Track the number of attempts to add a unit
    while army_points < max_points:
        units_attempted = 0
        unit_added = False  # Variable to track whether a unit was added successfully

        # Attempt to add units up to 10 times
        while units_attempted < 10 and not unit_added:
            newUnit = randint(1, 8)
            units_attempted += 1

            # Check the limit of Chaos Allies (no more than 25% of total units)
            if chaos_allies_count > total_units * 0.25:
                # Skip Chaos Allies if the limit has been reached
                newUnit = randint(1, 7)  # Force selection to non-Chaos-Allies units

            # Try to add a unit and check if it fits within the army point and unit count limits
            if newUnit == 1:
                name, cost, type = character()
                unit_added = add_unit(name, cost, 'Characters', 3, type)  # Limit for characters is 3
            elif newUnit in range(2, 5):  # Battle line units
                name, cost, type = battleLine()
                unit_added = add_unit(name, cost, 'Battle line', 6, type)  # Limit for battle line units is 6
                battle_line_count += unit_added  # Increment if battle line unit is added
            elif newUnit == 6:
                # Ensure Chaos Allies only if battle_line_count > 0
                if battle_line_count > 0:
                    name, cost, type = chaosAllies()
                    unit_added = add_unit(name, cost, 'Chaos Allies', battle_line_count, type)
            elif newUnit == 7:
                name, cost, type = otherDatasheet()
                unit_added = add_unit(name, cost, 'Other Datasheets', 3, type)  # Limit for other units is 3

            # If no unit was added after 10 attempts, break out
            if units_attempted >= 10 and not unit_added:
                print(f"Unable to add a valid unit after {units_attempted} attempts. Breaking out of the loop.")
                break  # Exit the loop if no valid unit can be added

        # If no unit was added and attempts were made, break out of the outer loop as well
        if not unit_added:
            print(f"Failed to add units after {units_attempted} attempts.")
            break  # Exit if no valid units can be added even after multiple attempts

    return csm_units, army_points



# Character generation (with cost)
def character():
    char_select = randint(1, 12)
    name, cost, type = unit_data['Characters'][char_select]
    return name, cost, type

# Battle Line generation
def battleLine():
    bl_select = randint(1, 6)
    bl_name, bl_cost, type = unit_data['Battle line'][bl_select]
    return bl_name, bl_cost, type

# Chaos Allies generation
def chaosAllies():
    ca_select = randint(1, 7)
    ca_name, ca_cost, type = unit_data['Chaos Allies'][ca_select]
    return ca_name, ca_cost, type

# Other Datasheet generation
def otherDatasheet():
    od_select = randint(1, 2)
    od_name, od_cost, type = unit_data['Other Datasheets'][od_select]
    return od_name, od_cost, type

# -------- ++++        GAME INTERFACE     ++++  ------------

# Start the application
print('')
print('+++ CSM ARMY LIST GENERATOR +++')

# Get user input to play the game
play_game = input("Create a Chaos Warband...? Y/N \n -> ").strip().lower()

# Exit if the user doesn't want to play
if play_game == 'n' or play_game == 'no':
    print("The Lords of Chaos are displeased, you pussy.")
    exit()

# Game size selection
while True:
    # Try to get an integer input from the user
    game_input = input("How big is this game? \n 1) Combat Patrol - 500.pts \n 2) Incursion - 1000.pts \n 3) Crusade - 1500.pts \n 4) Strike Force - 2000.pts  ** DEFAULT ** \n 5) Crusade - 2500.pts \n 6) Onslaught - 3000.pts \n -> ")

    # If the input is empty or not a valid integer, default to "Strike Force"
    if game_input.strip() == "" or not game_input.isdigit():
        game_name, max_points = battle_sizes[4]  # Strike Force is the default (2000 points)
        print(f'Creating a list for {battle_sizes[4][0]} ({max_points} pts).')
        break

    game_choice = int(game_input)

    if game_choice in battle_sizes:
        game_name, max_points = battle_sizes[game_choice]
        print(f'Creating a list for {game_name}')
        break
    else:
        print("Invalid selection. Please choose a valid option.")

# Generate the unit list
csm_units, army_points = generate_unit(max_points)

# Print generated units (sorted by type)
print("\nGenerated Army List:")

# Iterate through the unit types and display them in order
unit_types = ['Characters', 'Battle line', 'Other Datasheets', 'Chaos Allies']

for unit_type in unit_types:
    print(f"\n--- {unit_type} ---")
    unit_count = {}
    # Group units by their name and display consecutively
    for unit, cost in csm_units[unit_type]:
        unit_name = unit
        if unit_name not in unit_count:
            unit_count[unit_name] = []
        unit_count[unit_name].append(cost)

    # Now print each unit grouped
    for unit_name, costs in unit_count.items():
        for cost in costs:
            print(f"{unit_name} (Cost: {cost})")

# Print total army points
print(f"\nTotal Army Points: {army_points}")


