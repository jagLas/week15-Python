# Write your function, here.
def track_robot(inputs):
    location = [0,0]
    if len(inputs)==0:
        return location
    
    for input in inputs:
        amount = int(input.split()[1])
        x = input[0]
        if x == 'u':
            location[1] += amount
        elif x == 'r':
            location[0] += amount
        elif x == 'd':
            location[1] -= amount
        else:
            location[0] -= amount
    
    return location



print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]