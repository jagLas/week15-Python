def compare (str1, str2):
    return len(str1) == len(str2)

print(compare("AB", "CD"))              #> True
print(compare("ABC", "DE"))             #> False
print(compare("hello", "App Academy"))  #> False