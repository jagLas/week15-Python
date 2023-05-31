# Write your code here.
def string_multi_print(str):
    return lambda n: print(str * n)



string_multi_print('hello ')(2)  # Prints "hello hello "
string_multi_print('wahoo ')(3)  # Prints "wahoo wahoo wahoo "
