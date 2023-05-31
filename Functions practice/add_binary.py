def addBinary(a, b):
    a = list(a)
    b = list(b)

    while len(a) < len(b):
        a.insert(0, '0')

    while len(b) < len(a):
        b.insert(0, '0')

    carryover = '0'
    binary_sum = ''

    for i in range(len(a) - 1, -1, -1):
        
        if a[i] == '1' and b[i] == '1' and carryover == '1':
            binary_sum = '1' + binary_sum
        elif a[i] != '1' and b[i] != '1' and carryover != '1':
            binary_sum = '0' + binary_sum
            carryover = '0'
        elif a[i] == '1' and b[i] == '1' or a[i] == '1' and carryover == '1' or b[i] == '1' and carryover == '1':
            binary_sum = '0' + binary_sum
            carryover = '1'
        else:
            binary_sum = '1' + binary_sum
            carryover = '0'
    
    if carryover == '1':
        binary_sum = '1' + binary_sum
        
    return binary_sum

print(addBinary('11', '1'))

print(addBinary('1010', '1011'))
print(addBinary('1', '1011'))