#!/usr/bin/python
#coding:utf-8
import os

lis = os.listdir('/proc')

for nu in lis:
    try:
        nu1 = int(nu)
        print nu1
    except:
        continue
