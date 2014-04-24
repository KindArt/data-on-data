__author__ = 'Tristan J Cobourne'
#contentmatch.py
#This scripts aims to aid in profiling each column.
from re import *

#VARIABLES

alpha = compile('^[a-zA-Z\s]+$')
numeric = compile('[0-9-?/?\'?\s]+$')
alphanumeric = compile('(\d+[A-Za-z])|([A-Za-z]+\d)[\dA-Za-z]*')
non_alphanumeric = compile('[^a-zA-Z\d\s]+$')
email = compile('(^|)[-a-zA-Z0-9_.]+@([-a-zA-Z0-9]+\.)+[a-zA-Z]{2,6}(|$)')
date = compile(r'(\d+/\d+/\d+)')
year = compile('^(19|20)[\d\s]{2,2}$')
domain = compile(r'^(?:http|ftp)s?://'  # http:// or https://
                 r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                 r'localhost|' # localhost...
                 r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
                 r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
                 r'(?::\d+)?' # optional port
                 r'(?:/?|[/?]\S+)$', IGNORECASE)


#METHODS


def re_alpha(column):
    # Checks numeric characters
    alpha_valid = alpha.match(column)
    if alpha_valid:
        return True
    else:
        return False


def re_numeric(column):
    # Checks numeric characters
    numeric_valid = numeric.match(column)
    if numeric_valid:
        return True
    else:
        return False


def re_alphanumeric(column):
    # Checks alphanumeric characters
    alphanumeric_valid = alphanumeric.match(column)
    if alphanumeric_valid:
        return True
    else:
        return False


def re_non_alphanumeric(column):
    # Checks alphanumeric characters
    non_alphanumeric_valid = non_alphanumeric.match(column)
    if non_alphanumeric_valid:
        return True
    else:
        return False


def re_email(column):
    # Checks for emails
    email_valid = email.match(column)
    if email_valid:
        return True
    else:
        return False


def re_date(column):
    # Checks for emails
    date_valid = date.match(column)
    if date_valid:
        return True
    else:
        return False


def re_year(column):
    # Checks for emails
    year_valid = year.match(column)
    if year_valid:
        return True
    else:
        return False


def re_domain(column):
    domain_valid = domain.match(column)
    if domain_valid:
        return True
    else:
        return False


def re_currency(column):
    currency_valid = domain.match(column)
    if currency_valid:
        return True
    else:
        return False



# def alphanumeric_test():
# #Checks for alphanumeric values
#     cell = input('Enter an alphanumeric value: ')
#     alphanumeric_valid = alphanumeric.match(cell)
#     if alphanumeric_valid:
#         print('The cell contains only alphanumeric values.\n')
#     else:
#         print('Invalid. The cell contains other characters.\n')


# def re_alpha(file_list, tot_col, tot_rows):
#     # Checks alpha characters
#     true_count = 0
#     false_count = 0
#     for x in range(0, tot_col):
#         for y in range(0, tot_rows + 1):
#             cell_valid = alpha.file_list[y][x]
#             if cell_valid:
#                 true_count += 1
#             else:
#                 false_count += 1
#
#             if true_count > false_count:
#                         percentage = (true_count / tot_rows) * 100
#                         print(str(percentage) + '% chance that this column is alpha chars')