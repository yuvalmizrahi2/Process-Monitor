import os
import re
import IOprocessList
import platform
import FolderLock
def EnterTime():
    while 1:
        try:
            x = int(raw_input("Enter the amount of time to scan: "))
        except ValueError:
            print "wrong input enter again"
            continue
        else:
            return x
def EnterPath():
    while 1:
        path = raw_input("Enter the path to which files are created: ")
        if os.path.exists(path):
            os.chdir(path)
            break
        else:
            print "wrong input enter again"
def EnterDate():
    while 1:
        date = raw_input("Enter the first date in the format y-m-d H-M: ")
        r = re.compile('.{4}-.{2}-.{2} .{2}:.{2}')
        if r.match(date):
            listofprocess = IOprocessList.CheckIfDateExist(date)
            if listofprocess:
                return listofprocess
            else:
                print "Date does not exist enter again"
        else:
            print "wrong input enter again"
def EnterChoose():
    while 1:
        try:
            x = int(raw_input("Enter your choose: "))
            if not(x < 0 or x > 3):
                return x
            else:
                print "The number is not in range"
        except ValueError:
            print "wrong input enter again"
            continue
def CheckFiles():
    if platform.system() is "Windows":
        if os.path.exists("ProcessMonitor.{645ff040-5081-101b-9f08-00aa002f954e}"):
            FolderLock.OpenFolder()
            if os.stat("ProcessMonitor/processList.csv").st_size != 0:
                return CheckDataInFile()
            else:
                FolderLock.CloseFolder()
        return False
    else:
        if os.path.exists("ProcessMonitor"):
            if os.stat("ProcessMonitor/processList.csv").st_size != 0:
                return CheckDataInFile()
        return False

def CheckDataInFile():
    counter = 0
    with open("ProcessMonitor/processList.csv", 'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            if counter == 0:
                date = line[2]
                counter = counter + 1
            else:
                if date != line[2]:
                    counter = counter + 1
                if counter == 2:
                    FolderLock.CloseFolder()
                    return True
    FolderLock.CloseFolder()
    return False