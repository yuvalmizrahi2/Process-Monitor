import os.path
import time
lastmodified = ""
def CheckIfFileExists(path):
    return os.path.isfile(path)
def WriteTxtFile(newprocess , oldprocess , ExpectedDate , path):
    if CheckIfFileExists(path+"/Status_Log.txt") and (lastmodified == "" or os.stat(path+"/Status_Log.txt").st_mtime == lastmodified):
        with open(path+"/Status_Log.txt", 'a') as outtxt:
            outtxt.write("the date of the change is {0}\n\n".format(ExpectedDate))
            for proc in newprocess:
                if proc not in oldprocess:
                    print ("the process {0} number {1} is create\n".format(proc.name , proc.pid))
                    outtxt.write("the process {0} number {1} is create\n".format(proc.name , proc.pid))
            for proc in oldprocess:
                if proc not in newprocess:
                    print ("the process {0} number {1} is stop working\n".format(proc.name , proc.pid))
                    outtxt.write("the process {0} number {1} is stop working\n".format(proc.name , proc.pid))
            outtxt.write("\n")
    elif lastmodified == "" or os.stat(path+"/Status_Log.txt").st_mtime == lastmodified:
        with open(path+"/Status_Log.txt", 'w') as outtxt:
            outtxt.write("the date of the change is {0}\n\n".format(ExpectedDate))
            for proc in newprocess:
                if proc not in oldprocess:
                    print ("the process {0} number {1} is create\n".format(proc.name , proc.pid))
                    outtxt.write("the process {0} number {1} is create\n".format(proc.name, proc.pid))
            for proc in oldprocess:
                if proc not in newprocess:
                    print ("the process {0} number {1} is stop working\n".format(proc.name , proc.pid))
                    outtxt.write("the process {0} number {1} is stop working\n".format(proc.name, proc.pid))
            outtxt.write("\n")
    else:
        print "there was change in Status_Log file"
        time.sleep(30)

