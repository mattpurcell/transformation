#!/usr/bin/python
from math import log, exp 
from sys import argv
from fileinput import input

def logit(p):
    return log(p/(1-p))   

#print argv[1], logit(float(argv[1]))
for line in input():
    print logit(float(line))
