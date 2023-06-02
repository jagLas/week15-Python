#  Write your function, here.
import random

def rng(lst):
    lst = []
    for i in range(0, 100):
        lst.append(random.randint(-100, 100))
    return lst

print(rng([]))