import os.path
import csv
import datetime
from Process import Process
import ProcessScanner
import IOStatus_Log
import sys
import platform
import FolderLock
lastmodified = ""
def WriteCsvFile():
    list = ProcessScanner.ListOfProcess()
    expecteddate = datetime.datetime.now().strftime("%y-%m-%d %H-%M")
    if lastmodified == "" or os.stat("ProcessMonitor/processList.csv").st_mtime == lastmodified:
        lastprocess = ReadLastScanner()
        IOStatus_Log.WriteTxtFile(list , lastprocess , expecteddate)
        with open("ProcessMonitor/processList.csv", 'ab') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            for proc in list:
                writer.writerow([proc.pid, proc.name, expecteddate])
    else:
        print "there was change in processList file"
        sys.exit(1)

def ReadLastScanner():
    process = []
    date = ""
    with open("ProcessMonitor/processList.csv", 'rb') as f:
        reader = csv.reader(f)
        for line in reversed(list(reader)):
            p = Process(line[0],line[1])
            if not process:
                process.append(p)
                date = line[2]
            else:
                if date == line[2]:
                    process.append(p)
                else:
                    return process
    return process

def CheckIfDateExist(date):
    listofprocess = []
    if platform.system() is "Windows":
        FolderLock.OpenFolder()
    with open("ProcessMonitor/processList.csv", 'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            if line[2] == date:
                listofprocess.append(Process(line[0],line[1]))
    if platform.system() is "Windows":
        FolderLock.CloseFolder()
    return listofprocess




