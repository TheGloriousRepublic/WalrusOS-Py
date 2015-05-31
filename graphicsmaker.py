import warnings
import WaSh, filesys#, WalStack
try:  # import as appropriate for 2.x vs. 3.x
   import tkinter as tk
except:
   import Tkinter as tk

class graphic:
   def draw(self):
      pass
   
   def setColor(self, color):
      self.color=color

   def draw(self):
      for x in self.pixels:
         setPixel(*x, self.color)

class Point(graphic):
   def __init__(self, x, y):
      self.x=x
      self.y=y
      self.color='black'
      self.pixels=[(self.x, self.y)]

def setPixel(x, y, color='black'):
    desktop.create_line(x,y,x+1,y+1, fill=color)

def loadImg(xpos, ypos, dat):
    dat=dat.split()
    width=int(dat[0])
    height=int(dat[1])
    dat=dat[2:]
    if len(dat)==width*height:
        y=0
        while y<height:
            x=0
            while x<width:
               setPixel(xpos+x, ypos+y, dat[y*width+x])
               x+=1
            y+=1
    else:
        warnings.warn('width and height of image should equal '+str(len(dat)))
    
root = tk.Tk()
desktop = tk.Canvas(root, width=800, height=600)
desktop.pack()
