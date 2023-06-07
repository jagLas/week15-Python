# Write your function, here.
def vowels(string):
    return [char for char in string if char in 'aeiouAEIOU']



print(vowels("An amazing person")) #> ['A', 'a', 'a', 'i', 'e', 'o']
print(vowels("Coding is cool")) #> ['o', 'i', 'i', 'o', 'o']
print(vowels("People are NICE")) #> ['e', 'o', 'e', 'a', 'e', 'I', 'E']