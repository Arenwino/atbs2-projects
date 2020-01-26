'''
Chapter 10 Organizing Files

Insert Gaps

As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.

'''

import os
from fillingGaps import findMatchingFiles
insertAfter = 4
rootDir = 'test_files'
prefix = 'test'

for filename in os.listdir(rootDir):
    print(findMatchingFiles(rootDir, prefix))
    
