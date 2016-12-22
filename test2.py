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
    axiom = NotImplemented
    
    def __init__(self):
        self.color = cycle(colors)
        t.color(next(self.color))
        
    def curve_gen(self, level, seq):
        if level == 1:
            for i in seq:
                if i in self.consts:
                    yield self.consts[i]
            return None
        if level == 2:
            t.color(next(self.color))
        for i in seq:
            if i in self.rules:
                yield from self.curve_gen(level-1, self.rules[i])
            elif i in self.consts:
                yield self.consts[i]
                
    def __call__(self, level):
        for i in self.curve_gen(level, self.axiom):
            i()
    
class Gosper(SpaceCurve):
    rules = {'a' : 'a-b--b+a++aa+b-',
            'b' : '+a-bb--b-a++a+b',
            }

    axiom = 'a'
    
    def __init__(self, sideLength=7):
        super().__init__()
        self.consts = {'a' : lambda : t.forward(sideLength),
                       '+' : lambda : t.left(60),
                       '-' : lambda : t.left(-60),
                       'b' : lambda : t.forward(sideLength),
                       }

class Hilbert(SpaceCurve):
    
    rules = {'a' : '-bf+afa+fb-',
             'b' : '+af-bfb-fa+',
             }

    axiom = 'a'
    
    def __init__(self, sideLength=7):
        super().__init__()
        self.consts = {'f' : lambda : t.forward(sideLength),
                       '+' : lambda : t.right(90),
                       '-' : lambda : t.right(-90),
                       }

class Moore(SpaceCurve):
              
    rules = {'l' : '-rf+lfl+fr-',
             'r' : '+lf-rfr-fl+',
             }

    axiom = 'lfl+f+lfl'

    def __init__(self, sideLength=7):
        super().__init__()
        self.consts = {'f' : lambda : t.forward(sideLength),
                       '+' : lambda : t.left(90),
                       '-' : lambda : t.left(-90),
                       }

class SierpArrow(SpaceCurve):
    consts = {'a' : lambda sideLength : t.forward(sideLength),
              'b' : lambda sideLength : t.forward(sideLength),
              '+' : lambda _ : t.left(60),
              '-' : lambda _ : t.left(-60),
              }
              
    rules = {'a' : '+b-a-b+',
             'b' : '-a+b+a-',
             }
             
    axiom = 'a'
    
    def __init__(self, sideLength=7):
        super().__init__()
        self.consts = {'a' : lambda : t.forward(sideLength),
                       'b' : lambda : t.forward(sideLength),
                       '+' : lambda : t.left(60),
                       '-' : lambda : t.left(-60),
                       }

class Dragon(SpaceCurve):
    rules = {'x' : 'x+yf+',
             'y' : '-fx-y',
             }
             
    axiom = 'fx'
    
    def __init__(self, sideLength=7):
        super().__init__()
        self.consts = {'f' : lambda : t.forward(sideLength),
                       '+' : lambda : t.right(90),
                       '-' : lambda : t.right(-90),
                       }

class Plant(SpaceCurve):
    def left_bracket(stack):
        def inner():
            pos = t.position()
            heading = t.heading()
            stack.append((pos,heading))
        return inner
        
    def right_bracket(stack):
        def inner():
            t.up()
            pos, heading = stack.pop()
            t.setposition(pos)
            t.setheading(heading)
            t.down()
        return inner
              
    rules = {'x' : 'f-[[x]+x]+f[+fx]-x',
             'f' : 'ff',
             }
             
    axiom = 'x'
    
    def __init__(self, sideLength=7):
        super().__init__()
        self.color = cycle(['green'])
        t.width(3)
        t.setheading(45)
        self.stack = []
        self.consts = {'f' : lambda : t.forward(sideLength),
                       '+' : lambda : t.right(25),
                       '-' : lambda : t.right(-25),
                       '[' : Plant.left_bracket(self.stack),
                       ']' : Plant.right_bracket(self.stack),
                        }   

