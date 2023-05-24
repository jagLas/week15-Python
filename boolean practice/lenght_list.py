def length_list(array, length):
    return len(array) == length

print(length_list([], 1))   #>  False
print(length_list([], 0))   #>  True
print(length_list([5, 2], 2))   #>  True
print(length_list([1, 4, 3], 4))   #>  False
print(length_list([0, 2, "i", 0.9], 4))   #>  True