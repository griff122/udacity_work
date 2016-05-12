import sys
import time
import numpy

import plot_utils

def naive(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def russian(a,b):
    x = a; y = b;
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

if __name__ == "__main__":
    # first arg is max value, second arg is step
    numbers = range(1,int(sys.argv[1]),int(sys.argv[2]))
    print "Starting to test timings for function:"
    times_naive = []
    times_russian = []
    tot_numbers = len(numbers)
    s0 = time.time()
    for idx,val in enumerate(numbers):
        if idx%100 == 0:
            print " -- Working on %i/%i: current time: %.3f seconds"%(idx+1,tot_numbers,time.time() - s0)
        s1 = time.time()
        naive(val,val)
        times_naive.append(time.time() - s1)
        s2 = time.time()
        russian(val,val)
        times_russian.append(time.time() - s2)
    e0 = time.time()
    print "Time taken: %.3f seconds"%(e0 - s0)
    times = numpy.array([times_naive,times_russian]).transpose()
    numbers = numpy.array([numbers,numbers]).transpose()
    print "opening plot..."
    plot_utils.plot_data(numbers,times)
