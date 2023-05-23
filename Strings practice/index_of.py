# #using index function
# def index_of(str, char):
#     return str.lower().index(char)


#without using the index function.
def index_of (str, char):
    for i in range(len(str)):
        if str[i].lower() == char.lower():
            return i

print(index_of("Arm", "a"))  #> 0
print(index_of("Pie", "e"))  #> 2
print(index_of("Lucid", "i"))  #> 3
print(index_of("Obvious","u"))  #> 5