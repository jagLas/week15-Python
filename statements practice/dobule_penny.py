print("** Doubling Penny **")

# How many times would a penny need to double to generate a million dollars?
count = 0
total = 0

# STEP 2: Write the while loop

total += .01
while total < 1000000:
    count += 1
    total *= 2


print('Double', count, 'times')

# How much money has been generated at that point?
print('${:,}'.format(total))