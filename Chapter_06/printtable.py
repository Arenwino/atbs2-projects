'''
Chapter 6 Manipulating Strings

Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.

'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', '#David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tData):
    colWidth = [0] * len(tData)
    for col in range(len(tData)):
        for row in range(len(tData[0])):
            entryLength = len(tData[col][row])
            if(entryLength > colWidth[col]):
                colWidth[col] = entryLength
    for row in range(len(tData[0])):
        for col in range(len(tData)):
            print(tData[col][row].rjust(colWidth[col]) + ' ', end='')
        print()

printTable(tableData)
