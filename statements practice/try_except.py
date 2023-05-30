# Example 1
try:
    str = 'hello'
    str[0] = 'm'
    print(str)
except TypeError:
    print('Characters cannot be reassigned in strings')
finally:
    print('I happen regardless of any exceptions.')

# Example 2
try:
    print(x)
except NameError as e:
    print(f'Variable {e}')
finally:
    print('I happen regardless of any exceptions.')