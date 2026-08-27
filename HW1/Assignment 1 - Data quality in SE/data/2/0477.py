#!/usr/bin/env python
# coding:utf-8
import time
from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH)

HOST = '127.0.0.1'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from :', self.client_address
        self.wfile.write('[%s] %s' % (time.ctime(), 
                                      self.rfile.readline()))
        
tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever( )