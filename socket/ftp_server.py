#!/usr/bin/env python
#coding:utf8
import socket
from subprocess import Popen, PIPE
import os

HOST = ''
PORT = 9999
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print conn
print addr
while True:
    cmd = conn.recv(1024)
    if not cmd: break
    cmd = cmd.split()
    if cmd[0] == 'get':
        if  not os.path.exists(cmd[1]):
            conn.sendall('7758521')
            break
        with open(cmd[1]) as f:
            while 1:
                data = f.read(1024)
                conn.sendall(data)
                if not data:
                    conn.sendall('EOF')
                    break
    else:
       break
    if not cmd: break
conn.close()
