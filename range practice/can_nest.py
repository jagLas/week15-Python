# Your code, here.
def can_nest(lst1, lst2):
    if min(lst1) <= min(lst2): return False
    if max(lst1) >= max(lst2): return False
    return True



print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
print(can_nest([3, 1], [4, 0]))        #> True
print(can_nest([9, 9, 8], [8, 9]))     #> False
print(can_nest([1, 2, 3, 4], [2, 3]))  #> False