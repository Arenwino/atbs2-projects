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

import shutil, sys, os
from pathlib import Path

if(len(sys.argv) == 4):
    oldPath = Path(sys.argv[2])
    newPath = Path(sys.argv[3])
    for dirname in oldPath.glob(f'**/*.{sys.argv[1]}'): # **/.* find recursively all files
        if(os.path.exists(newPath) == False): # If the new dir doesn't exist, create it
            newPath.mkdir()
        print(f'Copying {dirname} to {newPath}')
        shutil.copy(dirname, newPath)
else: 
    print('Usage: python selectiveCopy.py filetype oldDir newDir')

