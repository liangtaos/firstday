#!/usr/bin/python
#coding:utf8

from subprocess import Popen, PIPE
import os

import sys
lis = []
data = Popen(['dmidecode'],stdout=PIPE).stdout.readlines()
con = False
for line in data:
    if line.startswith('System Information'):
        con = True
        continue
    if con:
        if line == '\n':
            break

        if not line[0].strip():
            lis.append(line.strip())
    
#aprint lis
dic_lis = []
for i in lis:
    chuli = i.split(': ')
    dic_lis.append(chuli) 
systemDict = dict(dic_lis)
out = {}
out['vendor'] = systemDict['Manufacturer']
out['product'] = systemDict['Product Name']
out['sn'] = systemDict['Serial Number']
print out

