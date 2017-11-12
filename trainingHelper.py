# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 21:49:45 2017

@author: lipec
"""
from random import choice
from numpy import array, dot, random
import logicalOperations as logic

# Structure: (Array [...values, bias], expectedResult)

# Two Bits 
training_data2 = [(array([0,0,1]), 0),
                  (array([0,1,1]), 0),
                  (array([1,0,1]), 0),
                  (array([1,1,1]), 0),
                ]

# Three Bits
training_data3 = [(array([0,0,0,1]), 0),
                  (array([0,0,1,1]), 0),
                  (array([0,1,0,1]), 0),
                  (array([0,1,1,1]), 0),
                  (array([1,0,0,1]), 0),
                  (array([1,0,1,1]), 0),
                  (array([1,1,0,1]), 0),
                  (array([1,1,1,1]), 0),
                ]

# Four Bits    
training_data4 = [(array([0,0,0,0,1]), 0),
                  (array([0,0,0,1,1]), 0),
                  (array([0,0,1,0,1]), 0),
                  (array([0,0,1,1,1]), 0),
                  (array([0,1,0,0,1]), 0),
                  (array([0,1,0,1,1]), 0),
                  (array([0,1,1,0,1]), 0),
                  (array([0,1,1,1,1]), 0),
                  (array([1,0,0,0,1]), 0),
                  (array([1,0,0,1,1]), 0),
                  (array([1,0,1,0,1]), 0),
                  (array([1,0,1,1,1]), 0),
                  (array([1,1,0,0,1]), 0),
                  (array([1,1,0,1,1]), 0),
                  (array([1,1,1,0,1]), 0),
                  (array([1,1,1,1,1]), 0),
                ]

# Five Bits
training_data5 = [(array([0,0,0,0,0,1]), 0),
                  (array([0,0,0,0,1,1]), 0),
                  (array([0,0,0,1,0,1]), 0),
                  (array([0,0,0,1,1,1]), 0),
                  (array([0,0,1,0,0,1]), 0),
                  (array([0,0,1,0,1,1]), 0),
                  (array([0,0,1,1,0,1]), 0),
                  (array([0,0,1,1,1,1]), 0),
                  (array([0,1,0,0,0,1]), 0),
                  (array([0,1,0,0,1,1]), 0),
                  (array([0,1,0,1,0,1]), 0),
                  (array([0,1,0,1,1,1]), 0),
                  (array([0,1,1,0,0,1]), 0),
                  (array([0,1,1,0,1,1]), 0),
                  (array([0,1,1,1,0,1]), 0),
                  (array([0,1,1,1,1,1]), 0),
                  (array([1,0,0,0,0,1]), 0),
                  (array([1,0,0,0,1,1]), 0),
                  (array([1,0,0,1,0,1]), 0),
                  (array([1,0,0,1,1,1]), 0),
                  (array([1,0,1,0,0,1]), 0),
                  (array([1,0,1,0,1,1]), 0),
                  (array([1,0,1,1,0,1]), 0),
                  (array([1,0,1,1,1,1]), 0),
                  (array([1,1,0,0,0,1]), 0),
                  (array([1,1,0,0,1,1]), 0),
                  (array([1,1,0,1,0,1]), 0),
                  (array([1,1,0,1,1,1]), 0),
                  (array([1,1,1,0,0,1]), 0),
                  (array([1,1,1,0,1,1]), 0),
                  (array([1,1,1,1,0,1]), 0),
                  (array([1,1,1,1,1,1]), 0),
                ]

# Six Bits              
training_data6 = [ (array([0,0,0,0,0,0,1]), 0),
                  (array([0,0,0,0,0,1,1]), 0),
                  (array([0,0,0,0,1,0,1]), 0),
                  (array([0,0,0,0,1,1,1]), 0),
                  (array([0,0,0,1,0,0,1]), 0),
                  (array([0,0,0,1,0,1,1]), 0),
                  (array([0,0,0,1,1,0,1]), 0),
                  (array([0,0,0,1,1,1,1]), 0),
                  (array([0,0,1,0,0,0,1]), 0),
                  (array([0,0,1,0,0,1,1]), 0),
                  (array([0,0,1,0,1,0,1]), 0),
                  (array([0,0,1,0,1,1,1]), 0),
                  (array([0,0,1,1,0,0,1]), 0),
                  (array([0,0,1,1,0,1,1]), 0),
                  (array([0,0,1,1,1,0,1]), 0),
                  (array([0,0,1,1,1,1,1]), 0),
                  (array([0,1,0,0,0,0,1]), 0),
                  (array([0,1,0,0,0,1,1]), 0),
                  (array([0,1,0,0,1,0,1]), 0),
                  (array([0,1,0,0,1,1,1]), 0),
                  (array([0,1,0,1,0,0,1]), 0),
                  (array([0,1,0,1,0,1,1]), 0),
                  (array([0,1,0,1,1,0,1]), 0),
                  (array([0,1,0,1,1,1,1]), 0),
                  (array([0,1,1,0,0,0,1]), 0),
                  (array([0,1,1,0,0,1,1]), 0),
                  (array([0,1,1,0,1,0,1]), 0),
                  (array([0,1,1,0,1,1,1]), 0),
                  (array([0,1,1,1,0,0,1]), 0),
                  (array([0,1,1,1,0,1,1]), 0),
                  (array([0,1,1,1,1,0,1]), 0),
                  (array([0,1,1,1,1,1,1]), 0),
                  (array([1,0,0,0,0,0,1]), 0),
                  (array([1,0,0,0,0,1,1]), 0),
                  (array([1,0,0,0,1,0,1]), 0),
                  (array([1,0,0,0,1,1,1]), 0),
                  (array([1,0,0,1,0,0,1]), 0),
                  (array([1,0,0,1,0,1,1]), 0),
                  (array([1,0,0,1,1,0,1]), 0),
                  (array([1,0,0,1,1,1,1]), 0),
                  (array([1,0,1,0,0,0,1]), 0),
                  (array([1,0,1,0,0,1,1]), 0),
                  (array([1,0,1,0,1,0,1]), 0),
                  (array([1,0,1,0,1,1,1]), 0),
                  (array([1,0,1,1,0,0,1]), 0),
                  (array([1,0,1,1,0,1,1]), 0),
                  (array([1,0,1,1,1,0,1]), 0),
                  (array([1,0,1,1,1,1,1]), 0),
                  (array([1,1,0,0,0,0,1]), 0),
                  (array([1,1,0,0,0,1,1]), 0),
                  (array([1,1,0,0,1,0,1]), 0),
                  (array([1,1,0,0,1,1,1]), 0),
                  (array([1,1,0,1,0,0,1]), 0),
                  (array([1,1,0,1,0,1,1]), 0),
                  (array([1,1,0,1,1,0,1]), 0),
                  (array([1,1,0,1,1,1,1]), 0),
                  (array([1,1,1,0,0,0,1]), 0),
                  (array([1,1,1,0,0,1,1]), 0),
                  (array([1,1,1,0,1,0,1]), 0),
                  (array([1,1,1,0,1,1,1]), 0),
                  (array([1,1,1,1,0,0,1]), 0),
                  (array([1,1,1,1,0,1,1]), 0),
                  (array([1,1,1,1,1,0,1]), 0),
                  (array([1,1,1,1,1,1,1]), 0),
                ]
def putResultsOnData(data, operation):
    result = []
    for element in data:
        operationResult = logic.expectedResult(element[0], operation)
        result.append( (element[0], operationResult) )

    return result

def getTrainingData(size,operation):
    switcher = {
        2: putResultsOnData(training_data2, operation),
        3: putResultsOnData(training_data3, operation),
        4: putResultsOnData(training_data4, operation),
        5: putResultsOnData(training_data5, operation),
        6: putResultsOnData(training_data6, operation),
    }
    
    return switcher.get(size,'Input Size not Supported')

