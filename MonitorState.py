import time
from FolderLock import OpenAndCloseFolder,MakeFolder
from IOprocessList import WriteCsvFile
MakeFolder()
X = input("enter the amount of time that the monitor need to scan the process: ")
while 1:
    OpenAndCloseFolder()
    WriteCsvFile()
    OpenAndCloseFolder()
    time.sleep(60 * X)




