def is_palindrome(str):
    reversed_str = [*str]
    reversed_str.reverse()
    return ''.join(reversed_str) == str

# # provided solution
# def is_palindrome(str):
#   reverse = ''.join(reversed(str))

#   return str == reverse

# is_palindrome('abc')
print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False