# Write your function, here.
def cap_space(string):
    response = ''
    for char in string:
        if char.isupper():
            response += ' ' + char.lower()
        else:
            response += char

    return response


print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"