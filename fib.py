#!/usr/bin/python

import sys

def fib(n, count):
    if n is 1 or n is 2:
#        print "count: ", count
        return 1
#    print n
    count = count + 1
    return fib(n-1, count) + fib(n-2, count)

index = int(sys.argv[1])

print fib(index, 0)
