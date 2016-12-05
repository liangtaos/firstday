#!/usr/bin/python
#coding:utf8

import os
import sys
from subprocess import PIPE,Popen
dir_ = '/proc'
pid_httpd = Popen(['pidof','httpd'], stdout=PIPE, stderr=PIPE)

pids = pid_httpd.stdout.read().split()

def pid_mem(pid):
    f = os.path.join(dir_,pid,'status')
    with open(f) as fd:
        for line in fd:
            if line.startswith('VmRSS'):
                mem = line.split()[1]
                break
    return mem
mem_all = 0
for i in pids:
    mem = pid_mem(i)
    mem = int(mem)
    mem_all += mem
with open('/proc/meminfo') as f:
    for line in f:
        if line.startswith('MemTotal'):
            lines = int(line.split()[1])
            break
mem_total = lines

print 'httpd has %s kb'% mem_all
print 'prection %s%%'% (mem_all / float(mem_total) * 100)

