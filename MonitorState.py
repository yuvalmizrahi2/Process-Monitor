import time
from FolderLock import OpenFolder,CloseFolder,MakeFolder
from IOprocessList import WriteCsvFile
MakeFolder()
X = input("enter the amount of time that the monitor need to scan the process: ")
while 1:
    OpenFolder()
    WriteCsvFile()
    CloseFolder()
    time.sleep(60 * X)




