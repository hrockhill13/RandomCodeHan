from random import randint

while True:
    def generate_stat():
        new_roll = [randint(1, 6) for _ in range(4)]
        return sum(new_roll) - min(new_roll)


    def generate_class():
        npc_class = []  # setting to empty list
        newClass = randint(1,4)
        while True:
            if newClass == 1:  # if it finds the item as an element
                npc_class.append('Fighter')  # add to the list
            if newClass == 2:
                npc_class.append('Rogue')
            if newClass == 3:
                npc_class.append('Mage')
            if newClass == 4:
                npc_class.append('Cleric')
            break
        return npc_class

    # Character Stats
    npc_class = generate_class()
    str_score = generate_stat()
    int_score = generate_stat()
    wis_score = generate_stat()
    dex_score = generate_stat()
    con_score = generate_stat()
    cha_score = generate_stat()

    # Show the results to the user
    print("    %s" % npc_class)
    print(">>> Character Stats <<<")
    print("     STR: ", str_score)
    print("     INT: ", int_score)
    print("     WIS: ", wis_score)
    print("     DEX: ", dex_score)
    print("     CON: ", con_score)
    print("     CHA: ", cha_score)

    hp_base = 0
    if npc_class == ['Fighter']:
        hp_base = 10
    if npc_class == ['Cleric']:
        hp_base = 8
    if npc_class == ['Rogue']:
        hp_base = 6
    if npc_class == ['Mage']:
        hp_base = 4
    print('')
    '''
        sumHP = 0
        if con_score < 8:
            sumHP = (hp_base -2)
        elif 8 < con_score < 10:
            sumHP = (hp_base -1)
        elif 10 < con_score < 12:
            sumHP = hp_base
        elif 11 < con_score < 14:
            sumHP = hp_base +1
        elif 13 < con_score < 16:
            sumHP = hp_base +2
        elif 15 < con_score < 18:
            sumHP = hp_base +3
        elif con_score == 18:
            sumHP = hp_base +4
    '''
    statMod = 0
    if generate_stat() < 8:
        statMod = -2
    elif 8 < generate_stat() < 10:
        statMod = -1
    elif 10 < generate_stat() < 12:
        statMod = 0
    elif 11 < generate_stat() < 14:
        statMod = 1
    elif 13 < generate_stat() < 16:
        statMod = 2
    elif 15 < generate_stat() < 18:
        statMod = 3
    elif generate_stat() == 18:
        statMod = 4

    print("  Hit Points: %.0f" % (hp_base+statMod))
    # Check if the user wants new stats

    save_roll = input("\nPress 'y' to accept, else re-roll: \n")
    if save_roll == 'y':
        break
