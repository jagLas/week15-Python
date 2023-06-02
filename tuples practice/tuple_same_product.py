import math

def tupleSameProduct(nums):
    # creates all unique products and store the pair that makes them
    products = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a = nums[i]
            b = nums[j]
            product = a * b
            try:
                products[product].append((a, b))
            except:
                products[product] = [(a, b)]

    count = 0
    for product in products:
        length = len(products[product])
        if length > 1:
            combinations = math.factorial(length) / math.factorial(length - 2) 
            count += int(combinations)

    return count * 4

print('\ncase1')
case1 = [2,3,4,6]
print(tupleSameProduct(case1))

print('\ncase 2')
case2 = [1,2,4,5,10]
print(tupleSameProduct(case2))

print('\ncase 3')
case3 = [2,3,4,6,8,12]
print(tupleSameProduct(case3))