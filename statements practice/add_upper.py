# Write your solution here.
def add_upper(string):
    uppers = ''

    for char in string:
        if char.isupper():
            uppers += char

    return uppers


print(add_upper("ApPlE"))        #> APE
print(add_upper("Coding"))       #> C
print(add_upper("PIano"))        #> PI
print(add_upper("SUPREME"))      #> SUPREME