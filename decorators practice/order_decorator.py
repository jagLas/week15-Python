# Write your function here.
def order_decorator(function):
    def wrapper(num):
        print(1)
        final = function(num)
        print(3)
        return final
    return wrapper


@order_decorator
def middle(num):
    print(num)
    return num * num

print(middle(2)) #> 1 2 3 4