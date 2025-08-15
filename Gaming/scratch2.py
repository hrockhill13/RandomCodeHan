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
        5: ('Cultist Firebrand', 45, astartes), 6: ('Great Unclean One', 250, [daemon, monster]), 7: ('Dark Apostle', 75, astartes),
        8: ('Dark Commune', 80, astartes), 9: ('Lord of Change', 260, [daemon, monster]), 10: ('Blood Thirster', 305, [daemon, monster]),
        11: ('Keeper of Secrets', 290, [daemon, monster]), 12: ('Change Caster', 60, daemon), 13: ('Blood Master', 65, daemon),
        14: ('Skull Master', 100, daemon), 15: ('Master of Executions', 80, astartes), 16: ('Master of Possession', 70, astartes),
        17: ('Sorcerer', 60, astartes), 18: ('Sorc_Terminator', 80, astartes), 19: ('Traitor Enforcer', 65, astartes),
        20: ('Rend Master on BloodThrone', 165, [daemon, monster]), 21: ('Warpsmith', 70, astartes), 22: ('Fateskimmer', 95, daemon),
        23: ('Fluxmaster', 60, daemon), 24: ('Exhalted Flamer', 65, daemon), 25: ('Infernal Enrapturess', 60, daemon),
        26: ('Contorted Epitome', 100, daemon), 27: ('Poxbringer', 55, daemon), 28: ('Tranceweaver', 60, daemon)
    },
    'Battle line': {1: ('Chaos Cultists', 50, astartes), 2: ('Legionaries', 90, astartes), 3: ('Bloodletters', 110, daemon),
                    4: ('BlueHorrors', 125, daemon), 5: ('Daemonettes', 100, daemon), 6: ('Plaguebearers', 110, daemon),
                    7: ('Nurglings', 35, daemon), 8: ('Pink Horrors', 140, daemon)},
    'Other Datasheets': {
        1: ('Accursed Cultists', 90, astartes), 2: ('Blood Crushers', 110, [daemon, monster]), 3: ('Flesh Hounds', 75, daemon),
        4: ('Skull Cannon', 95, [daemon, monster]), 5: ('Flamers', 65, daemon), 6: ('Screamers', 80, daemon), 7: ('Chaos Terminator Squad', 180, astartes),
        8: ('Burning Chariot', 115, [daemon, monster]), 9: ('Chosen', 125, astartes), 10: ('SoulGrinder', 190, [daemon, monster]),
        11: ('Fellgor Beastmen', 85, astartes), 12: ('Beasts of Nurgle', 65, [daemon, monster]), 13: ('Havocs', 125, astartes),
        14: ('Plague Drones', 110, [daemon, monster]), 15: ('Fiends', 110, [daemon, monster]), 16: ('Seekers of Slaanesh', 80, [daemon, monster]),
        17: ('Nemisis Claw', 110, astartes), 18: ('Possessed', 120, astartes), 19: ('Raptors', 90, astartes), 20: ('Traitor Guardsmen Squad', 70, astartes),
        21: ('Warp Talons', 125, astartes)
    },
}

# Define the battle sizes
battle_sizes = {
    1: ('Combat Patrol', 500),
    2: ('Skirmish', 1000),
    3: ('Crusade 1.5', 1500),
    4: ('Incursion', 2000),
    5: ('Crusade 2.5', 2500),
    6: ('Onslaught', 3000)
}

# -------- ++++ UNIT GENERATION FUNCTION ++++ ------------

def generate_unit(max_points):
    csm_units = {'Characters': [], 'Battle line': [], 'Other Datasheets': []}
    army_points = 0  # Initialize army_points as an integer
    astartes_points = 0  # Track points spent on astartes units
    daemon_points = 0  # Track points spent on daemon units
    unit_counts = {'Characters': {}, 'Battle line': {}, 'Other Datasheets': {}}
    unique_units_selected = set()  # Track unique units that have already been selected

    # Helper function to add units to the list
    def add_unit(name, cost, unit_type, unit_tags):
        nonlocal army_points, astartes_points, daemon_points
        if army_points + cost <= max_points:
            if unique in unit_tags and name in unique_units_selected:
                return False
            if unit_counts[unit_type].get(name, 0) < 3:
                unit_counts[unit_type][name] = unit_counts[unit_type].get(name, 0) + 1
                army_points += cost
                if astartes in unit_tags:
                    astartes_points += cost
                if daemon in unit_tags:
                    daemon_points += cost
                csm_units[unit_type].append((name, cost))
                if unique in unit_tags:
                    unique_units_selected.add(name)
                return True
        return False

    # First, select Astartes units until we reach half of max_points
    half_max_points = max_points / 2
    astartes_points = 0

    while astartes_points < half_max_points:
        unit = randint(1, 8)
        if unit <= 3:  # Characters
            name, cost, tags = list(unit_data['Characters'].values())[randint(0, 27)]
            if add_unit(name, cost, 'Characters', tags):
                print(f"Added Astartes character: {name} (Cost: {cost})")
        elif 4 <= unit <= 7:  # Battle Line
            name, cost, tags = list(unit_data['Battle line'].values())[randint(0, 7)]
            if add_unit(name, cost, 'Battle line', tags):
                print(f"Added Astartes battle line: {name} (Cost: {cost})")

    # Then, select Be'Lakor and Daemon units
    name, cost, tags = unit_data['Characters'][1]  # Be'Lakor is at index 1
    add_unit(name, cost, 'Characters', tags)  # Add Be'Lakor
    print(f"Added Be'Lakor: {name} (Cost: {cost})")

    while army_points < max_points:
        unit = randint(1, 8)
        if unit <= 3:  # Characters
            name, cost, tags = list(unit_data['Characters'].values())[randint(0, 27)]
            if add_unit(name, cost, 'Characters', tags):
                print(f"Added Daemon character: {name} (Cost: {cost})")
        elif 4 <= unit <= 7:  # Battle Line
            name, cost, tags = list(unit_data['Battle line'].values())[randint(0, 7)]
            if add_unit(name, cost, 'Battle line', tags):
                print(f"Added Daemon battle line: {name} (Cost: {cost})")

    # Return the units generated and the points spent
    return csm_units, army_points, astartes_points, daemon_points

# -------- ++++ GAME INTERFACE ++++ ------------

# Get user input to play the game
print('')
print('+++ CSM ARMY LIST GENERATOR +++')

# Get the game size input from the user
game_input = input("How big is this game? \n 1) Combat Patrol - 500.pts \n 2) Skirmish - 1000.pts \n 3) Crusade - 1500.pts \n 4) Incursion - 2000.pts \n 5) Crusade - 2500.pts \n 6) Onslaught - 3000.pts \n -> ")
game_choice = int(game_input) if game_input.isdigit() else 4  # Default to 'Incursion' if input is invalid
max_points = battle_sizes[game_choice][1]

# Generate the unit list
csm_units, army_points, astartes_points, daemon_points = generate_unit(max_points)

# Output results
print("\nGenerated Army List:")
for unit_type, units in csm_units.items():
    print(f"\n--- {unit_type} ---")
    for unit, cost in units:
        print(f"{unit} (Cost: {cost})")

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



print(f"\nTotal Army Points: {army_points}")
print(f"Total Astartes Points: {astartes_points}")
print(f"Total Daemon Points: {daemon_points}")
print(f"Valid: {army_points <= max_points}")
