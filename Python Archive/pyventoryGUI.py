#!/Python27/pythonw.exe
#python 2.7
                                                                # Mod for HP Computers ONLY!!!!!!!!
# import all needed libraries
import sys, os, csv
from Tkinter import *

# Gobal Variables
_DEBUG = 0     # 0 = no debuging, 1 =  Print lists on screen, 2 = print Lists to file..

def Logo():                                                     #Just a Cool Heading for the program
    print("\033[1;32m"                                              #set text to green (only works in terminal and powershell)
           " _______________.___.____   _______________ __________________________ _______________.___.       \n"
           " \______   \__  |   |\   \ /   /\_   _____/ \      \__    ___/\_____  \\\______   \__  |   |       \n"
           "  |     ___//   |   | \   Y   /  |    __)_  /   |   \|    |    /   |   \|       _//   |   |       \n"
           "  |    |    \____   |  \     /   |        \/    |    \    |   /    |    \    |   \\\____   |       \n"
           "  |____|    / ______|   \___/   /_______  /\____|__  /____|   \_______  /____|_  // ______| v0.5b \n"
           "            \/                          \/         \/                 \/       \/ \/              \n"
           "\033[1;37m"                                             #set color of text back to white
           )

def HelpScreen():                                               #The Help Screen will
    print(
            "Usage: pyventoryPC.py Master-File Master-Column Check-File [Check-Column]\n"
            " \n"
            "Master-File        The Master File is the file compaired against, this file MUST be in CSV format\n"
            "Master-Column      The Number of the Column in the Master-file you want to check with, MUST be a \n"
            "                   Number\n"
            "Check-File         The Check-File cotains the list of number to check in the Master-File, this \n"
            "                   file MUST be in CSV format\n"
            "/h                 Show this Screen\n"
            "\n"
            "Optional:\n"
            "[Check-Column]     Used to select a specific column to check with\n"
            "                   Without this Number the Default will be used. MUST be a Number"
            "\n"
            "NOTES:\n"
            "The 'Check-File' can also be a folder path that has files that were created using the \n"
            "inventory tag batch file.\n" 
            "if using a network path the path MUST be a maped network Drive. IP address/DNS paths will not work\n"
            "\n"
            "EXAMPLES:\n"
            "pyventory.py Master.csv 1 'z:\inventoryfiles\\' 2\n"
            "pyventory.py Master.csv 1 'z:\inventoryfiles\\' :: Defaults to Serial COLumn\n"
            "pyventory.py Master.csv 1 pcfiles.csv 2\n"
            "pyventory.py Master.csv 1 pcfiles.csv  :: Default to 0\n"
        )

def writefile(_filename, _info):                                #setup file to writ to.
    _writefile = open(_filename, "ab")                              #'ab'will create file also 'wb' will overwrite everytime the file is opened
    _writefilewriter = csv.writer(_writefile)                       #Setup CSV writer
    _writefilewriter.writerow(_info)
    _writefile.close()                                #write info given to def

def Convert2List(_filename, _column):                           #Read data from file and add it to a list. will make list all UPPER case
    _file = open(_filename, 'r')                                    #open file and ('r') read only.
    _filereader = csv.reader(_file)                                 #Setup CSV reader.
    _filelist = []                                                  #set blank list to recive data
    for row in list(_filereader):
        if row:                                                     #check if there is data on tha row.
            if row[_column] == '':                                  #check if there is data in the field
                pass
            else:
                _filelist.append(row.upper())                       #appedn data to list in UPPER case
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
    _LIST = Convert2List(_LISTfile)
    _INV = Convert2List(_INVfile)
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
    _INV = Convert2List(_INVfile)                                   #Send files to be converted to a list of lists
    writefile('INVimport.csv', (['ASD Number', 'Computer Name', 'Serial Number', 'Ethernet 2', 'School Number', 'Room #', 'Product Number', 'Purchase Install Date', 'Model', 'Brand/Make', 'owner', 'Manufacture Date', 'Ram', 'Type', 'User Type', 'User', 'Operating System', 'Notes', 'IP Address', 'NetUse', 'Hard Drive Size', 'CPU Speed', 'Equipment Status', 'Eligible for Replacement', 'Classification', 'z_isActive']))
    if _DEBUG > 0:
        print('FMimport')
        print((['ASD Number', 'Computer Name', 'Serial Number', 'Ethernet 2', 'School Number', 'Room #', 'Product Number', 'Purchase Install Date', 'Model', 'Brand/Make', 'owner', 'Manufacture Date', 'Ram', 'Type', 'User Type', 'User', 'Operating System', 'Notes', 'IP Address', 'NetUse', 'Hard Drive Size', 'CPU Speed', 'Equipment Status', 'Eligible for Replacement', 'Classification', 'z_isActive']))
    for row in _LIST:
        if row[_LISTcol].upper() not in _INV:                       #compaire items and write records to files
            if _DEBUG > 0:
                print(([row[2],row[0],row[1],'' if row[13] == 'None' else row[13],row[0][:3],row[3],'',row[5],row[7],row[7][0:2],row[4],row[12][5:],row[10],DeviceType(row[7]),'Student' if row[0][6] in str(range(0,10))  else 'Teacher',FindUser(row[0]),row[9][10:-10],'','DHCP','DATA',row[11],row[8],'Active','Yes' if row[4].upper() == 'TECHNOLOGY' else 'No','Inventory','1']))
            writefile('INVimport.csv', ([row[2],row[0],row[1],'' if row[13] == 'None' else row[13],row[0][:3],row[3],'',row[5],row[7],row[7][0:2],row[4],row[12][5:],row[10],DeviceType(row[7]),'Student' if str(row[0][6]) in range(0,10)  else 'Teacher',FindUser(row[0]),row[9][10:-10],'','DHCP','DATA',row[11],row[8],'Active','Yes' if row[4].upper() == 'TECHNOLOGY' else 'No','Inventory','1']))
        else:
            pass

class Welcome:
    
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        
        self.photo = PhotoImage(file="PyventoryGuilogo.gif")
        self.logo = Label(frame, image=self.photo)
        self.bframe = Frame(frame, height=50, width=500)
        self.bframe.pack_propagate(0) # don't shrink
        self.button = Button(self.bframe, text="RUN", fg="blue",command=self.inputwindow)
        
        self.logo.pack()
        self.bframe.pack()
        self.button.pack(fill=BOTH, expand=1)

    def inputwindow(self):
        _window = Frame(Tk(), height=200, width=400)
        _window.pack_propagate(0)
        root.destroy()
        _window.pack()
        _INVframe = Frame(_window, height=20, width=400)
        _INVframe.pack_propagate(0)
        _INVframe.pack()
        _INVlabel = Label(_INVframe, text='Inventory File')
        _INVlabel.pack(side=LEFT)
        tkvar = StringVar(_window)
        _menu = ['1','2','3','4','5']
        _INVentry = OptionMenu(_INVframe, tkvar, *_menu)
        _INVentry.pack()

        # _spacer = Frame(_window, height=10)
        # _spacer.pack()

        # _LISTframe = Frame(_window, height=20, width=400)
        # _LISTframe.pack_propagate(0)
        # _LISTframe.pack()
        # _LISTlabel = Label(_LISTframe, text='List File ')
        # _LISTlabel.pack(side=LEFT)
        # _LISTentry = Text(_LISTframe, height=2, width=40)
        # _LISTentry.pack() 

        
        




root = Tk()
app = Welcome(root)

root.mainloop()
root.destroy() # optional; see description below