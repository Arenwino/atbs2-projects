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
Leap years are every year evenly divisible by 4, except for years evenly divisible
by 100, unless the year is also evenly divisible by 400. Note how this calculation 
makes it impossible to make a reasonably sized regular expression
that can detect a valid date.

'''

import re

testDates = ['31/04/2000', '30/02/1900', '29/02/2000', '30/02/2000', '21/12/4123', '123/12/2222', '41/13/4123', '3a/23/3333']

monthWith30Days = (4,6,9,11)

dateRegex = re.compile(r'(^[0-3]\d)\/([0-1][0-9])\/([1-2]\d{3})')


for testDate in testDates:
    print(f'Checking: {testDate}')
    try:
        day, month, year = dateRegex.findall(testDate)[0]
    except:
        print(f'{testDate} is not a valid date.') 
    if((int(year) % 4) == 0 and (int(year) % 400) == 0 and not (int(year) % 100) != 0 ):
        leapYear = True
    if(int(month) in monthWith30Days and int(day) > 30):
        print(f'{month} has only 30 days') 
    elif(int(month) == 2 and int(day) > 28 and leapYear == False):
        print(f'{month} has only 28 days')
    elif(int(month) == 2 and int(day) > 29 and leapYear == True):
        print(f'{month} has only 29 days')
    elif(int(day) > 31):
        print(f'{month} has only 31 days')