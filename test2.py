# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 07:32:17 2016

@author: Myself
"""

import turtle as t
from collections import Iterable
from itertools import cycle

side = 7

numLines = 0;

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet',
          'blue violet', 'brown', 'burlywood', 'dark green', 'gold',
          'lavender']

color = cycle(colors)

a = lambda : t.forward(side)
p = lambda : t.left(60)
m = lambda : t.left(-60)
b = lambda : t.forward(side)

#a = lambda : print('a', end=', ')
#b = lambda : print('b', end=', ')
#m = lambda : print('m', end=', ')
#p = lambda : print('p', end=', ')

#a_seq = ('a','m','b','m','m','b','p','a','p','p','a','a','p','b','m')
#b_seq = ('p','a','m','b','b','m','m','b','m','a','p','p','a','p','b')
a_seq = (a,m,b,m,m,b,p,a,p,p,a,a,p,b,m)
b_seq = (p,a,m,b,b,m,m,b,m,a,p,p,a,p,b)
#a = [a]
#b = [b]

def run(seq):
    global numLines
    for i in seq:
        if isinstance(i, Iterable):
            
            run(i)
        else:
            if not (numLines % 800):
                t.color(next(color))
            numLines += 1
            i()

            
def gen(level, seq=a_seq):
    if level == 1:
        for i in seq:
            yield i
        return None
    if level == 2:
        t.color(next(color))
    for i in seq:
        if i is m or i is p:
            yield i
        elif i is a:
            yield from gen(level-1)
        else:
            yield from gen(level-1, b_seq)
            
    
def step(num):
    global a
    global b
    for i in range(num):
        c = [a,m,b,m,m,b,p,a,p,p,a,a,p,b,m]
        d = [p,a,m,b,b,m,m,b,m,a,p,p,a,p,b]
        a,b = c,d
    run(a)
#    run(b)

def reset():
    t.goto(350,350)
    t.clear()
    