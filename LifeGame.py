import pygame
import numpy as np
import time

width,height = 700,700
nX, nY = 50, 50
dimX = width/nX
dimY = height/nY

pygame.init()
screen = pygame.display.set_mode([height,width])

bg = (25,25,25)
live_color = (255,255,255)
dead_color = (128,128,128)
# cell state 1=life,0=death
gameState = np.zeros((nX,nY))

pause = False

ciclo = True
# cicle
while ciclo:
    newGameState = np.copy(gameState)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pause = not pause

        if event.type == pygame.QUIT:
            ciclo = False

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y = int(np.floor(posX/dimX)), int(np.floor(posY/dimY))
            newGameState[x,y] = not mouseClick[2]


    screen.fill(bg) # clean screen

    for x in range(0,nX):
        for y in range(0,nY):

            if not pause:
                # near neighborgs
                n_neigh  =  gameState[(x-1)%nX,(y-1)%nY] + gameState[x%nX,(y-1)%nY] + \
                            gameState[(x+1)%nX,(y-1)%nY] + gameState[(x-1)%nX,y%nY] + \
                            gameState[(x+1)%nX,y%nY] + gameState[(x-1)%nX,(y+1)%nY]+\
                            gameState[x%nX,(y+1)%nY] + gameState[(x+1)%nX,(y+1)%nY]

                # Rule 1 a death cell with exactly 3 neighborgs revives
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1

                # Rule 2: a living cell with less than 2 or more than 3 neighborgs alive deaths
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0

            poly = [(x*dimX,y*dimY),((x+1)*dimX,y*dimY),((x+1)*dimX,(y+1)*dimY),(x*dimX,(y+1)*dimY)]

            if newGameState[x,y] == 1:
                pygame.draw.polygon(screen,live_color,poly,0)
            else:
                pygame.draw.polygon(screen,dead_color,poly,1)

    gameState = np.copy(newGameState)
    pygame.display.flip()

pygame.quit()
