# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 21:53:42 2017

@author: lipec
"""

def executeOperation(x,operation):
    switcher = {
        'AND': x[0] and x[1],
        'OR': x[0] or x[1],
        'XOR': x[0] ^ x[1],
    }
    
    return switcher.get(operation,'')

def expectedResult(x,operation):
    result = x[0]
    for i in range(len(x)-1):
        if(i != 0):
            result = executeOperation( [x[i], result],operation)
    return result