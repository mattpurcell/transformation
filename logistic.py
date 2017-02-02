#!/usr/bin/python
from math import log, exp 
import sys
import fileinput
#from fileinput import input

def logistic(x):
    return (1.0/(1.0+exp(-x)))

def logistic2(a , b , x):
    return (b-a)*(1.0/(1.0+exp(-x)))+a

#print argv[1], logit(float(argv[1]))
#print sys.argv
if len(sys.argv) == 3:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    sys.argv = [sys.argv[0]]
#    print sys.argv
    for line in fileinput.input():
        print logistic2(a, b, float(line))
else:
    for line in fileinput.input():
        print logistic(float(line))
