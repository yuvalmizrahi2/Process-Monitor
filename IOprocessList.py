import os.path
import csv
import datetime
from Process import Process
import ProcessScanner
import IOStatus_Log
import sys
lastmodified = ""
def CheckIfFileExists(path):
    return os.path.isfile(path)

def WriteCsvFile(path):
    list = ProcessScanner.ListOfProcess()
    ExpectedDate = datetime.datetime.now().strftime("%y-%m-%d %H-%M")
    if lastmodified == "" or os.stat(path+"/processList.csv").st_mtime == lastmodified:
        lastprocess = ReadLastScanner(path+"/processList.csv")
        IOStatus_Log.WriteTxtFile(list , lastprocess , ExpectedDate , path)
        with open(path+"/processList.csv", 'ab') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            for proc in list:
                writer.writerow([proc.pid, proc.name, ExpectedDate])
    else:
        print "there was change in processList file"
        sys.exit(1)

def ReadLastScanner(path):
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


