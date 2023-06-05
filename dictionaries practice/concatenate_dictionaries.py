# Write your code here.
def concatenate_dictionaries(lst):
    newDict = {}
    for d in lst:
        for a, b in d.items():
            newDict[a] = b

    return newDict

"""
# Using **
def concatenate_dictionaries(lst):
    new_dict = {}
    for dict in lst:
        new_dict = { **new_dict, **dict }
    return new_dict

# Using .update
def concatenate_dictionaries2(lst):
    new_dict = {}
    for dict in lst:
        new_dict.update(dict)
    return new_dict

# Very manual solution
def concatenate_dictionaries3(lst):
    new_dict = {}
    for dict in lst:
        for key in dict.keys():
            new_dict[key] = dict[key]
    return new_dict

"""

lst = [
    {
        'a': 'this',
        'b': 'is'
    },
    {
        'c': 'the',
        'd': 'merged'
    },
    {
        'd': 'dictionary'
    }
]

print(concatenate_dictionaries(lst))
"""
Prints: 
{
    a: 'this',
    b: 'is',
    c: 'the',
    d: 'dictionary'
}
"""