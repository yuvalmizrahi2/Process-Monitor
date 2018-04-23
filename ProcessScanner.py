import psutil
from Process import Process

def ListOfProcess():
    list = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        p = Process(proc.pid, proc.name())
        list.append(p)
    return  list
