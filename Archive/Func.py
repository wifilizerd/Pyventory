#!/Python27/pythonw.exe
def PyventoryDBReadWrite(_readwrite):
    import csv
    import os
    from config import _importdir, _databasedir 
    if _readwrite == 'write':
        if os.path.isfile(os.path.join(_databasedir, 'PyventoryDB.csv')):         #check if pyventory file exsits already.
            _PyventoryDB = open(os.path.join(_databasedir, 'PyventoryDB.csv'), 'a')        #open csv file to edit 
            _PyventoryDBwriter = csv.writer(_PyventoryDB)      #using csv reader and list to create a list of list that are the csv rows
        else:
            _PyventoryDB = open(os.path.join(_databasedir, 'PyventoryDB.csv'), 'wb')        #open csv file to edit 
            _PyventoryDBwriter = csv.writer(_PyventoryDB)      #using csv reader and list to create a list of list that are the csv rows
        return _PyventoryDBwriter
    elif _readwrite == 'read':
        if os.path.isfile(os.path.join(_databasedir, 'PyventoryDB.csv')):
            _PyventoryDB = open(os.path.join(_databasedir, '_PyventoryDB.csv'))        #open csv file to edit 
            _PyventoryDBreader = csv.reader(_PyventoryDB)      #using csv reader and list to create a list of list that are the csv rows
            _PyventoryDBdata = list(_PyventoryDBreader)
        else:
            return "no database found"
        return _PyventoryDBdata
def CompanyDBReadWrite(_readwrite):
    import csv
    import os
    from config import _importdir, _databasedir
    if _readwrite == 'write':
        if os.path.isfile(os.path.join(_databasedir, 'CompanyDB.csv')):         #check if pyventory file exsits already.
            _CompanyDB = open(os.path.join(_databasedir, 'CompanyDB.csv'), 'a')        #open csv file to edit 
            _CompanyDBwriter = csv.writer(_CompanyDB)      #using csv reader and list to create a list of list that are the csv rows
        else:
            _CompanyDB = open(os.path.join(_databasedir, 'CompanyDB.csv'), 'wb')        #open csv file to edit 
            _CompanyDBwriter = csv.writer(_CompanyDB)      #using csv reader and list to create a list of list that are the csv rows
        return _CompanyDBwriter
    elif _readwrite == 'read':
        if os.path.isfile(os.path.join(_databasedir, 'CompanyDB.csv')):
            _CompanyDB = open(os.path.join(_databasedir, 'CompanyDB.csv'))        #open csv file to edit 
            _CompanyDBreader = csv.reader(_CompanyDB)      #using csv reader and list to create a list of list that are the csv rows
            _CompanyDBdata = list(_CompanyDBreader)
        else:
            return "no database found"
        return _CompanyDBdata
def importlisting():
    import csv
    import os
    from config import _importdir, _databasedir
    #selecting Import file will list all files in the imprt directory 
    print('current import directory, to change goto config.py')
    print(_importdir)
    _importlist = os.listdir(_importdir)
    _count = 1
    for _row in _importlist:
        print(str(_count) + " " + str(_row))
        _count += 1
    _importfile = _importlist[input("choose one: ") - 1] 
    _importfileopen = open(os.path.join(_importdir, _importfile))       #open csv file
    _importfilereader = csv.reader(_importfileopen)  #using csv reader to read file
    _importfiledata = list(_importfilereader)       #using csv reader and list to create a list of list that are the csv rows
    return _importfiledata

def PyventoryDBImportFromFile(): #used to add or create a pyventory database from a file.
    for row in importlisting():
        PyventoryDBReadWrite('write').writerow(row) # writing your date to pyventory company database file.

def PyventoryDBcompaireimport(_compaire): #used to comapire with companyDB and only add to pyventoryDB what is already in ComanydB.
    from config import _COMPUTERSERIAL, _COMPUTERASSET, _WIREDMAC, _WIRELESSMAC
    import1 = importlisting()
    print(import1[0:1][0:])
    compairecol = input("what column do you want to compaire the " + _compaire + " with : ")
    
    if isinstance(compairecol, (int, long)) == True:
        for asset in import1:
            for row in CompanyDBReadWrite('read'):   
                if asset[compairecol] == row[_compaire]:
                    print(row)
                    PyventoryDBReadWrite('write').writerow(row) # writing your date to pyventory company database file.
                    break
            else:
                PyventoryDBReadWrite('write').writerow([asset[0], 'missing'])
    else:
        print("plese enter in numbers only")
        PyventoryDBcompaireimport(_compaire) 

def CompanyDBupdate(): #used to create/update the company database file.
    for row in importlisting():
        CompanyDBReadWrite('write').writerow(row) # writing your date to pyventory company database file.

def ListMissingCDB(): # used to compair and list all items missing from CompanyDB that are in Pyventory
    pass

def PyventoryDBFind1Record(_field):
    from config import _COMPUTERSERIAL, _COMPUTERMODEL, _COMPUTERMAKE, _COMPUTERSERIAL,_COMPUTERNAME

    if _field == 1: #search record by Computer Serial Number
        return(CompanyDBReadWrite('read')[0][0-12])
    elif _field == 2:
        return(CompanyDBReadWrite('read')[3][0])
    elif _field == 3:
        return(_COMPUTERMAKE)    
    elif _field == 4:
        return(CompanyDBReadWrite('read')[3][_COMPUTERSERIAL]) 
    elif _field == 5:
        return(CompanyDBReadWrite('read')[3][_COMPUTERNAME])
