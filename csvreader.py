__author__ = 'Tristan J Cobourne'
#csvstream.py
#This script aims to read csv files and perform an analysis.
#Currently assumes all csv files have headers********
import csv
import sys
import os.path
import collections
import statistics as stats
from savefile import create_file


#METHODS


def read_csv(csv_file):
    """Reads the provided csv file and displays rows + headers"""
    global csv_list, header

#Open assign dictionaries to reader
    with open(csv_file, 'rt') as sf:
        reader = csv.reader(sf)

        #INIT VARIABLES
        csv_list = to_sequence(reader)
        header = csv_list[0]
        tot_col = len(header)
        tot_rows = len(csv_list) - 1  # Assumes Header

        ## PRINT ROWS
        # try:
        #     for row in csv_list:
        #         print(row)
        # except csv.Error as e:
        #     sys.exit('file %s, line %d: %s' % (csv_file, reader.line_num, e))

        #Add if statement here to change analysis type
        p_csv = stats.Analysis(csv_list, tot_col, tot_rows)
        p_csv.full_analysis()
        create_file(p_csv.get_results())


def file_check():
    """Checks whether the path to the file exists"""
    path = False
    while path is not True:
        csv_file = input('Please enter the path to the CSV file: ')
        if os.path.isfile(csv_file):
            path = True
            return csv_file
        else:
            print('File does not exist, please try again.\n')


def to_sequence(reader):
    """Turn iterable into a sequence, avoiding a copy if possible."""
    if not isinstance(reader, collections.Sequence):
        x = list(reader)
    return x