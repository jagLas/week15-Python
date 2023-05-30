# Write your solution here.
import re

def valid_zip_code(zip):
    zipFormat = re.compile('[0-9]{5,5}(?:-[0-9]{4,4})?$')
    if zipFormat.match(zip):
        return True
    return False

zip1 = '47243'
zip2 = '23128-'
zip3 = '01237-1238'
zip4 = '91374-31'
zip5 = '1321-9883'
zip6 = '6320'

print(valid_zip_code(zip1))     # '47243'
print(valid_zip_code(zip2))     # "The zip code you entered is invalid"
print(valid_zip_code(zip3))     # '01237-1238'
print(valid_zip_code(zip4))     # "The zip code you entered is invalid"
print(valid_zip_code(zip5))     # "The zip code you entered is invalid"
print(valid_zip_code(zip6))     # "The zip code you entered is invalid"