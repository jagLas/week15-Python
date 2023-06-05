# def numJewelsInStones(jewels: str, stones: str):
#     count = 0
#     for stone in stones:
#         if stone in jewels:
#             count += 1
    
#     return count

def numJewelsInStones(jewels: str, stones: str):
    jewelsSet = set(jewels)
    
    count = 0
    for stone in stones:
        if stone in jewelsSet:
            count += 1
    
    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels=jewels, stones=stones))

jewels = "z"
stones = "ZZ"
print(numJewelsInStones(jewels=jewels, stones=stones))