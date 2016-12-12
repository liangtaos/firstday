#!/usr/bin/env python

from multiprocessing import Process
import os

def func():
    print "process id: %s ppid: %s" % (os.getpid(), os.getppid())
    while True:
        37 * 15.37

for i in range(20):
    t = Process(target=func,args=())
    t.start()
    print "process id: %s" % os.getpid()
