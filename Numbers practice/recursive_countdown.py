# Write your function, here.
def recursive_countdown(n):
    if n == 0:
        return print(n)
    print(n)
    recursive_countdown(n-1)


recursive_countdown(5) #> 5 4 3 2 1