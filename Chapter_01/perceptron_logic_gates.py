#Natural Computing with Python
#Chapter 1 - Neural Networks
#Perceptron logic gates

import numpy as np

#Define the AND logic gate
def And(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-1.5, 1, 1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

#Define the OR logic gate
def Or(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-0.5, 1, 1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1
    
#Define the NAND logic gate
def Nand(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([1.5, -1, -1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

#MAIN function
if __name__ == '__main__':

    #input array
    input = [(0, 0), (1, 0), (0, 1), (1, 1)]

    #start evaluation
    print("AND")
    for x in input:
        y = And(x[0], x[1])
        print(str(x) + " -> " + str(y))

    print("OR")
    for x in input:
        y = Or(x[0], x[1])
        print(str(x) + " -> " + str(y))

    print("NAND")
    for x in input:
        y = Nand(x[0], x[1])
        print(str(x) + " -> " + str(y))
