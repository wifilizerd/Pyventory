from PyFileMaker import FMServer

fm = FMServer('https://workorders.alpinedistrict.org/fmi/webd#ASD%20Technology%20Dept')
fm.
# [and press Tab to see available methods and variables]
# help fm.getDbNames
# [displays help for the method]

fm.getDbNames()
# ['dbname','anoterdatabase']
fm.setDb('dbname')

fm.getLayoutNames()
# ['layoutname','anotherlayout']
fm.setLayout('layoutname')
