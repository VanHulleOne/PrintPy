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

def layer(parameters=None, **kwargs):
    localParams = kwargs
    try:
        localParams.update(parameters._asdict())
    except Exception:
        pass
    

def parameters(**parameters):
    return namedtuple('Parameters', parameters.keys())(**parameters)

def region(*, boundry, infill = True, parameters=None, **kwargs):
    localParams = kwargs
    try:
        localParams.update(parameters._asdict())
    except Exception:
        pass
    return namedtuple('Region', 'boundry infill ' +
                        ' '.join(localParams.keys()))(boundry=boundry,
                                                        infill=infill,
                                                        **localParams)



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
    
    
    
    
    
    
    
    
    
    
    
    