# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 07:32:17 2016

@author: Myself
"""

import turtle as t

f = lambda : t.forward(20)
p = lambda : t.left(60)
m = lambda : t.left(-60)
b = lambda : t.forward(20)

a = [f]
b = [b]

def step():
    a = [a,m,b,m,m,b,p,a,p,p,a,a,p,b,m]
    b = []