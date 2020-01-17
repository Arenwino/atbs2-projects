'''
Chapter 4 Lists

Comma Code

Say you have a list value like this:
    spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function
should be able to work with any list value passed to it. Be sure to test
the case where an empty list [] is passed to your function.

'''

spam = ['apples', 'bananas', 'tofu', 'cats']
emptylist = []
mixedlist = ['apples', 3.14, True, 'end']
def commacode(listinput):
    result = ''
    if len(listinput) > 0:
        for item in listinput[:-1]:
            result += str(item) + ', '
        result += 'and ' + listinput[-1]
    return result

print(commacode(spam))
print(commacode(emptylist))
print(commacode(mixedlist))