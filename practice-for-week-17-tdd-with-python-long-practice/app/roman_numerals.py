def parse(numeral):
    numeralDict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    count = 0

    # for every digit except the last
    for index in range(len(numeral) - 1):
        digit = numeral[index]
        digit_value = numeralDict[digit]
        next_digit = numeral[index + 1]
        next_value = numeralDict[next_digit]

        # check if the next digit is bigger than current numeral to decided to add or subtract
        if digit_value < next_value:
            count -= digit_value
        else:
            count += digit_value

    # add the last roman numeral
    count += numeralDict[numeral[-1]]
    
    return count