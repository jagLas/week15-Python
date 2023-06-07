# Write your function, here.
def dictionary_pairs(lst1, lst2):
    return {key: value for key, value in zip(lst1, lst2)}


print(dictionary_pairs(["name", "age", "food"], ["James", 24, "steak"])) #> {'Name': 'James', 'Age': 24, 'Food': 'steak'}
print(dictionary_pairs(["name", "age", "food"], ["Vivian", 21, "sushi"])) #> {'Name': 'Vivian', 'Age': 21, 'Food': 'sushi'}
print(dictionary_pairs(["name", "age", "food"], ["Alex", 6, "chocolate"])) #> {'Name': 'Alex', 'Age': 6, 'Food': 'chocolate'}