import InputCheck
import ManualMode
import MonitorState
import sys
def RunMainFrame():
    print "Hello to the Process Monitor"
    InputCheck.EnterPath()
    RunMainMenu()
def RunMainMenu():
    print "Select Menu:\n1. Monitor State\n2. Manual Mode\n3. Exit\n"
    choose = InputCheck.EnterChoose()
    if choose == 1:
        MonitorState.RunMonitorState()
    elif choose == 2:
        if InputCheck.CheckFiles():
            ManualMode.RunManualMode()
        else:
            print "Can not access the app"
            RunMainMenu()
    else:
        print "Bye bye"
        sys.exit(0)
RunMainFrame()

