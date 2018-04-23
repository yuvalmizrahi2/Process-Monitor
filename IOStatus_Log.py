import os.path
path = "C:/ProcessMonitor/Status_Log.txt"
def CheckIfFileExists():
    return os.path.isfile(path)
def WriteTxtFile(newprocess , oldprocess , ExpectedDate):
    if CheckIfFileExists():
        with open(path, 'a') as outtxt:
            outtxt.write("the date of the change is {0}\n\n".format(ExpectedDate))
            for proc in newprocess:
                if proc not in oldprocess:
                    outtxt.write("the process {0} number {1} is create\n".format(proc.name , proc.pid))
            for proc in oldprocess:
                if proc not in oldprocess:
                    outtxt.write("the process {0} number {1} is stop working\n".format(proc.name , proc.pid))
            outtxt.write("\n")
    else:
        with open(path, 'w') as outtxt:
            outtxt.write("the date of the change is {0}\n\n".format(ExpectedDate))
            for proc in newprocess:
                if proc not in oldprocess:
                    outtxt.write("the process {0} number {1} is create\n".format(proc.name, proc.pid))
            for proc in oldprocess:
                if proc not in oldprocess:
                    outtxt.write("the process {0} number {1} is stop working\n".format(proc.name, proc.pid))
            outtxt.write("\n")

