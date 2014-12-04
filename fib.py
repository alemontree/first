#!/usr/bin/python

import sys

def fib(n):
	if n is 1 or n is 2:
		return 1
	return fib(n-1) + fib(n-2)

index = int(sys.argv[1])

print fib(index)