# Write your function, here.
def third(lst):
    return [num**3 for num in lst]


print(third([2, 4, 8])) #> [8, 64, 512]
print(third([3, 5, 6])) #> [27, 125, 216]
print(third([1, 3, 7])) #> [1, 27, 343]