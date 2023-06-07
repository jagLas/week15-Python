# Write your function, here.
def fizzbuzz(lst):
    return [num for num in lst if num%3==0 and num%5==0]


print(fizzbuzz([15, 5, 10, 30])) #> [15, 30]
print(fizzbuzz([60, 20, 90, 20])) #> [60, 90]
print(fizzbuzz([-15, 120, 35, -30])) #> [-15, 120, -30]