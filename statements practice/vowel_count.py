# Write your solution here.
def vowel_count(string):
    string = string.lower()
    vowels = 'aeiou'
    count = 0
    for vowel in vowels:
        count += string.count(vowel)

    return count


print(vowel_count("App Academy"))         #> 4
print(vowel_count("Coding Expert"))       #> 4
print(vowel_count("Supreme"))             #> 3
print(vowel_count("Chamber of Secrets"))  #> 5