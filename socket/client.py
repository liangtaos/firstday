#!/usr/bin/python

import socket
import time


HOST = '127.0.0.1'
PORT = 9999
s = socket.socket()
s.connect((HOST, PORT))
for i in xrange(10):
    s.sendall('Hello World')
    data = s.recv(1024)
    print data,'i will sleep three'
    time.sleep(3)
s.close()
