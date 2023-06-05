# Write your code here.
def add_to_set(st, lst):
    for i in lst:
        st.add(i)
    return st

st = { 1, 2, 3, 4 }
lst = [12, 4, 42, 93, 2, 85]

print(add_to_set(st, lst))    # { 1, 2, 3, 4, 42, 12, 85, 93 }