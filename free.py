#!/usr/bin/python
#! coding:utf-8


with open('/proc/meminfo') as f:
    for line in f:
        if line.startswith('MemTotal:'):
            total = int(line.split()[1])/1024.0
            continue
        elif line.startswith('MemFree:'):
            free = int(line.split()[1])/1024.0
            continue
        else:
            continue
print '系统总的内存 %sM' % total 
print '未使用的内存 %sM'  % free
print '剩余的百分比 %.2f %%' % (((free/total)*100))

