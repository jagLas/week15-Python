# Write your function, here.
def is_valid_hex_code(str):
    if str[0] != '#':
        return False
    
    if len(str) != 7:
        return False
    
    validChars = ['a','b','c','d','e','f']
    
    for char in str[1:]:
        if char.lower() not in validChars and not char.isdigit():
            return False

    return True




print(is_valid_hex_code("#CD5C5C")) #> True
print(is_valid_hex_code("#EAECEE")) #> True
print(is_valid_hex_code("#eaecee")) #> True

print(is_valid_hex_code("#CD5C58C"))
# Prints False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# Prints False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# Prints false
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #