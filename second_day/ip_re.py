#!/usr/bin/python

import re

from subprocess import PIPE, Popen

def getinfo():
    data = Popen(['ifconfig'],stdout=PIPE).stdout.read()
    Ethernet = re.compile(r'eth[:\d]|br[:\d]')
    HW = re.compile(r'HWaddr ([\w:]{17})')
    inet_addr = re.compile(r'inet addr:([\d\.]{7,15})')
    net_name = re.findall(Ethernet,data)
    mac = re.findall(HW,data)
    ip = re.findall(inet_addr,data)
    info = zip(net_name, mac, ip)
    print info
     

getinfo()
