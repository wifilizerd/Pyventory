import sys, os, csv, pyventory

# CONFIG
_INVfile = "Legacy-Filemaker-02282018.csv"
_INVcol = 0
_Checkfile = 'inINV.csv'
_Checkcol = 0
# set to 0 for just checking if assest is in list set to 1 to save info to a list for latter addition to inventory

os.system('cls')
pyventory.Logo()
#http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20SHOW 'SMALL' font
print("\033[1;32m" + 
 "   ___ _           _                  _   ___                   _   \n"
 "  / __| |_  ___ __| |__  __ _ _ _  __| | | __|_ ___ __  ___ _ _| |_ \n"
 " | (__| ' \/ -_) _| / / / _` | ' \/ _` | | _|\ \ / '_ \/ _ \ '_|  _|\n"
 "  \___|_||_\___\__|_\_\ \__,_|_||_\__,_| |___/_\_\ .__/\___/_|  \__| v0.2\n"   
 "                                                 |_|                "                                                            
 + "\033[1;37m")
print('')
print('press x then enter to exit')
_INVlist = pyventory.Convert2List(_INVfile, _INVcol)
_CHECKlist = pyventory.Convert2List(_Checkfile, _Checkcol)

_CHECKcollist = []
for row in _CHECKlist:
    if row[int(_Checkcol)] not in _CHECKcollist:            #checking for duplicates
        _CHECKcollist.append(row[_Checkcol].lstrip('0'))
    else:
        pass

for asset in _INVlist:
    if asset[_INVcol] not in _CHECKcollist:
        pyventory.writefile('notscanned.csv', asset)
    else:
        pass