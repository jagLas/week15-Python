# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
            
#     return None

def twoSum(nums, target):
    differences = set(nums)
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in differences:
            j = nums.index(difference)
            if i != j:
                return [i, j]
            
    return None

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

nums = [3,2,4]
target = 6
print(twoSum(nums, target))

nums = [2,4,11,3]
target = 6
print(twoSum(nums, target))