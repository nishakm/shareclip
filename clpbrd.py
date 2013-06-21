import Tkinter as tk

class Clpbrd:
  def __init__(self,file_name:
    self.root = tk.Tk()
    self.root.withdraw()
    self.clipfile = file_name

  def dumpClipboard(self):
    content = self.root.clipboard_get()
    cfile = open(self.clipfile,'w')
    cfile.write(content)
    cfile.close()

  def dumpData(self):
    cfile = open(self.clipfile,'r')
    content = cfile.read()
    cfile.close()
    self.root.clipboard_set(content)
