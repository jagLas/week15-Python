# Write your function, here.
def first_last(lst):
    return [lst[0], lst[-1]]


print(first_last([5, 10, 15, 20, 25]))            #> [5, 25]
print(first_last([13, None, False, True]))        #> [13, True]
print(first_last([None, 4, "6", "hello", None]))  #> [None, None]