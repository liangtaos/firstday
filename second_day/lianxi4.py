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
dic = {}
for p, d, f in os.walk(sys.argv[1]):
    n_sum = 0
    for fd in f:
        files = os.path.join(p,fd)
        _md5 = getMd5(files)
        du = os.path.getsize(files)
        print _md5  ,files, os.path.getsize(files)
        n_sum += du
    print '目录',n_sum

 
