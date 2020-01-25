'''
Chapter 9 Reading and Writing Files

Regex Search

Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.

'''

from pathlib import Path
import pyinputplus as pyip
import re

# TODO: Bug in pyip??? inputRegexStr calls validateRegex instead of validateRegexStr
regex = pyip.inputRegexStr('Please input a regex: ')
pattern = re.compile(regex)

p = Path.cwd()
for txtFile in list(p.glob('*.txt')):
    with open(txtFile) as curFile:
        txtLines = curFile.readlines()
        for txtLine in txtLines:
            if(pattern.search(txtLine)):
                print(txtLine)