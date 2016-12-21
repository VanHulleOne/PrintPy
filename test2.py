# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 07:32:17 2016

@author: Myself
"""

import turtle as t
from collections import Iterable
from itertools import cycle

numLines = 0;

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet',
          'blue violet', 'brown', 'burlywood', 'dark green', 'gold',
          'lavender']

class Gosper: 
    

    
    def __init__(self, sideLength=7):
        self.sideLength = sideLength
        self.color = cycle(colors)
        t.color(next(self.color))
        self.a = lambda sideLength : t.forward(sideLength)
        self.p = lambda _ : t.left(60)
        self.m = lambda _ : t.left(-60)
        self.b = lambda sideLength : t.forward(sideLength)
        self.a_seq = (self.a,self.m,self.b,self.m,self.m,self.b,self.p,self.a,self.p,self.p,self.a,self.a,self.p,self.b,self.m)
        self.b_seq = (self.p,self.a,self.m,self.b,self.b,self.m,self.m,self.b,self.m,self.a,self.p,self.p,self.a,self.p,self.b)
              
    def gosper_curve_gen(self, level, seq):
        print(level)
        if level == 1:
            for i in seq:
                yield i
            return None
        if level == 2:
            t.color(next(self.color))
        for i in seq:
            if i is self.a:
                print('Is a')
                yield from self.gosper_curve_gen(level-1, self.a_seq)
            elif i is self.b:
                print('Is b')
                yield from self.gosper_curve_gen(level-1, self.b_seq)
            else:
                print('Not')
                yield i
    def __call__(self, level):
        for i in self.gosper_curve_gen(level, self.a_seq):
            i(self.sideLength)
            
def reset():
    t.goto(350,350)
    t.clear()
    