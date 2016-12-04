#!/usr/bin/python
import sys
import os
from optparse import OptionParser

def opt():
    parser = OptionParser("Usage: %prog [option] [file1] [file2]")
    parser.add_option("-c", "--char",
                      dest="chars",
                      action="store_true",
                      default=False,
                      help="only count chars")
    parser.add_option("-w", "--word",
                      dest="words",
                      action="store_true",
                      default=False,
                      help="only count words")
    parser.add_option("-l", "--line",
                      dest="lines",
                      action="store_true",
                      default=False,
                      help="only count lines")
    options, args = parser.parse_args()
    return options, args

def _getCount(data, fn):
    out = {}
    out['chars'] = len(data)
    out['words'] = len(data.split())
    out['lines'] = data.count('\n')
    return out

def main():
    options, args = opt()
    #print options, args
    if not (options.lines or options.words or options.chars):
        options.lines, options.words, options.chars = True, True, True
    if not args:
        data = sys.stdin.read()
        fn = ''
        out = _getCount(data, fn)
        if options.lines:
            print out['lines'],
        if options.words:
            print out['words'],
        if options.chars:
            print out['chars']
        
    
    total_lines, total_words, total_chars = 0, 0, 0
    for fd in args:
        if not os.path.isfile(fd):
            print 'wc: \033[0;0;31;40;1m%s\033[0m: No such file or directory' % fd
            sys.exit()
        with open(fd) as f:
            data = f.read()
            out = _getCount(data, fd)
            if options.lines:
                print out['lines'],
                total_lines += out['lines']
            if options.words:
                print out['words'],
                total_words += out['words']
            if options.chars:
                print out['chars'],
                total_chars += out['chars']
            print fd
    if len(args) > 1:
        if total_lines: 
            print totla_lines, 
        if total_words:
            print total_words,
        if total_chars:
            print total_chars,
        print 'total'



if __name__ == '__main__':
    main()

