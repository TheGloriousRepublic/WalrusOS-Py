from graphics import *
import filesys

class icon():
    def __init__(self, path):
        self.path=path
    def setIcon(self, path):
        self.path=path
    def delete(self):
        del self

data = filesys.fileSys(eval(open('data.txt').read()))
dtWidth = 600
dtHeight = 600
desktop = GraphWin('Desktop', dtWidth, dtHeight)
