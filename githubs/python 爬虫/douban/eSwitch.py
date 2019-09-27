 
 
def actionI():
    print("1")
def actionII():
    print("2")
def actionIII():
    print("3")
def switchDemo(a):
    if a==1:
        actionI()
    elif a==2:
        actionII()
    else:
        actionIII()
def dictDemo(a):
    dc ={"1":actionI,"2":actionII,"3":actionIII}
    dc[str(a)]()

class base():
    def __init__(self):
        self.idx = 0
    def do(self):
        pass
class heritI(base):
    def __init__(self):
        base.__init__(self)
        self.idx = 1
    def do(self):
        actionI()
class heritII(base):
    def __init__(self):
        base.__init__()
        self.idx = 2
    def do(self):
        actionII()
class heritIII(base):
    def __init__(self):
        base.__init__()
        self.idx = 3
    def do(self):
        actionIII()

def classDemo():
    a = heritI()
    a.do()
def main():
    switchDemo(2)
    dictDemo(3)
    classDemo()
if __name__ == '__main__':
    main()