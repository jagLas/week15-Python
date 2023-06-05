# Write your function, here.
def is_empty(dictionary):
    return len(dictionary) == 0

"""
Provided solution
# Write your function, here.
def is_empty(d):
  return not d

"""


print(is_empty({}))        #> True
print(is_empty({"a": 1}))  #> False