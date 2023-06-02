def tupleSameProduct(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            print(i, j)
    pass


case1 = [2,3,4,6]
print(tupleSameProduct(case1))

# case2 = [1,2,4,5,10]
# print(tupleSameProduct(case2))