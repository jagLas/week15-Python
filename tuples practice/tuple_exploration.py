# DO NOT EDIT
odds = 1,3,5,7,9
evens = 2,4,6,8

# Step 1: Print out the result of adding evens to odds
print(odds + evens)


# Step 2: Print out the result of multiplying odds by three
print(odds * 3)

# Step 3A: Use print to find out if odds is less than evens
print (odds < evens)

# Step 3B: Print out your explanation of why 3A has that result
print('tuples are compared position by position. So 1 < 2, 3 <4, etc.')

# Step 4: Print out the average of the numbers in evens using one line of code
print(sum(evens)/len(evens))

# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)
def minmaxmean(tup):
    return min(tup), max(tup), sum(tup)/len(tup)


# Step 5B: Use print to confirm you function is working on evens and odds
print(minmaxmean(odds))
print(minmaxmean(evens))

# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way