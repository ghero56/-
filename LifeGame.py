import pygame
import numpy as np
import time

pygame.init()

width,height = 1000,1000

# main screen
screen = pygame.display.set_mode((height , width))

# background
bg = 25 , 25 , 25
screen.fill(bg)

# Cells
nxC , nyC = 25 , 25

# dimension
dimCW = width/nxC
dimCH = height/nyC

# cell state 1=life , 0=death
gameState = np.zeros((nxC , nyC))

# cicle
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    for y in range(0,nxC):
        for x in range(0,nyC):
            # near neighborgs
            n_neigh  =  gameState[(x-1)%nxC , (y-1)%nyC] + \
                        gameState[(x)%nxC , (y-1)%nyC] + \
                        gameState[(x+1)%nxC , (y-1)%nyC] + \
                        gameState[(x-1)%nxC , (y)%nyC] + \
                        gameState[(x+1)%nxC , (y)%nyC] + \
                        gameState[(x-1)%nxC , (y+1)%nyC] + \
                        gameState[(x)%nxC , (y+1)%nyC] + \
                        gameState[(x+1)%nxC , (y+1)%nyC]

            # Rule 1 a death cell with exactly 3 neighborgs revives
            if gameState[x , y] == 0 and n_neigh == 3:
                newGameState[x , y] == 1

            # Rule 2: a living cell with less than 2 or more than 3 neighborgs alive deaths
            elif gameState[x , y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x , y] == 0

            poly = [((x)*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    ((x)*dimCW, (y+1)*dimCH)]

            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen , (128,128,128) , poly , 1)
            else:
                pygame.draw.polygon(screen , (255,255,255) , poly , 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()
