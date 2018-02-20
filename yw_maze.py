#!/usr/bin/env python
import pygame
from pygame import locals as pl

pygame.init()

ecran = pygame.display.set_mode((640, 640))#, pl.FULLSCREEN)
pygame.mouse.set_visible(False)

boucle = True
pause = False
while boucle:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            boucle = False
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_DOWN:
                print("haut")
            elif evenement.key == pygame.K_LEFT:
                print("gauche")
            elif evenement.key == pygame.K_RIGHT:
                print("right")
            elif evenement.key == pygame.K_UP:
                print("haut")
            elif evenement.key == pygame.K_p:
                print("PAUSE !")
                pause = not pause
            elif evenement.key == pygame.K_ESCAPE:
                boucle = False

pygame.quit()
