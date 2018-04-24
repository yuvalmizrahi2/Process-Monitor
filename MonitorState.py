import time
import FolderLock
import IOprocessList
import platform

X = input("Enter the amount of time to scan: ")
path = raw_input("Enter the path to which files are created: ")
if platform.system() is "Windows":
    FolderLock.MakeFolderWindows(path)
    while 1:
        FolderLock.CheckIfFolderDeleted(path + "/ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}")
        FolderLock.OpenFolder()
        IOprocessList.WriteCsvFile(path+"/ProcessMonitor")
        FolderLock.CloseFolder()
        time.sleep(60 * X)
else:
    FolderLock.MakeFolderLinux(path)
    while 1:
        FolderLock.CheckIfFolderDeleted(path + "/ProcessMonitor")
        IOprocessList.WriteCsvFile(path + "/ProcessMonitor")
        time.sleep(60 * X)






