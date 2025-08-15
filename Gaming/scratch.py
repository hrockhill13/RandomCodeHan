from random import randint

def generate_stat():
    return sum(sorted(randint(1, 6) for _ in range(4))[1:])

def generate_class():
    classes = ['Fighter', 'Rogue', 'Mage', 'Cleric']
    return [classes[randint(0, 3)]]

while True:
    npc_class = generate_class()
    stats = {
        'STR': generate_stat(),
        'INT': generate_stat(),
        'WIS': generate_stat(),
        'DEX': generate_stat(),
        'CON': generate_stat(),
        'CHA': generate_stat(),
    }

    print("    %s" % npc_class)
    print(">>> Character Stats <<<")
    for stat, value in stats.items():
        print(f"     {stat}: {value}")

    hp_base_mapping = {'Fighter': 10, 'Cleric': 8, 'Rogue': 6, 'Mage': 4}
    stat_mod_mapping = {(1, 7): -2, (8, 9): -1, (10, 11): 0, (12, 13): 1, (14, 15): 2, (16, 17): 3, (18, 18): 4}

    hp_base = hp_base_mapping[npc_class[0]]
    stat_mod = next(value for key, value in stat_mod_mapping.items() if key[0] <= stats['CON'] <= key[1])

    sum_hp = hp_base + stat_mod
    print("\n  Hit Points: %.0f" % sum_hp)

    save_roll = input("\nPress 'y' to accept, else re-roll: \n")
    if save_roll == 'y':
        break
