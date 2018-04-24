import time
from FolderLock import OpenFolder,CloseFolder,MakeFolderWindows,MakeFolderLinux
from IOprocessList import WriteCsvFile
import platform

X = input("Enter the amount of time to scan: ")
path = raw_input("Enter the path to which files are created: ")
if platform.system() is "Windows":
    MakeFolderWindows(path)
    while 1:
        OpenFolder()
        WriteCsvFile(path+"/ProcessMonitor")
        CloseFolder()
        time.sleep(60 * X)
else:
    while 1:
        MakeFolderLinux(path)
        WriteCsvFile(path + "/ProcessMonitor")
        time.sleep(60 * X)






