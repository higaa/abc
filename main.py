#!/usr/bin/env python

# from lib import library
import calclib
import strlib
import sys

def main():
    print(sys.version)
    a = 3
    b = 4
    s = 'hoge'
    t = strlib.makestr(s, a, b)
    print(t)
    return 0

if __name__ == '__main__': 
    main()