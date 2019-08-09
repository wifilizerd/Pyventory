import sys
import csv
import os

_SCCMfile = open('MRJH_SCCM.csv', 'r')
_SCCMfilereader = csv.reader(_SCCMfile)
_SCCMfiledata = list(_SCCMfilereader)
count = 0
_DEBUG = 0     # 0 = no debuging, 1 =  Print lists on screen, 2 = print Lists to file..
_pclist = []

def SCCMopen():
    count = 0
    _SCCMfile = open('MRJH_SCCM.csv', 'r')
    _SCCMfilereader = csv.reader(_SCCMfile)
    _SCCMfiledata = list(_SCCMfilereader)
    for i in _SCCMfiledata:
        if i:
            count += 1
    return(count)

def FMlistopen():
    count = 0
    _FMfile = open('MRJH-PC Filemaker 01312018.csv', 'r')
    _FMfilereader = csv.reader(_FMfile)
    _FMfiledata = list(_FMfilereader)
    for i in _FMfiledata:
        if i:
            count += 1
    return(count)


_SCCMcount = SCCMopen()
_FMcount = FMlistopen()
print("SCCM Shows: " + str(_SCCMcount) + " active PCs")
print("Were as FM Shows: " + str(_FMcount) + " inventored PCs")
# percent = _PCcount / float(count)
# print "You Have %s%% of PCs Accounted For" % str(percent)[2:-10]  # Note the double % sign
