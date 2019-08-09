#!/Python27/pythonw.exe
#python 2.7
# import all needed libraries
import csv
import os

# tESTING CSV FILE CONDENSING. TRYING TO TAKE INFORMATION FROM MULTIPLE CSV FILES AND PUT IT ALL INTO ONE FOR CHECKING.

# Variables
_FolderLocation = 'y:\InventoryFiles\\'
_filename = 'schoollist.csv'

_dirlist = os.listdir(_FolderLocation)
_schoolfiles = open(_filename, "ab")
_schoolfileswriter = csv.writer(_schoolfiles)
_schoolfileswriter.writerow(['computer name','serialnumber','asset_tag','computermake','computermodel','CPU','os','ram','hdd','Ethernet','Wi-Fi'])


for i in _dirlist:
    _dir = open(os.path.join(_FolderLocation + i), 'r')
    _dirreader = csv.reader(_dir)
    _dirdata = list(_dirreader)

    
    # if 'Wi-Fi' in _dirdata[9]:
    #     print(_dirdata[9])
  
    print(_dirdata[0][1].strip(),_dirdata[1][1].strip(),_dirdata[2][1].strip(),_dirdata[4][1][:2].strip(),_dirdata[4][1].strip(),_dirdata[5][1].strip(),_dirdata[6][1].strip(),_dirdata[7][1].strip(),_dirdata[8][1].strip(),_dirdata[9][1].strip(),_dirdata[10][1].strip() if 'Wi-Fi' in _dirdata[9]  else '')
    _schoolfileswriter.writerow([_dirdata[0][1].strip(),_dirdata[1][1].strip(),_dirdata[2][1].strip(),_dirdata[4][1][:2].strip(),_dirdata[4][1].strip(),_dirdata[5][1].strip(),_dirdata[6][1].strip(),_dirdata[7][1].strip(),_dirdata[8][1].strip(),_dirdata[9][1].strip(),_dirdata[10][1].strip() if 'Wi-Fi' in _dirdata[9]  else ''])
   