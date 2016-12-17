# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:00:46 2016

@author: lvanhulle
"""



import level

@level.boundry
def b1():
    points = ((0,0), (2,0), (2,3))
    return points

level.parameters(pathWidth = 0.5,
               layerHeight = 0.2,
               solidityRatio = 0.98,
               shiftX = 50,
               shiftY = 20,
               numShells = 2,
              )


             
#@level.region(numShells = 1,
#              solidityRatio = 0.76)
#def region1(b1):
#    pass