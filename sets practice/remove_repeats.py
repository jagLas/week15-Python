# Write your code here.
def remove_repeats(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    left_diff = str1 - str2
    right_diff = str2 - str1
    return left_diff | right_diff


str1 = 'aloha'
str2 = 'bonjour'

print(remove_repeats(str1, str2))    # {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}