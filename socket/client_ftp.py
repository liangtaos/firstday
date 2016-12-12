#!/usr/bin/python
#coding:utf8

import socket
import time
import tab
import os
HOST = '127.0.0.1'
PORT = 9997
s = socket.socket()
s.connect((HOST, PORT))
while True:
    cmd_ = raw_input('input: ').strip()
    cmd = cmd_.split()
    if cmd[2] == '.' or './':
        cmd[2] = os.path.join(os.getcwd(), cmd[1].split('/')[-1])
    if not cmd:
        print '请输入命令'
        continue
    if cmd == 'q':
        break
    s.sendall(cmd_)
    with open(cmd[2], 'w') as f:
        while 1:
            data = s.recv(1024)
            if data.endswith('EOF'):
                data_ = data[:-3]
                f.write(data_)
                print "destination file is %s" % cmd[2]
                break
            f.write(data)
            if data == '7758521':
                print 'Is not a file or direction %s on server'% cmd[1]
                os.system('rm -rf %s'% cmd[2])
                break
s.close()
