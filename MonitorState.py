import time
import FolderLock
import IOprocessList
import platform
import InputCheck
def RunMonitorState():
    x = InputCheck.EnterTime()
    if platform.system() is "Windows":
        FolderLock.MakeFolderWindows()
        while 1:
            FolderLock.CheckIfFolderDeleted("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}")
            FolderLock.OpenFolder()
            IOprocessList.WriteCsvFile()
            FolderLock.CloseFolder()
            time.sleep(60 * x)
    else:
        FolderLock.MakeFolderLinux()
        while 1:
            FolderLock.CheckIfFolderDeleted("ProcessMonitor")
            IOprocessList.WriteCsvFile("ProcessMonitor")
            time.sleep(60 * x)