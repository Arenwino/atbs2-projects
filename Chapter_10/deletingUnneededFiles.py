'''
Chapter 10 Organizing Files

Deleting Unneeded Files

It’s not uncommon for a few unneeded but humongous files or folders to
take up the bulk of the space on your hard drive. If you’re trying to free up
room on your computer, you’ll get the most bang for your buck by deleting
the most massive of the unwanted files. But first you have to find them.
Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than
100MB. (Remember that to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their absolute path to the screen.

'''

#! python3
# deletingUnneededFiles.py - Print every file of the given path which is over $size
# Usage: python deletingUnneededFiles.py path size

import os, sys
from pathlib import Path

if(len(sys.argv) == 3):
    searchedDir = Path(sys.argv[1])

    try:
        minSize = int(sys.argv[2]) 
    except ValueError:
        print(f'{minSize} is not an Integer.')
    else:
        # save each filename and size in a tuple under the key 'entries' in a dict
        fileTable = {} 
        fileTable['entries'] = []
        fileTable.setdefault('pathlength', 0)

        for dirname, dirnames , filenames in os.walk(searchedDir):
            for filename in filenames:
                fileSize = os.path.getsize(os.path.join(dirname, filename))

                # check if the current file is bigger than the size given in the second argument
                if(fileSize > minSize):
                    abspath = os.path.abspath(filename) 
                    fileTable['entries'].append((abspath, fileSize))
                    pathlength = len(abspath)
                    if pathlength > fileTable['pathlength']:   # Check for the longest pathlength in dir 
                        fileTable['pathlength'] = pathlength

        # pretty print the filenames and sizes     
        for filePath, size in fileTable['entries']:
            print(filePath.ljust(fileTable['pathlength']+1) + str(size))

else:
    print('Usage: python deletingUnneededFiles.py path size')