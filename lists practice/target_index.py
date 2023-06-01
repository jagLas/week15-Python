def targetIndices(nums, target):
    nums.sort()
    indices = []
    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)
    return indices

nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums, target))

nums = [1,2,5,2,3]
target = 3
print(targetIndices(nums, target))