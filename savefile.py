__author__ = 'Tristan J Cobourne'
#savefile.py
#This script will aid in the creation of reports


def create_file(results):
    txt_name = file_name_check()
    text_file = open(txt_name, "w")

    for item in results:
        text_file.write('%s\n' % item)

    text_file.close()


def file_name_check():
    txt_name = ''
    while txt_name == '':
        txt_name = input('\nPlease provide a name for the save file: ')
        if txt_name != '':
            txt_name += '.txt'
            return txt_name
        else:
            print('The file name cannot be empty.')