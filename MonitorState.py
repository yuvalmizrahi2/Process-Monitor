import time
import FolderLock
import IOprocessList
import platform
import InputCheck
import MainFrame
def RunMonitorState():
    x = InputCheck.EnterTime()
    if platform.system() is "Windows":
        FolderLock.MakeFolderWindows()
        while 1:
            FolderLock.CheckIfFolderDeleted("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}")
            FolderLock.OpenFolder()
            IOprocessList.WriteCsvFile()
            FolderLock.CloseFolder()
            try:
                print "If you want to go back to the menu press CTRL + C"
                time.sleep(x*60)
            except KeyboardInterrupt:
                MainFrame.RunMainMenu()
    else:
        FolderLock.MakeFolderLinux()
        while 1:
            FolderLock.CheckIfFolderDeleted("ProcessMonitor")
            IOprocessList.WriteCsvFile()
            try:
                print "If you want to go back to the menu press CTRL + C"
                time.sleep(x*60)
            except KeyboardInterrupt:
                MainFrame.RunMainMenu()