#************************************************
# Rules of the game
#   1. If the ant is on a black square, it turns
#       right 90 and moves forward one unit
#   2. If the ant is on a white square, it turns
#       left 90 and moves forward one unit
#   3. When the ant leaves a square, it inverts
#       colour
#
# SEE: http://mathworld.wolfram.com/LangtonsAnt.html
#************************************************
 
import sys, pygame
from pygame.locals import *
import time
 
dirs = ((-1, 0),(0, 1),(1, 0),(0, -1))
 
cellSize = 8 # size in pixels of the board (4 pixels are used to draw the grid)
numCells = 100 # length of the side of the board

#drawing parameters

background = 1, 1, 1 # background colour; black here
foreground = 23, 23, 23 # foreground colour; the grid's colour; dark gray here
textcol = 177, 177, 177 # the colour of the step display in the upper left of the screen
antwalk = 44, 88, 44 # the ant's trail; greenish here
antant = 222, 44, 44 # the ant's colour; red here
fps = 1.0 / 40 # time between steps; 1.0 / 40 means 40 steps per second
 

pygame.init()

size = width, height = numCells * cellSize, numCells * cellSize

pygame.display.set_caption("Langton's Ant")
# Screen is now an object representing the window in which we paint
screen = pygame.display.set_mode(size) 
screen.fill(background)
# IMPORTANT: No changes are displayed until this function gets called
pygame.display.flip() 

for i in range(1, numCells):
    pygame.draw.line(screen, foreground, (i * cellSize, 1),\
                     (i * cellSize, numCells * cellSize), 2)
    pygame.draw.line(screen, foreground, (1, i * cellSize),\
                     (numCells * cellSize, i * cellSize), 2)

# IMPORTANT: No changes are displayed until this function gets called
pygame.display.flip() 
font = pygame.font.Font(None, 36)
coord_ant_X = int(numCells / 2)
coord_ant_Y = coord_ant_X
antdir = 0
board = [[False] * numCells for e in range(numCells)]
step = 1
pause = False
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                exit
            elif event.type == KEYUP:
                if event.key == 32: # If space pressed, pause or unpause
                    pause = not pause
    if pause:
        time.sleep(fps)
        continue


    text = font.render("%d " % (step), True, textcol, background)
    screen.blit(text, (10, 10))
     
    if board[coord_ant_X][coord_ant_Y]:
        board[coord_ant_X][coord_ant_Y] = False # See rule 3
        screen.fill(background, pygame.Rect(coord_ant_X * cellSize + 1,\
                                            coord_ant_Y * cellSize + 1,\
                                            cellSize - 2, cellSize - 2))
        antdir = (antdir + 1) % 4 # See rule 1
    else:
        board[coord_ant_X][coord_ant_Y] = True # See rule 3
        screen.fill(antwalk, pygame.Rect(coord_ant_X * cellSize + 1,\
                                         coord_ant_Y * cellSize + 1,\
                                         cellSize - 2, cellSize - 2))
        antdir = (antdir + 3) % 4 # See rule 2

    coord_ant_X = (coord_ant_X + dirs[antdir][0]) % numCells
    coord_ant_Y = (coord_ant_Y + dirs[antdir][1]) % numCells

    # The current square (i.e. the ant) is painted a different colour
    screen.fill(antant, pygame.Rect(coord_ant_X * cellSize + 1,\
                                    coord_ant_Y * cellSize + 1, \
                                    cellSize -2, cellSize -2))

    pygame.display.flip() # IMPORTANT: No changes are displayed until this function gets called

    step += 1
    time.sleep(fps)

 

