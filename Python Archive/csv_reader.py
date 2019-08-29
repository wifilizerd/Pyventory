import csv
_filelist = []
# with open('MRJH2018-12102018.csv', newline=''):
for row in csv.reader(open('MRJH2018-12102018.csv', newline='')):
    if row:                                                     #check if there is data on tha row.
        if row[int(0)] == '':                                  #check if there is data in the field
            pass
        else:
            row.append('')
            _filelist.append(row)
                                           #append data to list in UPPER case
# self.p_print(4, Directories._TC['_INFO'], _filelist)
print(_filelist[0])

# with open('MRJH2018-12102018.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
