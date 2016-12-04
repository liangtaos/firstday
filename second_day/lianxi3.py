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
    m_sum = ''
    for fd in f:
        files = os.path.join(p,fd)
        _md5 = getMd5(files)
        #print _md5  ,files, os.path.getsize(files)
        if dic.has_key(_md5):
            dic[_md5].append(files)
        else:
            dic[_md5] = [ files ]

for k, v in dic.items():
    if len(v) > 1:
        print k, v
 
