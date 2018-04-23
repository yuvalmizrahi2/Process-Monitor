class Process:
    def __init__(self , pid , name):
        self.pid = pid
        self.name = name
    def __eq__(self, other):
        return int(self.pid) == int(other.pid) and self.name == other.name
