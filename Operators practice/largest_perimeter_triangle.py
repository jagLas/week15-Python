def largestPerimeter(nums):
    nums = sorted(nums, reverse=True)

    while len(nums) >= 3:
        s1 = nums[0]
        s2 = nums[1]
        s3 = nums[2]

        if s3 + s2 > s1:
            return s1 + s2 + s3
        
        nums.pop(0)
    
    return 0




# nums = [2,1,2]
# print(largestPerimeter(nums))

# nums = [1,2,1,10]
# print(largestPerimeter(nums))

nums = [3,6,2,3]
print(largestPerimeter(nums))