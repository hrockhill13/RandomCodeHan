# AG_Belakor.py
# Han Rockhill
# python version 3.12.2
# 03/06/2025
# Write a program that creates a random CSM army based on some basic initial criteria
# current criteria :
#                   1 Character or Belakor (to meet warlord criteria)
#                   1 Battle Line (to meet action monkey needs)
#                   # then astartes <= # daemons
#                   TBA : if unit is Unique limit is 1 instead of 3


from random import randint

# Define unit tags
unique = str('unique')
astartes = str('astartes')
daemon = str('daemon')
monster = str('monster')

# Define unit types and their costs
unit_data = {
    'Characters': {
        1: ("Be'Lakor", 375, unique), 2: ('Chaos Lord', 90, astartes), 3: ('CL-Terminator', 95, astartes), 4: ('CL-JumpPack', 90, astartes),
        5: ('Cultist Firebrand', 45, astartes), 6: ('Great Unclean One', 250, [daemon,monster]), 7: ('Dark Apostle', 75, astartes), 8: ('Dark Commune', 80, astartes),
        9: ('Lord of Change', 260, [daemon,monster]), 10: ('Blood Thirster', 305, [daemon,monster]), 11: ('Keeper of Secrets', 290, [daemon,monster]),
        12: ('Change Caster', 60, daemon), 13: ('Blood Master', 65, daemon), 14: ('Skull Master', 100, daemon),
        15: ('Master of Executions', 80, astartes), 16: ('Master of Possession', 70, astartes), 17: ('Sorcerer', 60, astartes),
        18: ('Sorc_Terminator', 80, astartes), 19: ('Traitor Enforcer', 65, astartes), 20: ('Rend Master on BloodThrone', 165, [daemon,monster]),
        21: ('Warpsmith', 70, astartes), 22: ('Fateskimmer', 95, daemon), 23: ('Fluxmaster', 60, daemon), 24: ('Exhalted Flamer', 65, daemon),
        25: ('Infernal Enrapturess', 60, daemon), 26: ('Contorted Epitome', 100, daemon), 27: ('Poxbringer', 55, daemon), 28: ('Tranceweaver', 60, daemon)
    },
    'Battle line': {1: ('Chaos Cultists', 50, astartes), 2: ('Legionaries', 90, astartes), 3: ('Bloodletters', 110, daemon),  4: ('BlueHorrors', 125, daemon),
                    5: ('Daemonettes', 100, daemon), 6: ('Plaguebearers', 110, daemon), 7: ('Nurglings', 35, daemon), 8: ('Pink Horrors', 140, daemon),},
    'Other Datasheets': {
        1: ('Accursed Cultists', 90,  astartes), 2: ('Blood Crushers', 110, [daemon,monster]), 3: ('Flesh Hounds', 75, daemon), 4: ('Skull Cannon', 95, [daemon,monster]),
        5: ('Flamers', 65, daemon), 6: ('Screamers', 80, daemon), 7: ('Chaos Terminator Squad', 180, astartes),
        8: ('Burning Chariot', 115, [daemon,monster]), 9: ('Chosen', 125, astartes), 10: ('SoulGrinder', 190, [daemon,monster]), 11: ('Fellgor Beastmen', 85, astartes), 12: ('Beasts of Nurgle', 65, [daemon,monster]),
        13: ('Havocs', 125, astartes), 14: ('Plague Drones', 110, [daemon,monster]), 15: ('Fiends', 110, [daemon,monster]), 16: ('Seekers of Slaanesh', 80, [daemon,monster]),  17: ('Nemisis Claw', 110, astartes),
        18: ('Possessed', 120, astartes), 19: ('Raptors', 90, astartes), 20: ('Traitor Guardsmen Squad', 70, astartes), 21: ('Warp Talons', 125, astartes)
    },
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

# -------- ++++  UNIT GENERATION FUNCTION  ++++  ------------

def generate_unit(max_points):
    csm_units = {'Characters': [], 'Battle line': [], 'Other Datasheets': []}
    army_points = 0  # Initialize army_points as an integer
    astartes_points = 0  # Track points spent on astartes units
    unit_counts = {'Characters': {}, 'Battle line': {}, 'Other Datasheets': {}}
    battle_line_count = 0  # Track the number of battle line units for transport limit
    unique_units_selected = set()  # Track unique units that have already been selected

    # Helper function to track units and enforce the limit
    def add_unit(name, cost, unit_type, limit, unit_tag):
        nonlocal army_points, astartes_points
        if army_points + cost <= max_points:
            # Ensure 'unique' units can only be added once
            if unit_tag == unique and name in unique_units_selected:
                return False  # Skip adding this unit if it's already selected
            if max_points == 500:
                    if unit_tag == monster or unit_tag == unique:
                        return False # skip adding monsters or unique in boarding action games
            if unit_counts[unit_type].get(name, 0) < limit:
                unit_counts[unit_type][name] = unit_counts[unit_type].get(name, 0) + 1
                army_points += cost
                if unit_tag == astartes:
                    astartes_points += cost  # Track astartes points
                csm_units[unit_type].append((name, cost))  # Add the unit as a tuple (name, cost)
                if unit_tag == unique:
                    unique_units_selected.add(name)  # Mark the unit as selected
                return True
        return False

    # Ensure Be'Lakor is selected first if the game size is not 500, or non-unique if Boarding Action
    if max_points == 500:
        # Add a non-unique character (to meet Warlord requirement)
        char_name, char_cost, char_type = character_non_unique()
        add_unit(char_name, char_cost, 'Characters', 3, char_type)  # Limit for characters is 3
    else:
        # Otherwise, select Be'Lakor
        char_name, char_cost, char_type = ("Be'Lakor", 375, unique)
        add_unit(char_name, char_cost, 'Characters', 3, char_type)  # Limit for characters is 1

    # Track the number of units added for balancing purposes
    while army_points < max_points:
        units_attempted = 0
        unit_added = False
        while units_attempted < 10 and not unit_added:  # Try up to 10 random selections
            # Randomly select a unit type
            newUnit = randint(1, 8)
            units_attempted += 1

            # Try to add a unit and check if it fits within the army point and unit count limits
            if newUnit in range(1, 2):  # Characters
                name, cost, unit_tag = character()
                unit_added = add_unit(name, cost, 'Characters', 3, unit_tag)  # Limit for characters is 3
            elif newUnit in range(3, 5):  # Battle Line
                name, cost, unit_tag = battleLine()
                unit_added = add_unit(name, cost, 'Battle line', 6, unit_tag)  # Limit for battle line units is 6
                battle_line_count += unit_added  # Increment if battle line unit is added
            elif newUnit in range(6, 7):  # Other Datasheets
                name, cost, unit_tag = otherDatasheet()
                unit_added = add_unit(name, cost, 'Other Datasheets', 3, unit_tag)  # Limit for other units is 3

            # After adding a unit, check if it exceeds the astartes points limit (close to 50%)
            if unit_added:
                if astartes_points + cost > max_points * 0.5 and unit_tag == astartes:
                    # Undo the addition if it exceeds the astartes points limit
                    army_points -= cost
                    if unit_tag == astartes:
                        astartes_points -= cost
                    csm_units[unit_type].remove((name, cost))  # Remove the unit from the list
                    unit_added = False  # Revert the unit addition

        # If we couldn't add any units in 10 attempts, break out of the loop
        if not unit_added:
            break

    # If there are still points left, we will now fill in the remaining points with available units
    while army_points < max_points:
        # Try adding a unit that fits the remaining points
        possible_units = []
        for unit_category in unit_data.values():
            for unit in unit_category.values():
                name, cost, unit_tag = unit
                if army_points + cost <= max_points:
                    possible_units.append((name, cost, unit_tag))

        if not possible_units:
            break  # No possible units can be added without exceeding points

        # Randomly select a unit from possible options
        name, cost, unit_tag = possible_units[randint(0, len(possible_units) - 1)]
        add_unit(name, cost, 'Other Datasheets', 3, unit_tag)

    return csm_units, army_points




# Character generation (with cost)
def character():
    char_select = randint(1, 28)
    name, cost, type = unit_data['Characters'][char_select]
    return name, cost, type

# Character generation for non-unique characters
def character_non_unique():
    char_select = randint(2, 28)  # Avoid Be'Lakor (id 1)
    name, cost, type = unit_data['Characters'][char_select]
    return name, cost, type

# Battle Line generation
def battleLine():
    bl_select = randint(1, 8)
    bl_name, bl_cost, type = unit_data['Battle line'][bl_select]
    return bl_name, bl_cost, type

# Other Datasheet generation
def otherDatasheet():
    od_select = randint(1, 21)
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
unit_types = ['Characters', 'Battle line', 'Other Datasheets',]

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

# Track the points for Astartes and Daemon units
astartes_points = 0
daemon_points = 0

# Iterate through the units to calculate points
for unit_type in unit_types:
    for unit, cost in csm_units[unit_type]:
        # Check if the unit is Astartes
        if astartes in unit:
            astartes_points += cost
        # Check if the unit is Daemon
        if daemon in unit:
            daemon_points += cost

# Print total army points
print(f"\nTotal Army Points: {army_points}")

# Print total Astartes points
print(f"\nTotal Astartes Points: {astartes_points}")

# Print total Daemon points
print(f"Total Daemon Points: {daemon_points}")
