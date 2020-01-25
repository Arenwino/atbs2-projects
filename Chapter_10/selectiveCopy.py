'''
Chapter 10 Organizing Files

Selective Copy

Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.

'''

#! python3
# selectiveCopy.py - Copies files of a certain filetype to a new location
# Usage: python selectiveCopy.py filetype oldDir newDir

import shutil, sys, pathlib, os

if(len(sys.argv) == 4):
    oldPath = pathlib.Path(sys.argv[2])
    newPath = pathlib.Path(sys.argv[3])
    fileGenerator = oldPath.glob(f'*.{sys.argv[1]}')
    # TODO: find out how to check for an empty generator
    print(fileGenerator)
    for dirname in fileGenerator:
        if(os.path.exists(newPath) == False): # If the new dir doesn't exist, create it
            newPath.mkdir()
        print(f'Copying {dirname} to {newPath}')
        shutil.copy(dirname, newPath)
else: 
    print('Usage: python selectiveCopy.py filetype oldDir newDir')

