# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:00:46 2016

@author: lvanhulle
"""
g = 10

def getLocals(func):
    loc = None
    def wrapped(*args, **kwargs):
        print(locals(), "Yo")
        return func(*args, **kwargs)
    print(loc)
    return wrapped

def h(a=1, b=2):
    i = 3
    j = 4
    print(locals())
    return a+b+i+j
