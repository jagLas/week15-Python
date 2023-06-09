# Write your function here.

def exponent_decorator(function):
    def inner(*args):
        result = function(*args)
        return result**2
    return inner

def multiplier_decorator(function):
    def inner(*args):
        result = function(*args)
        return result * 3
    return inner

@exponent_decorator
@multiplier_decorator
def num(a, b):
    return a + b



print(num(5, 2))  #> 441
print(num(8, 2))  #> 900
print(num(4, 9))  #> 1521