#!/usr/bin/env python

import socket

HOST = ''
PORT = 9999
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print conn
print addr
while True:
    data = conn.recv(1024)
    print data
    conn.sendall(data.upper())
    if not data:
        break
conn.close()
