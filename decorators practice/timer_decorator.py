# Write your function here.
from datetime import datetime

def timer_decorator(function):
    def wrapper(*args, **kwargs):
        before_time = datetime.now()
        function(*args)
        after_time = datetime.now()
        return after_time - before_time
    return wrapper

@timer_decorator
def greet_me(name):
    return f"hello {name}"

@timer_decorator
def sum_of_two(sum1, sum2):
    return sum1 + sum2

print(greet_me("Penelope")) # approximately 0:00:00.000006
print(sum_of_two(13, 7)) # approximately 0:00:00.000002