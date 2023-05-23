def concat_name (first_name, last_name):
    return last_name + ', ' + first_name


print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("Mary", "Jane"))   #> "Jane, Mary"