# Write your function, here.
def gas_prices(lst, limit):
    return [price if price > limit else 0 for price in lst]


print(gas_prices([2.55, -1.45, 10.22, 5.78, -5.92, 6.16], 3.99)) #> [0, 0, 10.22, 5.78, 0, 6.16]
print(gas_prices([5.95, 6.62, 2.22, 6.78, 8.92, 7.03], 2.50)) #> [5.95, 6.62, 0, 6.78, 8.92, 7.03]
print(gas_prices([4.55, 4.15, 2.57, 3.78, 2.92, 0.16], 5.00)) #> [0, 0, 0, 0, 0, 0]