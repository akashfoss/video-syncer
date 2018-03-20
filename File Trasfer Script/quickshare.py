#! /usr/bin/env python
import SimpleHTTPServer
import SocketServer
import socket
import sys


try:
    PORT=int(raw_input('Enter Port Number or Simply press Enter/Return :'))
except ValueError:
    PORT = 8000

Host = socket.gethostbyname(socket.gethostname())

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "\n Your folder is Quickshared on :  ", Host+":"+str(PORT)
print "\n Use Ctrl+C to stop sharing"
httpd.serve_forever()


