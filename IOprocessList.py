import os.path
import csv
import datetime
from Process import Process
from ProcessScanner import ListOfProcess
from IOStatus_Log import WriteTxtFile
path = "C:/ProcessMonitor/processList.csv"
def CheckIfFileExists():
    return os.path.isfile(path)

def WriteCsvFile():
    list = ListOfProcess()
    ExpectedDate = datetime.datetime.now().strftime("%y-%m-%d %H-%M")
    if CheckIfFileExists():
        lastprocess = ReadLastScanner()
        WriteTxtFile(list , lastprocess , ExpectedDate)
        with open(path, 'ab') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            for proc in list:
                writer.writerow([proc.pid, proc.name, ExpectedDate])
    else:
        with open(path, 'wb') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            writer.writerow(["PID", "NAME", "DATE"])
            for proc in list:
                writer.writerow([proc.pid, proc.name, ExpectedDate])

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


