"""
In this problem, you'll explore the difference between a
dictionary in Python and a plain-old JavaScript object.
Try declaring a dictionary representing a cat using the same notation
as you would in JavaScript, with the properties for name, breed, and age.

Did you run into any errors executing your code?
Try adding or removing quotations around the keys
in your dictionary and see what effect that may have.
"""

cat = {
    'name': 'Spiffy',
    'breed': 'Cheshire',
    'age': 8
}

print(cat)

# it fails as it tries to use the name, and breed, age variables, which are not defined