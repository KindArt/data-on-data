__author__ = 'Tristan J Cobourne'
#main.py
#This script is used to manage all the other scripts.

import csvreader as csv

#VARIABLES


delimiter = None
quote_char = None
header = None


def main():
    #delimiter = input('\nWhat is the delimiter for the CSV file? ')
    #quote_char = input('\nIs the quote character \' or \"? ')
    global delimiter, quote_char

    #Initial opening text
    print('Developed by: Tristan Cobourne\n' +
          'Welcome to Data on Data (PRE-ALPHA)\n')

    #print('Please direct Data on Data to your dataset:')  # User interaction
    file = csv.file_check()  # Checks if file exist
    #file = r'/Users/TJxKA/Documents/workspace/Data On Data/csv/MOTsitelist.csv'
    #csv_file = r'C:\Users\TJxKA\workspace\Data On Data\csv\test.csv'

    input('When you are ready to begin profiling, please press Enter...\n')

    csv.read_csv(file)

    input('Analysis complete. To exit press enter...\n')
    exit()

main()