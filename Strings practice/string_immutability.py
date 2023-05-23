def test_mutation(str):
    str[1] = 'b'
    print(str)

#should throw a typeError because strings are immutable
test_mutation('Call')