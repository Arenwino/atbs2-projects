'''
Chapter 16 Working with CSV Files and JSON Data

Excel-to-CSV Converter

Excel can save a spreadsheet to a CSV file with a few mouse clicks, but if
you had to convert hundreds of Excel files to CSVs, it would take hours of
clicking. Using the openpyxl module from Chapter 12, write a program that
reads all the Excel files in the current working directory and outputs them
as CSV files.

A single Excel file might contain multiple sheets; you’ll have to
create one CSV file per sheet. The filenames of the CSV files should be
<excel filename>_<sheet title>.csv, where <excel filename> is the filename of
the Excel file without the file extension (for example, 'spam_data', not
'spam_data.xlsx') and <sheet title> is the string from the Worksheet object’s
title variable.

This program will involve many nested for loops. The skeleton of the
program will look something like this:

...

Download the ZIP file excelSpreadsheets.zip from https://nostarch.com
/automatestuff2/ and unzip the spreadsheets into the same directory as
your program. You can use these as the files to test the program on.

'''

import os, logging, openpyxl, csv
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

for excelFile in os.listdir('.'):
    if not excelFile.endswith('xlsx'):
        logging.debug(f'{excelFile} is not an excel workbook')
        continue
    
    with open(excelFile, mode='rb') as wbFileObject:
        wb = openpyxl.load_workbook(excelFile)

        logging.debug(f'loading {excelFile}')
        # Skip non-xlsx files, load the workbook object.
        for sheetName in wb.sheetnames:
            logging.debug(f'loading sheet: {sheetName}')
            # Loop through every sheet in the workbook.
            sheet = wb[sheetName]

            # Create the CSV filename from the Excel filename and sheet title.
            csvFilename = f'{Path(excelFile).stem}_{sheetName}.csv'
            
            with open(csvFilename, mode='w', newline='') as csvFile:
          
                # Create the csv.writer object for this CSV file.
                csvWriter = csv.writer(csvFile)

                # Loop through every row in the sheet.
                for rowNum in range(1, sheet.max_row + 1):
                    rowData = [] # append each cell to this list
    
                # Loop through each cell in the row.
                    for colNum in range(1, sheet.max_column + 1):
                        # Append each cell's data to rowData.
                        rowData.append(sheet.cell(rowNum, colNum).value)
                # Write the rowData list to the CSV file.
                    csvWriter.writerow(rowData)
                logging.info(f'Wrote {sheet.max_row} rows to {csvFile.name}')