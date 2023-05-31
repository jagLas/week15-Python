def addBinary(a, b):
    longest = 0
    shortest = 0

    bit_sum = ''
    if len(a) > len(b):
        longest = len(a)
        shortest = len(b)
    else:
        longest = len(b)
        shortest = len(a)

    i = -1
    carryover = 0

    while(i >= -shortest):
        digit1 = int(a[i])
        digit2 = int(b[i])
        digit_sum = digit1 + digit2 + carryover
        if digit_sum == 0:
            bit_sum = '0' + bit_sum
        elif digit_sum == 1:
            bit_sum = '1' + bit_sum
        else:
            bit_sum = '0' + bit_sum
            carryover = 1
        i -= 1

    return bit_sum
    print('longest:', longest, 'shortest:', shortest)




print(addBinary('11', '1'))

# print(addBinary('1010', '1011'))
# print(addBinary('0', '1011'))