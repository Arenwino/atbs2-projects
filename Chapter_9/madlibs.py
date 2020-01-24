'''
Chapter 9 Reading and Writing Files

Mad Libs

Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to
replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.

'''

#! python3
# madlibs.py <filename> - reads <filename> and replaces any occurrences of 
# 'ADJECTIVE', 'NOUN', 'ADVERB', 'VERB'.

import pyinputplus as pyip
import re
import sys

keywords = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

if(len(sys.argv) == 2):
    with open(sys.argv[1]) as txtfile:
        txt = txtfile.read()

    for keyword in keywords:
        while(keyword in txt):
            print(f'Found {keyword}')
            replacement = pyip.inputStr(f'Enter an {keyword.lower()}: ')
            txt = txt.replace(keyword, replacement, 1)

    print(txt)

    with open('madlibs_subs.txt', 'w') as newTxtfile:
        newTxtfile.write(txt)