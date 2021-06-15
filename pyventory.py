#!/Python27/pythonw.exe
#1/bin/python
#python 3.9
#Pyventory - 2.1
# import all needed libraries
import sys, os, csv, json, datetime
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from datetime import datetime, date
# Gobal Variables
_DEBUG = 1         # 0 = no output, 1 =  Standered Output, 2 = Detail output, 3 = Basic Debug, 4 = pause Debug , 5 = everything,


# InventoryFile = ""
pyventory_db = ".pv_db.json"
autoSave_file = "~autosave.csv"
# ScannedFile =  ""
currentscanlist = []
versionnumber = '2.1'

class Directories:          # Directories
    # http://ozzmaker.com/add-colour-to-text-in-python/
    _TC = {                     # TEXT COLOR
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
    _INV_ROW = {                # CSV Inventory Column Numbers
        "Asset":              0,            # Asset Tag Number
        "Make":               1,            # Device Make (Apple, HP, Samsung)
        "Class":              2,            # Inventory, Infrastructure, Printers
        "Name":               3,            # Device Name
        "Cpu":                4,            # CPU
        "Modified by":        21,            # Last Modified Username
        "Modified Date":      22,            # Last Modified Date
        "Rotation Eligible":  7,            # Yes/No, Eligible for Rotation
        "Status":             8,            # Active, Condemned, Surplus
        "Wired Mac Addr":     9,
        "Wireless Mac Addr":  10,
        "Server Mac Addr":    11,
        "Hdd":                14,
        "Tag":                15,
        "IP Addr":            16,
        "Last Inv date":      17,
        "MDM Date":           18,
        "Mfg Year":           19,
        "Model":              20,
        "Creator":            5,
        "Create Date":        6,
        "VLAN":               23,
        "Notes":              24,
        "OS":                 25,
        "Owner":              26,
        "Product #":          27,
        "InstallDate":        28,
        "Ram":                29,
        "Room #":             30,
        "School #":           31,
        "Serial #":           32,
        "Unknown":            100,     # 100 = unknow column from
        "MDM Purchased":      101,     # Yes/No
        "Device Type":        35,     # LapMain, Chromebook, etc
        "Username":           36,
        "UserType":           37,     # Student, Teacher, Admin, Etc
        "Rotation Year":      38,     # Year to be Rotated
        "School Name":        47,     # School Name, Scan File Format 
        }
    _WS1_Col = {
        "Last Seen Date":      0,
        "Serial #":           17,
        }
    _CM_Col = {
        "Last Sync Date":      3,
        "Serial #":            1,
        }
    _SCCM_Col = {
        "Last Active Date":    2,
        "Serial #":            1,
        }
class Utilities:            # Utilities
    def BulkChecker(self):
        self.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("CSV files","*.csv")))
        self.data = self.jsonOpenSave('OPEN')
        messagebox.showinfo("Bulk Checker", 'press ok and wait until the Complete Message apperes.')
        for i in self.CSV2List(self.filename):
            self.p_print(4, Directories._TC['_INFO'], i[0])
            self.CheckScan(i[0])
        messagebox.showinfo('Bulk Checker', 'Bulk Check Complete')
    def Logo(self, _head):      # Used to call the logo and headings for the UI.
        if _head.upper() == 'MAIN':         # PYVENTORY
            self.p_print(1, Directories._TC['_GREEN'], 
                " _______________.___.____   _______________ __________________________ _______________.___.       \n"
                " \______   \__  |   |\   \ /   /\_   _____/ \      \__    ___/\_____  \\\______   \__  |   |       \n"
                "  |     ___//   |   | \   Y   /  |    __)_  /   |   \|    |    /   |   \|       _//   |   |       \n"
                "  |    |    \____   |  \     /   |        \/    |    \    |   /    |    \    |   \\\____   |       \n"
                "  |____|    / ______|   \___/   /_______  /\____|__  /____|   \_______  /____|_  // ______| v0.6.5 \n"
                "            \/                          \/         \/                 \/       \/ \/              ")
        elif _head.upper() == 'SCAN':       # SCAN AND CHECK       
            self.p_print(1, Directories._TC["_GREEN"], 
                # http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20CHECK 'SMALL' font
                ' ___  ___   _   _  _                _    ___ _  _ ___ ___ _  __ \n'
                '/ __|/ __| /_\ | \| |  __ _ _ _  __| |  / __| || | __/ __| |/ / \n'
                '\__ | (__ / _ \| .` | / _` |   \/ _` | | (__| __ | _| (__| | <  \n'
                '|___/\___/_/ \_|_|\_| \__,_|_||_\__,_|  \___|_||_|___\___|_|\_\ \n')
        elif _head.upper() == 'PROGRESS':   # PROGRESS     
            self.p_print(1, Directories._TC["_GREEN"], 
                # http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20SHOW 'SMALL' font
                " ___                             \n"
                "| _ \_ _ ___  __ _ _ _ ___ ______\n"
                "|  _/ '_/ _ \/ _` | '_/ -_|_-<_-<\n"
                "|_| |_| \___/\__, |_| \___/__/__/\n"   
                "             |___/               \n")
        elif _head.upper() == 'DELETE':       #DELETE
            self.p_print(1, Directories._TC["_GREEN"],
                # http://patorjk.com/software/taag/#p=display&f=Small&t=DELETE%0A 'SMALL' font
                " ___  ___ _    ___ _____ ___ \n"
                "|   \| __| |  | __|_   _| __|\n"
                "| |) | _|| |__| _|  | | | _| \n"
                "|___/|___|____|___| |_| |___|\n")
    def Help(self, _help):      # Used to call the Help info.
        if _help.upper() == 'MAIN':         # Pyventory Main Menu Help
            return(
                "\n"
                "Pyventory Help. \n"
                "scan           Open scan and check screen.\n"
                "update         Update inventory Database.\n"
                "progress       Shows lists by school and room, of inventory stats.\n"
                "delete         Delete screen to remove records from database\n"
                "help           Open this menu.\n"
                "x or exit      Quit Program\n"
            )
        elif _help.upper() == 'SCAN':       # Scan and Check Help Menu
            return(
                "ScanandCheck Help. \n"
                "{ASSET TAG}    Enter the Asset tag to lookup\n"
                "x or exit      Save and Exit to Main Menu\n"
            )   
        elif _help.upper() == 'PROGRESS':   # Progress Page Help Menu
            return(
                "Progress Help\n"
                "all            Show all Room and there current Progress.\n"
                "{school #}     Enter School # to show a list of only rooms in the school\n"
                "{room #}       (Must enter school # fist) Lists all devices assigned to room#.\n"
                "x or exit      Exit to Main Menu\n"
            )
        elif _help.upper() == "UPDATE":     # in place for the current interface setup, used for allowing the menu to run update.
            return(
                "Updateing Pyventory Database.......\n"
            )
        elif _help.upper() == 'DELETE':
            return(
                "Delete Help\n"
                "{asset tag}    The Asset tag you wish to remove from the database.\n"
                "help           Will Display This Message.\n"
                "x or exit      Quit to Main Menu"
                "\n"
                "PLEASE NOTE: This will delete all record of the asset tage.\n"
                "and you cannot recover from this action without a backup.\n"
            )
        else:
            return('null')
    def pyventory_db_check(self):               # Used to check if the pyventory_db has been created then prompts user to updated if no database file is found.
        self.p_print(4, Directories._TC['_HEADING'], '******pyventory_db_check()******')
        if os.path.exists(pyventory_db):
            return('DB is good')
        else:
            return('Please Run Update before Continuing.')
    def pyventory_db_update(self, _filename):   # databnase update modual
        self.p_print(4, Directories._TC['_HEADING'], '******pyventory_db_update({})******'.format(_filename))
        if type(_filename) != 'Nonetype':  
            Updated_pyventory_db = {}
            UpdateFile_school_list = [] 
            updatefile_list = self.CSV2List(_filename)          # takes a .CSV file from inventory database and turn it to a list for proccessing.

            if os.path.exists(pyventory_db):                    # Check if file
                data = self.jsonOpenSave('OPEN')                # set DB to data
                self.DbBackup(data, ('db'+ self.TimeStamp() + '.json'))
                os.remove(pyventory_db)                         # remove old database file
            else:
                data = {}

            self.p_print(4, Directories._TC['_INFO'], updatefile_list)
            self.p_print(2, Directories._TC["_INFO"], "Updating Pyventory Database, Please Wait...")

            for row in updatefile_list:                         # Create Llist of locations ids from CSV(update list)
                if row[Directories._INV_ROW['School #']] not in UpdateFile_school_list:
                    UpdateFile_school_list.append(row[Directories._INV_ROW['School #']])

                    # Need to make a check during the update if the asset record is in the school list.



            for row in updatefile_list:
                self.p_print(4, Directories._TC['_INFO'], row)
                
                if str(row[Directories._INV_ROW['Asset']]).lstrip('0') in data:      # check if asset tage is in Database.
                    datecode = data[str(row[Directories._INV_ROW['Asset']]).lstrip('0')]["Scan Year"]           # pulled from existing data to be added to new database.

                    Updated_pyventory_db[str(row[Directories._INV_ROW['Asset']]).lstrip('0')] = {}   # create new record in json file
                    Updated_pyventory_db[str(row[Directories._INV_ROW['Asset']]).lstrip('0')].update({   # add data to record
                        "Asset": str(row[Directories._INV_ROW['Asset']]).lstrip('0'),
                        "Serial #": row[Directories._INV_ROW["Serial #"]],
                        "Class": row[Directories._INV_ROW["Class"]],       
                        "Device Type": row[Directories._INV_ROW["Device Type"]],    
                        "Make": row[Directories._INV_ROW["Make"]],
                        "Model": row[Directories._INV_ROW["Model"]],
                        "Cpu": row[Directories._INV_ROW["Cpu"]],
                        "Product #": row[Directories._INV_ROW["Product #"]],
                        "Ram": row[Directories._INV_ROW["Ram"]],
                        "OS": row[Directories._INV_ROW["OS"]],
                        "Hdd": row[Directories._INV_ROW["Hdd"]],
                        "School #": row[Directories._INV_ROW["School #"]],
                        "Room #": row[Directories._INV_ROW["Room #"]],
                        "Username": row[Directories._INV_ROW["Username"]],
                        "IP Addr": row[Directories._INV_ROW["IP Addr"]],
                        "Name": row[Directories._INV_ROW["Name"]],        
                        "Wired Mac Addr": row[Directories._INV_ROW["Wired Mac Addr"]],
                        "Wireless Mac Addr": row[Directories._INV_ROW["Wireless Mac Addr"]],
                        "Server Mac Addr": row[Directories._INV_ROW["Server Mac Addr"]],
                        "InstallDate": row[Directories._INV_ROW["InstallDate"]],
                        "Owner": row[Directories._INV_ROW["Owner"]],
                        "UserType": row[Directories._INV_ROW["UserType"]],    
                        "Status": row[Directories._INV_ROW["Status"]],      
                        "Mfg Year": row[Directories._INV_ROW["Mfg Year"]],
                        "Rotation Year": row[Directories._INV_ROW["Rotation Year"]],    
                        "Rotation Eligible": row[Directories._INV_ROW["Rotation Eligible"]],        
                        "School Name": row[Directories._INV_ROW["School Name"]],
                        "Scan Year": datecode,
                        })
                else:
                    Updated_pyventory_db[str(row[Directories._INV_ROW['Asset']]).lstrip('0')] = {}
                    Updated_pyventory_db[str(row[Directories._INV_ROW['Asset']]).lstrip('0')].update({
                        "Asset": str(row[Directories._INV_ROW['Asset']]).lstrip('0'),
                        "Serial #": row[Directories._INV_ROW["Serial #"]],
                        "Class": row[Directories._INV_ROW["Class"]],       
                        "Device Type": row[Directories._INV_ROW["Device Type"]],    
                        "Make": row[Directories._INV_ROW["Make"]],
                        "Model": row[Directories._INV_ROW["Model"]],
                        "Cpu": row[Directories._INV_ROW["Cpu"]],
                        "Product #": row[Directories._INV_ROW["Product #"]],
                        "Ram": row[Directories._INV_ROW["Ram"]],
                        "OS": row[Directories._INV_ROW["OS"]],
                        "Hdd": row[Directories._INV_ROW["Hdd"]],
                        "School #": row[Directories._INV_ROW["School #"]],
                        "Room #": row[Directories._INV_ROW["Room #"]],
                        "Username": row[Directories._INV_ROW["Username"]],
                        "IP Addr": row[Directories._INV_ROW["IP Addr"]],
                        "Name": row[Directories._INV_ROW["Name"]],        
                        "Wired Mac Addr": row[Directories._INV_ROW["Wired Mac Addr"]],
                        "Wireless Mac Addr": row[Directories._INV_ROW["Wireless Mac Addr"]],
                        "Server Mac Addr": row[Directories._INV_ROW["Server Mac Addr"]],
                        "InstallDate": row[Directories._INV_ROW["InstallDate"]],
                        "Owner": row[Directories._INV_ROW["Owner"]],
                        "UserType":  row[Directories._INV_ROW["UserType"]],    
                        "Status": row[Directories._INV_ROW["Status"]],      
                        "Mfg Year": row[Directories._INV_ROW["Mfg Year"]],
                        "Rotation Year": row[Directories._INV_ROW["Rotation Year"]],    
                        "Rotation Eligible": row[Directories._INV_ROW["Rotation Eligible"]],        
                        "School Name": row[Directories._INV_ROW["School Name"]],    
                        "Scan Year": [],
                        })
            for recordid in data:
                if data[str(recordid)]["School #"] not in UpdateFile_school_list and len(data[str(recordid)]["School #"]) > 2 :
                    datecode = data[str(recordid)]["Scan Year"]           # pulled from existing data to be added to new database.
                    Updated_pyventory_db[str(data[str(recordid)]['Asset']).lstrip('0')] = {}   # create new record in json file
                    Updated_pyventory_db[str(data[str(recordid)]['Asset']).lstrip('0')].update({   # add data to record
                        "Asset": str(data[str(recordid)]['Asset']).lstrip('0'),
                        "Serial #": data[str(recordid)]["Serial #"],
                        "Class": data[str(recordid)]["Class"],       
                        "Device Type": data[str(recordid)]["Device Type"],    
                        "Make": data[str(recordid)]["Make"],
                        "Model": data[str(recordid)]["Model"],
                        "Cpu": data[str(recordid)]["Cpu"],
                        "Product #": data[str(recordid)]["Product #"],
                        "Ram": data[str(recordid)]["Ram"],
                        "OS": data[str(recordid)]["OS"],
                        "Hdd": data[str(recordid)]["Hdd"],
                        "School #": data[str(recordid)]["School #"],
                        "Room #": data[str(recordid)]["Room #"],
                        "Username": data[str(recordid)]["Username"],
                        "IP Addr": data[str(recordid)]["IP Addr"],
                        "Name": data[str(recordid)]["Name"],        
                        "Wired Mac Addr": data[str(recordid)]["Wired Mac Addr"],
                        "Wireless Mac Addr": data[str(recordid)]["Wireless Mac Addr"],
                        "Server Mac Addr": data[str(recordid)]["Server Mac Addr"],
                        "InstallDate": data[str(recordid)]["InstallDate"],
                        "Owner": data[str(recordid)]["Owner"],
                        "UserType": data[str(recordid)]["UserType"],    
                        "Status": data[str(recordid)]["Status"],      
                        "Mfg Year": data[str(recordid)]["Mfg Year"],
                        "Rotation Year": data[str(recordid)]["Rotation Year"],    
                        "Rotation Eligible": data[str(recordid)]["Rotation Eligible"],        
                        "School Name": data[str(recordid)]["School Name"],
                        "Scan Year": datecode,
                        })
        self.jsonOpenSave('SAVE', Updated_pyventory_db) 
    def DbBackup(self, _data, _filename=''):
        if _filename == '':
            pass
        else:
            with open(_filename, 'w') as backupfile:
                json.dump(_data, backupfile)
    def FileBrowser(self, _extention, _new):    # Used to Display and  select what file to load. basic text interface file browser
        self.p_print(4, Directories._TC['_HEADING'], '******FileBrowser({0:}, {1:})******'.format(_extention, _new))
        _filelist = os.listdir(".") # list directory to a list
        count = 0
        files = []
        print('     {0:} - {1:}'.format('X', "Quit"))
        for filename in _filelist:
            if filename.endswith(_extention):   # if file ends with specified extention.
                files.append(filename)          # then add file to list (_files)
                print('     {0:} - {1:}'.format(count, filename))   # print out list of file names to select from
                count += 1
        _filechoose = ''
        while len(str(_filechoose)) < 1:
            _filechoose = input('File:')
            try:
                self.p_print(4, Directories._TC['_INFO'], _filechoose)
                if _filechoose[0] in ('0123456789'):
                    self.p_print(4, Directories._TC['_INFO'], files[int(_filechoose)])
                    return(files[int(_filechoose)])
                else:
                    break
            except ValueError:
                self.p_print(1, Directories._TC['_ERROR'], 'ERROR: Please Enter Project Name or Number')
    def CSVwriter(self, _filename, _info):      # Writes(appends) data to CSV files one line at a time.
        with open(_filename, 'a') as _file:
            _writer = csv.writer(_file)
            _writer.writerows([_info]) 
    def CSV2List(self, _filename, _column=Directories._INV_ROW['Asset']):    # Used to read data from a CSV file and add it to a list if the _column has data.
        self.p_print(4, Directories._TC['_HEADING'], '******CSV2List({0:}, {1:})******'.format(_filename, _column))
        _filelist = []  # set blank list to recive data
        for row in csv.reader(open(_filename, newline='')):
            if row: # check if there is data on tha row.
                if row[int(_column)] == '': # check if there is data in the field
                    pass
                else:
                    _filelist.append(row)   # append data to list in UPPER case
        self.p_print(4, Directories._TC['_INFO'], _filelist)
        return(_filelist)
    def CleanBlankRows(self,_list):             # Used to remove Blank Rows from lists.
        self.p_print(4, Directories._TC['_HEADING'], '******CleanBlankRows(_list(see list _DEBUG = 5))******')
        self.p_print(5, Directories._TC['_HEADING'], '******CleanBlankRows({0:})******'.format(_list))
        _cleanlist = [] # set blank list to recive data
        for row in _list:
            if row: # check if there is data on tha row.
                _cleanlist.append(row)  # append data to list in UPPER case
        return(_cleanlist)
    def is_good_char (self, _char):
        return(ord(_char) <= 127)
    def clean_str (self, _str):
        return(''.join(filter(self.is_good_char,_str)))
    def Dupcheck(self, _list):                  # Used to checks for duplicates data in a list.
        self.p_print(4, Directories._TC['_HEADING'], '******Dupcheck(_list(see list _DEBUG = 5))******')
        self.p_print(5, Directories._TC['_HEADING'], '******Dupcheck({0:})******'.format(_list))
        _nodup = []
        for row in _list:
            if row not in _nodup:   # checking if data already exits in new list
                _nodup.append(row)
            else:
                pass
        return(_nodup)  # retunr new list
    def p_print(self, _debug, _color, _string): # Used as a specialized Print Command.
        # No Print Heading because of Endless loop.
        if _debug <= _DEBUG:
            print(_color + str(_string) + Directories._TC["_RESET"])
            if _debug >= 4:
                input('Waiting...')   
    def ClearScreen(self):                      # Used to Clear the Screen fo rthe UI, based on the OS being used.
        if sys.platform == 'win32': # Windows
            os.system('cls')
        elif sys.platform == 'darwin':  # macOS
            os.system('clear')
    def GetSingleList(self, _list, _column):    # Used to get one column of data from a csv List.
        self.p_print(4, Directories._TC['_HEADING'], '******GetSingleList(_INVlist(see list _DEBUG = 5), {0:})******'.format(_column))
        self.p_print(5, Directories._TC['_HEADING'], '******GetSingleList({0:}, {1:})******'.format(_list, _column))
        _Slist = []
        for _row in _list:
            if _row[int(Directories._INV_ROW[_column])].lstrip('0'):
                if _row[int(Directories._INV_ROW[_column])].upper().lstrip('0') not in _Slist:
                    _Slist.append(_row[int(Directories._INV_ROW[_column])].upper().lstrip())
        self.p_print(4, Directories._TC['_YELLOW'], _Slist)        
        return(_Slist)
    def AssetDisply(self, _list):       # Used to Print Asset info to UI
        self.p_print(4, Directories._TC['_HEADING'], '******AssetDisplay(_list(_list(see list _DEBUG = 5))******')
        self.p_print(5, Directories._TC['_HEADING'], '******AssetDisplay({0:})******'.format(_list))
        if len(_list) > 2:
            return('{0:>18} : {1:19} : {2:26} : {3:10} : {4:20} : {5:20} : {6:3} - {7:}'.format(
                _list[0], 
                _list[1], 
                _list[2], 
                _list[3], 
                _list[4], 
                _list[5], 
                _list[6], 
                _list[7]))
    def DisplayCurrentScan(self, _cscanlist, _rm='ALL'):    # Used to display asset info from the current scan list to the UI.
        self.p_print(4, Directories._TC["_HEADING"], "******DisplayCurrentScan(_cscanlist(_list(see list _DEBUG = 5), {0:})******".format(_rm))
        self.p_print(5, Directories._TC["_HEADING"], "******DisplayCurrentScan({0:}, {1:})******".format(_cscanlist, _rm))
        data = self.jsonOpenSave('OPEN', '')
        for asset in _cscanlist:
            data_list = []
            self.p_print(4, Directories._TC['_INFO'], asset)
            if asset in data:
                for i in data[asset]:
                    data_list.append(i["Asset"])
                    data_list.append(i["Serial #"])
                    data_list.append(i["Name"])
                    data_list.append(i["Room #"])
                    data_list.append(i["Wired Mac Addr"])
                    data_list.append(i["Wireless Mac Addr"])
                    data_list.append(i["School #"])
                    data_list.append(i["School Name"])
                self.p_print(5, Directories._TC['_INFO'], data_list)    
                if i["Serial #"]:   # control point, based on serial # 
                    self.AssetDisply(data_list)
                else:
                    self.AssetDisply(data_list)
    def DisplayScanned(self, _scan,):
        self.data = self.jsonOpenSave('OPEN', '')
        self._scan = _scan
        self.data_list = []

        if self._scan in self.data:
            self.data_list.append(self.data[self._scan]["Asset"])
            self.data_list.append(self.data[self._scan]["Serial #"])
            self.data_list.append(self.data[self._scan]["Name"])
            self.data_list.append(self.data[self._scan]["Room #"])
            self.data_list.append(self.data[self._scan]["Wired Mac Addr"])
            self.data_list.append(self.data[self._scan]["Wireless Mac Addr"])
            self.data_list.append(self.data[self._scan]["School #"])
            self.data_list.append(self.data[self._scan]["School Name"])
            self.p_print(5, Directories._TC['_INFO'], self.data_list)    
        else:
            self.data_list.append(_scan)
            self.data_list.append('')
            self.data_list.append('')
            self.data_list.append('')
            self.data_list.append('')
            self.data_list.append('')
            self.data_list.append('')
            self.data_list.append('')
        return(self.AssetDisply(self.data_list))
    def CheckScan(self, _scan):      # Used to Check the asset tag that has been entered agesnt the inventory database.
        self.p_print(4, Directories._TC['_HEADING'], '******CheckScan({0:})******'.format(_scan))
        global currentscanlist
        self._scan = _scan
        self.data = self.jsonOpenSave('OPEN', '')
        if self._scan in self.data or self._scan.lstrip('0') in self.data:
            currentscanlist.append(self._scan)
            self.save2db(self._scan)
            self.p_print(4, Directories._TC['_INFO'], 'ASSET TAG FOUND') 
        else:
            currentscanlist.append(self._scan)
            self.newAssetRecord(self._scan)
            self.save2db(self._scan)
            self.p_print(4, Directories._TC['_INFO'], 'ASSET TAG NOT FOUND')   
    def numberChecker(self, _scan):             # checks the entered asset tag to enforce numbers only
        self.p_print(4, Directories._TC['_HEADING'], '******numberChecker({0:})******'.format(_scan))
        checklist = []
        for num in _scan:
            if num in '1234567890':
                checklist.append('GREEN')
            else:
                checklist.append('RED')
        if 'RED' in checklist:
            self.p_print(2, Directories._TC['_RED'], "Invalid Entry")
            return(False) 
        else:
            return(_scan)   # Green across the board!
    def ScanYearGen(self):                      # generats the year code, based on what month it is. (i.e. 19-29)
        self.p_print(4, Directories._TC['_HEADING'], '******ScanYearGen()******')
        now =  date.today()
        tyear = now.year
        tmonth = now.month
        return("{0:}-{1:}".format(str(tyear)[2:], str(tyear+1)[2:]) if tmonth > 6 else "{0:}-{1:}".format(str(tyear-1)[2:], str(tyear)[2:]))
    def TimeStamp(self):
        self.p_print(4, Directories._TC['_HEADING'], '******ScanYearGen()******')
        now =  date.today()
        return(str(now.strftime("%Y")) + str(now.strftime("%m")) + str(now.strftime("%d")) + str(now.strftime("%H")) + str(now.strftime("%M")))
    def autoSave(self, _scan):                  # writes scan to the autosave file.
        self.p_print(4, Directories._TC['_HEADING'], '******autoSave()******')
        self.CSVwriter(autoSave_file, _scan)
    def save2db(self, _scan):                          # Save changes to database.
        self.p_print(4, Directories._TC['_HEADING'], '******save2db({0:})******'.format(_scan))
        self.data = self.jsonOpenSave('OPEN', '')
        self._scan = _scan

        self.p_print(4, Directories._TC["_INFO"], self.data[self._scan])
        self.p_print(4, Directories._TC["_INFO"], self.ScanYearGen())
        self.p_print(4, Directories._TC["_INFO"], self.data[self._scan]["Scan Year"])

        if self.ScanYearGen() in self.data[self._scan]["Scan Year"]:    # check if Year code is already in the list.
            pass
        else:
            # print(i["Scan Year"])
            self.data[self._scan]["Scan Year"].append(self.ScanYearGen())
        self.p_print(4, Directories._TC["_INFO"], self.data[self._scan]["Scan Year"])
        self.p_print(4, Directories._TC["_INFO"], self.data[self._scan])
            
        self.jsonOpenSave('SAVE', self.data)
        self.p_print(4, Directories._TC["_INFO"], self.data[self._scan])
    def Serial2Asset(self, _serial):
        self.p_print(4, Directories._TC['_HEADING'], '******Serial2Asset({0:})******'.format(_serial))
        self.data = self.jsonOpenSave('OPEN', '')
        self._serial = _serial

        for asset in self.data:
            if self.data[asset]["Serial #"] == self._serial:
                return(self.data[asset]["Asset"])
    def newAssetRecord(self, _scan):            # create new blank record in pyventory_db
        self.p_print(4, Directories._TC['_HEADING'], '******newAssetRecord({0:})******'.format(_scan))
        data = self.jsonOpenSave('OPEN', '')
        data[_scan] = {}
        data[_scan].update({
            "Asset": _scan,
            "Serial #": "",
            "Class": "",       
            "Device Type": "",    
            "Make": "",
            "Model": "",
            "Cpu": "",
            "Product #": "",
            "Ram": "",
            "OS": "",
            "Hdd": "",
            "School #": "",
            "Room #": "",
            "Username": "",
            "IP Addr": "",
            "Name": "",        
            "Wired Mac Addr": "",
            "Wireless Mac Addr": "",
            "Server Mac Addr": "",
            "InstallDate": "",
            "Owner": "",
            "UserType": "",    
            "Status": "",      
            "Mfg Year": "",
            "Rotation Year": "",    
            "Rotation Eligible": "",        
            "School Name": "",    
            "Scan Year": [],
            })
        self.jsonOpenSave("SAVE", data)
    def jsonOpenSave(self, _opensave, _info=''):
        if _opensave.upper() == "OPEN": 
            with open(pyventory_db) as pv_data:
                data = json.load(pv_data)
                return(data)
        if _opensave.upper() == "SAVE":
            with open(pyventory_db, 'w') as outfile:    # open database file and write over it with new data
                json.dump(_info, outfile, sort_keys=True, indent=4) # sort_key will sort the records and indent organizes the file to easy to read json.
                # json.dump(_info, outfile) # sort_key will sort the records and indent organizes the file to easy to read json.
    def prograssSchoolList(self):
        schoollist = []
        data = self.jsonOpenSave('OPEN') 
        for i in data:
            if str(data[i]['School #']) not in schoollist and len(data[i]['School #']) == 3:
                schoollist.append(data[i]['School #'])
        self.p_print(4, Directories._TC['_INFO'], schoollist)
        schoollist.sort()
        return(schoollist)
    def progressRoomList(self, school='SCHOOL'):
        win = Windows()
        roomlist = []
        data = self.jsonOpenSave('OPEN')
        
        if school == 'SCHOOL':
            for i in data:
                if data[i]['Room #']:
                    if data[i]['Room #'].upper() not in roomlist:
                        roomlist.append(data[i]['Room #'].upper())
        else:
            for i in data:
                if school in data[i]['School #']:
                    if data[i]['Room #'].upper() not in roomlist:
                        roomlist.append(data[i]['Room #'].upper())
        self.p_print(4, Directories._TC['_INFO'], roomlist)
        
        roomlist.sort()
        return(roomlist)
    def progressDisplay(self, school='ALL'):
        schoollist = self.prograssSchoolList()
        if school == 'ALL':
            for s in schoollist:
                self.p_print(1, Directories._TC['_HEADING'], '|{0:<20}|{1:>4}/{2:<4}|{3:>5}%|'.format(
                        s,
                        self.scannedInSchool(s),
                        self.totalInSchool(s),
                        ('0' if int(self.scannedInSchool(s)) == 0 else str((int(self.scannedInSchool(s))/int(self.totalInSchool(s)))*100)[:3])))
                for r in self.progressRoomList(s):
                    self.p_print(1, (Directories._TC['_GREEN'] if ((self.scannedInRoom(s, r)/self.totalInRoom(s, r))*100 if self.scannedInRoom(s, r) > 0 else 0) > 99 else Directories._TC['_RESET']), '|{0:^20}|{1:>4}/{2:<4}|{3:>5}%|'.format(
                        '{BLANK}' if r == '' else r.replace('\u000b', ''),
                        self.scannedInRoom(s, r),
                        self.totalInRoom(s, r),
                        (0 if self.scannedInRoom(s, r) < 1 else str((self.scannedInRoom(s, r)/self.totalInRoom(s, r))*100)[:3])))
        
        elif school in schoollist:
            self.p_print(1, Directories._TC['_HEADING'], '|{0:<20}|{1:>4}/{2:<4}|{3:>5}%|'.format(
                        school,
                        self.scannedInSchool(school),
                        self.totalInSchool(school),
                        ('0' if int(self.scannedInSchool(school)) == 0 else str((int(self.scannedInSchool(school))/int(self.totalInSchool(school)))*100)[:3])))
            for r in self.progressRoomList(school):
                self.p_print(1, (Directories._TC['_GREEN'] if ((self.scannedInRoom(school, r)/self.totalInRoom(school, r))*100 if self.scannedInRoom(school, r) > 0 else 0) > 99 else Directories._TC['_RESET']), '|{0:^20}|{1:>4}/{2:<4}|{3:>5}%|'.format(
                    '{BLANK}' if r == '' else r.replace('\u000b', ''),
                    self.scannedInRoom(school, r),
                    self.totalInRoom(school, r),
                    (0 if self.scannedInRoom(school, r) < 1 else str((self.scannedInRoom(school, r)/self.totalInRoom(school, r))*100)[:3])))
    def scannedInRoom(self, school, room): 
        count = 0
        data = self.jsonOpenSave('OPEN')
        for i in data:
            if data[i]['School #'] == school and data[i]['Room #'].upper() == room and self.ScanYearGen() in data[i]['Scan Year']:
                count += 1
        return(count)
    def scannedInSchool(self, school):
        count = 0
        data = self.jsonOpenSave('OPEN')
        for i in data:
            if data[i]['School #'] == school and self.ScanYearGen() in data[i]['Scan Year']:
                count += 1
        return(count)
    def totalInRoom(self, school, room):
        count = 0
        data = self.jsonOpenSave('OPEN')
        for i in data:
            if data[i]['School #'] == school and data[i]['Room #'].upper() == room:
                count += 1
        return(count)
    def totalInSchool(self, school):
        count = 0
        data = self.jsonOpenSave('OPEN')
        for i in data:
            if data[i]['School #'] == school:
                count += 1
        return(count)
    def progressRoomDisplay(self, school, room):
        data = self.jsonOpenSave('OPEN', '')
        assetsinroom = []
        
        for i in data:
            for r in data[i]:
                if r['School #'].upper() == school and r['Room #'].upper() == room:
                    assetsinroom.append(r['Asset'])
        for asset in assetsinroom:
            data_list = []
            self.p_print(4, Directories._TC['_INFO'], asset)
            for i in data[asset]:
                data_list.append(i["Asset"])
                data_list.append(i["Serial #"])
                data_list.append(i["Name"])
                data_list.append(i["Room #"])
                data_list.append(i["Wired Mac Addr"])
                data_list.append(i["Wireless Mac Addr"])
                data_list.append(i["School #"])
                data_list.append(i["School Name"])
            self.p_print(5, Directories._TC['_INFO'], data_list)    
            
            if self.ScanYearGen() in i["Scan Year"]:   # control point, based on serial # 
                self.AssetDisply(data_list)
            else:
                self.AssetDisply(data_list)
    def assetsinroom(self, _school, _room):
        self.data = self.jsonOpenSave('OPEN')
        self.assetslist = []
        for asset in self.data:
                if self.data[asset]['School #'] == _school and self.data[asset]['Room #'].upper() == _room.upper():
                    self.assetslist.append(self.data[asset]['Asset'])
        self.assetslist.sort()
        return(self.assetslist)
    def assetstatus(self, _asset):
        self.data = self.jsonOpenSave('OPEN')
        self.asset = _asset
        if self.ScanYearGen() in self.data[self.asset]['Scan Year']:
            return('CHECKED')
        else:
            return('UNCHECKED')
    def RecordeRemover(self, _asset):
        self.data = self.jsonOpenSave('OPEN')
        if _asset in self.data:
            print(self.data[_asset])
            # self.data[_asset].clear()
            del self.data[_asset]
        if _asset in self.data:
            print(self.data[_asset])
        self.jsonOpenSave("SAVE", self.data)
    def AutoChecker(self, _LSdate):
        AutoCutil = Utilities()
        self.CutOff = 2
        self._CurrentDate = date.today()
        self._LSdate = _LSdate

        if int(self._LSdate.strftime('%Y')) == int(self._CurrentDate.strftime('%Y')) and int(self._LSdate.strftime('%m')) > (int(self._CurrentDate.strftime('%m')) - self.CutOff):
            return(True)

        elif int(self._CurrentDate.strftime('%m')) <= self.CutOff and self._LSdate.strftime('%m') >= (12 - (self.CutOff - int(self._CurrentDate.strftime('%m')))):
            return(True)
        else:
            return(False)
    def DbCleanUp(self):
        self.data = self.jsonOpenSave('OPEN', '')
        deleterecordlist = []
        for record in self.data:
            # print(self.ScanYearGen(), self.data[record]["Scan Year"])
            if self.ScanYearGen() not in self.data[record]["Scan Year"]:    # check if Year code is already in the list.
                deleterecordlist.append(record)
        # print(self.data['103059']['Asset'])
        for record in deleterecordlist:
            # print(self.data[record])
            if self.data[record]['Asset'] in deleterecordlist:
                self.data.pop(record, None)
        self.jsonOpenSave('SAVE', self.data)
        messagebox.showinfo("Database Cleanup", "the Database have been cleaned up")

class Interface:
    def __init__(self):
        pass
    def Menu(self, _logo = "Main", _help = "Main"):
        global currentscanlist
        self._logo = _logo
        self._help = _help
        self.interfaceResponce = 'Main'
        mainUtil = Utilities()
        
        mainUtil.p_print(4, Directories._TC['_HEADING'], '******Interface.Menu()******')
        while self.interfaceResponce.upper() != "X" and self.interfaceResponce.upper() != "EXIT":
            if mainUtil.Help(self.interfaceResponce) == 'null':
                self.interfaceResponce = 'Main'
                self._logo = self.interfaceResponce
            mainUtil.ClearScreen()
            mainUtil.Logo(self._logo)
            mainUtil.p_print(1, Directories._TC["_INFO"], mainUtil.pyventory_db_check())
            mainUtil.p_print(2, Directories._TC["_YELLOW"], mainUtil.Help(self._logo))
            
            if self.interfaceResponce.upper() == "SCAN":
                while self.interfaceResponce.upper() == "SCAN":
                    mainUtil.ClearScreen()
                    mainUtil.Logo(self._logo)
                    mainUtil.p_print(2, Directories._TC["_YELLOW"], mainUtil.Help(self._logo))
                    mainUtil.p_print(1, Directories._TC['_HEADING'], '{0:>10} : {1:16} : {2:17} : {3:12} : {4:19} : {5:19} : {6:3} - {7:}'.format(
                        'Asset Tag', 
                        'Serial #', 
                        'Name', 
                        'Room #', 
                        'Wire MAC', 
                        'Wireless MAC', 
                        'School #', 
                        'Name'))
                    mainUtil.DisplayCurrentScan(currentscanlist)
                    self.scanResponce = input("Scan-")
                    if self.scanResponce.upper() == 'X' or self.scanResponce.upper() == "EXIT":
                        mainUtil.save2db()
                        self.interfaceResponce = "null"
                    elif self.scanResponce.upper() == 'HELP':
                        mainUtil.p_print(1, Directories._TC["_YELLOW"], mainUtil.Help(self._logo))
                    elif mainUtil.numberChecker(str(self.scanResponce).lstrip('0')) == str(self.scanResponce).lstrip('0'):
                        mainUtil.CheckScan(str(self.scanResponce).lstrip('0'))
                    else:
                        pass  

            if self.interfaceResponce.upper() == "PROGRESS":
                data = mainUtil.jsonOpenSave('OPEN')
                schoollist = mainUtil.prograssSchoolList()
                while self.interfaceResponce.upper() == "PROGRESS":
                    self.pregressResponce = input("Progress-")
                    if self.pregressResponce.upper() == "X" or self.pregressResponce.upper() == "EXIT":
                        self.interfaceResponce = "null"
                    elif self.pregressResponce.upper() == "HELP":
                        mainUtil.p_print(2, Directories._TC["_YELLOW"], mainUtil.Help(self._logo))
                    elif self.pregressResponce.upper() == "ALL":
                        mainUtil.progressDisplay()
                    elif self.pregressResponce.upper() in schoollist:
                        while self.pregressResponce.upper() in schoollist:
                            roomlist = mainUtil.progressRoomList(self.pregressResponce.upper())
                            self.schoolResponce = input("Progress/" + self.pregressResponce.upper() + '-')
                            if self.schoolResponce.upper() == 'X' or self.schoolResponce.upper() == 'EXIT':
                                 self.pregressResponce = 'null'

                            elif self.schoolResponce.upper() == "HELP":
                                mainUtil.p_print(2, Directories._TC["_YELLOW"], mainUtil.Help(self._logo))

                            elif self.schoolResponce.upper() == 'ALL':
                                mainUtil.progressDisplay(self.pregressResponce.upper())
                            
                            elif self.schoolResponce.upper() in roomlist:
                                mainUtil.progressRoomDisplay(self.pregressResponce, self.schoolResponce.upper())
                            elif mainUtil.numberChecker(str(self.schoolResponce).lstrip('0')) == str(self.schoolResponce).lstrip('0'):
                                mainUtil.CheckScan(str(self.schoolResponce).lstrip('0'))
                                mainUtil.save2db()    
                    
            if self.interfaceResponce.upper() == "UPDATE":
                mainUtil.pyventory_db_update(mainUtil.FileBrowser(".csv", False))
                self.interfaceResponce = "none"
            
            if self.interfaceResponce.upper() == "DELETE":
                while self.interfaceResponce.upper() == 'DELETE':
                    mainUtil.ClearScreen()
                    mainUtil.Logo(self._logo)
                    mainUtil.p_print(2, Directories._TC["_YELLOW"], mainUtil.Help(self._logo))
                    data = mainUtil.jsonOpenSave('OPEN')
                    mainUtil.p_print(1, Directories._TC['_WARNING'], 'PLEASE ENTER THE ASSET NUMBER YOU WANT TO REMOVE.')
                    self.deleteResponce = input("Delete Record-")
                    if self.deleteResponce.upper() == 'HELP':
                        mainUtil.p_print(2, Directories._TC["_YELLOW"], mainUtil.Help(self._logo))
                    if self.deleteResponce.upper() == "X" or self.deleteResponce.upper() == "EXIT":
                        self.interfaceResponce = 'null'
                    if str(self.deleteResponce).lstrip('0') in data:
                        for i in data:
                            if i == str(self.deleteResponce).lstrip('0'):
                                del data[str(self.deleteResponce).lstrip('0')]
                                mainUtil.p_print(1, Directories._TC['_WARNING'], '{0:} Has Been Removed.'.format(str(self.deleteResponce).lstrip('0')))
                                break
                        mainUtil.jsonOpenSave('SAVE', data)

            if self.interfaceResponce == 'Main':
                self.interfaceResponce = input(self._logo + " Menu-")
                if mainUtil.Help(self.interfaceResponce) != 'null':         #is there is no help menu for the entry restart MENU()
                    self._logo = self.interfaceResponce
                    self._help = self.interfaceResponce   
class Windows:
    def AssetReport(self, _asset):
        AssetReportutil = Utilities()
        self.data = AssetReportutil.jsonOpenSave('OPEN')
        
        if 'asset' in self.progresstreeview.selection()[0]:
            self._asset = self.progresstreeview.selection()[0].split('-')[2][5:]
        
            self.AssetReportwindow = Toplevel()
            self.AssetReportwindow.geometry("800x600") #Width x Height
            self.AssetReportwindow.title('Asset Report')

            #tech idetification
            self.techIDframe = LabelFrame(self.AssetReportwindow, pady=10, padx=10)
            self.techIDLabel = Label(self.techIDframe, text='Technology Identification', padx=7, bg='black', fg='white')

            self.seriallabel = Label(self.techIDframe, text='Serial #', padx=7)
            self.serialentry = Entry(self.techIDframe, width=25, bg='light gray')
            
            self.tagelabel = Label(self.techIDframe, text='ASD #', padx=7)
            self.tageentry = Entry(self.techIDframe, width=15, bg='light gray')

            self.typelabel = Label(self.techIDframe, text='Type',padx=7)
            self.typeentry = Entry(self.techIDframe, bg='light gray')

            self.statuslabel = Label(self.techIDframe, text='STATUS',padx=7)
            self.statusentry = Entry(self.techIDframe, width=21, bg='light gray')

            # Computer Information
            self.compinfoframe = LabelFrame(self.AssetReportwindow, pady=10, padx=10)
            self.compinfoLabel = Label(self.compinfoframe, text='Computer Information', padx=7, bg='black', fg='white')

            self.makeLabel = Label(self.compinfoframe, text='Make', padx=7)
            self.makeentry = Entry(self.compinfoframe, width=40, bg='light gray')

            self.modellabel = Label(self.compinfoframe, text='Model', padx=7)
            self.modelentry = Entry(self.compinfoframe, width=25, bg='light gray')

            self.CPUSpeedlabel = Label(self.compinfoframe, text='CPU Speed', padx=7)
            self.CPUSpeedentry = Entry(self.compinfoframe, width=40, bg='light gray')

            self.Productlabel = Label(self.compinfoframe, text='Product #',padx=7)
            self.Productentry = Entry(self.compinfoframe, width=25, bg='light gray')

            self.ramlabel = Label(self.compinfoframe, text='RAM',padx=7)
            self.ramentry = Entry(self.compinfoframe, width=14, bg='light gray')

            self.oslabel = Label(self.compinfoframe, text='OS',padx=7)
            self.osentry = Entry(self.compinfoframe, width=52, bg='light gray')

            self.harddrivelabel = Label(self.compinfoframe, text='Hard Drive',padx=7)
            self.harddriveentry = Entry(self.compinfoframe, width=14, bg='light gray')

            #Details 
            self.detailframe = LabelFrame(self.AssetReportwindow, pady=10, padx=10)
            self.detailLabel = Label(self.detailframe, text='Details', padx=7, bg='black', fg='white')
            #school #
            self.schoolnumberlabel = Label(self.detailframe, text='School #', padx=7)
            self.schoolnumberentry = Entry(self.detailframe, width=20, bg='light gray')
            #Room
            self.roomlabel = Label(self.detailframe, text='Room', padx=7)
            self.roomentry = Entry(self.detailframe, width=15, bg='light gray')
            #User
            self.userlabel = Label(self.detailframe, text='User', padx=7)
            self.userentry = Entry(self.detailframe, width=25, bg='light gray')
            #School Name
            self.schoolnameentry = Entry(self.detailframe, width=25, bg='light gray')
            
            #IP Sddress
            self.ipaddresslabel = Label(self.detailframe, text='IP Address', padx=7)
            self.ipaddressentry = Entry(self.detailframe, width=25, bg='light gray')
            # Installed
            self.installdatelabel = Label(self.detailframe, text='Installed', padx=7)
            self.installdateentry = Entry(self.detailframe, width=21, bg='light gray')
            # Computer Name
            self.computernamelabel = Label(self.detailframe, text='Computer Name', padx=7)
            self.computernameentry = Entry(self.detailframe, width=25, bg='light gray')
            # Owner
            self.ownerlabel = Label(self.detailframe, text='Owner', padx=7)
            self.ownerentry = Entry(self.detailframe, width=21, bg='light gray')
            # Wired MAC
            self.wiredmaclabel = Label(self.detailframe, text='wired MAC', padx=7)
            self.wiredmacentry = Entry(self.detailframe, width=25, bg='light gray')
            # User type
            self.usertypelabel = Label(self.detailframe, text='User Type', padx=7)
            self.usertypeentry = Entry(self.detailframe, width=21, bg='light gray')
            # Wireless MAC
            self.wirelessmaclabel = Label(self.detailframe, text='Wireless Mac', padx=7)
            self.wirelessmacentry = Entry(self.detailframe, width=25, bg='light gray')
            # status
            self.computerstatuslabel = Label(self.detailframe, text='Status', padx=7)
            self.computerstatusentry = Entry(self.detailframe, width=21, bg='light gray')
            # MAC3
            self.mac3label = Label(self.detailframe, text='MAC3', padx=7)
            self.mac3entry = Entry(self.detailframe, width=25, bg='light gray')
            # Mfg year
            self.mfgyearlabel = Label(self.detailframe, text='Mfg Year', padx=7)
            self.mfgyearentry = Entry(self.detailframe, width=21, bg='light gray')
            # Net Used
            self.netusedlabel = Label(self.detailframe, text='Net Use', padx=7)
            self.netusedentry = Entry(self.detailframe, width=25, bg='light gray')
            # Year to be Rotated
            self.rotationyearlabel = Label(self.detailframe, text='Year to be Rotated', padx=7)
            self.rotationyearentry = Entry(self.detailframe, width=21, bg='light gray')
            # eligible for rotation
            self.rotationeligiblelabel = Label(self.detailframe, text='eligible for Rotation', padx=7)
            self.rotationeligibleentry = Entry(self.detailframe, width=21, bg='light gray')

            # grid 
            # tech id
            self.techIDframe.grid(column=0, row=0)
            self.techIDLabel.grid(column=0, row=0, columnspan=2, sticky='w')

            self.seriallabel.grid(column=0, row=1, sticky='e')
            self.serialentry.grid(column=1, row=1, sticky='w')

            self.tagelabel.grid(column=2, row=1, sticky='e')
            self.tageentry.grid(column=3, row=1, sticky='w')

            self.typelabel.grid(column=4, row=1, sticky='e')
            self.typeentry.grid(column=5, row=1, sticky='w')

            self.statuslabel.grid(column=6, row=1, sticky='e')
            self.statusentry.grid(column=7, row=1, sticky='w')

            # computer info
            self.compinfoframe.grid(column=0, row=1)
            self.compinfoLabel.grid(column=0, row=0, columnspan=2, sticky='w')

            self.makeLabel.grid(column=0, row=1, sticky='e')
            self.makeentry.grid(column=1, row=1, sticky='w')

            self.modellabel.grid(column=2, row=1, sticky='e')
            self.modelentry.grid(column=3, row=1, sticky='w')

            self.CPUSpeedlabel.grid(column=0, row=2, sticky='e')
            self.CPUSpeedentry.grid(column=1, row=2, sticky='w')

            self.Productlabel.grid(column=2, row=2, sticky='e')
            self.Productentry.grid(column=3, row=2, sticky='w')

            self.ramlabel.grid(column=4, row=2, sticky='e')
            self.ramentry.grid(column=5, row=2, sticky='w')

            self.oslabel.grid(column=0, row=3, sticky='e')
            self.osentry.grid(column=1, row=3, sticky='w', columnspan=2)

            self.harddrivelabel.grid(column=4, row=3, sticky='e')
            self.harddriveentry.grid(column=5, row=3, sticky='w')

            #details
            self.detailframe.grid(column=0, row=2)
            self.detailLabel.grid(column=0, row=0, columnspan=2, sticky='w')

            self.schoolnumberlabel.grid(column=0, row=1, sticky='e')
            self.schoolnumberentry.grid(column=1, row=1, sticky='w')
            
            self.roomlabel.grid(column=2, row=1, sticky='e')
            self.roomentry.grid(column=3, row=1, sticky='w')
            
            self.userlabel.grid(column=4, row=1, sticky='e')
            self.userentry.grid(column=5, row=1, sticky='w')
            
            self.schoolnameentry.grid(column=0, row=2, sticky='e')
            

            self.ipaddresslabel.grid(column=0, row=3, sticky='e')
            self.ipaddressentry.grid(column=1, row=3, sticky='w')

            self.installdatelabel.grid(column=2, row=3, sticky='e')
            self.installdateentry.grid(column=3, row=3, sticky='w')

            self.computernamelabel.grid(column=0, row=4, sticky='e')
            self.computernameentry.grid(column=1, row=4, sticky='w')

            self.ownerlabel.grid(column=2, row=4, sticky='e')
            self.ownerentry.grid(column=3, row=4, sticky='w')

            self.wiredmaclabel.grid(column=0, row=5, sticky='e')
            self.wiredmacentry.grid(column=1, row=5, sticky='w')

            self.usertypelabel.grid(column=2, row=5, sticky='e')
            self.usertypeentry.grid(column=3, row=5, sticky='w')

            self.wirelessmaclabel.grid(column=0, row=6, sticky='e')
            self.wirelessmacentry.grid(column=1, row=6, sticky='w')

            self.computerstatuslabel.grid(column=2, row=6, sticky='e')
            self.computerstatusentry.grid(column=3, row=6, sticky='w')

            self.mac3label.grid(column=0, row=7, sticky='e')
            self.mac3entry.grid(column=1, row=7, sticky='w')

            self.mfgyearlabel.grid(column=2, row=7, sticky='e')
            self.mfgyearentry.grid(column=3, row=7, sticky='w')

            self.netusedlabel.grid(column=0, row=8, sticky='e')
            self.netusedentry.grid(column=1, row=8, sticky='w')
            
            self.rotationyearlabel.grid(column=2, row=8, sticky='e')
            self.rotationyearentry.grid(column=3, row=8, sticky='w')

            self.rotationeligiblelabel.grid(column=2, row=9, sticky='e')
            self.rotationeligibleentry.grid(column=3, row=9, sticky='w')

            # add text to entries

            self.check = AssetReportutil.assetstatus(self._asset)
            self.tageentry.insert(0, self.data[self._asset]['Asset'])
            self.serialentry.insert(0, self.data[self._asset]['Serial #'])
            self.schoolnameentry.insert(0, self.data[self._asset]['School Name'])
            self.typeentry.insert(0, self.data[self._asset]['Device Type'])
            self.statusentry.insert(0, self.check)
            self.makeentry.insert(0, self.data[self._asset]['Make'])
            self.modelentry.insert(0, self.data[self._asset]['Model'])
            self.CPUSpeedentry.insert(0, self.data[self._asset]['Cpu'])
            self.Productentry.insert(0, self.data[self._asset]['Product #'])
            self.ramentry.insert(0, self.data[self._asset]['Ram'])
            self.osentry.insert(0, self.data[self._asset]['OS'])
            self.harddriveentry.insert(0, self.data[self._asset]['Hdd'])
            self.schoolnumberentry.insert(0, self.data[self._asset]['School #'])
            self.roomentry.insert(0, self.data[self._asset]['Room #'])
            self.userentry.insert(0, self.data[self._asset]['Username'])
            self.ipaddressentry.insert(0, self.data[self._asset]['IP Addr'])
            self.installdateentry.insert(0, self.data[self._asset]['InstallDate'])
            self.computernameentry.insert(0, self.data[self._asset]['Name'])
            self.ownerentry.insert(0, self.data[self._asset]['Owner'])
            self.wiredmacentry.insert(0, self.data[self._asset]['Wired Mac Addr'])
            self.usertypeentry.insert(0, self.data[self._asset]['UserType'])
            self.wirelessmacentry.insert(0, self.data[self._asset]['Wireless Mac Addr'])
            self.computerstatusentry.insert(0, self.data[self._asset]['Status'])
            self.mac3entry.insert(0, self.data[self._asset]['Server Mac Addr'])
            self.mfgyearentry.insert(0, self.data[self._asset]['Mfg Year'])
            # self.netusedentry.insert(0, self.data[self._asset][''])
            self.rotationyearentry.insert(0, self.data[self._asset]['Rotation Year'])
            self.rotationeligibleentry.insert(0, self.data[self._asset]['Rotation Eligible'])
            self.AssetReportwindow.mainloop()
    def bulkchecker(self):
        bulkutil = Utilities()
        self.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
        self.data = bulkutil.jsonOpenSave('OPEN', '')
        messagebox.showinfo("Bulk Checker", 'press ok and wait until the Complete Message apperes.')
        for i in bulkutil.CSV2List(self.filename):
            bulkutil.p_print(4, Directories._TC['_INFO'], i[0])
            bulkutil.CheckScan(i[0])
        messagebox.showinfo('bulk checker', 'bulk check complete')
    def Checker(self):
        checkutil = Utilities()
        self._scan = self.Scan.get()
        
        if checkutil.numberChecker(self._scan) == False:
            pass
        else:
            self._data = checkutil.jsonOpenSave('OPEN', '')
            if self._scan.lstrip('0') in self._data:    
                self.cScanList.insert(END, checkutil.DisplayScanned(self._scan.lstrip('0')))
            else:
                self.cScanList.insert(END, checkutil.DisplayScanned(self._scan.lstrip('0')))
                # self.cScanList.configure(bg='red')
            checkutil.CheckScan(self._scan.lstrip('0'))
        self.Scan.delete(first=0, last=100)
    def IndividualWindow(self):
        util = Utilities()
        # self.schoolmenulist = {}

        if os.path.exists(pyventory_db):
            self.schoollist = util.prograssSchoolList()
            self.IndividualMainWindow = Toplevel()
            self.IndividualMainWindow.title('Individual scanner')
            self.IndividualMainWindow.minsize(900, 500) #Width x Height
            self.IndividualMainWindow.columnconfigure(4, weight=1)
            self.IndividualMainWindow.rowconfigure(2, weight=1)        

            self.cScanList = Listbox(self.IndividualMainWindow, bg='black', fg='white', height=30, width=150)
            self.cScanList.insert(END, '{0:>15} : {1:30} : {2:30} : {3:10} : {4:20} : {5:20} : {6:3} - {7:}'.format(
                            'Asset Tag', 
                            'Serial #', 
                            'Name', 
                            'Room #', 
                            'Wire MAC', 
                            'Wireless MAC', 
                            'School #', 
                            'Name'))
            
            self.ScanLabel = Label(self.IndividualMainWindow, text='Asset Tag:')
            self.Scan = Entry(self.IndividualMainWindow, width=30)
            self.EnterButton = Button(self.IndividualMainWindow, text='Enter', padx=10, command=self.Checker)
            self.EnterFrame = Frame(self.IndividualMainWindow, height=5)
                
            self.cScanList.grid(column=0, row=0, columnspan=5, padx=10, pady=10)
            self.ScanLabel.grid(column=2, row=1)
            self.Scan.grid(column=3, row=1)
            self.Scan.focus()
            self.EnterButton.grid(column=4, row=1)
            self.EnterFrame.grid(column=0, row=2)
            self.Scan.bind("<Return>", lambda e:self.Checker())

            self.IndividualMainWindow.mainloop()
        else:
            messagebox.showinfo("Error", "No Database Found run Database>Update")  
    def ProgressWindow(self):
        ProgressWindowutil = Utilities()
        if os.path.exists(pyventory_db):
            self.schoollist = ProgressWindowutil.prograssSchoolList()
            self.schoollist.sort()
            self.ProgressMainWindow = Toplevel()
            self.progresstreeview = ttk.Treeview(self.ProgressMainWindow)       #treeview setup
            self.progresstreeview.config(selectmode='browse')

            self.ProgressMainWindow.title('Progress')
            self.ProgressMainWindow.minsize(1100, 750)
            self.ProgressMainWindow.columnconfigure(4, weight=1)
            self.ProgressMainWindow.rowconfigure(2, weight=1)
            
            self.progresstreeview.config(height=35, columns=('Status', 'Percent'))
            self.progresstreeview.column('#0', width=800)
            self.progresstreeview.column('Status', width=75)
            self.progresstreeview.column('Percent', width=150)
            self.progresstreeview.heading('Status', text='Status')
            self.progresstreeview.heading('Percent', text='Percent complete')

            for schoolnumber in self.schoollist:
                self.schoolID = 'school' + schoolnumber +'-'
                self.progresstreeview.insert('', 'end', self.schoolID, text=('(BLANK)' if schoolnumber == '' else schoolnumber))
                self.roomlist = ProgressWindowutil.progressRoomList(schoolnumber)
                self.progresstreeview.set(self.schoolID, 'Percent', (str(ProgressWindowutil.scannedInSchool(schoolnumber)) + "/" + str(ProgressWindowutil.totalInSchool(schoolnumber))))
                
                self.roomlist.sort()
                for room in self.roomlist:
                    self.devicelist = ProgressWindowutil.assetsinroom(schoolnumber, room)
                    self.roomID = (self.schoolID + 'room' +'(blank)' + '-' if room == '' else self.schoolID + 'room' + room + '-')
                    self.progresstreeview.insert(self.schoolID, 'end', self.roomID, text=('(BLANK)' if room == '' else room))
                    self.progresstreeview.set(self.roomID, 'Percent', (str(ProgressWindowutil.scannedInRoom(schoolnumber, room)) + "/" + str(ProgressWindowutil.totalInRoom(schoolnumber, room))))
                
                    
                    for asset in self.devicelist:
                        self.assetID = self.roomID + 'asset' + asset
                        self.progresstreeview.insert(self.roomID, 'end', self.assetID, text=('(BLANK)' if asset == '' else asset))
                        self.progresstreeview.set(self.assetID, 'Status', ProgressWindowutil.assetstatus(asset))

            self.progresstreeview.bind('<<TreeviewSelect>>', self.AssetReport)

            self.progresstreeview.pack()
            self.ProgressMainWindow.mainloop()
        else:
            messagebox.showinfo("Error", "No Database Found run Database>Update")  
    def Updater(self):
        updateutil = Utilities()
        filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
        if filename:
            updateutil.pyventory_db_update(filename)
            messagebox.showinfo("Database Updater", "Database has been updated with: " + filename)    
    def Auto_WS1(self):
        Auto_WS1util = Utilities()
        self._WS1List = Auto_WS1util.CSV2List(filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*"))))
        self._LastSeenCutoff = 2
        self._CurrentDate = date.today()

        for row in self._WS1List:
            Asset = Auto_WS1util.Serial2Asset(row[Directories._WS1_Col['Serial #']])
            if str(Asset) == "None":
                pass
            else:
                if Auto_WS1util.AutoChecker(datetime.strptime(Auto_WS1util.clean_str(row[Directories._WS1_Col['Last Seen Date']]).replace('"', ""), '%m/%d/%Y %I:%M:%S %p')) is True and Asset is not None:
                    Auto_WS1util.save2db(Asset)   
        messagebox.showinfo("WorkSpace One", "Automation Complete")         
    def Auto_CM(self):
        Auto_CMutil = Utilities()
        self._CMList = Auto_CMutil.CSV2List(filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*"))))
        self._LastSeenCutoff = 2
        self._CurrentDate = date.today()

        for row in self._CMList:
            Asset = Auto_CMutil.Serial2Asset(row[Directories._CM_Col['Serial #']])
            if Auto_CMutil.clean_str(row[Directories._CM_Col['Last Sync Date']]) == 'lastPolicySync':
                pass
            else:
                if Auto_CMutil.AutoChecker(datetime.strptime(Auto_CMutil.clean_str(row[Directories._CM_Col['Last Sync Date']]).replace('"', ""), '%Y-%m-%d %I:%M %p')) is True and Asset is not None:
                    Auto_CMutil.save2db(Asset)
        messagebox.showinfo("Chrome MAnagment", "Automation Complete")
    def Auto_SCCM(self):
        Auto_SCCMutil = Utilities()
        self._SCCMList = Auto_SCCMutil.CSV2List(filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*"))))
        self._LastSeenCutoff = 2
        self._CurrentDate = date.today()

        for row in self._SCCMList:
            if len(row) <= 2:
                pass
            else:
                # print(len(row), row)
                Asset = Auto_SCCMutil.Serial2Asset(row[Directories._SCCM_Col['Serial #']])
                if Asset == '' or Auto_SCCMutil.clean_str(row[Directories._SCCM_Col['Last Active Date']]) == '':
                    pass
                else:
                    if row[Directories._SCCM_Col['Last Active Date']] == 'Last Activity':
                        pass
                    else:
                        # print(datetime.strptime(Auto_SCCMutil.clean_str(row[Directories._SCCM_Col['Last Active Date']]).replace('"', ""), '%m/%d/%Y  %I:%M:%S %p'))
                        if Auto_SCCMutil.AutoChecker(datetime.strptime(Auto_SCCMutil.clean_str(row[Directories._SCCM_Col['Last Active Date']]).replace('"', ""), '%m/%d/%Y  %I:%M:%S %p')) is True and Asset is not None:
                            Auto_SCCMutil.save2db(Asset)
        messagebox.showinfo("SCCM", "Automation Complete")

#GUI Start
# Main Windows
Main = Tk()
Main.geometry("600x300") #Width x Height
Main.title('Pyventory - 2.0')

# Manu Bar setup
menubar = Menu(Main)

# scan menu
scannerwin = Windows()
ScanMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Scan", menu=ScanMenu) # added after ScanMenu so no error
ScanMenu.add_command(label="Individual", command=scannerwin.IndividualWindow)
ScanMenu.add_command(label = "Bulk", command=scannerwin.bulkchecker)
ScanMenu.add_separator()
ScanMenu.add_command(label = "Close", command=Main.quit)

# Database Menu
dbwin = Windows()
dbutil = Utilities()
DatabaseMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Database", menu=DatabaseMenu)
DatabaseMenu.add_command(label="Update", command=dbwin.Updater)
DatabaseMenu.add_command(label="Progress", command=dbwin.ProgressWindow)
DatabaseMenu.add_command(label = "Cleanup", command=dbutil.DbCleanUp)
# DatabaseMenu.add_command(label = "Delete", command='')

# Automation Menu
autowin = Windows()
AutoMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Automation", menu=AutoMenu)
AutoMenu.add_command(label="WorkSpace One", command=autowin.Auto_WS1)
AutoMenu.add_command(label="Google Managment", command=autowin.Auto_CM)
AutoMenu.add_command(label="SCCM", command=autowin.Auto_SCCM)   
# AutoMenu.add_command(label="", command='')

# Help Menu
# HelpMenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Help", menu=HelpMenu)
# HelpMenu.add_command(label = "About", command='')
# HelpMenu.add_command(label="View Help", command='')
# HelpMenu.add_command(label = "Configure", command='')
# HelpMenu.add_separator()
# HelpMenu.add_command(label = "Check for Update", command='')

# Main Menu Loop
Main.config(menu=menubar)

# Code to add widgets will go here...

spacer = LabelFrame(Main, height=20) # made as a space from the top of the window
spacer.pack()
logopic = PhotoImage(file="img/Logo.gif")
logo = Canvas(Main,bg="black", height=200, width=500)
logo.create_image(502,0, anchor=NE, image=logopic)
logo.pack()

pyventory_version = Label(Main, text=versionnumber)
pyventory_version.pack()

Main.mainloop()