# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:41:46 2016

@author: Myself
"""
from functools import wraps
from collections import namedtuple

_parameters = {}

def boundry(func):
    points = func()
    if points[0] != points[-1]:
        try:
            points.append(points[0])
        except Exception:
            points = list(points) + [points[0]]
    # TODO: Check if the boundry is valid
    boundry = []
    iterPoints = iter(points)
    prev = next(iterPoints)
    for curr in iterPoints:
        boundry.append((prev, curr))
        prev = curr
    
    def inner():
        return boundry
    
    return inner

def parameters(*args, **parameters):
    global _parameters
    _parameters = parameters
#    print(_parameters)


def region(*, boundry, parameters=None, **kwargs):
    if parameters is None:
        pass
    print(boundry, parameters, kwargs)
    return 'Worked'

#def region(*args, **localParams):
#    def wrapper(func):
#        def inner(boundery):
#            pars = {}
#            for key, value in _parameters.items():
#                if key in localParams:
#                    pars[key] = localParams[key]
#                else:
#                    pars[key] = value
#            print(pars)
#            return 'region done'
#        return inner
#    return wrapper
    
    
    
    
    
    
    
    
    
    
    
    