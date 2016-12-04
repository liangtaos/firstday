#!/usr/bin/python
#coding:utf8


import os
import sys
import hashlib

import md5


def main(path):
    if not os.path.exists(path):
        print 'Not find this dirctory in this computer'
    for p, d, f in os.walk(path):
        for fd in f:
            fileMd5 = os.path.join(p,fd)
            a, b = md5.jiaoyan(fileMd5)
            yield '%s %s' %(a,b)
    








if __name__ == '__main__':
    del sys.argv[0]
    for i in sys.argv:
        s = main(i)
        print s.next()
        print s.next()
   
