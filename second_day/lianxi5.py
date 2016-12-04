#!/usr/bin/env python
#coding:utf-8


import os
import operator
import sys
dic = {}
for p, d, f in os.walk(sys.argv[1]):
    for i in f:
        files = os.path.join(p,i)
        try:
            du = os.path.getsize(files)
        except:
            continue
        dic[files] = du
dic1 = sorted(dic.iteritems(), key=operator.itemgetter(1),reverse=True)
print dic1
print '*' * 60
for k,v in dic1[:10]:
    print k  ,v
