# Write your function here.
def world_decorator(func_to_decorate):
    def func_wrapper():
        print('Hello')
        func_to_decorate()
        print('Goodnight')
    return func_wrapper



@world_decorator
def world():
    print("World")

world() #> Hello World Goodnight