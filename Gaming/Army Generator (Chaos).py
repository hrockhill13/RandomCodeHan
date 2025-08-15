# AG_csm.py
# Han Rockhill
# python version 3.12.2
# 03/06/2025
# Write a program that creates a random CSM army based on some basic initial criteria
# current criteria :
#                   1 Character (to meet warlord criteria)
#                   1 Battle Line (to meet action monkey needs)
#                   # Dedicated Transports <= # Battle Line
#                   TBA : if unit is Unique limit is 1 instead of 3

from random import randint


damned = str('d')
unique = str('unique')
astartes = str('a')
vehicle = str('vehicle')
spawn = str('spawn')
monster = str('monster')

# Define unit types and their costs
unit_data = {
    'Characters': {
        1: ('Abaddon', 280, unique), 2: ('Chaos Lord', 90, astartes), 3: ('CL-Terminator', 95, astartes), 4: ('CL-JumpPack', 90, astartes),
        5: ('Cultist Firebrand', 45, damned), 6: ('Cypher', 90, unique), 7: ('Dark Apostle', 75, astartes), 8: ('Dark Commune', 80, damned),
        9: ('Fabius Bile', 85, unique), 10: ('Haarken Worldclaimer', 90, unique), 11: ('Demon Prince', 165, monster),
        12: ('Demon Prince w/Wings', 180, monster), 13: ('Huron Blackheart', 80, unique), 14: ('Lord Discordant', 160, vehicle),
        15: ('Master of Executions', 80, astartes), 16: ('Master of Possession', 70, astartes), 17: ('Sorcerer', 60, astartes),
        18: ('Sorc_Terminator', 80, astartes), 19: ('Traitor Enforcer', 65, damned), 20: ('Vashtorr', 175, unique), 21: ('Warpsmith', 70, astartes)
    },
    'Battle line': {1: ('Chaos Cultists', 50, damned), 2: ('Legionaries', 90, astartes)},
    'Dedicated Transport': {1: ('Rhino', 75, vehicle)},
    'Other Datasheets': {
        1: ('Accursed Cultists', 90,  damned), 2: ('Chaos Bikers', 70, vehicle), 3: ('Chaos Land Raider', 240, vehicle),
        4: ('Chaos Predator Annihilator', 135, vehicle),
        5: ('Chaos Predator Destructor', 140, vehicle), 6: ('Chaos Spawn', 70, spawn), 7: ('Chaos Terminator Squad', 180, astartes),
        8: ('Chaos Vindicator', 185, vehicle),
        9: ('Chosen', 125, astartes), 10: ('Defiler', 190, vehicle), 11: ('Fellgor Beastmen', 85, damned), 12: ('Forgefiend', 180, vehicle),
        13: ('Havocs', 125, astartes), 14: ('Helbrute', 130, vehicle),
        15: ('Heldrake', 205, vehicle), 16: ('Khorne Lord of Skulls', 450, vehicle), 17: ('Maulerfiend', 130, vehicle), 18: ('Nemisis Claw', 110, astartes),
        19: ('Obliterators', 160, monster),
        20: ('Possessed', 120, astartes), 21: ('Raptors', 90, astartes), 22: ('Traitor Guardsmen Squad', 70, damned), 23: ('Venomcrawler', 120, vehicle),
        24: ('Warp Talons', 125, astartes)
    },
}

# Define the battle sizes
battle_sizes = {
    1: ('Boarding Action', 500),
    2: ('Incursion', 1000),
    3: ('Crusade 1.5', 1500),
    4: ('Strike Force', 2000),
    5: ('Crusade 2.5', 2500),
    6: ('Onslaught', 3000)
}

# -------- ++++  UNIT GENERATION FUNCTION  ++++  ------------

def generate_unit(max_points):
    csm_units = {'Characters': [], 'Battle line': [], 'Dedicated Transport': [], 'Other Datasheets': []}
    army_points = 0  # Initialize army_points as an integer
    unit_counts = {'Characters': {}, 'Battle line': {}, 'Dedicated Transport': {}, 'Other Datasheets': {}}
    battle_line_count = 0  # Track the number of battle line units for transport limit
    unique_units_selected = set()  # Track unique units that have already been selected
    # boarding_action_units = set()  # Track vehicle units to omit them in boarding action

    # Helper function to track units and enforce the limit
    def add_unit(name, cost, unit_type, limit, unit_tag):
        nonlocal army_points
        if army_points + cost <= max_points:
            # Ensure 'unique' units can only be added once
            if unit_tag == unique and name in unique_units_selected:
                return False  # Skip adding this unit if it's already selected
            if max_points ==500:
                    if unit_tag == vehicle or unit_tag == monster:
                        return False # skip adding vehicles in boarding action games
            if unit_counts[unit_type].get(name, 0) < limit:
                unit_counts[unit_type][name] = unit_counts[unit_type].get(name, 0) + 1
                army_points += cost
                csm_units[unit_type].append((name, cost))  # Add the unit as a tuple (name, cost)
                if unit_tag == unique:
                    unique_units_selected.add(name)  # Mark the unit as selected
                return True
        return False

    # Always add a character unit first
    char_name, char_cost, char_type = character()
    add_unit(char_name, char_cost, 'Characters', 3, char_type)  # Limit for characters is 3

    # add a battle line unit next
    # bl_name, bl_cost, bl_type = battleLine()
    # add_unit(bl_name, bl_cost, 'Battle line', 6, bl_type)  # Limit for battle line units is 6
    # battle_line_count += 1  # Increment battle line count

    # Now, fill the rest of the units randomly, checking if the army_points are within the allowed limit
    while army_points < max_points:
        units_attempted = 0
        unit_added = False
        while units_attempted < 10 and not unit_added:  # Try up to 10 random selections
            # Randomly select a unit type
            newUnit = randint(1, 8)
            units_attempted += 1

            # Try to add a unit and check if it fits within the army point and unit count limits
            if newUnit in range(1,2):
                name, cost, type = character()
                unit_added = add_unit(name, cost, 'Characters', 3, type)  # Limit for characters is 3
            elif newUnit in range(3,4):
                name, cost, type = battleLine()
                unit_added = add_unit(name, cost, 'Battle line', 6, type)  # Limit for battle line units is 6
                battle_line_count += unit_added  # Increment if battle line unit is added
            elif newUnit == 5:
                name, cost, type = dedicatedTransport()
                # Limit dedicated transports based on battle line units
                unit_added = add_unit(name, cost, 'Dedicated Transport', (battle_line_count/1.5), type)  # Limit based on battle line count
            elif newUnit in range(6,7):
                name, cost, type = otherDatasheet()
                unit_added = add_unit(name, cost, 'Other Datasheets', 3, type)  # Limit for other units is 3

        # If we couldn't add any units in 10 attempts, break out of the loop
        if not unit_added:
            break

    return csm_units, army_points

# Character generation (with cost)
def character():
    char_select = randint(1, 21)
    name, cost, type = unit_data['Characters'][char_select]
    return name, cost, type

# Battle Line generation
def battleLine():
    bl_select = randint(1, 2)
    bl_name, bl_cost, type = unit_data['Battle line'][bl_select]
    return bl_name, bl_cost, type

# Dedicated Transport generation
def dedicatedTransport():
    dt_select = 1
    dt_name, dt_cost, type = unit_data['Dedicated Transport'][dt_select]
    return dt_name, dt_cost, type

# Other Datasheet generation
def otherDatasheet():
    od_select = randint(1, 24)
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
    game_input = input("How big is this game? \n 1) Boarding Action - 500.pts \n 2) Skirmish - 1000.pts \n 3) Crusade - 1500.pts \n 4) Incursion - 2000.pts  ** DEFAULT ** \n 5) Crusade - 2500.pts \n 6) Onslaught - 3000.pts \n -> ")

    # If the input is empty or not a valid integer, default to "Incursion"
    if game_input.strip() == "" or not game_input.isdigit():
        game_name, max_points = battle_sizes[4]  # Incursion is the default (2000 points)
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
unit_types = ['Characters', 'Battle line', 'Dedicated Transport', 'Other Datasheets']

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



