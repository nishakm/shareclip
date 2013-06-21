import SimpleHTTPServer
import SocketServer
import os

ROOT_DIR = "stuff"
PORT = 9999

handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("",PORT),handler)
path = os.path.abspath(ROOT_DIR)
print "Simple HTTP server running on port", PORT, "at location", path
os.chdir(path)
httpd.serve_forever()

#root = tkinter.Tk()
#content = root.clipboard_get()
#outfile = fopen("clipboard",'w')
#outfile.write(content)
#outfile.close()
