# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:00:46 2016

@author: lvanhulle
"""

def getLocals(func):
    loc = None
    def wrapped(*args, **kwargs):
        nonlocal loc
        loc = locals()
        print(locals())
        return func(*args, **kwargs)
    print(loc)
    return wrapped

def h(a=1, b=2):
    i = 3
    j = 4
    return a+b+i+j
