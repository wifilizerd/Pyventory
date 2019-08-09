#!/Python27/pythonw.exe
#python 2.7
#Pyventory - 0.6
# import all needed libraries
import sys, os, csv

# Gobal Variables

def writefile(_filename, _extention, _info):                    #setup file to write to.
    _file = _filename + '.' + _extention                               
    _writefile = open(_file, "ab")                                  #'ab'will create file also 'wb' will overwrite everytime the file is opened
    _writefilewriter = csv.writer(_writefile)                       #Setup CSV writer
    _writefilewriter.writerow(_info)                                #write info to _filename given _extention allows to used this def to write to other files types
    _writefile.close()                                              #close file after writing

def CSVReader(_filename):                                       #Setup CSV reader.
    _file = open(_filename, "r")
    return(csv.reader(_file))
  
def Convert2List(_filename, _column):                           #Read data from file and add it to a list.
    _filereader = CSVReader(_filename)
    _filelist = []                                                  #set blank list to recive data
    for row in list(_filereader):
        if row:                                                     #check if there is data on tha row.
            if row[int(_column)] == '':                                  #check if there is data in the field
                pass
            else:
                _filelist.append(row)                       #appedn data to list in UPPER case
    return(_filelist)

def MACcheck(_Mac):                                             #checking for Ethernet MAc address
    for i in _Mac:
        if 'ETH' in i[0].upper():                                   #check if 'ETH'ernet is in the mac address information if so retunr the mac address
            return(i[1])

def WMACcheck(_Mac):                                            #Checking For wireless MAC Address
    for i in _Mac:
        if 'W' in i[0].upper():                                      #check if 'W'ifi is in the mac address information if so retunr the mac address
            return(i[1])

def DeviceType(_Device):                                        #Determining eather Desktop or Laptop baske on model type.
    #Change work look up to list of word to check 
    for i in _Device:
        if "BOOK" in i[0].upper():                                  #Check if 'BOOK' is in the device informaion, if so it is a laptop if not it is a desktop.
            return('Laptop')
        else:
            return('Desktop')

def FindUser(_compname):                                        #Getting username from computer name, or setting student in there is no name.
    if str(_compname[6]) in str(range(0,9)):                        #check if there is a number in place 6 in the computer name is so the computer is a student devices
        return('Student')
    else:
        return(_compname[3:-1])                                     #otherwise the computer is assigned and the username is pulled out of the computer name

def Compress2LIST(_FolderLocation):                             #Used to convert Vertical Date from inventory files to a Horizontal list.
    #0-ComputerName, 1-Serial, 2-Asset, 14-WiFiMac, 15-HWMac        #Notes for setting the column from the pclist
    for i in os.listdir(_FolderLocation):                           #open all files in _folderlocation one at a time read the information and save it to a list for Export2INV
        _file = open(os.path.join(_FolderLocation + i), 'r')
        _filereader = csv.reader(_file)
        _filedata = list(_filereader)
        _pclist = []
        if _DEBUG > 0:                                              #Set _DEGUB to 1 to print list data to the screen 
            print('_filedata')
            print(_filedata)
        if _DEBUG > 1:                                              #set _DEBUG to 2 to save list to a file
            _pclistfile = open('Compress2Listfile.csv', 'ab')
            _pclistfilewriter = csv.writer(_pclistfile)
            _pclistfilewriter.writerow([_filedata[0][1].strip(),_filedata[1][1].strip(),_filedata[2][1].strip(),_filedata[3][1].strip(),_filedata[4][1].strip(),_filedata[5][1].strip(),_filedata[6][1].strip(),_filedata[7][1].strip(),_filedata[8][1].strip(),_filedata[9][1].strip(),_filedata[10][1].strip(),_filedata[11][1][2:].strip(),_filedata[12][1].split('/')[2],_filedata[13][1].strip(),WMACcheck(_filedata[14:]),MACcheck(_filedata[14:])])
        _pclist.append([_filedata[0][1].strip(),_filedata[1][1].strip(),_filedata[2][1].strip(),_filedata[3][1].strip(),_filedata[4][1].strip(),_filedata[5][1].strip(),_filedata[6][1].strip(),_filedata[7][1].strip(),_filedata[8][1].strip(),_filedata[9][1].strip(),_filedata[10][1].strip(),_filedata[11][1][2:].strip(),_filedata[12][1].split('/')[2],_filedata[13][1].strip(),WMACcheck(_filedata[14:]),MACcheck(_filedata[14:])])
    if _DEBUG > 0:                                                  #Set _DEGUB to 1 to print list data to the screen 
        print('_pclist')
        print(_pclist)
    return(_pclist)
            
def NotinINV(_INVfile, _INVcol, _LISTfile, _LISTcol):           #used to compaire lists with inventory and find what is no in inventory. NOT FOR IMPORT INTO INVENTORY.
    #NOTE: Remember the leading 000 can cause problems, need to findout how to check the number including leading 0's
    _LIST = Convert2List(_LISTfile, _LISTcol)
    _INV = Convert2List(_INVfile, _INVcol)
    INVcolumnlist = []
    for row in _INV:                                                #createing list of inventory information for faster checking.
        if _DEGUB > 0:
            print(row[_INVcol].upper(),)
        INVcolumnlist.append(row[_INVcol].upper(),)
    for row in _LIST:
        if row[_LISTcol].upper() not in INVcolumnlist:          #compaireing Lists with serial numbers and writing those whole rows out to CSV
            if _DEBUG > 0:
                print(row)
            writefile('NotInInventory.csv', row) 

def Export4INV(_INVfile, _INVcol, _FolderLocation, _LISTcol):   #used to output what is not in Inventory to a csv file that can be imported into inventory
     #WORK ON: Memory Checking and rounding up.
    _LIST = Compress2LIST(_FolderLocation)
    _INV = Convert2List(_INVfile, _INVcol)                                   #Send files to be converted to a list of lists
    writefile('INVimport.csv', (['ASD Number', 'Computer Name', 'Serial Number', 'Ethernet 2', 'School Number', 'Room #', 'Product Number', 'Purchase Install Date', 'Model', 'Brand/Make', 'owner', 'Manufacture Date', 'Ram', 'Type', 'User Type', 'User', 'Operating System', 'Notes', 'IP Address', 'NetUse', 'Hard Drive Size', 'CPU Speed', 'Equipment Status', 'Eligible for Replacement', 'Classification', 'z_isActive']))
    if _DEBUG > 0:
        print('FMimport')
        print((['ASD Number', 'Computer Name', 'Serial Number', 'Ethernet 2', 'School Number', 'Room #', 'Product Number', 'Purchase Install Date', 'Model', 'Brand/Make', 'owner', 'Manufacture Date', 'Ram', 'Type', 'User Type', 'User', 'Operating System', 'Notes', 'IP Address', 'NetUse', 'Hard Drive Size', 'CPU Speed', 'Equipment Status', 'Eligible for Replacement', 'Classification', 'z_isActive']))
    for row in _LIST:
        if row[int(_LISTcol)].upper() not in _INV:                       #compaire items and write records to files
            if _DEBUG > 0:
                print(([row[2],row[0],row[1],'' if row[13] == 'None' else row[13],row[0][:3],row[3],'',row[5],row[7],row[7][0:2],row[4],row[12][5:],row[10],DeviceType(row[7]),'Student' if row[0][6] in str(range(0,10))  else 'Teacher',FindUser(row[0]),row[9][10:-10],'','DHCP','DATA',row[11],row[8],'Active','Yes' if row[4].upper() == 'TECHNOLOGY' else 'No','Inventory','1']))
            writefile('INVimport.csv', ([row[2],row[0],row[1],'' if row[13] == 'None' else row[13],row[0][:3],row[3],'',row[5],row[7],row[7][0:2],row[4],row[12][5:],row[10],DeviceType(row[7]),'Student' if str(row[0][6]) in range(0,10)  else 'Teacher',FindUser(row[0]),row[9][10:-10],'','DHCP','DATA',row[11],row[8],'Active','Yes' if row[4].upper() == 'TECHNOLOGY' else 'No','Inventory','1']))
        else:
            pass
