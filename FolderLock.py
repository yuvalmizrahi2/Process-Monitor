import os
import sys

def CheckIfFolderDeleted(path):
    if not os.path.exists(path):
        print "the folder deleted by the hacker"
        sys.exit(1)
def MakeFolderWindows(path):
    os.chdir(path)
    if not os.path.exists("ProcessMonitor") and not os.path.exists("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}"):
        os.mkdir("ProcessMonitor")
        with open(path + "/ProcessMonitor/Status_Log.txt", 'w'): pass
        with open(path + "/ProcessMonitor/processList.csv", 'wb'): pass
        CloseFolder()
def MakeFolderLinux(path):
    os.chdir(path)
    if not os.path.exists("ProcessMonitor"):
        os.mkdir("ProcessMonitor")
def CloseFolder():
    os.rename("ProcessMonitor", "ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}")
    os.popen('attrib +h ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}')
def OpenFolder():
    os.popen('attrib -h ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}')
    os.rename("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}", "ProcessMonitor")