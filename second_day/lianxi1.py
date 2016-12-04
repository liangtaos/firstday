#!/usr/bin/python
#coding:utf-8

import os
import hashlib
import sys

def getMd5(path):
    m = hashlib.md5()
    try:
        with open(path) as f:
            for line in f:
                m.update(line)
    except:
        return None
    return m.hexdigest()
           
if not os.path.isdir(sys.argv[1]):
    print 'error'
    sys.exit()

for p, d, f in os.walk(sys.argv[1]):
    for fd in f:
        files = os.path.join(p,fd)
        if files == '/root/lianxi/lianxi1.py':
            continue
        _md5 = getMd5(files)
        print _md5  ,files, os.path.getsize(files)

