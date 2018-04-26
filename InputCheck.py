import os
import re
import IOprocessList
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
