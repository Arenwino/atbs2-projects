'''
Chapter 10 Organizing Files

Filling in the Gaps

Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the 
numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.

'''

# fillingGaps.py - Renames all files with the given prefix in a dir, 
# so there are no gaps in the numbering sequence. It checks where the 
# sequence start and pads all files to the same length of leading zeros 
# Usage: python fillingGaps.py rootDir filenamePrefix

import sys, os, re, shutil
from pathlib import Path
from operator import itemgetter

def findMatchingFiles(rootDir, filenamePrefix):
    ''' Matches the files in the rootDir to the given prefix and
        returns a list with the Path, integer literal, the integer literal 
        as int and the suffix of the filename.
    '''
    pattern = re.compile(r'(' + filenamePrefix + r')(\d+)(.*)')
    gapFileList = []

    for filename in os.listdir(rootDir):
        mo = pattern.match(filename) 
        if mo is not None:
            intLiteral = mo.group(2)
            fileSuffix = mo.group(3)
            gapFileList.append([Path(rootDir).resolve() / filename, intLiteral, int(intLiteral), fileSuffix])

    return gapFileList

def getLongestIntLiteral(sortedFileList):
    ''' Returns the size of the longest integer literal e.g. 0002 --> 4
        TODO: Maybe there is a shorter pythonic version
    ''' 

    lengthIntLiteral = 0
    for sortedFile in sortedFileList:
        if len(sortedFile[1]) > lengthIntLiteral:
            lengthIntLiteral = len(sortedFile[1])
    return lengthIntLiteral

def renameFiles(sortedFileList, lengthIntLiteral, filenamePrefix, gapAt=0):
    ''' Loops through every file in the list. If the number in
        the file name is not the next in the sequence or hasn't the right 
        amount of leading zeros renames it. 

    '''

    # Find out where the sequence begins
    start = sortedFileList[0][2]

    if(gapAt is not 0):
        sortedFileList = sortedFileList[gapAt-sortedFileList[0][2]:]
        start=gapAt-1+start

    for i, gapFile in enumerate(sortedFileList, start=start):

            ''' Check if the index is not the same as the number OR
                the length of the integer literal is not the length of the longest 
                integer literal in the list
            '''

            if (i is not gapFile[2] or len(gapFile[1]) is not lengthIntLiteral):
                # i:0{lengthNumber} pads the new number to the length of the longest int literal
                shutil.move(gapFile[0], Path(os.path.dirname(gapFile[0])) / f'{filenamePrefix}{i:0{lengthIntLiteral}}{gapFile[3]}')

if __name__ == "__main__":

    if(len(sys.argv) == 3):
        rootDir = Path(sys.argv[1])
        filenamePrefix = sys.argv[2]

        gapFileList = findMatchingFiles(rootDir, filenamePrefix)

        # Sort the list of files by the number
        sortedFileList = sorted(gapFileList, key=itemgetter(int(2)))
        lengthIntLiteral = getLongestIntLiteral(sortedFileList)
        renameFiles(sortedFileList, lengthIntLiteral, filenamePrefix)

    else:
        print('Usage: python fillingGaps.py rootDir filenamePrefix')

