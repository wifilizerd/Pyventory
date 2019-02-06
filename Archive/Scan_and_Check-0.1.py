import sys, os, csv, pyventory

# CONFIG
_INVfile = "Legacy-Filemaker-02282018.csv"
_INVcol = 0
# set to 0 for just checking if assest is in list set to 1 to save info to a list for latter addition to inventory
_ADD = 1    

os.system('cls')
pyventory.Logo()
#http://patorjk.com/software/taag/#p=display&f=Small&t=SCAN%20and%20CHECK 'SMALL' font
print("\033[1;32m" + 
 ' ___  ___   _   _  _                _    ___ _  _ ___ ___ _  __ \n'
 '/ __|/ __| /_\ | \| |  __ _ _ _  __| |  / __| || | __/ __| |/ / \n'
 '\__ | (__ / _ \| .` | / _` |   \/ _` | | (__| __ | _| (__| | <  \n'
 '|___/\___/_/ \_|_|\_| \__,_|_||_\__,_|  \___|_||_|___\___|_|\_\ v0.1'                                                               
 + "\033[1;37m")
print('')
print('press x then enter to exit')
if _ADD > 0:
    print('Noteing recorde is enabled')
_scan = 0
_assetLIST = []
for row in pyventory.Convert2List(_INVfile, _INVcol):
    _assetLIST.append(row[_INVcol].lstrip('0'))


while _scan is not 'x':
    _scan = raw_input(':')
    # print(_scan)
    if _scan.lstrip('0') in _assetLIST or _scan in _assetLIST:
        for row in pyventory.Convert2List(_INVfile, _INVcol):
            if row[int(_INVcol)] == _scan.lstrip('0') or row[int(_INVcol)] == _scan:
                print("\033[1;32m" + str(row) + "\033[1;37m")
                pyventory.writefile('inINV.csv', row)
    else:
        if _scan == 'x':
            break
        print("\033[1;31m" + _scan + ' and ' + str(_scan).lstrip('0') + ' not found' + "\033[1;37m")
        if _ADD > 0:
            print("\033[1;33m" 'add information for asset tage ' + _scan)
            _asset = _scan
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
            
            if '!' in _serial:
                _pserial = _serial
            
            pyventory.writefile('Add.csv', (_asset, _serial, _type, _make, _model, _cpu, _ram, _hdd, _os, _school, _room, _user, _compname, _mac, _wmac, _installdate, _owner, _usertype, _status, _year, _yearrotate, _rotate, _notes))
