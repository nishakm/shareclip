import sys
import socket

class Client:
  def __init__(self,host,port,file_name):
    self.host = host
    self.port = port
    self.file_name = file_name
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def send(self):
    try:
      clpbrd = open(self.file_name,'r')
      content = clpbrd.read()
    except IOError:
      print "Could not read from file"
      sys.exit(1)
    try:
      print "Connecting to", self.host, "on port", self.port 
      self.sock.connect(self.host,self.port)
      self.sock.sendall(content)
    finally:
      self.sock.close()
      
