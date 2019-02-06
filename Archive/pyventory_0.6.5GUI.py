#!/Python27/pythonw.exe
#!/bin/python
#python 2.7
#Pyventory - 0.6.5

# import all needed libraries
import sys, os, csv 
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

# Gobal Variables
_DEBUG = 1     # 0 = no output, 1 =  Standered Output, 2 = Detail output, 3 = Basic Debug, 4 = pause Debug , 5 = everything,
InventoryFile = " "
InventoryList = []
InventoryAssetList = []
ScannedFile =  " "
ScannedList = []
window = Tk()


_TC = {
    #http://ozzmaker.com/add-colour-to-text-in-python/
    #TEST STYLE;TEXT COLOR; BG COLORm
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

_INV_ROW = {
    "Asset":              0,
    "Make":               1,
    "Class":              2,    # Inventory, Infrastructure, Printers
    "Name":               3,    # Device Name
    "Cpu":                4,
    "Modified by":        5,
    "Modified Date":      6,
    "Rotation Eligible":  7,      # Yes/No, Eligible for Rotation
    "Status":             8,      # Active, Condemned, Surplus
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

def Logo(_head):                         #Just a Cool Heading for the program
    if _head.upper() == 'MAIN':
        p_print(1, _TC['_GREEN'], " _______________.___.____   _______________ __________________________ _______________.___.       \n"
            " \______   \__  |   |\   \ /   /\_   _____/ \      \__    ___/\_____  \\\______   \__  |   |       \n"
            "  |     ___//   |   | \   Y   /  |    __)_  /   |   \|    |    /   |   \|       _//   |   |       \n"
            "  |    |    \____   |  \     /   |        \/    |    \    |   /    |    \    |   \\\____   |       \n"
            "  |____|    / ______|   \___/   /_______  /\____|__  /____|   \_______  /____|_  // ______| v0.6.3 \n"
            "            \/                          \/         \/                 \/       \/ \/              ")
    elif _head.upper() == 'SCAN':       #http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20CHECK 'SMALL' font
        p_print(1, _TC["_GREEN"], ' ___  ___   _   _  _                _    ___ _  _ ___ ___ _  __ \n'
            '/ __|/ __| /_\ | \| |  __ _ _ _  __| |  / __| || | __/ __| |/ / \n'
            '\__ | (__ / _ \| .` | / _` |   \/ _` | | (__| __ | _| (__| | <  \n'
            '|___/\___/_/ \_|_|\_| \__,_|_||_\__,_|  \___|_||_|___\___|_|\_\ \n')
    elif _head.upper() == 'PROGRESS':     #http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20SHOW 'SMALL' font
        p_print(1, _TC["_GREEN"], " ___                             \n"
            "| _ \_ _ ___  __ _ _ _ ___ ______\n"
            "|  _/ '_/ _ \/ _` | '_/ -_|_-<_-<\n"
            "|_| |_| \___/\__, |_| \___/__/__/\n"   
            "             |___/               ")

def Help(_menu):                                                #The Help Screen- broken down so specified potion can be called were needed.
    if _menu == 'main':                                             #Pyventory Main Menu Help
        return(
            "Pyventory Help. \n"
            "scan       open scan and check function.\n"
            "update     Change or update inventory and scanned files.\n"
            "progress   shows list by room of devices scanned outof devices in room and percent complete in room\n"
            "help       open additional info.\n"
            "x          quit\n"
            )
    elif _menu == 'scan':                                           #ScanandCheck Help Menu
        return(
            "add        enable taking notes if the recorde is not found in inventory file.\n"
            "notadd     disable taking notes if the recorde is not found in inventory file.\n"
            "ask        ask each time to take notes if the recorde is not found in inventory file.\n"
            "room       set room number to check.\n"
            "x          quit\n"
        )   
    elif _menu == 'progress':                                         #ProgressPage Help Menu
        return(
            "all        Show all Room and there current Progress.\n"
            "(room #)   Show All not scanned devices in the room.\n"
            "export     Saves all Not Scanned Asset info to a file. \n"
            "x          quit\n"
        )

def SetFile(_filetoopen):
    global ScannedFile
    global InventoryFile
    _filetoopen = window.filename = tkFileDialog.askopenfilename(initialdir = "/",title = '{0:} {1:}'.format(_filetoopen[:-4], _filetoopen[-4:]), filetypes = (("csv files","*.csv"),("all files","*.*")))
    print(_filetoopen)
    print(os.path.join(_filetoopen))


def setup(_list, _file):
    p_print(4, _TC['_HEADING'], '******setup({0:}, {1:})******'.format(_list, _file))
    I_list = []
    p_print(4, _TC['_INFO'], 'Convert2List({0:},{1:})'.format(_file, _INV_ROW['Asset']))
    for l in Convert2List(_file, _INV_ROW['Asset']):
        I_list.append(l)
    p_print(4, _TC['_INFO'], I_list)
    return(I_list)

        
def writefile(_filename, _info):                                #setup file to write to.
    p_print(4, _TC['_HEADING'], '******writefile({0:}, {1:})******'.format(_filename, _info))
    _openfile = open(_filename, "ab")                              #'ab'will create file also 'wb' will overwrite everytime the file is opened
    _openfilewriter = csv.writer(_openfile)                        #Setup CSV writer
    _openfilewriter.writerow(_info)                                #write info to _filename given _extention allows to used this def to write to other files types
    _openfile.close()

def CSVReader(_filename):                                       #Setup CSV reader.
    p_print(4, _TC['_HEADING'], '******CSVReader({0:})******'.format(_filename))
    _file = open(os.path.join(_filename), "rU")
    return(csv.reader(_file))
  
def Convert2List(_filename, _column):                           #Read data from file and add it to a list.
    p_print(4, _TC['_HEADING'], '******Convert2List({0:}, {1:})******'.format(_filename, _column))
    _filereader = CSVReader(_filename)
    _filelist = []                                                  #set blank list to recive data
    for row in list(_filereader):
        if row:                                                     #check if there is data on tha row.
            if row[int(_column)] == '':                                  #check if there is data in the field
                pass
            else:
                _filelist.append(row)                               #append data to list in UPPER case
    return(_filelist)


def Dupcheck(_list):                                            #checking for duplicates
    p_print(4, _TC['_HEADING'], '******Dupcheck(_list)******')
    _nodup = []
    for row in _list:
        if row not in _nodup:
            _nodup.append(row)
        else:
            pass
    return(_nodup)

def p_print(_debug, _color, _string):
    if _debug <= _DEBUG:
        print(_color + str(_string) + _TC["_RESET"])
        if _debug == 4:
            raw_input('Waiting...')
        
def ClearScreen():
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'darwin':
        os.system('clear')

def GetRoomList(_INVList):
    p_print(4, _TC['_HEADING'], '******GetRoomList(InventoryFileList)******')
    _list = []
    p_print(4, _TC['_YELLOW'], _INVList)
    for _row in _INVList:
        if _row[int(_INV_ROW['Room #'])].upper():
            if _row[int(_INV_ROW['Room #'])].upper() not in _list:
                _list.append(_row[int(_INV_ROW['Room #'])].upper())
            
    return(_list)

def GetAssetInfo(_INVList, _asset):
    for row in _INVList:
        if _asset == row[_INV_ROW['Asset']]:
            return(row)

def RoomCounter(_INVList, _SCANList, _room):
    count = 0
    if _SCANList:
        for scan in _SCANList:
            for row in _INVList:
                if scan.upper() == row[_INV_ROW['Asset']].upper():
                    if _room.upper() == row[_INV_ROW['Room #']].upper():
                        count += 1
    else:
        for row in _INVList:
            if _room.upper() == row[_INV_ROW['Room #']].upper():
                count += 1
    return(count)

def AssetDisply(_list, _color):
    p_print(4, _TC['_HEADING'], '******AssetDisplay({0:}, {1:})******'.format(_list, _color))
    if len(_list) > 2:
        # p_print(1, _TC['_HEADING'], ''.format('Asset Tag', 'Serial #', 'Name', 'Room #', 'Wire MAC', 'Wireless MAC', 'School # - Name'))
        p_print(1, _TC[_color], '{0:>10} : {1:16} : {2:17} : {3:12} : {4:19} : {5:19} : {6:3} - {7:}'.format(_list[_INV_ROW['Asset']], _list[_INV_ROW['Serial #']], _list[_INV_ROW['Name']], _list[_INV_ROW['Room #']], _list[_INV_ROW['Wired Mac Addr']], _list[_INV_ROW['Wireless Mac Addr']], _list[_INV_ROW['School #']], _list[_INV_ROW['School Desc']]))
    else:
        p_print(1, _TC[_color], '{0:>10}  :'.format(_list[_INV_ROW['Asset']]))

def MakeMissing(_INVfile):
    return(_INVfile.split('-')[0])

def CheckAsset(_assettag, _INVassetlist):
    # compaire the input asset tag with inventory asset tag list
    p_print(4, _TC['_HEADING'], '******Check()******')
    return(_assettag.lstrip('0') in _INVassetlist.lstrip('0'))        #compare of entry and inventory Asset.
        
    

def addinfo(_filename, _scan):                                  #used to gather info about assets that are not found in list then stored for later entery.
    p_print(4, _TC['_HEADING'], '******addinfo({0:}, {1:})******'.format(_filename, _scan))
    print('add information for asset tage ' + _scan)
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
    writefile((_filename), (_asset, str(_scan), _serial, _type, _make, _model, _cpu, _ram, _hdd, _os, _school, _room, _user, _compname, _mac, _wmac, _installdate, _owner, _usertype, _status, _year, _yearrotate, _rotate, _notes))

def SCANandCHECK():                                             #Scan asset tage and Check them in an inventory file
    p_print(4, _TC['_HEADING'], "******SCANandCHECK()******")
    
    # VARIABLES
    _ADD = 'ASK'                #Used to indicate Note taking
    Scan = 0                    #VAR set for taking asset tags
    InventoryAssetList = []
    RoomNumber = 'ALL'
    RoomsList = []             #List of Rooms
    ScannedAssetList = []      #list of scanned asset tags
    currentscan = []
    ScannedList = []
    InventoryList = []
    _helpscreen = ''
    global ScannedFile
    global InventoryFile
    
    # setupFiles()
    
    # SandC = Toplevel(master=window)
    # SandC.title("SCANandCHECK")
    # Label(SandC, text='it Worked', bg='black', fg='green', font='none 24 bold').grid(row=0, column=0, sticky=N)

    ClearScreen()
    ScannedList = setup(ScannedList, ScannedFile)
    InventoryList = setup(InventoryList, InventoryFile)

    p_print(4, _TC['_YELLOW'], "******SCANNED LIST******")
    p_print(4, _TC['_YELLOW'], str(ScannedList))
    p_print(4, _TC['_YELLOW'], "******INVENTORY LIST******")
    p_print(4, _TC['_YELLOW'], str(InventoryList)) 
    
    for row in ScannedList:                     
        ScannedAssetList.append(row[_INV_ROW['Asset']])
    for row in InventoryList:                     
        InventoryAssetList.append(row[_INV_ROW['Asset']])
      
    
    # p_print(1, _TC['_HEADING'], '{0:8}   :   {1:14}    :   {2:14}    :   {3:12}    :   {4:14}    :   {5:14}    :   {6:40}'.format('Asset Tag', 'Serial #', 'Name', 'Room #', 'Wire MAC', 'Wireless MAC', 'School # - Name'))
    while Scan != 'x':          #Start of the entery process this is the loop that will take info and check in the inventory file.
        ClearScreen()
        Logo('MAIN')
        Logo('SCAN')
        print('')
        p_print(2, _TC["_YELLOW"], Help('scan'))
        if _helpscreen == 1:
            p_print(1, _TC['_YELLOW'], Help('scan'))
            _helpscreen = 0
    # ADD/NOTADD/ASK---------------------------------------------------------------------- 
        if _ADD == 'ADD':
            p_print(1, _TC['_YELLOW'],'Taking notes ALWAYS')
        elif _ADD == 'NOTADD':
            p_print(1, _TC['_YELLOW'], 'Not taking Notes')
        elif _ADD == 'ASK':
            p_print(1, _TC['_YELLOW'], 'ASK each time to take notes')
    # --------------------------------------------------------------------------------------- 
        p_print(1,_TC['_YELLOW'], '{0:>4}/{1:<0} - {2:}'.format(len(Dupcheck(ScannedAssetList)), len(Dupcheck(InventoryAssetList)), 'Devices Scanned'))
        p_print(1, _TC['_HEADING'], '{0:>10} : {1:16} : {2:17} : {3:12} : {4:19} : {5:19} : {6:25}'.format('Asset Tag', 'Serial #', 'Name', 'Room #', 'Wire MAC', 'Wireless MAC', 'School # - Name'))
        
        p_print(3, _TC['_INFO'], currentscan) 

        for asset in currentscan:
                p_print(4, _TC['_YELLOW'], asset)
                if asset in InventoryAssetList:
                    if RoomNumber.upper() == 'ALL':
                        AssetDisply(GetAssetInfo(InventoryList, asset), '_GREEN')
                    else:
                        if RoomNumber.upper() == GetAssetInfo(InventoryList, asset)[_INV_ROW["Room #"]].upper():
                            AssetDisply(GetAssetInfo(InventoryList, asset), '_GREEN')
                        else:
                            AssetDisply(GetAssetInfo(InventoryList, asset), '_YELLOW')
                else:
                    AssetDisply([asset], '_RED')
        
        Scan = raw_input('Scan - ' + RoomNumber.upper() +":")
        
        if Scan.upper() == 'ADD':                                  #add command used to turn on adding info if entery is not found.
            _ADD = 'ADD'
        elif Scan.upper() == 'NOTADD':                             #notadd commadn used to turn off adding info in entery in not found
            _ADD = 'NOTADD'
        elif Scan.upper() == 'ASK':                                #ask command used to set program to ask user each time a record is not found if info should be added.
            _ADD = 'ASK'
        
        elif Scan.upper() == 'HELP':                               #help commadn used to show the help screen
            _helpscreen = 1
        
        elif Scan.upper() == 'ROOM':
    # RoomNumberSelect--------------------------------------------------------------------        
            RoomsList = GetRoomList(InventoryList)
            p_print(3, _TC['_YELLOW'], str(RoomsList))
            for r in RoomsList:
                print(r)
            p_print(1, _TC['_GREEN'], " enter 'all' to check all rooms")
            RoomNumber = raw_input('Room:')
    # -----------------------------------------------------------------------        
    # ScanandCheckCore---------------------------------------------------------------------------------------        
        elif Scan in InventoryAssetList or Scan.lstrip('0') in InventoryAssetList:        #compaire of entery and inventory Asset.
            currentscan.append(Scan)
            if RoomNumber.upper() == 'ALL':
                for row in InventoryList:
                    if row[_INV_ROW['Asset']] == Scan.lstrip('0') or row[_INV_ROW['Asset']] == Scan:
                        AssetDisply(row, '_GREEN')
                        writefile(ScannedFile, [row[_INV_ROW['Asset']]])
            else:
                for row in InventoryList:
                    if row[_INV_ROW['Asset']] == Scan.lstrip('0') or row[_INV_ROW['Asset']] ==Scan:
                        if RoomNumber.upper() == row[_INV_ROW['Room #']].upper():
                            AssetDisply(row, '_GREEN')
                            writefile(ScannedFile, [row[_INV_ROW['Asset']]])
                        else:
                            AssetDisply(row, '_YELLOW')
                            writefile(ScannedFile, [row[_INV_ROW['Asset']]])
                            writefile((ScannedFile[:-11] + "NotFound.csv"), [str(Scan), str(RoomNumber).upper()])
                            p_print(1, _TC['_YELLOW'], 'Notes add to "NotFound" List.')

        elif Scan.upper() == 'X' or Scan.upper() == 'EXIT':                            #x command used to exit scan and check
            break
        else:
            writefile(ScannedFile, [Scan])      #add to filename to destiguish different files.
            currentscan.append(Scan)
            if _ADD == 'NOTADD':
                pass
            else:
                p_print(1, _TC['_RED'], '{0:} and {1:} Not Found'.format(Scan, Scan.lstrip('0')))
                if _ADD == 'ADD':
                    addinfo((ScannedFile[:-11] + "NotFound.csv"), str(Scan))
            
                elif _ADD == 'ASK':
                    _verify = 0
                    while _verify == 0:
                        print('Do you want to add info (y or n)?')
                        _ask = raw_input(':')
                        if _ask.lower() == 'y':
                            _verify = 1
                            addinfo((ScannedFile[:-11] + "NotFound.csv"), str(Scan))
                        if _ask.lower() == 'n':
                            _verify = 1
                            break

def ProgressPage():                                                        
    p_print(4, _TC['_HEADING'], '******ProgressPage()******')
    #  --setup--------------------------------------------------------------------------
    ScannedList = []
    InventoryList = []
    ScannedAssetList = []
    InventoryAssetList = []
    RoomsList = []
    progressmenu = ''
    _helpscreen = 0
    global ScannedFile
    global InventoryFile  
    MissingFile = (MakeMissing(ScannedFile) + '-NotScanned.csv')

    ClearScreen()
    ScannedList = setup(ScannedList, ScannedFile)
    InventoryList = setup(InventoryList, InventoryFile)
    
    for row in ScannedList:                     
        ScannedAssetList.append(row[_INV_ROW['Asset']])
    for row in InventoryList:                     
        InventoryAssetList.append(row[_INV_ROW['Asset']])
    RoomsList = GetRoomList(InventoryList)
 
    
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
                writefile(MissingFile, [room.upper()])
                for row in InventoryList:
                    if row[_INV_ROW['Room #']].upper() == room.upper() and row[_INV_ROW['Asset']] not in ScannedAssetList:
                        p_print(3, _TC['_INFO'], ['', row])
                        writefile(MissingFile, ['', row])

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
                AssetDisply(GetAssetInfo(InventoryList, asset), '_YELLOW')
    
        progressmenu = raw_input('Progress:')
        

def Interface():
    # ClearScreen()
    # _interfacemenu = 'update' 
    # while _interfacemenu != 'x':
    #     ClearScreen()
    #     p_print(4, _TC['_HEADING'], '******Interface()******')
    #     if _interfacemenu.lower() == 'scan':
    #         SCANandCHECK()
    #     elif _interfacemenu.lower() == 'progress':
    #         ProgressPage()
    #     elif _interfacemenu.lower() == 'update':
    #         setupFiles()
    #         _interfacemenu = ''
    #     ClearScreen()
    #     Logo('MAIN')
    #     p_print(2, _TC['_YELLOW'], Help('main'))
    #     if _interfacemenu.lower() == 'help':
    #         p_print(1, _TC['_YELLOW'], Help('main'))
    #     _interfacemenu = raw_input('Pyventory:')
    
    # VARIABLES
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    setfilemenu = Menu(filemenu, tearoff=0)
    global ScannedFile
    global InventoryFile
    # MANI WINDOW
    window.title('Pyventory')
    window.configure(background='black')
    window.config(menu=menubar)

    Label(window, text='Pyventory', fg='green', bg='black', font='none 30 bold').grid(row=0, column=0, sticky=W)
    Label(window, text='0.6.5', fg='green', bg='black', font='none 12').grid(row=0, column=1, sticky=S)
    # Label(window, text=InventoryFile).grid(row=1, column=0)
    # Label(window, text=ScannedFile).grid(row=2, column=0)
    Button (window, text='Scan', justify='center', padx='2', command=lambda : CheckAsset(Scan, InventoryAssetList)).grid(row=1, column=0, stick=W)
    Button (window, text='Progress', justify='center',padx='2').grid(row=1, column=0)
    Scan = Entry(window,width='10').grid(row=2, column=0)
    # MENU BAR
    menubar.add_cascade(label="Menu", menu=filemenu)
    # menubar.add_cascade(label="Edit", menu=editmenu)
    # menubar.add_cascade(label="Help", menu=helpmenu)
        # FILE MANU
    filemenu.add_command(label="New")
    filemenu.add_cascade(label="Set", menu=setfilemenu)
    filemenu.add_command(label="Scan",command=SCANandCHECK)
    filemenu.add_command(label="Progress")
    # filemenu.add_command(label="Save as...")
    # filemenu.add_command(label="Close")
    filemenu.add_separator()
    filemenu.add_command(label="Exit")

    setfilemenu.add_command(label="Inventory File", command=lambda : SetFile('InventoryFile'))
    setfilemenu.add_command(label="Scanned File", command=lambda : SetFile('ScannedFile'))

    
    window.mainloop()


Interface()


