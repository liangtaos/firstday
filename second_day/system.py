#!/usr/bin/python
#coding:utf8

from subprocess import Popen, PIPE
import os
import sys
def getip():
    out = {}
    ips = []
    data = Popen(['ifconfig'],stdout=PIPE).stdout.read()
    data1 = data.split('\n\n')
    for i in data1:
        if i.startswith('lo'):
            break
        chuli = i.split('\n')
        name = chuli[0].split()[0]
        
        ip = chuli[1].split()[2].split(':')[-1]
        ips.append(ip)
    out['ip'] = ips
    return out

def getInfo():
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
    dic_lis = []
    for i in lis:
        chuli = i.split(': ')
        dic_lis.append(chuli) 
    systemDict = dict(dic_lis)
    out = {}
    out['vendor'] = systemDict['Manufacturer']
    out['product'] = systemDict['Product Name']
    out['sn'] = systemDict['Serial Number']
    return out

def getCpu():
    out = {}
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.startswith('model name'):
                out['cpu_model'] = line.split(': ')[-1].strip()
            if line.startswith('cpu cores'):
                out['cpu_cores'] = line.split(': ')[-1].strip()

    return out
def mem():
    with open('/proc/meminfo') as f:
        for line in f:
            if line.startswith('MemTotal'):
                mem = '%.2f G' % (int(line.split()[1]) /1024.0 / 1024.0) 
                break
    return mem
   
if __name__ == '__main__':
    info = {}
    ips = getip()
    infos = getInfo()
    p = Popen('cat /etc/issue',shell=True,stdout=PIPE)
    system_ = p.stdout.read().split('\n')[0]
    hostname = Popen('hostname',shell=True,stdout=PIPE)
    hostname = hostname.stdout.read().strip()
    info['hostname'] = hostname
    info['osver'] = system_
    cpu = getCpu()
    info['mem'] = mem()
    info.update(ips)
    info.update(infos)
    info.update(cpu)
    print info

