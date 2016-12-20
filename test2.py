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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

color = cycle(colors)

f = lambda : t.forward(side)
p = lambda : t.left(60)
m = lambda : t.left(-60)
b = lambda : t.forward(side)

a = [f]
b = [b]

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
    global a
    global b
    t.goto(300,300)
    t.clear()
    a = [f]
    b = [b]
    