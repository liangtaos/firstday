#!/usr/bin/python
#coding:utf8


import sys
import os
import readline
#path = './'

#file = 'hello.py'

file = raw_input('请给出要统计的文件的路径 ')

if '/' in file:

    path1 = file
else:
    path1 = './' + file
if not os.path.isfile(path1):
    print '文件不存在'
    sys.exit()
class Wc(object):
    chuli = open(path1).read()
    def ci(self):
        danci = len(self.chuli.split())
        return danci
    def fu(self):
        sum = len(self.chuli)
        return sum
   
    def hang(self):
        hangshu = self.chuli.count('\n')
        return hangshu
a = Wc()
print '单词数是 %s ' % (a.ci()),
print '字符串数 %s' % (a.fu()),
print '行数 %s' % a.hang(),
print '文件名 %s' % (path1.split('/')[-1])
