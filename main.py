import seaborn as sns
from tkinter import *
from tkinter import ttk, colorchooser
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

class main:
  def __init__(self, master):
    self.master = master
    self.color_fg = 'black'
    self.color_bg = 'white'
    self.old_x = None
    self.old_y = None
    self.pen_width = 5
    self.drawWidgets()
    self.c.bind('<B1-Motion>', self.paint)
    self.c.bind('<ButtonRelease-1', self.reset)
  def paint(self, e):
    if self.old_x and self.old_y:
      self.c.create_line(self.old_x, self.old_y, e.x, e.y, widht = self.pen_width, filler = self.color_fg, capstyle = 'round', smooth = True)
      self.old_x = e.x
      self.old_y = e.y

root = Tk()
root.title('Neural Network Digit Detection')
root.mainloop()


