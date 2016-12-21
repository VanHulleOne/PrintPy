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
    
    rules = NotImplemented
    consts = NotImplemented
    axiom = NotImplemented
    
    def __init__(self, sideLength=7):
        self.sideLength = sideLength
        self.color = cycle(colors)
        t.color(next(self.color))
        
    def curve_gen(self, level, seq):
        cls = type(self)

        if level == 1:
            for i in seq:
                if i in cls.consts:
                    yield cls.consts[i]
            return None
        if level == 2:
            t.color(next(self.color))
        for i in seq:
            if i in cls.rules:
                yield from self.curve_gen(level-1, cls.rules[i])
            elif i in cls.consts:
                yield cls.consts[i]
                
    def __call__(self, level):
        cls = type(self)
        for i in self.curve_gen(level, cls.axiom):
            i(self.sideLength)
    
class Gosper(SpaceCurve):
    rules = {'a' : 'a-b--b+a++aa+b-',
            'b' : '+a-bb--b-a++a+b',
            }
            
    consts = {'a' : lambda sideLength : t.forward(sideLength),
              '+' : lambda _ : t.left(60),
              '-' : lambda _ : t.left(-60),
              'b' : lambda sideLength : t.forward(sideLength),
              }

    axiom = 'a'
    

class Hilbert(SpaceCurve):
    consts = {'f' : lambda sideLength : t.forward(sideLength),
              '+' : lambda _ : t.right(90),
              '-' : lambda _ : t.right(-90),
              }
    
    rules = {'a' : '-bf+afa+fb-',
             'b' : '+af-bfb-fa+',
             }

    axiom = 'a'

class Moore(SpaceCurve):
    consts = {'f' : lambda sideLength : t.forward(sideLength),
              '+' : lambda _ : t.left(90),
              '-' : lambda _ : t.left(-90),
              }
              
    rules = {'l' : '-rf+lfl+fr-',
             'r' : '+lf-rfr-fl+',
             }

    axiom = 'lfl+f+lfl'
                  