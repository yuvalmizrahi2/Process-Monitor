import os

def MakeFolder():
    os.chdir("C:/")
    if not os.path.exists("ProcessMonitor") and not os.path.exists("C:/ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}"):
        os.mkdir("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}")
def CloseFolder():
    os.rename("ProcessMonitor", "ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}")
    os.popen('attrib +h ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}')
def OpenFolder():
    os.popen('attrib -h ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}')
    os.rename("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}", "ProcessMonitor")
