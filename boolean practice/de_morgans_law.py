def de_morgans_law(a, b):
    return (not a) or (not b)

def de_morgans_law_alt(a, b):
    return not (a and b)


print(de_morgans_law(True, True)) # False
print(de_morgans_law(True, False)) # True
print(de_morgans_law(False, False)) # True
print(de_morgans_law("", [])) # True
print(de_morgans_law(2, 2)) # False
print(de_morgans_law(2, 0)) # True