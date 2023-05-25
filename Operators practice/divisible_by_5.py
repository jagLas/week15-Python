# Write your function, here.
def divisible_by_five(n):
    return n % 5 == 0


print(divisible_by_five(5))    #> True
print(divisible_by_five(-55))  #> True
print(divisible_by_five(37))   #> False