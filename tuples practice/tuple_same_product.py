def tupleSameProduct(nums):
    # creates all unique pairs numbers and stores their products
    products = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pair = nums[i] , nums[j]
            products[pair] = nums[i]*nums[j]
    print(products)

    # find pairs whose products match
    count = 0
    for pair in products:
        for pair2 in products:
            if pair == pair2:
                continue
            if pair[0] in pair2:
                continue
            if pair[1] in pair2:
                continue
            if pair[0] * pair[1] == pair2[0] * pair2[1]:
                count += 1


    # adjust count based on rearranging pairs (*4 maybe?)

    return count * 4

print('\ncase1')
case1 = [2,3,4,6]
print(tupleSameProduct(case1))

print('\ncase 2')
case2 = [1,2,4,5,10]
print(tupleSameProduct(case2))