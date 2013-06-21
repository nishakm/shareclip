import clpbrd
import os

def main():
  #read the config file
  conf_file = open("sc.conf",'r')
  conf_list = conf_file.readlines()
  conf_file.close()

  #settings
  ROOT_DIR = conf_list[0].split(" ")[2][:-1]
  TARGET_HOST = conf_list[1].split(" ")[2][:-1]
  PORT = conf_list[2].split(" ")[2][:-1]
 
  #copy clipboard
  filename = os.path.join(ROOT_DIR,"clipboard")
  cb = clpbrd.Clpbrd(filename)
  cb.dumpClipboard()

main()
