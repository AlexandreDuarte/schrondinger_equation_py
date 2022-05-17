# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from matplotlib import pyplot
from numpy import *
import cmath

f0 = array([[complex(0,0) for a in range(0,40)] for b in range(0,40)])
f1 = array([[complex(0,0) for a in range(0,40)] for b in range(0,40)])
V = array([[complex(0,0) for a in range(0,40)] for b in range(0,40)])

f0[20][1] = complex(1,1)
V[20][4] = complex(0,4)
V[15][6] = complex(0,4)

a = 0.07
b = 5

dt = 0.08
ds2 = 8

def calculateStep(i, j):
    dif = (-4*f0[i][j] + f0[i+1][j] + f0[i-1][j] + f0[i][j+1] + f0[i][j-1])*dt/ds2 - V[i][j]*f0[i][j]*dt
    f1[i][j] = complex(0,1)*dif - f0[i][j]


pyplot.figure(figsize=(40,40))

for step in range (0,4000):
    for x in range(1,39):
        for y in range(1,39):
            calculateStep(x, y)
    
    graph = [[(a*a.conjugate()).real for a in b] for b in f1]
    if step % 20 == 0:
        pyplot.imshow(graph)
        pyplot.pause(0.05)
        
        
    f0 = f1.copy()
    

pyplot.show()