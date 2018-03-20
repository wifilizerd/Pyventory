#!/Python27/pythonw.exe
#python 2.7
#Pyventory - 0.6.1
# import all needed libraries
import sys, os, csv

# Gobal Variables
_DEBUG = 0     # 0 = no debuging, 1 =  Print lists on screen, 2 = print Lists to file..

def Logo():                                                     #Just a Cool Heading for the program
    print("\033[1;32m"                                              #set text to green (only works in terminal, python(CMD) and powershell)
            " _______________.___.____   _______________ __________________________ _______________.___.       \n"
            " \______   \__  |   |\   \ /   /\_   _____/ \      \__    ___/\_____  \\\______   \__  |   |       \n"
            "  |     ___//   |   | \   Y   /  |    __)_  /   |   \|    |    /   |   \|       _//   |   |       \n"
            "  |    |    \____   |  \     /   |        \/    |    \    |   /    |    \    |   \\\____   |       \n"
            "  |____|    / ______|   \___/   /_______  /\____|__  /____|   \_______  /____|_  // ______| v0.6.1 \n"
            "            \/                          \/         \/                 \/       \/ \/              "
            "\033[1;37m"                                             #set color of text back to white
           )

def Help(_menu):                                                #The Help Screen- broken down so specified potion can be called were needed.
    if _menu == 'main':                                             #Pyventory Main Menu Help
        print(
            "Pyventory Help. \n"
            "scan       open scan and check function.\n"
            "export     open check and export function.\n"
            "help       open additional info.\n"
            )
    elif _menu == 'scan':                                           #ScanandCheck Help Menu
        print(
            "add        enable taking notes if the recorde is not found in inventory file.\n"
            "notadd     disable taking notes if the recorde is not found in inventory file.\n"
            "ask        ask each time to take notes if the recorde is not found in inventory file.\n"
        )   
    elif _menu == 'export':                                         #CheckandExport Help Menu
        pass

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

def FileBrowser(_extention, _new):                              #Used to select what file to load and create new files if wanted.
    _filelist = os.listdir(".")                                     # list directory to a list
    _count = 0
    _files = []
    for ext in _filelist:
        if ext.endswith(_extention):                                #if file ends with specified extention.
            _files.append(ext)                                      #add file to list (_files)
            print('     ' + str(_count) + ' ' + ext)
            _count += 1
    if _DEBUG > 0:
        print(_files)
    if _new == 1:                                                   #allows user to create a new filename if wanted, however also allows file create restrictions. when set to 0
        print('or type name of new file(no extention)')    
    _filechoose = raw_input('File:')
    if _DEBUG > 0:
        print(_filechoose)
        print(_files[int(_filechoose)])
    if _new == 1:
        if _DEBUG > 0:
            print(_filechoose) in str(range(0, (_count + 1)))
        if str(_filechoose) in str(range(0, (_count + 1))):              #check if user entered number or new file name.
            if 'scanned' in _files[int(_filechoose)]:               #check for existing filename and remove program added charicters on the end of filename
                if _DEBUG > 0:
                    print(_files[int(_filechoose)][:-12])
                return(_files[int(_filechoose)][:-12])
            elif 'notfound' in _files[int(_filechoose)]:
                if _DEBUG > 0:
                    print(_files[int(_filechoose)][:-13])
                return(_files[int(_filechoose)][:-13])
        else:
            return(_filechoose)                                     #returns filename use entered
    else:  
        return(_files[int(_filechoose)])                            #returns filename based on location in list 

def columnselect(_filename):                                    #lists info in CSV file from the first row so user can select the column based on content.
    _row = 0
    _columnchoose = 'n'
    while _columnchoose == 'n':
        print(_row)
        _count = 0
        _INVlist = Convert2List(_filename, 0)
        for asset in _INVlist[int(_row)]:
            print('     ' + str(_count) + ' ' + asset)
            _count += 1
        print("\033[1;32m" + 'Select the Column you wish to use.')      #listing help info of known column from inventory files.
        print('Known Coumns for defult exports ONLY')
        print('0 - Asset tages')
        print('9 - Wired Mac address')
        print('10 - Wireless Mac address')
        print('27 - Room Number')
        print('29 - Serial Number')
        print('n - for a new list if needed info not displayed')
        print("\033[1;37m")
        _columnchoose = raw_input('Column:')
        if _columnchoose.lower() == 'n':
            _row += 1
    return(_columnchoose)

def Counter(_list):
    count = 0
    for i in _list:
        count += 1
    return(count)

def Countroom(_list, _room, _col):
    count = 0
    for l in _list:
        if l[int(_col)] == _room:
            count += 1
    return(count)

def Dupcheck(_list):
    _nodup = []
    for row in _list:
        if row not in _nodup:                                   #checking for duplicates
            _nodup.append(row)    
        else:
            pass
    return(_nodup)

def addinfo(_filename, _scan):                                  #used to gather info about assets that are not found in list then stored for later entery.
    _scan = _scan
    _asset = raw_input('Asset tage:')
    _serial = raw_input('serial #:')
    _type = raw_input('device type: ')
    _make = raw_input('make: ')
    _model = raw_input('model: ')
    _cpu = raw_input('cpu: ')
    _ram = raw_input('ram: ')
    _hdd = raw_input('hard drive:')
    _os = raw_input('OS: ')
    _school = raw_input('school #: ')
    _room = raw_input('room: ')
    _user = raw_input('user: ')
    _compname = raw_input('computer name: ')
    _mac = raw_input('wired MAC: ')
    _wmac =raw_input('wireless MAC: ')
    _installdate = raw_input('install date: ')
    _owner = raw_input('owner: ')
    _usertype = raw_input('user type: ')
    _status = raw_input('status: ')
    _year = raw_input('mtg. year: ')
    _yearrotate = raw_input('year to be rotated: ')
    _rotate = raw_input('eligible for rotation: ')
    _notes = raw_input('Notes: ')
    print("\033[1;37m")
    writefile((_filename),('csv'), (_asset, str(_scan), _serial, _type, _make, _model, _cpu, _ram, _hdd, _os, _school, _room, _user, _compname, _mac, _wmac, _installdate, _owner, _usertype, _status, _year, _yearrotate, _rotate, _notes))

def SCANandCHECK():                                             #Interface for scanning or entering information to check with,``
    # CONFIG                                                        # designed to enter in asset tage and search the inventory file for the tag. 
    _ADD = 2                                                        # also works with Serial numbers.
    _RoomNumber = 'all'
    _Roomcol = ''
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    print("\033[1;32m" + 'Select your Scanned file or create new one.' + "\033[1;37m")
    _Savefile = FileBrowser('.csv', 1)
    if _DEBUG < 1:                                                 
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    print("\033[1;32m" + 'Select your Inventory file.' + "\033[1;37m")
    _INVfile = FileBrowser('.csv', 0)
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    _INVcol = columnselect(_INVfile)
    
    if _DEBUG > 0:
        print(_INVfile)
        print(_INVcol)
        print(_Savefile)    
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
        
    _assetLIST = []
    for row in Convert2List(_INVfile, _INVcol):                     # convert list of lists into a single list of specified column info.
        _assetLIST.append(row[int(_INVcol)].lstrip('0'))
    if (_Savefile + "-scanned.csv") in os.listdir("."):
        _saveLIST = []
        for row in Convert2List(_Savefile + "-scanned.csv", 0):                     
            _saveLIST.append(row[0])
    Logo()
    #http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20CHECK 'SMALL' font
    print("\033[1;32m" + #green
    ' ___  ___   _   _  _                _    ___ _  _ ___ ___ _  __ \n'
    '/ __|/ __| /_\ | \| |  __ _ _ _  __| |  / __| || | __/ __| |/ / \n'
    '\__ | (__ / _ \| .` | / _` |   \/ _` | | (__| __ | _| (__| | <  \n'
    '|___/\___/_/ \_|_|\_| \__,_|_||_\__,_|  \___|_||_|___\___|_|\_\ \n'                                                               
    + "\033[1;37m") #white
    print('')
    print('Ask each time to take notes')
    print('Type "help" for help menu')
    print('press "x" then enter to exit')
    if (_Savefile + "-scanned.csv") in os.listdir("."):             #adding percent complete NEED to CHECK FOR SDUPLICATES
        print("\033[1;33m" + str(Counter(Dupcheck(_saveLIST))) + '/' + str(Counter(Dupcheck(_assetLIST))) + ' Devices Scanned' + "\033[1;37m")
    


    _scan = 0
    while True:                                                     #Start of the entery process this is the loop that will take info and check in the inventory file.
        _scan = raw_input('Scan:')
        if _scan.lower() == 'add':                                  #add command used to turn on adding info if entery is not found.
            _ADD = 1
            print('Taking notes is ENABLED')
        elif _scan.lower() == 'notadd':                             #notadd commadn used to turn off adding info in entery in not found
            if _ADD == 0:
                print('Taking notes is DISABLED')
            else:
                _ADD = 0
                print('Taking notes is DISABLED')
        elif _scan.lower() == 'ask':                                #ask command used to set program to ask user each time a record is not found if info should be added.
            _ADD = 2
            print('Ask each time to take notes')
        elif _scan.lower() == 'help':                               #help commadn used to show the help screen
            Help('scan')
        elif _scan.lower() == 'room':
            if _Roomcol == '':
                _Roomcol = columnselect(_INVfile)
            _RoomList = Convert2List(_INVfile, _Roomcol)
            _Rooms = []
            for room in _RoomList:
                if room[int(_Roomcol)] not in _Rooms:
                    _Rooms.append(room[int(_Roomcol)])
            for r in _Rooms:
                print(r)
            print("\033[1;32m" + " enter 'all' to check all rooms" + "\033[1;37m") #white
            _RoomNumber = raw_input('Room:')
        elif _scan.lstrip('0') in _assetLIST or _scan in _assetLIST:#compaire of entery and inventory info.
            if _RoomNumber == 'all':
                for row in Convert2List(_INVfile, _INVcol):
                    if row[int(_INVcol)] == _scan.lstrip('0') or row[int(_INVcol)] == _scan:
                        print("\033[1;32m" + str(row) + "\033[1;37m")
                        writefile((_Savefile + "-scanned"),'csv', row)
            else:
                for row in Convert2List(_INVfile, _INVcol):
                    if row[int(_INVcol)] == _scan.lstrip('0') or row[int(_INVcol)] == _scan:
                        if row[int(_Roomcol)].upper() == _RoomNumber.upper():
                            print("\033[1;32m" + str(row) + "\033[1;37m")
                            writefile((_Savefile + "-scanned"),'csv', row)
                        else:
                            print("\033[1;33m" + _scan + ' is listed in room ' + str(row[int(_Roomcol)]) + "\033[1;37m")
                            print("\033[1;32m" + str(row) + "\033[1;37m")
                            writefile((_Savefile + "-scanned"),'csv', row)
                            writefile((_Savefile + "-NotFound"),'csv', ([str(_scan), str(row[int(_Roomcol)])]))
                            print("\033[1;33m" + 'Notes add to "NotFound" List.' + "\033[1;37m")

        elif _scan.lower() == 'x':                                  #x commadn used to exit scan and check
            break
        else:
            writefile((_Savefile + "-scanned"),'csv', [_scan])      #add to filename to destiguish different files.
            print("\033[1;31m" + _scan + ' and ' + str(_scan).lstrip('0') + ' not found' + "\033[1;37m")
            if _ADD == 1:
                print("\033[1;33m" 'add information for asset tage ' + _scan)
                addinfo((_Savefile + "-NotFound"), str(_scan))
            elif _ADD == 2:
                _askverify = 0
                while _askverify == 0:
                    print('Do you want to add info (y or n)?')
                    _ask = raw_input(':')
                    if _ask.lower() == 'y':
                        _askverify = 1
                        addinfo((_Savefile + "-NotFound"), _scan)
                    if _ask.lower() == 'n':
                        _askverify = 1
                        break
                            
def CheckandExport():                                           #Interface to Check what records have not been entered/scanned and list all avalable info.
    # CONFIG                                                         
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    print("\033[1;32m" + 'Select your Scanned file.' + "\033[1;37m")
    _scanfile = FileBrowser('.csv', 0)
    if _DEBUG > 0:
        print(_scanfile)
        pause=raw_input('Check:')
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    _scancol = columnselect(_scanfile) 
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    print("\033[1;32m" + 'Select your Inventory file.' + "\033[1;37m")
    _INVfile = FileBrowser('.csv', 0)
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    _INVcol = columnselect(_INVfile)
    if _DEBUG > 0:
        print(_INVfile)
        print(_INVcol)
        print(_scanfile)
        print(_scancol)    
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    Logo()
    #http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20SHOW 'SMALL' font
    print("\033[1;32m" + 
    "   ___ _           _                  _   ___                   _   \n"
    "  / __| |_  ___ __| |__  __ _ _ _  __| | | __|_ ___ __  ___ _ _| |_ \n"
    " | (__| ' \/ -_) _| / / / _` | ' \/ _` | | _|\ \ / '_ \/ _ \ '_|  _|\n"
    "  \___|_||_\___\__|_\_\ \__,_|_||_\__,_| |___/_\_\ .__/\___/_|  \__|\n"   
    "                                                 |_|                "                                                            
    + "\033[1;37m")
    print('')
    print('Please wait, Checking recordes')
    _INVlist = Convert2List(_INVfile, _INVcol)
    _scanlist = Convert2List(_scanfile, _scancol)

    _scancollist = []
    for row in _scanlist:
        if row[int(_scancol)] not in _scancollist:            #checking for duplicates
            _scancollist.append(row[int(_scancol)].lstrip('0'))    
        else:
            pass

    for asset in _INVlist:
        if asset[int(_INVcol)] not in _scancollist:
           writefile((_scanfile[:-12] + "-NotScanned"),('csv'), asset)
        else:
            pass

def Stats():                                                        
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    print("\033[1;32m" + 'Select your Scanned file.' + "\033[1;37m")
    _scanfile = FileBrowser('.csv', 0)
    if _DEBUG > 0:
        print(_scanfile)
        pause=raw_input('Check:')
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    _scancol = columnselect(_scanfile) 
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    print("\033[1;32m" + 'Select your Inventory file.' + "\033[1;37m")
    _INVfile = FileBrowser('.csv', 0)
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    _INVcol = columnselect(_INVfile)
    if _DEBUG < 1:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
    _Roomcol = columnselect(_INVfile)
    _Roomlist = []
    for room in Convert2List(_INVfile, _Roomcol):
        _Roomlist.append(room[int(_Roomcol)])
    _Rooms = Dupcheck(_Roomlist)
    
    
    for i in sorted(_Rooms):
        _assetlist = Convert2List(_INVfile, _Roomcol)
        _savelist = Convert2List(_scanfile, _Roomcol)
        print(i + "      " + str(Countroom(_assetlist, i, _Roomcol)) + '/' + str(Countroom(_savelist, i, _Roomcol)))
        

    # if _DEBUG > 0:
    #     print(_INVfile)
    #     print(_INVcol)
    #     print(_scanfile)
    #     print(_scancol)    
    # if _DEBUG < 1:
    #     if sys.platform == 'win32':
    #         os.system('cls')
    #     elif sys.platform == 'darwin':
    #         os.system('clear')
    # Logo()

def Interface():
    while True:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
        Logo()
        Help('main')
        _interfacemenu = raw_input('Pyventory:')
        if _interfacemenu.lower() == 'scan':
            SCANandCHECK()
        elif _interfacemenu.lower() == 'export':
            CheckandExport()
        elif _interfacemenu.lower() == 'exit' or _interfacemenu.lower() == 'x':
            break

Interface()
# Stats()