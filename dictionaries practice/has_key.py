# Write your function, here.
def has_key(dictionary, value):
    if value in dictionary:
        return True
    return False



print(has_key({ "a": 44, "b": 45, "c": 46 }, "d"))
# False

print(has_key({ "craves": True, "midnight": True, "snack": True }, "morning"))
# False

print(has_key({ "pot": 1, "tot": 2, "not": 3 }, "not"))
# True