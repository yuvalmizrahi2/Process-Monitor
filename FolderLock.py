import os
import sys

def CheckIfFolderDeleted(path):
    if not os.path.exists(path):
        print "the folder deleted by the hacker"
        sys.exit(1)
def MakeFolderWindows():
    if not os.path.exists("ProcessMonitor") and not os.path.exists("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}"):
        os.mkdir("ProcessMonitor")
        with open("ProcessMonitor/Status_Log.txt", 'w'): pass
        with open("ProcessMonitor/processList.csv", 'wb'): pass
        CloseFolder()
def MakeFolderLinux():
    if not os.path.exists("ProcessMonitor"):
        os.mkdir("ProcessMonitor")
        with open("ProcessMonitor/Status_Log.txt", 'w'): pass
        with open("ProcessMonitor/processList.csv", 'wb'): pass
def CloseFolder():
    os.rename("ProcessMonitor", "ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}")
    os.popen('attrib +h ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}')
def OpenFolder():
    os.popen('attrib -h ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}')
    os.rename("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}", "ProcessMonitor")