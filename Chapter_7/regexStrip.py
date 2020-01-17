'''
Chapter 7 Pattern Matching with Regular Expressions

Regex Version of the strip() Method

Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.

'''

import re

testStrings = [ 'No spaces', ' leading space', '    lots of leading spaces', 'trailing space ', 
                ' leading and trailing space ']
testStringsOptChars = ['  *** leading *** space', '****** leading and trailing space *****']

def regexStrip(stripme, removeChars=None):
    if removeChars == None:
        return re.sub(r'(^ *)|( *$)', '', stripme)
    else:
        escapedRemoveChars = ''
        regexEscapes = ['*', '\\', '{', '}', '[', ']', '(', ')', '^', '$', '.', '+', '?', '|']
        for char in removeChars:
            if(char in regexEscapes):
                escapedRemoveChars += '\\' + char
        return re.sub('^' + escapedRemoveChars + '*|' + escapedRemoveChars + '*$', '', stripme)
    
for testS in testStrings:
    print(regexStrip(testS) == testS.strip()) 
for testOptS in testStringsOptChars:
    print(regexStrip(testS, '*') == testS.strip('*'))