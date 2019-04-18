"""
Homework 3 
CIS4930
Summer 17
Ryan Winter
rw15e
"""

from __future__ import print_function
import sys

class Fibonacci:
    def __init__(self, len):
        self.len = len
	self.nums = [0,1]
	for i in range(2, len):
	    self.nums.append(self.nums[i-1]+self.nums[i-2])

    def __str__(self):
        return "The first {0} Fibonacci numbers are {1}".format(self.len, self.nums) 

    def __iter__(self):
        self.x = 0
        self.y = 1
	self.counter = 0
        return self

    def next(self):
        self.counter = self.counter + 1
	if self.counter == 1:
	    print("0",end=' ')
        if self.x > self.len:
            raise StopIteration
        self.x, self.y = self.y, self.x + self.y
        return self.x

    def get_nums(self):
        print (self.nums)

# fib generator, should take in a single OPTIONAL parameter. 
# if not parameter, produce fib numbers indefinitely 
MISSING = object()
def fibonacci_gen(len=MISSING):
    x, y = 0, 1
    if len is MISSING:
	print("No parameter given!")
	for z in xrange(sys.maxint):
	    yield x
	    x, y = y, x + y
	#len = -5
	#while len == -5:
	#    for z in xrange(int(len)):
	#	yield x
	#	x, y = y, x + y
    else:
        for z in xrange(int(len)):
	    yield x
	    x, y = y, x + y

  

