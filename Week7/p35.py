# p35.py (codingBat2.py)
# Han Rockhill
# Python 3.12.2
# 03/09/2024 - 03/15/2024

# squirrel party
def cigar_party(cigars, is_weekend):
    if 40 <= cigars <= 60 and not is_weekend:
        print('Inclusive squirrel party?')
        return True
    elif is_weekend and 40 <= cigars > 60:
        print('Weekend squirrel party?')
        return True
    else:
        print('Squirrel party?')
        return False
# proofs
print(cigar_party(30, False))  # I expect False
print(cigar_party(50, False))  # I expect True
print(cigar_party(70, True))   # I expect True


# counting evens
def count_evens(ranList):
    isEven = 0  # start at zero
    for num in ranList: # look at each value in the list
        if num % 2 == 0: # if even divisible
            isEven += 1  # add one to the count
    return isEven # return the count
# proofs
count_evens([2, 1, 2, 3, 4]) # → 3
count_evens([2, 2, 0]) #→ 3
count_evens([1, 3, 5]) #→ 0

# 2 consecutive 2s (has22)
def has22(list22):
    for num2 in range(len(list22) -1): # check the numbers for length of the list, but ignore the last one
        if list22[num2] == 2 and list22[num2+1] == 2: # check each number 2 against the next number and see if it's also 2
            return True # if tw0 consecutive numbers are 2 return true
    return False  # if no 2 are together return false
# proofs
has22([1, 2, 2]) #  → True
has22([1, 2, 1, 2]) #  → False
has22([2, 1, 2]) #  → False