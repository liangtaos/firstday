#!/usr/bin/python
import sys
import random

times = 0
sys_number = random.randint(1,20)
while 1:
    if times > 6:
        print 'you lose'
        sys.exit()
    use_number = raw_input('Please input a number in 0-20:')
    try:
        use_number = int(use_number)
    except:
        print 'please input a number 0-20 hao ma ?'
        continue
    if use_number > sys_number:
        print 'too big'
    elif use_number < sys_number:
        print 'too small'
    else:
        print 'you hit'
        sys.exit()
    times += 1
        
    
