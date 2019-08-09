#!/Python27/pythonw.exe
#1/bin/python
#python 3.7
#Pyventory - 0.6.4
# import all needed libraries
import sys, os, csv 

# Gobal Variables
_DEBUG = 2          # 0 = no output, 1 =  Standered Output, 2 = Detail output, 3 = Basic Debug, 4 = pause Debug , 5 = everything,
InventoryFile = ""
ScannedFile =  ""
# Direcotries                                           # Directories
_TC = {                                                 # COLOR List
    # http://ozzmaker.com/add-colour-to-text-in-python/
                                        # TExT STYLE/TEXT COLOR/BG COLOR
    "_HEADING": "\033[4;37;40m",        # Underline/White/Black
    "_WARNING": "\033[0;30;43m",        # Bold/Black/Yellow
    "_ERROR":   "\033[1;37;41m",        # Bold/White/Red
    "_INFO":    "\033[1;36;40m",        # Bold/Cyan/Black
    "_GREEN":   "\033[1;32;40m",        # Bold/Green/Black
    "_RED":     "\033[1;31;40m",        # Bold/Red/Black
    "_YELLOW":  "\033[1;33;40m",        # Bold/Yellow/Black
    "_RESET":   "\033[0;37;40m",        # No Effect/White/Black
    "_TEST":    "\033[1;31;40m"         # Testing
        }
_INV_ROW = {                                            # CSV Inventory Column Numbers
    "Asset":              0,
    "Make":               1,
    "Class":              2,        # Inventory, Infrastructure, Printers
    "Name":               3,        # Device Name
    "Cpu":                4,
    "Modified by":        5,
    "Modified Date":      6,
    "Rotation Eligible":  7,        # Yes/No, Eligible for Rotation
    "Status":             8,        # Active, Condemned, Surplus
    "Wired Mac Addr":     9,
    "Wireless Mac Addr":  10,
    "Server Mac Addr":    11,
    "Hdd":                12,
    "Tag":                13,
    "IP Addr":            14,
    "MDM Date":           15,
    "Mfg Year":           16,
    "Model":              17,
    "Creator":            18,
    "Create Date":        19,
    "VLAN":               20,
    "Notes":              21,
    "OS":                 22,
    "Owner":              23,
    "Product #":          24,
    "InstallDate":        25,
    "Ram":                26,
    "Room #":             27,
    "School #":           28,
    "Serial #":           29,
    "Unknown":            30,
    "MDM Purchased":      31,     # Yes/No
    "Device Type":        32,     # Laptop, Chromebook, etc
    "Username":           33,
    "UserType":           34,     # Student, Teacher, Admin, Etc
    "Rotation Year":      35,     # Year to be Rotated
    "School Name":        36,     # School Name, Scan File Format
    "School Desc":        42,     # School Name, Inventory Format 
    }
_Schools = {                                            # Directory of all Locations and codes
    "Administration Bldg." : "99",
    "Alpine Elementary School" : "103",
    "American Fork High School" : "704",
    "American Fork Jr. High School" : "405",
    "Aspen Elementary School" : "107",
    "ATEC" : "819",
    "Barratt Elementary School" : "112",
    "Belmont Elementary" : "114",
    "Black Ridge Elementary" : "115",
    "Bonneville Elementary School" : "117",
    "Brookhaven Elementary" : "203",
    "Business Services" : "96",
    "Canyon View Junior High School" : "411",
    "Cascade Elementary School" : "121",
    "Cedar Ridge Elementary School" : "123",
    "Cedar Valley  Elementary School" : "125",
    "Cedar Valley High School" : "721",
    "Central Elementary School" : "129",
    "Cherry Hill Elementary School" : "134",
    "Clear Creek Camp" : "806",
    "CTE" : "99",
    "Dan Peterson School" : "810",
    "Data Services" : "97",
    "Deerfield Elementary School" : "138",
    "District Media Center" : "95",
    "Dry Creek Elementary" : "139",
    "Eagle Valley Elementary School" : "141",
    "Eaglecrest Elementary School" : "140",
    "East Shore Online High School (Adult Ed)" : "790",
    "East Transportation Department" : "85",
    "Educational Services" : "92",
    "Foothill Elementary School" : "144",
    "Forbes Elementary School" : "145",
    "Fox Hollow Elementary School" : "147",
    "Freedom Elementary School" : "148",
    "Frontier Middle School" : "417",
    "Geneva Elementary School" : "156",
    "Greenwood Elementary School" : "161",
    "Grovecrest Elementary School" : "166",
    "Harvest Elementary School" : "170",
    "Hidden Hollow Elementary School" : "171",
    "Highland Elementary School" : "172",
    "Hillcrest Elementary School" : "175",
    "Holbrooke Farms Elementary" : "113",
    "Horizon School" : "808",
    "Human Resources" : "94",
    "Lakeridge Junior High School" : "423",
    "Legacy Elementary School" : "183",
    "Lehi Elementary School" : "187",
    "Lehi High School" : "735",
    "Lehi Junior High School" : "441",
    "Lindon Elementary School" : "191",
    "Lone Peak High School" : "737",
    "Manila Elementary School" : "196",
    "Meadow Elementary School" : "200",
    "Mount Mahogany Elementary School" : "204",
    "Mountain Ridge Junior High School" : "494",
    "Mountain Trails Elementary School" : "205",
    "Mountain View High School" : "739",
    "North Point Elementary School" : "207",
    "Northridge Elementary School" : "209",
    "Nutrition Services Department" : "98",
    "Oak Canyon Junior High School" : "485",
    "Orchard Elementary School" : "212",
    "Orem Elementary School" : "215",
    "Orem High School" : "754",
    "Orem Junior High School" : "459",
    "Physical Facilities Department" : "83",
    "Pleasant Grove High School" : "779",
    "Pleasant Grove Junior High School" : "478",
    "Polaris High School" : "782",
    "Pony Express Elementary School" : "217",
    "Purchasing Department" : "89",
    "Ridgeline Elementary School" : "218",
    "River Rock Elementary" : "201",
    "Riverview Elementary School" : "219",
    "Rocky Mountain Elementary School" : "220",
    "Sage Hills Elementary School" : "222",
    "Saratoga Shores Elementary School" : "223",
    "Scera Park Elementary School" : "226",
    "Sego Lily Elementary School" : "232",
    "Sharon Elementary School" : "237",
    "Shelley Elementary School" : "242",
    "Skyridge High School" : "785",
    "Snow Springs Elementary School" : "247",
    "Special Education" : "93",
    "Springside Elementary" : "202",
    "Student Services" : "82",
    "Summit Program" : "792",
    "Suncrest Elementary School" : "253",
    "Technology Department" : "91",
    "Thunder Ridge Elementary School" : "256",
    "Timberline Middle School" : "488",
    "Timpanogos High School" : "786",
    "Traverse Mountain Elementary School" : "258",
    "Valley View Elementary School" : "264",
    "Vineyard Elementary School" : "271",
    "Vista Heights Middle School" : "490",
    "West Transportation" : "86",
    "Westfield Elementary School" : "275",
    "Westlake High School" : "789",
    "Westmore Elementary School" : "277",
    "Willowcreek Middle School" : "496",
    "Windsor Elementary School" : "286"   
    }
# Headings                                              # Headings
def Logo(_head):                                        # Used to call the logo and headings for the UI.
    if _head.upper() == 'MAIN':
        p_print(1, _TC['_GREEN'], 
            " _______________.___.____   _______________ __________________________ _______________.___.       \n"
            " \______   \__  |   |\   \ /   /\_   _____/ \      \__    ___/\_____  \\\______   \__  |   |       \n"
            "  |     ___//   |   | \   Y   /  |    __)_  /   |   \|    |    /   |   \|       _//   |   |       \n"
            "  |    |    \____   |  \     /   |        \/    |    \    |   /    |    \    |   \\\____   |       \n"
            "  |____|    / ______|   \___/   /_______  /\____|__  /____|   \_______  /____|_  // ______| v0.6.4 \n"
            "            \/                          \/         \/                 \/       \/ \/              ")
    elif _head.upper() == 'SCAN':       
        p_print(1, _TC["_GREEN"], 
            # http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20CHECK 'SMALL' font
            ' ___  ___   _   _  _                _    ___ _  _ ___ ___ _  __ \n'
            '/ __|/ __| /_\ | \| |  __ _ _ _  __| |  / __| || | __/ __| |/ / \n'
            '\__ | (__ / _ \| .` | / _` |   \/ _` | | (__| __ | _| (__| | <  \n'
            '|___/\___/_/ \_|_|\_| \__,_|_||_\__,_|  \___|_||_|___\___|_|\_\ \n')
    elif _head.upper() == 'PROGRESS':     
        p_print(1, _TC["_GREEN"], 
            # http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20SHOW 'SMALL' font
            " ___                             \n"
            "| _ \_ _ ___  __ _ _ _ ___ ______\n"
            "|  _/ '_/ _ \/ _` | '_/ -_|_-<_-<\n"
            "|_| |_| \___/\__, |_| \___/__/__/\n"   
            "             |___/               ")
def Help(_help):                                        # Used to call the Help info.
    if _help == 'main':                                     # Pyventory Main Menu Help
        return(
            "Pyventory Help. \n"
            "scan       open scan and check function.\n"
            "update     Change or update inventory and scanned files.\n"
            "progress   shows list by room of devices scanned outof devices in room and percent complete in room\n"
            "help       open additional info.\n"
            "x          quit\n"
        )
    elif _help == 'scan':                                   # ScanandCheck Help Menu
        return(
            "ScanandCheck Help. \n"
            "add        enable taking notes if the recorde is not found in inventory file.\n"
            "notadd     disable taking notes if the recorde is not found in inventory file.\n"
            "ask        ask each time to take notes if the recorde is not found in inventory file.\n"
            "room       set room number to check.\n"
            "x          quit\n"
        )   
    elif _help == 'progress':                               # ProgressPage Help Menu
        return(
            "all        Show all Room and there current Progress.\n"
            "(room #)   Show All not scanned devices in the room.\n"
            "export     Saves all Not Scanned Asset info to a file. \n"
            "x          quit\n"
        )
# Utilities                                             #Utilities
def setupFiles():                                       # Used to Load both Inventory and Scanned files into pyventory memory.
    p_print(4, _TC['_HEADING'], '******setupFiles()******')
    global ScannedFile                                      # global set to modify global variable.
    global InventoryFile
    Logo('MAIN')
    p_print(1, _TC['_GREEN'], 'Select your Inventory file.')
    InventoryFile = FileBrowser('.csv', False)              # CSV file exported from Database.
    p_print(1, _TC['_GREEN'], 'Select your Scanned file or create new one.')
    p_print(2, _TC["_INFO"], "new file name only NO extention needed.(i.e. school number + year)")
    ScannedFile = FileBrowser('.csv', True)                 # new or exsisting project file.
def FileBrowser(_extention, _new):                      # Used to Display and  select what file to load and create new files if needed.
    p_print(4, _TC['_HEADING'], '******FileBrowser({0:}, {1:})******'.format(_extention, _new))
    _filelist = os.listdir(".")                                     # list directory to a list
    count = 0
    files = []
    for filename in _filelist:
        if filename.endswith(_extention):                                #if file ends with specified extention.
            files.append(filename)                                      #add file to list (_files)
            print('     {0:} - {1:}'.format(count, filename))
            count += 1
    _filechoose = ''
    while len(str(_filechoose)) < 1:
        if _new == True:
            print('or type name of new Project.')
        _filechoose = input('File:')
        try:
            p_print(4, _TC['_INFO'], _filechoose)
            if _filechoose[0].upper() in ('ZYXWVUTSRQPONMLKJIHGFEDCBA'):
                if _filechoose[0].upper() == 'X':
                    break
                else:    
                    writeFile((_filechoose + "-scanned.csv"), '')
                    return(_filechoose + "-scanned.csv")
            if _filechoose[0] in ('0123456789'):
                if len(_filechoose) > 2:
                    writeFile((_filechoose + "-scanned.csv"), '')
                    return(_filechoose + "-scanned.csv")
                else:
                    p_print(4, _TC['_INFO'], files[int(_filechoose)])
                    return(files[int(_filechoose)])
            else:
                if _new == False:
                    _filechoose = ''
                    p_print(1, _TC['_ERROR'], "NO new file at this point")
                    break
        except ValueError:
            p_print(1, _TC['_ERROR'], 'ERROR: Please Enter Project Name or Number')
     
def writeFile(_filename, _info):                        # Used to Write information to Files.
    p_print(4, _TC['_HEADING'], '******writeFile({0:}, {1:})******'.format(_filename, _info))
    _openfile = open(_filename, "a")                              #'ab'will create file also 'wb' will overwrite everytime the file is opened
    _openfilewriter = csv.writer(_openfile)                        #Setup CSV writer
    _openfilewriter.writerow(_info)                                #write info to _filename given _extention allows to used this def to write to other files types
    _openfile.close()
def File2List(_filename, _column=_INV_ROW['Asset']):    # Used to read data from a CSV file and add it to a list if the _column has data.
    p_print(4, _TC['_HEADING'], '******File2List({0:}, {1:})******'.format(_filename, _column))
    _filelist = []                                                  #set blank list to recive data
    for row in list(open(_filename, "rU")):
        if row:                                                     #check if there is data on tha row.
            if row[int(_column)] == '':                                  #check if there is data in the field
                pass
            else:
                _filelist.append(row)                               #append data to list in UPPER case
    return(_filelist)
def CleanBlankRows(_list):                              # Used to Clean Blank Rows from lists.
    p_print(4, _TC['_HEADING'], '******CleanBlankRows(_list(see list _DEBUG = 5))******')
    p_print(5, _TC['_HEADING'], '******CleanBlankRows({0:})******'.format(_list))
    _cleanlist = []                                                  #set blank list to recive data
    for row in _list:
        if row:                                                     #check if there is data on tha row.
            _cleanlist.append(row)                               #append data to list in UPPER case
    return(_cleanlist)
def Dupcheck(_list):                                    # Used to checks for duplicates data in a list.
    p_print(4, _TC['_HEADING'], '******Dupcheck(_list(see list _DEBUG = 5))******')
    p_print(5, _TC['_HEADING'], '******Dupcheck({0:})******'.format(_list))
    _nodup = []
    for row in _list:
        if row not in _nodup:
            _nodup.append(row)
        else:
            pass
    return(_nodup)
def p_print(_debug, _color, _string):                   # Used as a specialized Print Command.
    # No Print command to Endless loop.
    if _debug <= _DEBUG:
        print(_color + str(_string) + _TC["_RESET"])
        if _debug >= 4:
            input('Waiting...')   
def ClearScreen():                                      # Used to Clear the Screen fo rthe UI, based on the OS being used.
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'darwin':
        os.system('clear')
def GetSingleList(_INVList, _column):                   # USed to take a list of lists and pull one column of info into one list.
    p_print(4, _TC['_HEADING'], '******GetSingleList(_INVlist(see list _DEBUG = 5), {0:})******'.format(_column))
    p_print(5, _TC['_HEADING'], '******GetSingleList({0:}, {1:})******'.format(_INVlist, _column))
    _list = []
    for _row in _INVList:
        if _row[int(_INV_ROW[_column])].lstrip('0'):
            if _row[int(_INV_ROW[_column])].upper().lstrip('0') not in _list:
                _list.append(_row[int(_INV_ROW[_column])].upper().lstrip())
    p_print(4, _TC['_YELLOW'], _list)        
    return(_list)
def GetAssetInfo(_asset):                               # Used to take an asset number and look up the row of info from the INVentory File.
    p_print(4, _TC['_HEADING'], '******GetAssetInfo({0:})******'.format(_asset))
    INVcleanlist = CleanBlankRows(list(csv.reader(open(InventoryFile, "rU"))))
    for row in INVcleanlist:
        p_print(4, _TC['_YELLOW'], row)
        item = row[_INV_ROW['Asset']]
        if _asset.lstrip('0') == item.lstrip('0'):
            return(row)   
def CountAssetsInRoom(_file, _rm):                      # Used to Count the Number of assets that are listed in a room.
    p_print(4, _TC['_HEADING'], '******CountAssetsInRoom({0:},{1:})******'.format(_file, _rm))
    INVassetList = GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Asset')
    FileList = Dupcheck(CleanBlankRows(list(csv.reader(open(_file, "rU")))))
    count = 0
    for row in FileList:
        p_print(4, _TC['_YELLOW'], row)
        p_print(4, _TC['_YELLOW'], GetAssetInfo(row[_INV_ROW['Asset']]))
        if row[_INV_ROW['Asset']] in INVassetList:
            if _rm.upper() == GetAssetInfo(row[_INV_ROW['Asset']])[_INV_ROW['Room #']]:
                p_print(4, _TC['_YELLOW'], GetAssetInfo(row[_INV_ROW['Asset']]))
                count += 1    
    return(count)
def AssetDisply(_list, _color):                         # Used to Print Asset info to UI
    p_print(4, _TC['_HEADING'], '******AssetDisplay(_list(_list(see list _DEBUG = 5), {:})******'.format(_color))
    p_print(5, _TC['_HEADING'], '******AssetDisplay({0:}, {1:})******'.format(_list, _color))
    if len(_list) > 2:
        # p_print(1, _TC['_HEADING'], ''.format('Asset Tag', 'Serial #', 'Name', 'Room #', 'Wire MAC', 'Wireless MAC', 'School # - Name'))
        p_print(1, _TC[_color], '{0:>10} : {1:16} : {2:17} : {3:12} : {4:19} : {5:19} : {6:3} - {7:}'.format(_list[_INV_ROW['Asset']], _list[_INV_ROW['Serial #']], _list[_INV_ROW['Name']], _list[_INV_ROW['Room #']], _list[_INV_ROW['Wired Mac Addr']], _list[_INV_ROW['Wireless Mac Addr']], _list[_INV_ROW['School #']], _list[_INV_ROW['School Desc']]))
    else:
        p_print(1, _TC[_color], '{0:>10}  :'.format(_list[_INV_ROW['Asset']]))
def GetProjectName(_file):                              # Used to strip teh file name down to only the Project title.
    return(_file.split('-')[0])
def addinfo(_filename, _scan):                          # Used to gather info about assets that are not found in list then stored for later entery.
    p_print(4, _TC['_HEADING'], '******addinfo({0:}, {1:})******'.format(_filename, _scan))
    print('add information for asset tage ' + _scan)
    _scan = _scan
    _asset = input('Asset tage:')
    _serial = input('serial #:')
    _type = input('device type: ')
    _make = input('make: ')
    _model = input('model: ')
    _cpu = input('cpu: ')
    _ram = input('ram: ')
    _hdd = input('hard drive:')
    _os = input('OS: ')
    _school = input('school #: ')
    _room = input('room: ')
    _user = input('user: ')
    _compname = input('computer name: ')
    _mac = input('wired MAC: ')
    _wmac =input('wireless MAC: ')
    _installdate = input('install date: ')
    _owner = input('owner: ')
    _usertype = input('user type: ')
    _status = input('status: ')
    _year = input('mtg. year: ')
    _yearrotate = input('year to be rotated: ')
    _rotate = input('eligible for rotation: ')
    _notes = input('Notes: ')
    print("\033[1;37m")
    writeFile((_filename), (_asset, str(_scan), _serial, _type, _make, _model, _cpu, _ram, _hdd, _os, _school, _room, _user, _compname, _mac, _wmac, _installdate, _owner, _usertype, _status, _year, _yearrotate, _rotate, _notes))
def RoomSelect():                                       # Used to select a room to check with.
    p_print(4, _TC["_HEADING"], "******RoomSelect()******")   
    p_print(3, _TC['_YELLOW'], GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Room #'))
    for r in GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Room #'):
        print(r)
    p_print(1, _TC['_GREEN'], " enter 'all' to check all rooms")
    return(input('Room:'))
def DisplayCurrentScan(_cscanlist, _rm):                # Used to display asste info from the curren scan list to the UI.
    p_print(4, _TC["_HEADING"], "******DisplayCurrentScan(_cscanlist(_list(see list _DEBUG = 5), {0:})******".format(_rm))
    p_print(5, _TC["_HEADING"], "******DisplayCurrentScan({0:}, {1:})******".format(_cscanlist, _rm))
    for asset in _cscanlist:
        p_print(4, _TC['_YELLOW'], asset)
        if asset in GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Asset'):
            if _rm.upper() == 'ALL':
                AssetDisply(GetAssetInfo(asset), '_GREEN')
            else:
                if _rm.upper() == GetAssetInfo(asset)[_INV_ROW["Room #"]].upper():
                    AssetDisply(GetAssetInfo(asset), '_GREEN')
                else:
                    AssetDisply(GetAssetInfo(asset), '_YELLOW')
        else:
            AssetDisply([asset], '_RED')
def DisplayProgress(_rm):                               # USed to Display the percent complete in each room.
    p_print(4, _TC['_HEADING'], '******DisplayProgress({0:})******'.format(_rm))
    RoomList = GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Room #')
    if _rm.upper() == 'ALL':
        # for room in sorted(GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Room #')):
        for room in sorted(RoomList):
            scannedinroom = CountAssetsInRoom(ScannedFile, room)
            INVinroom = CountAssetsInRoom(InventoryFile, room)
            roompercent = (float(scannedinroom/int(INVinroom))*100)
            _c = "_YELLOW"
            if roompercent <= 25.0:
                _c = "_RED"
            elif roompercent == 100.0:
                _c = "_GREEN"
            p_print(1, _TC[_c], '{0:18} - {1:>3}/{2:<3} {3:>3.0f}%'.format(room, scannedinroom, INVinroom, roompercent))
    elif _rm.upper in RoomList:
        pass
def ListAssetsInRoom(_rm):                              # Used to List all asste listed as in a selected room.
    p_print(4, _TC["_HEADING"], "******ListAssetsInRoom({0:})******".format(_rm))
    assetlist = []
    for row in Dupcheck(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU"))))):
        if _rm.upper() == row[_INV_ROW['Room #']].upper():
            assetlist.append(row[_INV_ROW['Asset']])
    return(assetlist)
def CheckScan(_scan, _rm):                              # Used to Check the asset tag that has been entered agesnt the inventory file.
    if _rm.upper() == 'ALL':
        for row in CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))):
            if row[_INV_ROW['Asset']] == _scan:
                AssetDisply(row, '_GREEN')
                writeFile(ScannedFile, [row[_INV_ROW['Asset']]])
    else:
        for row in CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))):
            if row[_INV_ROW['Asset']] == _scan:
                if _rm.upper() == row[_INV_ROW['Room #']].upper():
                    AssetDisply(row, '_GREEN')
                    writeFile(ScannedFile, [row[_INV_ROW['Asset']]])
                else:
                    AssetDisply(row, '_YELLOW')
                    writeFile(ScannedFile, [row[_INV_ROW['Asset']]])
                    writeFile((ScannedFile[:-11] + "NotFound.csv"), [_scan, _rm.upper()])
#Interface                                              #Interface
def ScanMenu():                                         # The UI for the scan interface.
    p_print(4, _TC['_HEADING'], "******ScanMenu()******")
    # VARIABLES
    scan = ''
    roomnumber = 'ALL'
    currentscanlist = []
    input('')
    inventoryassetlist = GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Asset')

    #INTERFACE
    while scan != 'x':
        ClearScreen()
        Logo('MAIN')
        Logo('SCAN')
        print('')
        p_print(2, _TC["_YELLOW"], Help('scan'))
        
        if str(scan).upper() == 'HELP':
            p_print(1, _TC['_YELLOW'], Help('scan'))
        p_print(1,_TC['_YELLOW'], '{0:>4}/{1:<0} - {2:}'.format(len(Dupcheck(CleanBlankRows(list(csv.reader(open(ScannedFile, "rU")))))), len(Dupcheck(inventoryassetlist)), 'Devices Scanned'))
        p_print(1, _TC['_HEADING'], '{0:>10} : {1:16} : {2:17} : {3:12} : {4:19} : {5:19} : {6:25}'.format('Asset Tag', 'Serial #', 'Name', 'Room #', 'Wire MAC', 'Wireless MAC', 'School # - Name'))
        p_print(3, _TC['_INFO'], currentscanlist) 
        DisplayCurrentScan(currentscanlist, roomnumber)
        
        scan = input('Scan - ' + roomnumber.upper() +":")
        if str(scan).upper() == 'ROOM':
            roomnumber = RoomSelect()
        elif str(scan).lstrip('0') == '':
            pass
        elif str(scan).lstrip('0') in inventoryassetlist:
            currentscanlist.append(str(scan).lstrip('0'))
            CheckScan(scan, roomnumber)
        else:
            currentscanlist.append(str(scan).lstrip('0'))
            writeFile(ScannedFile, [str(scan).lstrip('0')])      #add to filename to destiguish different files.
            p_print(1, _TC['_RED'], '{0:} Not Found'.format(str(scan).lstrip('0')))
def ProgressMenu():                                     # The UI for the Progress Interface.
    p_print(4, _TC['_HEADING'], '******ProgressMenu()******')
    # VARIABLES
    # ScannedAssetList = GetSingleList(CleanBlankRows(list(csv.reader(open(ScannedFile, "rU")))), 'Asset')
    # inventoryassetlist = GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Asset')
    # MissingFile = (ScannedFile.split('-')[0] + '-NotScanned.csv')
    RoomsList = GetSingleList(CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))), 'Room #')
    progressmenu = ''

    #INTERFACE
    ClearScreen()
    # Logo('MAIN')
    Logo('PROGRESS')
    print('')
    p_print(2, _TC['_YELLOW'], Help('progress'))
    
    while progressmenu.upper() != 'X':
        if progressmenu in RoomsList or progressmenu.upper() == 'ALL':
            DisplayProgress(progressmenu)
        else:
            pass

        progressmenu = input('Progress:')
def ProgressPage():                                     # OLD Progress Menu...                   
    # p_print(4, _TC['_HEADING'], '******ProgressPage()******')
    # ScannedList = []
    # InventoryList = []
    # ScannedAssetList = []
    # InventoryAssetList = []
    # RoomsList = []
    # progressmenu = ''
    # _helpscreen = 0
    # global ScannedFile
    # global InventoryFile  
    # MissingFile = (GetProjectName(ScannedFile) + '-NotScanned.csv')


    # ClearScreen()
    # ScannedList = setup(ScannedList, ScannedFile)
    # InventoryList = setup(InventoryList, InventoryFile)
    
    # for row in CleanBlankRows(list(csv.reader(open(ScannedFile, "rU")))):                     
    #     ScannedAssetList.append(row[_INV_ROW['Asset']])
    # for row in CleanBlankRows(list(csv.reader(open(InventoryFile, "rU")))):                     
    #     InventoryAssetList.append(row[_INV_ROW['Asset']])

    # RoomsList = GetRoomList(InventoryList)
    
    # totalpercent = (float(len(Dupcheck(ScannedAssetList)))/int(len(Dupcheck(InventoryList))))*100
    while progressmenu.lower() != 'x':
        ClearScreen()
        Logo('MAIN')
        Logo('PROGRESS')
        print('')
        p_print(2, _TC['_YELLOW'], Help('progress'))
        
        if progressmenu.lower() == 'all':
            for _room in sorted(RoomsList):
                p_print(4, _TC['_YELLOW'], _room)
                roompercent = (float(RoomCounter(Dupcheck(InventoryList), Dupcheck(ScannedAssetList), _room))/int(RoomCounter(Dupcheck(InventoryList), [], _room)))*100
                _c = "_YELLOW"
                if roompercent <= 25.0:
                    _c = "_RED"
                elif roompercent == 100.0:
                    _c = "_GREEN"
                p_print(1, _TC[_c], '{0:18} - {1:>3}/{2:<3} {3:>3.0f}%'.format(_room, RoomCounter(Dupcheck(InventoryList), Dupcheck(ScannedAssetList), _room), RoomCounter(Dupcheck(InventoryList), [], _room), roompercent))
 
        elif progressmenu.lower() == 'help':
            p_print(2, _TC['_YELLOW'], Help('progress'))
        
        elif progressmenu.lower() == 'export':
            p_print(1, _TC['_INFO'], 'Exporting Records to file...')
            p_print(3, _TC['_INFO'], MissingFile)
            
            if os.path.exists(MissingFile):
                os.remove(MissingFile)

            for room in sorted(RoomsList):
                p_print(3, _TC['_INFO'], [room.upper()])
                writeFile(MissingFile, [room.upper()])
                for row in InventoryList:
                    if row[_INV_ROW['Room #']].upper() == room.upper() and row[_INV_ROW['Asset']] not in ScannedAssetList:
                        p_print(3, _TC['_INFO'], ['', row])
                        writeFile(MissingFile, ['', row])

        elif progressmenu.upper() in RoomsList:
            ClearScreen()
            RoomAssetList = []
            for row in Dupcheck(InventoryList):
                if progressmenu.upper() == row[_INV_ROW['Room #']].upper():
                    RoomAssetList.append(row[_INV_ROW['Asset']])
            p_print(4, _TC['_INFO'], RoomAssetList)
            for asset in Dupcheck(RoomAssetList):
                if asset in Dupcheck(ScannedAssetList):
                    RoomAssetList.remove(asset)
            p_print(4, _TC['_INFO'], RoomAssetList)
            p_print(1, _TC['_HEADING'], progressmenu.upper())
            p_print(1, _TC['_HEADING'], '{0:>10} : {1:15} : {2:17} : {3:12} : {4:19} : {5:19} : {6:40}'.format('Asset Tag', 'Serial #', 'Name', 'Room #', 'Wire MAC', 'Wireless MAC', 'School # - Name'))
            for asset in Dupcheck(RoomAssetList):
                AssetDisply(GetAssetInfo(asset), '_YELLOW')
    
        progressmenu = input('Progress:')
def MainMenu():                                         # The UI for the Main Menu.
    ClearScreen()
    p_print(4, _TC['_HEADING'], '******Interface()******')
    _interfacemenu = 'update' 
    while _interfacemenu != 'x':
        ClearScreen()
        if _interfacemenu.lower() == 'scan':
            ScanMenu()
        elif _interfacemenu.lower() == 'progress':
            ProgressMenu()
        elif _interfacemenu.lower() == 'test':
            ProgressMenu()
        elif _interfacemenu.lower() == 'update':
            setupFiles()
            _interfacemenu = ''
        ClearScreen()
        Logo('MAIN')
        p_print(2, _TC['_YELLOW'], Help('main'))
        if _interfacemenu.lower() == 'help':
            p_print(1, _TC['_YELLOW'], Help('main'))
        _interfacemenu = input('Pyventory:')

MainMenu()