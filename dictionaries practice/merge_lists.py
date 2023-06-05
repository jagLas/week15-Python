# Write your code here.
def merge_lists(lst1, lst2):
    return dict(zip(lst1, lst2))

lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
print(merged_dict)      # { 'a': 1, 'b': 2 }