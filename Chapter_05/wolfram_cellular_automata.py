import numpy
import matplotlib.pyplot as pyplot
from matplotlib import animation

N = 100
M = 200


print("Wolfram - Cellular Automata simple simulator\n")
ruleset = input("Wolfram Rule to simulate(#): ")

cell = numpy.zeros((N, M), numpy.int8)
cell[0,int((M-1)/2)] = -1


wolframRule = "{0:08b}".format(int(ruleset))
wolframRule = list(wolframRule)
contFlag = False


def buildCA(data):
    global cell
    newCell = cell.copy()

    for i in range(1, N):
        for j in range(M):
            c = cell[(i-1)%N, j]
            r = cell[(i-1)%N, (j+1)%M]
            l = cell[(i-1)%N, (j-1)%M]
            #111
            if l == -1 and c == -1 and r == -1:
                if wolframRule[0] == '1':
                    newCell[i, j] = -1
                else:
                    newCell[i, j] = 0
            #110
            if l == -1 and c == -1 and r == 0:
                if wolframRule[1] == '1':
                    newCell[i, j] = -1
                else:
                    newCell[i, j] = 0
            #101
            if l == -1 and c == 0 and r == -1:   
                if wolframRule[2] == '1':
                    newCell[i, j] = -1
                else:
                    newCell[i, j] = 0
            #100
            if l == -1 and c == 0 and r == 0:  
                if wolframRule[3] == '1':
                    newCell[i, j] = -1
                else:
                    newCell[i, j] = 0
            #011
            if l == 0 and c == -1 and r == -1:   
                if wolframRule[4] == '1':
                    newCell[i, j] = -1
                else:
                    newCell[i, j] = 0
            #010
            if l == 0 and c == -1 and r == 0:   
                if wolframRule[5] == '1':
                    newCell[i, j] = -1
                else:
                    newCell[i, j] = 0
            #001
            if l == 0 and c == 0 and r == -1:   
                 if wolframRule[6] == '1':
                    newCell[i, j] = -1
                 else:
                     newCell[i, j] = 0
            #000
            if l == 0 and c == 0 and r == 0:  
                 if wolframRule[7] == '1':
                    newCell[i, j] = -1
                 else:
                     newCell[i, j] = 0


    for i in range(1, N):
        for j in range(M):
            if cell[i, j] != newCell[i, j]:
                contFlag = True
            else:
                contFlag = False


    if contFlag == True:
        print("finshed.")


    mat.set_data(newCell)
    cell = newCell
    return mat


fig, axes = pyplot.subplots()

mat = axes.matshow(cell)
ani = animation.FuncAnimation(fig, buildCA, interval=50, save_count=50)
pyplot.show()
