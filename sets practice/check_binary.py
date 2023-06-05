# Write your code here.
def check_binary(str):
    st = set(str)
    if len(st) == 1:
        return '0' in st or '1' in st
    if len(st) == 2:
        return '0' in st and '1' in st
    return False

str1 = '1010001010010100101'
str2 = '1010010015010101010'

print(check_binary(str1))       # True
print(check_binary(str2))       # False