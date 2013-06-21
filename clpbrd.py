import Tkinter as tk

root = tk.Tk()
clipfile = "clipboard"

def dumpClipboard():
  content = root.clipboard_get()
  cfile = fopen(clipfile,'w')
  cfile.write(content)
  cfile.close()

def dumpData():
  cfile = fopen(clipfile,'r')
  content = cfile.read()
  cfile.close()
  root.clipboard_set(content)
