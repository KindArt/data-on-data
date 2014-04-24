__author__ = 'Tristan J Cobourne'
#statistics.py
#This script contains the methods to perform the analysis.
#The analysis will be split into two segments: Basic & Advanced.
import operator
import regex

results = []


class Analysis:

    def __init__(self, file_list, tot_col, tot_rows):
        self.file_list = file_list
        self.tot_col = tot_col
        self.tot_rows = tot_rows
        self.empty = self.calc_empty()

    def get_results(self):
        return results

    def full_analysis(self):
        """Currently runs all the analysis methods"""
        print('FULL ANALYSIS\n' +
              '----------------------------------\n')
        #print('Basic Statistics')  # Remove this and run 'basic_stats'
        results.append('FULL ANALYSIS\n' +
                       '----------------------------------\n')
        print('Basic Information\n' +
              '----------------------------')
        results.append('Basic Information\n' +
                       '----------------------------')
        self.info_density()
        self.calc_total_rows()
        self.show_empty()
        self.calc_null()
        self.calc_col_len()
        self.calc_row_len()
        self.calc_col_info()
        self.regex_info()

    def calc_total_rows(self):
        """Calculates the total number of rows minus the header"""
        #total_rows = len(self.file_list) - 1  # Minus header
        print('Total number of rows: ' + str(self.tot_rows))
        results.append('Total number of rows: ' + str(self.tot_rows))

    def calc_null(self):
        """Calculates the total number of null fields"""
        null = 0
        for x in range(0, self.tot_col):
            for y in range(1, self.tot_rows + 1):
                if self.file_list[y][x].lower() == 'null':
                    null += 1
        print('Total number of null fields: ' + str(null))
        results.append('Total number of null fields: ' + str(null))

    def calc_empty(self):
        """Calculates the total number of empty fields"""
        empty = 0
        for x in range(0, self.tot_col):
            for y in range(1, self.tot_rows + 1):
                if self.file_list[y][x] == '':
                    empty += 1
                    #print(csv_list[y][x] + ' %s %s' % (x, y))
        return empty

    def show_empty(self):
        print('Total number of empty fields: ' + str(self.empty))
        results.append('Total number of empty fields: ' + str(self.empty))

    def info_density(self):
        """Calculates the percentage of populated fields. Not including header."""
        tot_fields = self.tot_col * self.tot_rows  # Total number of fields
        pop_fields = 100 - ((self.empty / tot_fields) * 100)

        print('Information density (%): ' + str(pop_fields) + '%')
        results.append('Information density (%): ' + str(pop_fields) + '%')

    def calc_col_len(self):  # Calculates length of each column
        """Calculates the length of each column"""
        print('\nColumn Lengths\n' +
              '--------------')
        results.append('\nColumn Lengths\n' +
                       '--------------')
        for x in range(0, self.tot_col):
            blank = 0
            for y in range(1, self.tot_rows + 1):
                if self.file_list[y][x] == '':
                    blank += 1
            column_count = self.tot_rows - blank

            results.append('Column \'' + self.file_list[0][x] + '\' length: ' + str(column_count))
            print('Column \'' + self.file_list[0][x] + '\' length: ' + str(column_count))

    def calc_row_len(self):
        """Calculates the maximum & Minimum length of each row"""
        print('\nRow Lengths\n' +
              '--------------')
        results.append('\nRow Lengths\n' +
                       '--------------')
        li = []
        for y in range(1, self.tot_rows + 1):
            blank = 0
            for x in range(0, self.tot_col):
                if self.file_list[y][x] == '':
                    blank += 1
                max_row_len = self.tot_col - blank
            li.append(max_row_len)

        results.append('Maximum row length: ' + str(max(li)) +
                       '\nMinimum row length: ' + str(min(li)))
        print('Maximum row length: ' + str(max(li)) +
              '\nMinimum row length: ' + str(min(li)))

    def calc_col_info(self):
        """Calculates max, min and dup values in each column"""
        print('\nCOLUMN VALUE INFORMATION\n' +
              '----------------------------')
        results.append('\nCOLUMN VALUE INFORMATION\n' +
                       '----------------------------')
        li = []
        for x in range(0, self.tot_col):
            print(str('\n' + self.file_list[0][x]) +
                  '\n--------------')  # Prints name of column

            results.append('\n' + self.file_list[0][x] +
                           '\n--------------')

            for y in range(1, self.tot_rows + 1):
                li.append(self.file_list[y][x])
                li_no_empty = [x for x in li if x != '']  # List with no empty fields

            # MAX & MIN VALUE
            print('Maximum value: ' + str(max(li)))
            print('Minimum value: ' + str(min(li_no_empty)))
            results.append('Maximum value: ' + str(max(li)))
            results.append('Minimum value: ' + str(min(li_no_empty)))

            # MAX & MIN LENGTH
            li_b = []
            li_c = []
            for a in range(0, len(li)):
                li_b.append(len(li[a]))

            print('Maximum length: ' + str(max(li_b)))
            results.append('Maximum length: ' + str(max(li_b)))

            for b in range(0, len(li_no_empty)):
                li_c.append(len(li_no_empty[b]))

            print('Minimum length: ' + str(min(li_c)))
            results.append('Minimum length: ' + str(min(li_c)))

            del li_b[:]
            del li_c[:]

            # DISTINCT
            unique_set = set(li)  # Counts blanks
            unique_set.discard('')  # Does not account for null values
            unique_count = len(unique_set)

            print('Distinct values: ' + str(unique_count))
            results.append('Distinct values: ' + str(unique_count))

            # DUPLICATES
            value_count = {}
            for c in li:
                value_count[c] = value_count.get(c, 0) + 1
            dups = {key: value for key, value in value_count.items() if value > 1}
            sorted_dups = sorted(dups.items(), key=operator.itemgetter(1))

            print('\nDuplicate values\n' +
                  '-------')
            results.append('\nDuplicate values\n' +
                           '-------')

            for item in sorted_dups:
                print('{}'.format(str(item[0])) + ' : ' + str(item[1]))
                results.append('{}'.format(str(item[0])) + ' : ' + str(item[1]))

            # for key, num in dups.items():
            #     print('{} : {}'.format(key, num))
            #     results.append('{} : {}'.format(key, num))

            del li[:]

    def setup_regex(self):
        re_list = []
        for x in range(0, self.tot_col):
            for y in range(0, self.tot_rows + 1):
                re_list.append(self.file_list[y][x])

    def regex_info(self):
        merged_col = []
        print('\nREGULAR EXPRESSIONS\n' +
              '----------------------------------')
        results.append('\nREGULAR EXPRESSIONS\n' +
                       '----------------------------------')
        for x in range(0, self.tot_col):
            print('\n' + self.file_list[0][x] +
                  '\n--------------')
            results.append('\n' + self.file_list[0][x] +
                           '\n--------------')
            for y in range(0, self.tot_rows + 1):
                merged_col.append(self.file_list[y][x])

            del merged_col[0]
            match_col = ' '.join(merged_col)
            #print(merged_col)
            #print(match_col)
            #if regex.re_alpha(match_col) is True:
            #print(match_col)
            if regex.re_alpha(match_col):
                print('Contains only alpha characters.')
                results.append('Contains only alpha characters.')
            del merged_col[:]
            if regex.re_numeric(match_col):
                print('Contains only numeric characters possibly with one of the following separators: +'
                      ' - /')
                results.append('Contains only numeric characters possibly with one of the following separators: +'
                               ' - /')
            del merged_col[:]
            if regex.re_alphanumeric(match_col):
                print('Contains only alphanumeric characters.')
                results.append('Contains only alphanumeric characters.')
            del merged_col[:]
            if regex.re_non_alphanumeric(match_col):
                print('Contains only non-alphanumeric characters.')
                results.append('Contains only non-alphanumeric characters.')
            del merged_col[:]
            if regex.re_email(match_col):
                print('Contains only email addresses.')
                results.append('Contains only email addresses.')
            del merged_col[:]
            if regex.re_date(match_col):
                print('Contains only dates.')
                results.append('Contains only dates.')
            del merged_col[:]
            # if regex.re_year(match_col):
            #     print('Contains only years.')
            #     results.append('Contains only years.')
            # del merged_col[:]
            # if regex.re_domain(match_col):
            #     print('Contains only domains.')
            #     results.append('Contains only domains.')
            # del merged_col[:]


            # if true_count > false_count:
            #     percentage = (true_count / self.tot_rows) * 100
            #     print(str(percentage) + '% chance that this column is a domain')

        true_count = 0
        false_count = 0