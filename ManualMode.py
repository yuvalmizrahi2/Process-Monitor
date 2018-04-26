import InputCheck
import MainFrame
def RunManualMode():
    firstdate = InputCheck.EnterDate()
    seconddate = InputCheck.EnterDate()
    for proc in firstdate:
        if proc not in seconddate:
            print ("the process {0} number {1} is create\n".format(proc.name, proc.pid))
    for proc in seconddate:
        if proc not in firstdate:
            print ("the process {0} number {1} is stop working\n".format(proc.name, proc.pid))
    MainFrame.RunMainFrame()
