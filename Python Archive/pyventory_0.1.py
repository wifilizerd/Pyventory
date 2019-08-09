#!/Python27/pythonw.exe
#python 2.7
#Pyventory 0.1
# import all needed libraries
import sys
import csv

_importDB = open(sys.argv[4])   
_importDBreader = csv.reader(_importDB)     
_importDBdata = list(_importDBreader)

_companyDB = open(sys.argv[2])
_companyDBreader = csv.reader(_companyDB)
_companyDBdata = list(_companyDBreader)

def _notinlist(_company,_companycol,_import,_importcol):
    _missingDB = open("notinlist.csv", "wb")
    _missingDBwriter = csv.writer(_missingDB)
    #import files into a list
    _companyDBlist = []
    for row in _companyDBdata:
        if row:
            if row[int(_companycol)] == '':
                pass
            else:
                _companyDBlist.append(row[int(_companycol)].upper())
    _importDBlist = []
    
    for row in _importDBdata:
        if row:
            # print(repr(_importDBdata))
            if row[int(_importcol)] == '':
                pass
            else:
                _importDBlist.append(row[int(_importcol)].upper())
    #compaire items and write records to files
    for item in _importDBlist:
        if item.upper() not in _companyDBlist:
            # print(item)
            _missingDBwriter.writerow([item,])
        else:
            pass
    _missingDB.close()

def _popnotinlist(_company,_companycol,_import,_importcol):
    _notinlist(_company,_companycol,_import,_importcol)
    _missingDB = open("notinlist.csv")
    _missingDBreader = csv.reader(_missingDB)
    _missingDBdata = list(_missingDBreader)

    _popnotinlist = open("popnotinlist.csv", "wb")
    _popnotinlistwriter = csv.writer(_popnotinlist)

    for item in _missingDBdata:
        for row in _importDBdata:
            if row:
                if item[0].upper() == row[int(sys.argv[5])].upper():
                    print(item[0].upper().strip(), row[int(sys.argv[5])].upper().strip())
                    _popnotinlistwriter.writerow((item + row))
    
def _inlist(_company,_companycol,_import,_importcol):
    
    _exportDB = open("Inlist.csv", "wb")
    _exportDBwriter = csv.writer(_exportDB)
    #import files into a list
    _companyDBlist = []
    for row in _companyDBdata:
        if row[int(_companycol)] == '':
            pass
        else:
            _companyDBlist.append(row[int(_companycol)])
    _importDBlist = []
    for row in _importDBdata:
        if row[int(_importcol)] == '':
            pass
        else:
            _importDBlist.append(row[int(_importcol)])
    #compaire items and write records to files
    for item in _importDBlist:
        if item.upper() in _companyDBlist.upper():
            print(item)
            _exportDBwriter.writerow([item,])
        else:
            pass
    _importDB.close()
        
def _popinlist(_company,_companycol,_import,_importcol):
    _inlist(_company,_companycol,_import,_importcol)
    _exportDB = open("Inlist.csv")
    _exportDBreader = csv.reader(_exportDB)
    _exportDBdata = list(_exportDBreader)

    _popinlist = open("popinlist.csv", "wb")
    _popinlistwriter = csv.writer(_popinlist)

    for item in _exportDBdata:
        for row in _companyDBdata:
            if item[0].upper() == row[int(sys.argv[3])].upper():
                print((item + row))
                _popinlistwriter.writerow((item + row))

  

if len(sys.argv) != 6:
    print("need more info")
else:
    if sys.argv[1] == '-inlist':
        _inlist(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == '-notinlist':
        _notinlist(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == '-popinlist':
        _popinlist(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == '-popnotinlist':
        _popnotinlist(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

# _inlist("filemaker11302017.csv", 29, "Chromebooks-12-26-2017.csv", 13)
# _notinlist("filemaker11302017.csv", 29, "Chromebooks-12-26-2017.csv", 13)