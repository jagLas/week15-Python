# STEP 1: Complete analyze function to return 5 values
#    - minimum
#    - maximum
#    - mean (a.k.a. average)
#    - median (center point)
#    - mode (most repeated)

import math

def analyze(nums):
    return (min(nums), max(nums), round(sum(nums)/len(nums),2), median(nums=nums), mode(nums))

# STEP 2: Complete median function to return center number
#         WITHOUT using built-in function
def median(nums):
    nums = list(nums)
    nums.sort()
    center = int(len(nums)/2)

    if len(nums) % 2 == 1:
        return nums[center]
    
    mid1 = nums[center - 1]
    mid2 = nums[center]

    return (mid1+mid2)/2

# STEP 3: Complete mode function to return most-repeated number
#         WITHOUT using built-in function
# BONUS B: Catch special case where more than one value repeats the most
def mode(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    mostUsed = float('-inf')
    for num in frequency:
        if frequency[num] > mostUsed:
            mostUsed = frequency[num]

    mode = [num for num in frequency if frequency[num] == mostUsed ]
    if len(mode) == 1: return mode[0]
    return tuple(mode)

# DO NOT EDIT - sample data for checking your work
sample1 = 1,2,3,4,5,6,7,8,9
sample2 = [37,45,23,65,75,34,23,23,23,65,12,99]
print(('min', 'max', 'mean', 'median', 'mode'))
print(analyze(sample1))
print(analyze(sample2))

# BONUS A: Print more samples as you see fit
