'''
Chapter 7 Pattern Matching with Regular Expressions

Date Detection

Write a regular expression that can detect dates in the DD/MM/YYYY format. 
Assume that the days range from 01 to 31, the months range from 01
to 12, and the years range from 1000 to 2999. Note that if the day or month
is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each
month or for leap years; it will accept nonexistent dates like 31/02/2020 or
31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April,
June, September, and November have 30 days, February has 28 days, and
the rest of the months have 31 days. February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly 
divisible by 100, unless the year is also evenly divisible by 400. Note how 
this calculation makes it impossible to make a reasonably sized regular 
expression that can detect a valid date.
'''

import re

passwords = [ 'shortpw', '8charact', 'onlylower', 'ONLYUPPER', 'NoDigitDigit', 'C0rrectPw']

def checkPassword(password):
    print(f'Checking {password}:')
    lengthRegex = re.compile(r'.{8,}') # Length >= 8
    upperLowerRegex = re.compile(r'([a-z])([A-Z])') # At least one upper- and lowercase letter
    oneDigitRegex = re.compile(r'\d')
    if lengthRegex.search(password) is None:
        print(f'Password is not long enough. Must be at least 8 characters, {password}: {len(password)}')
        return False
    if upperLowerRegex.search(password) is None:
        print(f'Password must have at least one Uppercase and one lowercase letter, {password}')
        return False
    if oneDigitRegex.search(password) is None:
        print(f'Password must have at least one digit, {password}')
        return False

    return True

for pw in passwords:
    print(checkPassword(pw))