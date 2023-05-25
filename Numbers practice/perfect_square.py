# Write your function, here.
def perfect_square(a,b):
    if b**2 == a:
        return True
    return False


print(perfect_square(15, 5)) #> False
print(perfect_square(25, 5)) #> True
print(perfect_square(81, 9)) #> True
print(perfect_square(9, 2))  #> False