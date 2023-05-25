# Write your function, here.
def recursive_fib(num):
    if num == 1 or num==2:
        return 1
    return recursive_fib(num-1) + recursive_fib(num-2)

print(recursive_fib(1))     #> 1
print(recursive_fib(2))     #> 1
print(recursive_fib(4))     #> 3
print(recursive_fib(6))     #> 8
print(recursive_fib(12))    #> 144