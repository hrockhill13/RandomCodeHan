# p37.py
# Han Rockhill
# Python 3.12.2
# 03/09/2024 - 03/15/2024
#
# Centered Averages
# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
# ignore just one copy, and likewise for the largest value. Use int division to produce the final average.
# You may assume that the array is length 3 or more.
def centered_average(nums):
    listLen = len(nums)     # define list length variable
    for n in range(listLen - 1):    # put the list in order from smallest to largest
        for i in range(listLen - n - 1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]          # create the placeholder
                nums[i] = nums[i + 1]
                nums[i + 1] = temp      # use the placeholder
        suM = 0                     # set sum to 0
        for i in range(1, len(nums)-1, 1):
            suM += nums[i]                  # add to the sum
    averageIndex= int(suM/(len(nums)-2))        # find the average as an int
    return averageIndex                     # return average
# proofs
print(centered_average([1, 2, 3, 4, 100])) # → 3
print(centered_average([1, 1, 5, 5, 10, 8, 7])) # → 5
print(centered_average([-10, -4, -2, -4, -2, 0])) #  → -3



#SUM 13
# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
    listLen = len(nums)
    sumAll = 0  # total of count
    alsoBad = 0 # total of dont count
    for i in range(listLen):
        if nums[i] != 13:
            sumAll += nums[i]   # add to sum list
        else:
            if i < listLen - 1:  # Check if there's a number after 13
                alsoBad += nums[i+1]   # add to also bad list
    if not nums or sumAll == 0:  # if nothing in nums or all elements are 13, return 0
        return 0
    return sumAll - alsoBad # return sum of everythign not 13

# Proof
print(sum13([]))            # → 0
print(sum13([1, 2, 2, 1]))  # → 6
print(sum13([1, 1]))        # → 2
print(sum13([1, 2, 2, 1, 13]))


# Big Diff
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
    listLen = len(nums)            # define list length
    for n in range(listLen -1):         # put the list in order from smallest to largest
        for i in range(listLen -n -1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]          # create placeholder
                nums[i] = nums[i + 1]
                nums[i + 1] = temp     # use placeholder
    small = nums[0]   # first number in list is the smallest
    large = nums[-1]  # last number in list is the largest (counting backwards)
    diffSvL = large - small         # get the big diff
    return diffSvL              # return diff

# proofs
print(big_diff([10, 3, 5, 6]))  # → 7
print(big_diff([7, 2, 10, 9]))  # → 8
print(big_diff([2, 10, 7, 2]))  # → 8
print(big_diff([7, 6, 8, 5]))  # → 3