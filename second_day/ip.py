#!/usr/bin/python
from subprocess import PIPE, Popen
import os
import sys
def getip():
    out = {}
    data = Popen(['ifconfig'],stdout=PIPE).stdout.read()
    data1 = data.split('\n\n')
    for i in data1:
        if i.startswith('lo'):
            sys.exit()  
        chuli = i.split('\n')
        #print chuli
        name = chuli[0].split()[0]
        ip = chuli[1].split()[2].split(':')[-1]
        out[name] = ip

    return out       
        
         


if __name__ == '__main__':
    getip()
    
