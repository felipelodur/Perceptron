# Perceptron
Implementation of Perceptron as coursework for Artificial Intelligence course @ PUC Minas


## Program Files
- **logicalOperations.py:** Calculates expected result for logical operations (And, Or and Xor)
- **trainingHelper.py:** Sets up training data.
- **perceptron.py:** Perceptron implementation. 

## Input File
In the input directory, there is one example input file. Each line represents one input, that needs to in the (2-6) range. That is, a minimum of 2 bits and a maximum of 6 bits per line.
Each bit is considered a entry in the system and the chosen logical operation will be applied as if it is a multiple entry.

## How to run
With every file in the same directory, run *python perceptron.py*, and, when required, enter input file relative or full path, learning rate, number of iterations and logical operation.

If any dependency is missing in your environment, run *pip install dependency*. Missing dependencies will be indicated when running *perceptron.py*.
