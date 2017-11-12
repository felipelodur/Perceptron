# Dependencies
from numpy import dot, random
import trainingHelper as trainData

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

def expectedResult(x,operation):
    result = x[0]
    for i in range(len(x)-1):
        if(i != 0):
            result = executeOperation( [x[i], result],operation)
    return result
        

def trainAndPredict(trainingData, valueToPredict, iterations):
    weight = random.rand(len(valueToPredict))  # Random Weights for First Iteration
    errors = []              # Differences between expected and prediction values
    
    # Train
    for i in range(iterations):
        x, expected = trainingData[i % len(trainingData)]
        result = dot(weight, x)
        error = expected - unitStep(result)
        errors.append(error)
        weight += learningRate * error * x
    
    # Predict
    valuePrediction = unitStep(dot(valueToPredict, weight))
    print("{}: {} -> {}".format(valueToPredict[:len(valueToPredict)-1],
          valuePrediction,
          resultMessage(valuePrediction, expectedResult(valueToPredict,operation)))
    ) 



responseIterations = int(input("Insert number of iterations = "))
n = biggerThanZero(responseIterations)

responseLearning =  float(input("Insert learning rate = "))
learningRate = zeroToOne(responseLearning)

responseOperation = input("Choose AND, OR or XOR = ")
operation = checkOperation(responseOperation)

responseFile = input("Insert input filename  = ")

lines = [line.rstrip('\n') for line in open(responseFile)]


for line in lines:
    inputArray = []
    for i in range(len(line)):
        inputArray.append(int(line[i]))
    
    trainingData = trainData.getTrainingData(len(line),operation)
    inputArray.append(1)
    trainAndPredict(trainingData, inputArray, n)


