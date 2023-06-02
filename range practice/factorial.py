# Write your function, here.
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(factorial(1))     #> 1
print(factorial(8))     #> 40320
print(factorial(12))    #> 479001600