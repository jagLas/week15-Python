def is_last_character_n(str):
    return str.lower().endswith('n')


print(is_last_character_n("Aiden"))  #> True
print(is_last_character_n("Piet"))   #> False
print(is_last_character_n("Bert"))   #> False
print(is_last_character_n("Dean"))   #> True