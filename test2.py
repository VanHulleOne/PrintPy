# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 07:32:17 2016

@author: Myself
"""

import turtle as t
from itertools import cycle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet',
          'blue violet', 'brown', 'burlywood', 'dark green', 'gold',
          'lavender']

def reset():
    t.goto(350,350)
    t.clear()

    
class SpaceCurve:
    
    def __init__(self, sideLength=7):
        self.sideLength = sideLength
        self.color = cycle(colors)
        t.color(next(self.color))
        
    def curve_gen(self, level, seq=None):
        cls = type(self)
        
        if seq is None:
            seq = cls.a_seq
        
        if level == 1:
            for i in seq:
                yield i
            return None
        if level == 2:
            t.color(next(self.color))
        for i in seq:
            if i is cls.a:
                yield from self.curve_gen(level-1)
            elif i is cls.b:
                yield from self.curve_gen(level-1, cls.b_seq)
            else:
                yield i
                
    def __call__(self, level):
        for i in self.curve_gen(level):
            i(self.sideLength)
    
class Gosper(SpaceCurve):
    a = lambda sideLength : t.forward(sideLength)
    p = lambda _ : t.left(60)
    m = lambda _ : t.left(-60)
    b = lambda sideLength : t.forward(sideLength)   
    
    a_seq = (a,m,b,m,m,b,p,a,p,p,a,a,p,b,m)
    b_seq = (p,a,m,b,b,m,m,b,m,a,p,p,a,p,b)
    

class Hilbert(SpaceCurve):
    a = lambda _ : None
    b = lambda _ : None
    f = lambda sideLength : t.forward(sideLength)
    p = lambda _ : t.right(90)
    m = lambda _ : t.right(-90)
    
    a_seq = (m,b,f,p,a,f,a,p,f,b,m)
    b_seq = (p,a,f,m,b,f,b,m,f,a,p)
                   