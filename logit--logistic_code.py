#!/usr/bin/python

from math import log
from math import exp 

a = 1
b = 200

def logit_func(a, b, x):
    return log(x-a) - log(b-x)
    
print logit_func(a, b, 60)        

m = logit_func(a, b, 60)

print round(m, 2)



def logistic_func(a , b , x):
    return (b-a)*(1/(1+exp(-x)))+a
    



print logistic_func(a, b, logit_func(a, b, 60))

