# -*- coding: utf-8 -*-

# Dependencies
from random import choice
from numpy import array, dot, random

# Lambda Auxiliary Functions
unitStep = lambda x: 0 if x < 0 else 1
resultMessage = lambda x,y: 'RIGHT' if x == y else 'WRONG'
zeroToOne = lambda x: x if 0 < x < 1  else 1
biggerThanZero = lambda x: x if x > 0 else 1
operationCheck = lambda x: x if x in ('AND','OR','XOR') else 'AND'

def checkOperation(operation):
    return operationCheck(operation.upper())

def executeOperation(x,operation):
    switcher = {
        'AND': x[0] and x[1],
        'OR': x[0] or x[1],
        'XOR': x[0] ^ x[1],
    }
    
    return switcher.get(operation,'')

# TODO - XOR as Unique value vs XOR as cascade
def expectedResult(x,operation):
    result = x[0]
    for i in range(len(x)-1):
        if(i != 0):
            result = executeOperation( [x[i], result],operation)
    return result
    

responseIterations = int(input("Insert number of iterations = "))
n = biggerThanZero(responseIterations)

responseLearning =  float(input("Insert learning rate = "))
learningRate = zeroToOne(responseLearning)

responseOperation = input("Choose AND, OR or XOR = ")
operation = checkOperation(responseOperation)

# TODO - Change to ReadFromFile
# Structure: (Array [...values, bias], expectedResult)
training_data = [ (array([0,0,0,1]), 0),
                  (array([0,0,1,1]), 0),
                  (array([0,1,0,1]), 0),
                  (array([0,1,1,1]), 0),
                  (array([1,0,0,1]), 0),
                  (array([1,0,1,1]), 0),
                  (array([1,1,0,1]), 0),
                  (array([1,1,1,1]), 1),
                ]

weight = random.rand(4)  # Random Weights for First Iteration
errors = []              # Difference between expected and prediction values
n = 500                  # Iterations

for i in range(n):
    x, expected = choice(training_data)
    result = dot(weight, x)
    error = expected - unitStep(result)
    errors.append(error)
    weight += learningRate * error * x
    
for x, _ in training_data:
    result = unitStep(dot(x, weight))
    print("{}: {} -> {}".format(x[:len(x)-1], result, resultMessage(result,expectedResult(x,operation))))