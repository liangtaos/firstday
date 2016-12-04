#!/usr/bin/python
#coding:utf8
import hashlib
import sys
import os



def jiaoyan(fd):
    m = hashlib.md5()
    if not os.path.isfile(fd):
        print '输入不是一个文件'
        sys.exit()
    with open(fd) as f:
        for line in f:
            m.update(line)
    return m.hexdigest()  , fd

if __name__ == '__main__':
    print jiaoyan(sys.argv[1])
        
