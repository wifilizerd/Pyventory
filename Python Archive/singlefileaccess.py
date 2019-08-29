import sys, os, csv 

pyventory_db = ".pv_db.csv"

def pyventory_db_Setup():
    global pyventory_db
    if os.path.exists(pyventory_db):
        print('found it...')
    else:
        print('file made...')
        writeFile(pyventory_db, '')


    
    
    pass

def writeFile(_filename, _info):                        # Used to Write information to Files.
    # p_print(4, Directories._TC['_HEADING'], '******writeFile({0:}, {1:})******'.format(_filename, _info))
    _openfile = open(_filename, "a")                              #'ab'will create file also 'wb' will overwrite everytime the file is opened
    _openfilewriter = csv.writer(_openfile)                        #Setup CSV writer
    _openfilewriter.writerow(_info)                                #write info to _filename given _extention allows to used this def to write to other files types
    _openfile.close()

def setupFiles():                                       # Used to Load both Inventory and Scanned files into pyventory memory.
    # p_print(4, Directories._TC['_HEADING'], '******setupFiles()******')
    # global ScannedFile                                      # global set to modify global variable.
    # global InventoryFile
    # Logo('MAIN')
    # p_print(1, Directories._TC['_GREEN'], 'Select your Inventory file.')
    InventoryFile = FileBrowser('.csv', False)              # CSV file exported from Database.
    # p_print(1, Directories._TC['_GREEN'], 'Select your Scanned file or create new one.')
    # p_print(2, Directories._TC["_INFO"], "new file name only NO extention needed.(i.e. school number + year)")
    ScannedFile = FileBrowser('.csv', True)                 # new or exsisting project file.
def FileBrowser(_extention, _new):                      # Used to Display and  select what file to load and create new files if needed.
    # p_print(4, Directories._TC['_HEADING'], '******FileBrowser({0:}, {1:})******'.format(_extention, _new))
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
            # p_print(4, Directories._TC['_INFO'], _filechoose)
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
                    # p_print(4, Directories._TC['_INFO'], files[int(_filechoose)])
                    return(files[int(_filechoose)])
            else:
                if _new == False:
                    _filechoose = ''
                    # p_print(1, Directories._TC['_ERROR'], "NO new file at this point")
                    break
        except ValueError:
            # p_print(1, Directories._TC['_ERROR'], 'ERROR: Please Enter Project Name or Number')
            pass



pyventory_db_Setup()
