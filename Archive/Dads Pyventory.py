#!/Python27/pythonw.exe
#1/bin/python
#python 2.7
#Pyventory - 0.6.3
# import all needed libraries
import sys, os, csv

# Gobal Variables
_DEBUG = 0     # 0 = no output, 1 =  Standered Output, 2 = Detail output, 3 = Basic Debug, 4 = pause Debug , 5 = everything,

# _LABEL  = 0
# _COL    = 1

INV_ROW = {
    "Asset Tag":    0,
    "Device Name":  3,
    "Wired Mac":    9,
    "Wireless Mac": 10,
    "Room":         27,
    "School":       28,
    "Serial":       29,
    "School Desc":  42
}

    # "Asset":              0,
    # "Make":               1,
    # "Class":              2,    # Inventory, Infrastructure, Printers
    # "Name":               3,    # Device Name
    # "Cpu":                4,
    # "Modified by":        5,
    # "Modified Date":      6,
    # "Rotation Eligible":  7,      # Yes/No, Eligible for Rotation
    # "Status":             8,      # Active, Condemned, Surplus
    # "Wired Mac Addr":     9,
    # "Wireless Mac Addr":  10,
    # "Server Mac Addr":    11,
    # "Hdd":                12,
    # "Tag":                13,
    # "IP Addr":            14,
    # "MDM Date":           15,
    # "Mfg Year":           16,
    # "Model":              17,
    # "Creator":            18,
    # "Create Date":        19,
    # "VLAN":               20,
    # "Notes":              21,
    # "OS":                 22,
    # "Owner":              23,
    # "Product #":          24,
    # "InstallDate":        25,
    # "Ram":                26,
    # "Room #":             27,
    # "School #":           28,
    # "Serial #":           29,
    # "Unknown":            30,
    # "MDM Purchased":      31,     # Yes/No
    # "Device Type":        32,     # Laptop, Chromebook, etc
    # "Username":           33,
    # "UserType":           34,     # Student, Teacher, Admin, Etc
    # "Rotation Year":      35,     # Year to be Rotated
    # "School Name":        36,     # School Name, Scan File Format
    # "School Desc":        42,     # School Name, Inventory Format 

# -------------------------------------------------------------------------------------------------------------------------------
def Logo(self, _logo='main', _clr=None):              #Just a Cool Heading for the program
    self.dprint(4, self._HEADING, "Routine: Logo({0}, {1})".format(_title, _clr), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    if _logo == 'main':
        logotxt = 
            " _______________.___.____   _______________ __________________________ _______________.___.\n"
            " \______   \__  |   |\   \ /   /\_   _____/ \      \__    ___/\_____  \\\______   \__  |   |\n"
            "  |     ___//   |   | \   Y   /  |    __)_  /   |   \|    |    /   |   \|       _//   |   |\n"
            "  |    |    \____   |  \     /   |        \/    |    \    |   /    |    \    |   \\\____   |\n"
            "  |____|    / ______|   \___/   /_______  /\____|__  /____|   \_______  /____|_  // ______| v0.6.2\n"
            "            \/                          \/         \/                 \/       \/ \/\n\n"
    elif _logo == 'scan_check':
        logotxt = 
        " ___  ___   _   _  _                _    ___ _  _ ___ ___ _  __ \n"
        "/ __|/ __| /_\ | \| |  __ _ _ _  __| |  / __| || | __/ __| |/ / \n"
        "\__ | (__ / _ \| .` | / _` |   \/ _` | | (__| __ | _| (__| | <  \n"
        "|___/\___/_/ \_|_|\_| \__,_|_||_\__,_|  \___|_||_|___\___|_|\_\ \n"

    elif _logo == 'check_export':
        logotxt = 
        "   ___ _           _                  _   ___                   _   \n"
        "  / __| |_  ___ __| |__  __ _ _ _  __| | | __|_ ___ __  ___ _ _| |_ \n"
        " | (__| ' \/ -_) _| / / / _` | ' \/ _` | | _|\ \ / '_ \/ _ \ '_|  _|\n"
        "  \___|_||_\___\__|_\_\ \__,_|_||_\__,_| |___/_\_\ .__/\___/_|  \__|\n"
        "                                                 |_|                \n"
    
    self.dprint(0, self._MENU, logotxt, _clr)
           
# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def Help(self, _menu):                                                #The Help Screen- broken down so specified potion can be called were needed.
    self.dprint(4, self._HEADING, "Routine: Help({0})".format(_menu), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    if _menu == 'main':                                             #Pyventory Main Menu Help
        helptxt = 
            "Pyventory Help. \n",
            "scan       open scan and check function.\n",
            "export     open check and export function.\n",
            "help       open additional info.\n",

    elif _menu == 'scan':                                           #ScanandCheck Help Menu
        helptxt = 
            "Scan Help. \n",
            "add        enable taking notes if the recorde is not found in inventory file.\n",
            "notadd     disable taking notes if the recorde is not found in inventory file.\n",
            "ask        ask each time to take notes if the recorde is not found in inventory file.\n",
            "room       set room number to check.\n",

    elif _menu == 'export':                                         #CheckandExport Help Menu
        helptxt = 
            "Export Help. \n",
            "           To be created\n",

    elif _menu == 'help':
        helptxt = 
            "\tAsk each time to take notes\n"
            "\tType 'help' for help menu\n"
            "\tPress 'x' then enter to exit\n"


    elif _menu == 'check':
        helptxt = 'Please wait, Checking records'

    elif _menu == 'column':                                         #CheckandExport Help Menu
            "Column Help. \n",
            "Select the Column you wish to use.\n",                    #listing help info of known column from inventory files.
            "Known Columns for default exports ONLY\n",

            "{0:2} - {1}\n".format(INV_ROW["Asset Tag"], "Asset Tag")

            "{0:2} - {1}\n".format(INV_ROW["Asset Tag"][_COL], INV_ROW["Asset Tag"][_LABEL])
            "{0:2} - {1}\n".format(INV_ROW["Wired Mac"][_COL], INV_ROW["Wired Mac"][_LABEL])
            "{0:2} - {1}\n".format(INV_ROW["Wireless Mac"][_COL], INV_ROW["Wireless Mac"][_LABEL])
            "{0:2} - {1}\n".format(INV_ROW["Room #"][_COL], INV_ROW["Room #"][_LABEL])
            "{0:2} - {1}\n".format(INV_ROW["Serial #"][_COL], INV_ROW["Serial #"][_LABEL])
            "{0:2} - {1}\n".format("n", "for a new list if needed info not displayed")

            # "0 - Asset tags\n",
            # "9 - Wired Mac address\n",
            # "10 - Wireless Mac address\n",
            # "27 - Room Number\n",
            # "29 - Serial Number\n",
            # "n - for a new list if needed info not displayed\n",


    self.dprint(0, self._MENU, helptxt)

# -------------------------------------------------------------------------------------------------------------------------------
_TC = {
    "_GREEN":   "\033[1;32m",       # Green
    "_RED":     "\033[1;31m",       # Red
    "_YELLOW":  "\033[1;33m",       # Yellow
    "_RESET":   "\033[1;37m"        # White
}

def p_print(self, _debug, _color, _string):
    # -------------------------------------------------------------------------------------------------------------------------------
    # if _debug <= _DEBUG:
    if 1:
        print(_color + _string + _TC["_RESET"])
        if _debug == 4:
            raw_input('Waiting...')
        

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
_RESET = "\033[0;0m"
_WHITE = "\033[0;97m"
_RED = "\033[0;31m"
_GREEN = "\033[0;32m"
_YELLOW = "\033[0;33m"
_BLUE = "\033[0;34m"
_MAGENTA = "\033[0;35m"
_CYAN = "\033[0;36m"

_MENU = _BLUE
_HEADING = _GREEN
_TITLE = _GREEN
_DICT = _CYAN
_INPUT = _WHITE
_OUTPUT = _BLUE
_GOOD = _GREEN
_BAD = _RED
_WARNING = _YELLOW
_ERROR = _RED
# -------------------------------------------------------------------------------------------------------------------------------

def dprint(self, _level=0, _type="\033[0;0m", _text=None, _clr=None):
    # Display text message according to _level parameter
    # If DEBUG = 4 AND _type = HEADING progress will wait for ENTER Key at Header Displays
    # _level = 1 min - 5 max, _type = Text style (color)
    # -------------------------------------------------------------------------------------------------------------------------------

    if _clr:
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')

    if (_level <= self.DEBUG):
        print _type, _text, self._RESET
        if self.text:
            if _level == 4 and self.DEBUG_LEVEL == 4 and _type == self._HEADING:
                raw_input("Press Enter to Continue ...")
# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def is_command(self, _prompt, _command):
    # return True if response[0] == _command
    # return False if _response[0] does not match requested _command
    self.dprint(4, self._HEADING, "Routine: is_command({0}, {1})".format(_prompt, _command), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    _response = raw_input("{0}: ".format(_prompt))

    if _response[0].upper() == _command[0].upper():
        return(True)
    else:
        return(False)

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def print_row(self, _outfile, _row):
    self.dprint(4, self._HEADING, "Routine: print_row({0}, {1})".format(_outfile, _row), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    self.dprint(0, self._MENU, "{0:12}:{1}".format(INV_ROW["Asset Tag"][_LABEL], INV_ROW["Asset Tag"][_COL]))
    self.dprint(0, self._MENU, "{0:12}:{1}".format(INV_ROW["Serial #"][_LABEL], INV_ROW["Serial #"][_COL]))
    self.dprint(0, self._MENU, "{0:12}:{1}".format(INV_ROW["Device Name"][_LABEL], INV_ROW["Device Name"][_COL]))
    self.dprint(0, self._MENU, "{0:12}:{1}".format(INV_ROW["Room #"][_LABEL], INV_ROW["Room #"][_COL]))
    self.dprint(0, self._MENU, "{0:12}:{1}".format(INV_ROW["Wired Mac"][_LABEL], INV_ROW["Wired Mac"][_COL]))
    self.dprint(0, self._MENU, "{0:12}:{1}".format(INV_ROW["Wireless Mac"][_LABEL], INV_ROW["Wireless Mac"][_COL]))
    self.dprint(0, self._MENU, "{0:12}:{1} {2}".format(INV_ROW["School"][_LABEL], INV_ROW["School"][_COL], INV_ROW["School_Desc"][_COL]))
    writefile(_outfile, 'csv', _row)

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------

def Counter(self, _list):
    self.dprint(4, self._HEADING, "Routine: Counter({0})".format(_list), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    # count = 0
    # for i in _list:
    #     count += 1

    count = _list.count()
    count = count(_list)
    count = len(_list)
    return(count)

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def Countroom(self, _list, _room, _col):
    self.dprint(4, self._HEADING, "Routine: Countroom({0},{1},{2})".format(_list, _room, _col), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    count = 0
    for l in _list:
        if l[int(_col)] == _room:
            count += 1
    return(count)

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def Dupcheck(self, _list):
    self.dprint(4, self._HEADING, "Routine: Dupcheck({0})".format(_list), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    _nodup = []
    for row in _list:
        if row not in _nodup:                                   #checking for duplicates
            _nodup.append(row)    
        # else:
            # pass
    return(_nodup)

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def ScanInRoom(self, _inv,_scan, _room):
    self.dprint(4, self._HEADING, "Routine: ScanInRoom({0},{1},{2})".format(_inv, _scan, _room), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    count = 0
    _scanlist = []
    for asset in _scan:
        _scanlist.append(asset[0])
    for row in _inv:
        # if row[27] == _room:
        if row[INV_ROW["Room #"][_COL]] == _room:
            if row[0] in _scanlist:
                count += 1
    return(count)

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def writefile(self, _filename, _extention, _info):                    #setup file to write to.
    self.dprint(4, self._HEADING, "Routine: writefile({0},{1},{2})".format(_filename, _extension, _info), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    _file = _"{0}.{1}".format(filename, _extention)                               
    _writefile = open(_file, "ab")                                  #'ab'will create file also 'wb' will overwrite everytime the file is opened
    _writefilewriter = csv.writer(_writefile)                       #Setup CSV writer
    _writefilewriter.writerow(_info)                                #write info to _filename given _extention allows to used this def to write to other files types
    _writefile.close()                                              #close file after writing

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def CSVReader(self, _filename):                                       #Setup CSV reader.
    self.dprint(4, self._HEADING, "Routine: CSVReader({0})".format(_filename), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    _file = open(_filename, "rU")
    return(csv.reader(_file))
  
# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def Convert2List(self, _filename, _column):                               # Read data from file and add it to a list.
    self.dprint(4, self._HEADING, "Routine: Convert2List({0},{1})".format(_filename, _column, 0))
    # -------------------------------------------------------------------------------------------------------------------------------

    _filereader = CSVReader(_filename)
    _filelist = []                                                  # set blank list to recive data
    for row in list(_filereader):
        if row:                                                     # check if there is data on tha row.
            if row[_column]:                                        # check if there is data in the field
                _filelist.append(row)                               # append data to list in UPPER case
            # if row[int(_column)] == '':                           # check if there is data in the field
            #     pass
            # else:
            #     _filelist.append(row)                             # append data to list in UPPER case
    return(_filelist)

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def FileBrowser(self, _extention, _new):                              #Used to select what file to load and create new files if wanted.
    self.dprint(4, self._HEADING, "Routine: FileBrowser({0},{1})".format(_extension, _new), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    _filelist = os.listdir(".")                                     # list directory to a list
    _count = 0
    _files = []

    for ext in _filelist:
        if ext.endswith(_extention):                                #if file ends with specified extention.
            _files.append(ext)                                      #add file to list (_files)
            self.dprint(0, self._MENU, "\t{0} {1}",format(_count, ext), 0)
            _count += 1
    self.dprint(0, self._MENU, _files, 0)

    if _new == 1:                                                   #allows user to create a new filename if wanted, however also allows file create restrictions. when set to 0
        self.dprint(0, self._MENU, "or enter name of new file(no extention)", 0)
    _filechoose = raw_input('File:')

    self.dprint(0, self._MENU, _filechoose, 0)
    self.dprint(0, self._MENU, _files[int(_filechoose)], 0)
    if _new == 1:
        print(_filechoose) in str(range(0, (_count + 1)))
        if str(_filechoose) in str(range(0, (_count + 1))):              #check if user entered number or new file name.
            if 'scanned' in _files[int(_filechoose)]:               #check for existing filename and remove program added charicters on the end of filename
                self.dprint(0, self._MENU, _files[int(_filechoose)][:-12], 0)
                return(_files[int(_filechoose)][:-12])
            elif 'notfound' in _files[int(_filechoose)]:
                self.dprint(0, self._MENU, _files[int(_filechoose)][:-13], _clr)
                return(_files[int(_filechoose)][:-13])
        else:
            return(_filechoose)                                     #returns filename use entered
    else:  
        return(_files[int(_filechoose)])                            #returns filename based on location in list 

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def columnselect(self, _filename):                                    #lists info in CSV file from the first row so user can select the column based on content.
    self.dprint(4, self._HEADING, "Routine: columnselect({0})".format(_filename), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    _row = 0
    _columnchoose = 'n'

    while _columnchoose == 'n':
        _count = 0
        _INVlist = Convert2List(_filename, 0)
        for asset in _INVlist[int(_row)]:
            self.dprint(0, self._MENU, "{0:6} {1}".format(_count, asset), 0)
            _count += 1

        Help('column')

        _columnchoose = raw_input('Column:')
        if _columnchoose.lower() == 'n':
            _row += 1
    return(_columnchoose)

# -------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------
def addinfo(self, _filename, _scan):                                  #used to gather info about assets that are not found in list then stored for later entery.
    self.dprint(4, self._HEADING, "Routine: addinfo({0},{1})".format(_filename, _scan), 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    # _scan = _scan
    _asset = raw_input('Asset tag:')
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

    self.dprint(5, self._MENU, "Clear the Screen", 1)
    writefile((_filename),('csv'), (_asset, str(_scan), _serial, _type, _make, _model, _cpu, _ram, _hdd, _os, _school, _room, _user, _compname, _mac, _wmac, _installdate, _owner, _usertype, _status, _year, _yearrotate, _rotate, _notes))

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def SCANandCHECK(self, ):                                             #Interface for scanning or entering information to check with,``
    self.dprint(4, self._HEADING, "routine: SCANandCHECK()", 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    # CONFIG                                                        # designed to enter in asset tage and search the inventory file for the tag. 
    _ADD = 2                                                        # also works with Serial numbers.
    _RoomNumber = 'all'
    _Roomcol = ''

    self.dprint(0, self._MENU, "Select your Scanned file or create new one")

    _Savefile = FileBrowser('.csv', 1)
    _Scanfile = "{0}-scanned.csv".format(_Savefile)
    _Notfoundfile = "{0}-NotFound.csv".format(_Savefile)
    self.dprint(0, self._MENU, "Select your Inventory file.")

    _INVfile = FileBrowser('.csv', 0)
    self.dprint(5, self._MENU, "Clear the Screen", 1)
    _INVcol = 0                                                     # Original Code: columnselect(_INVfile)
    
    self.dprint(3, self._MENU, "INVfile -".format(_INVfile))
    self.dprint(3, self._MENU, "INVCol -".format(_INVCol))
    self.dprint(3, self._MENU, "Savefile -".format(_Savefile))

    self.dprint(5, self._MENU, "Clear the Screen", 1)

    _assetLIST = []
    for row in Convert2List(_INVfile, _INVcol):                     # convert list of lists into a single list of specified column info.
        _assetLIST.append(row[int(_INVcol)].lstrip('0'))
    if (_Scanfile) in os.listdir("."):
        _saveLIST = []
        for row in Convert2List(_Scanfile, 0):                     
            _saveLIST.append(row[0])

    Logo("main", 1)         # Just a Cool Heading for the program
    Logo("scan_check", 0)
    Help("help", 0)

    if (_Scanfile) in os.listdir("."):             #adding percent complete NEED to CHECK FOR DUPLICATES
        self.dprint(0, self._MENU, "{0}/{1} Devices Scanned".format(Counter(Dupcheck(_saveLIST)), Counter(Dupcheck(_assetLIST)), ), 0)

    _scan = 0
    while True:
        # elif is_command(_prompt, "H)elp"):
        _RoomNumber = "all"                                                     #Start of the entery process this is the loop that will take info and check in the inventory file.
        _scan = raw_input("Scan - {0}:".format(_RoomNumber))
        if _scan.lower() == 'add':                                  #add command used to turn on adding info if entery is not found.
            _ADD = 1
            self.dprint(3, self._MENU, "Taking notes is ENABLED")
        elif _scan.lower() == 'notadd':                             #notadd commadn used to turn off adding info in entery in not found
            if _ADD == 0:
            self.dprint(3, self._MENU, "Taking notes is DISABLED")
            else:
                _ADD = 0
                self.dprint(3, self._MENU, "Taking notes is DISABLED")
        elif _scan.lower() == 'ask':                                #ask command used to set program to ask user each time a record is not found if info should be added.
            _ADD = 2
            self.dprint(3, self._MENU, "Ask each time to take notes")
        elif _scan.lower() == 'help':                               #help commadn used to show the help screen
            Help('scan')
        elif _scan.lower() == 'room':
            _Roomcol = INV_ROW["Room #"][_COL]                     # Original Code: columnselect(_INVfile)
            # _Roomcol = 27                                         # Original Code: columnselect(_INVfile)
            _RoomList = Convert2List(_INVfile, _Roomcol)
            _Rooms = []
            for room in _RoomList:
                if room[int(_Roomcol)].upper() not in _Rooms:
                    _Rooms.append(room[int(_Roomcol)].upper())
            for r in _Rooms:
                self.dprint(3, self._MENU, "{0}".format(r))

            self.dprint(3, self._MENU, "Enter 'all' to check all rooms")
            _RoomNumber = raw_input('Room:')

        elif _scan.lstrip('0') in _assetLIST or _scan in _assetLIST:        #compare of entry and inventory info.
            if _RoomNumber.upper() == 'ALL':
                for row in Convert2List(_INVfile, _INVcol):
                    if row[int(_INVcol)] == _scan.lstrip('0') or row[int(_INVcol)] == _scan:
                        print_row(_Scanfile, row[0])
            else:
                for row in Convert2List(_INVfile, _INVcol):
                    if row[int(_INVcol)] == _scan.lstrip('0') or row[int(_INVcol)] == _scan:
                        if row[int(_Roomcol)].upper() == _RoomNumber.upper():
                            print_row(_Scanfile, row[0])
                        else:
                            print_row(_Scanfile, row[0])
                            writefile(_Notfoundfile,'csv', ([str(_scan), str(_RoomNumber.upper())]))
                            self.dprint(1, self._MENU, "Notes add to 'NotFound' List.")

        elif _scan.upper() == 'X' or _scan.upper() == 'EXIT':                            #x command used to exit scan and check
            break
        else:
            writefile(_Scanfile,'csv', [_scan])      #add to filename to destiguish different files.
            self.dprint(3, self._MENU, "{0} and {1} not found".format(scan,_scan).lstrip('0'))
            if _ADD == 1:
                self.dprint(3, self._MENU, "Add information for asset tag")
                addinfo(_Notfoundfile, str(_scan))
            elif _ADD == 2:
                _askverify = 0
                while _askverify == 0:
                    self.dprint(3, self._MENU, "Do you want to add info (y or n)?")
                    _ask = raw_input(':')
                    if _ask.lower() == 'y':
                        _askverify = 1
                        addinfo(_Notfoundfile, _scan)
                    elif _ask.lower() == 'n':
                        _askverify = 1
                        break

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def CheckandExport(self, ):                                           #Interface to Check what records have not been entered/scanned and list all avalable info.
    self.dprint(4, self._HEADING, "Routine: CheckandExport()", 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    # CONFIG                                                         
    self.dprint(3, self._MENU, "Select your Scanned file.")

    _scanfile = FileBrowser('.csv', 0)
    NotScannedfile = "{0}-NotScanned".format(_scanfile)

    if _DEBUG > 0:
        self.dprint(0, self._MENU, _scanfile, 0)
        pause=raw_input('Check:')

    self.dprint(5, self._MENU, "Clear the Screen", 1)

    _scancol = 0                     # columnselect(_scanfile) 
    self.dprint(0, self._MENU, "Select your Inventory file.")

    _INVfile = FileBrowser('.csv', 0)
    self.dprint(5, self._MENU, "Clear the Screen", 1)

    _INVcol = 0                      # columnselect(_INVfile)
    self.dprint(3, self._MENU, _INVfile, 0)
    self.dprint(3, self._MENU, _INVcol, 0)
    self.dprint(3, self._MENU, _scanfile, 0)
    self.dprint(3, self._MENU, _scancol, 0)
    self.dprint(5, self._MENU, "Clear the Screen", 1)


    Logo("main", 1)         # Just a Cool Heading for the program
    Logo("check_export", 0)
    Help("Check", 0)

    _INVlist = Convert2List(_INVfile, _INVcol)
    _scanlist = Convert2List(_scanfile, _scancol)

    _scancollist = []
    for row in _scanlist:
        if row[int(_scancol)] not in _scancollist:            #checking for duplicates
            _scancollist.append(row[int(_scancol)].lstrip('0'))    
        # else:
            # pass

    for asset in _INVlist:
        if asset[int(_INVcol)] not in _scancollist:
           writefile((_NotScannedfile),('csv'), asset)
        # else:
            # pass

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def Stats(self, ):                                                        
    self.dprint(4, self._HEADING, "Routine: Stats()", 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    #CONFIG
    self.dprint(0, self._MENU, "Select your Scanned file.", 1)

    _scanfile = FileBrowser('.csv', 0)
    self.dprint(1, self._MENU, _scanfile, 1)

    pause=raw_input('Check:')
    self.dprint(5, self._MENU, "Clear the Screen", 1)

    _scancol = 0 
    self.dprint(5, self._MENU, "Select your Inventory file.", 1)

    _INVfile = FileBrowser('.csv', 0)
    # self.dprint(5, self._MENU, "Clear the Screen", 1)

    _INVcol = 0
    self.dprint(5, self._MENU, "Clear the Screen", 1)

    # _Roomcol = 27
    _Roomcol = INV_ROW["Room #"][_COL]
    _Roomlist = []
    for room in Convert2List(_INVfile, _Roomcol):
        _Roomlist.append(room[int(_Roomcol)])
    _Rooms = Dupcheck(_Roomlist)
    
    for room in sorted(_Rooms):
        _assetlist = Convert2List(_INVfile, _Roomcol)
        _savelist = Convert2List(_scanfile, _scancol)
        _percent = float(int(ScanInRoom(_assetlist,_savelist,room)))/int(Countroom(_assetlist, room, _Roomcol))*100
        # _statistics = room + "  " + str(ScanInRoom(_assetlist,_savelist,room)) + '/' + str(Countroom(_assetlist, room, _Roomcol))+ ' ' + str("%"+str(float(int(ScanInRoom(_assetlist,_savelist,room)))/int(Countroom(_assetlist, room, _Roomcol))*100))
        _c = "_YELLOW"
        if _percent <= 25.0:
            _c = "_RED"
        elif _percent == 100.0:
            _c = "_GREEN"
        p_print(1, _TC[_c], '{0:16} - {1:>3}/{2:3} {3:.0f}%'.format(room, str(ScanInRoom(_assetlist,_savelist,room)), str(Countroom(_assetlist, room, _Roomcol)), float(int(ScanInRoom(_assetlist,_savelist,room)))/int(Countroom(_assetlist, room, _Roomcol))*100))
        p_print(2, _TC[_c], '{0:16} - {1:>3}/{2:3} {3:.0f}%'.format(room, str(ScanInRoom(_assetlist,_savelist,room)), str(Countroom(_assetlist, room, _Roomcol)), float(int(ScanInRoom(_assetlist,_savelist,room)))/int(Countroom(_assetlist, room, _Roomcol))*100))

    # Logo("main", 1)         # Just a Cool Heading for the program

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
def Interface(self, ):
    self.dprint(4, self._HEADING, "Routine: Interface()", 0)
    # -------------------------------------------------------------------------------------------------------------------------------

    while True:
        Logo("main", 1)         # Just a Cool Heading for the program
        Help('main')
        _interfacemenu = raw_input('Pyventory:')
        if _interfacemenu.lower() == 'scan':
            SCANandCHECK()
        elif _interfacemenu.lower() == 'export':
            CheckandExport()
        elif _interfacemenu.lower() == 'stats':
            Stats()
        elif _interfacemenu.lower() == 'exit' or _interfacemenu.lower() == 'x':
            break

# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
# Interface()
main(self)
    self.dprint(4, self._HEADING, "Routine: main()", 0)
    # -------------------------------------------------------------------------------------------------------------------------------
    while raw_input('Check:') not in ('x', 'X'):
        Logo("main", 1)         # Just a Cool Heading for the program
        Stats()

# -------------------------------------------------------------------------------------------------------------------------------
