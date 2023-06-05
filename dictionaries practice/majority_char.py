# Write your code here.
def majority_char(string):
    threshold = len(string)/2
    charCount = {}
    for char in string:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    for char, count in charCount.items():
        if count > threshold:
            return char
    
    return None

str = 'all'
str2 = 'welcome to the jungle'

print(majority_char(str))           # 'l'
print(majority_char(str2))          # None