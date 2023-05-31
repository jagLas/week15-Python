# Write your code here.
sample_function = lambda a, b, input = 'default': a + b + input


# sample_function(input = "asdf", "a", "b")      # ERROR
# sample_function("asdf", input = "a", "b")      # ERROR
print(sample_function("asdf", "a", input = "b"))      # VALID