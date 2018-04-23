import os.path
import csv
import datetime
from Process import Process
from ProcessScanner import ListOfProcess
from IOStatus_Log import WriteTxtFile
import sys
path = "C:/ProcessMonitor/processList.csv"
lastmodified = ""
def CheckIfFileExists():
    return os.path.isfile(path)

def WriteCsvFile():
    list = ListOfProcess()
    ExpectedDate = datetime.datetime.now().strftime("%y-%m-%d %H-%M")
    if CheckIfFileExists() and (lastmodified == "" or os.stat(path).st_mtime == lastmodified):
        lastprocess = ReadLastScanner()
        WriteTxtFile(list , lastprocess , ExpectedDate)
        with open(path, 'ab') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            for proc in list:
                writer.writerow([proc.pid, proc.name, ExpectedDate])
    elif lastmodified == "" or os.stat(path).st_mtime == lastmodified:
        with open(path, 'wb') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            writer.writerow(["PID", "NAME", "DATE"])
            for proc in list:
                writer.writerow([proc.pid, proc.name, ExpectedDate])
    else:
        print "there was change in processList file"
        sys.exit(1)

def ReadLastScanner():
    process = []
    date = ""
    with open(path, 'rb') as f:
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


