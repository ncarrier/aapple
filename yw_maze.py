#!/usr/bin/env python
import pygame
from pygame import locals as pl

pygame.init()

sol = 0
mur = 1
out = 2
labyrinthe = [[mur, mur, mur, mur, mur, mur, mur, mur, mur, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, out, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, mur, mur, mur, mur, mur, mur, mur, mur, mur]]

ecran = pygame.display.set_mode((640, 640))#, pl.FULLSCREEN)
pygame.mouse.set_visible(False)

image_mur = pygame.image.load("./resources/64/mur_64.jpg").convert()
image_sol = pygame.image.load("./resources/64/sol_64.jpg").convert()
image_out = pygame.image.load("./resources/64/sortie_64.png").convert_alpha()
image_heros = pygame.image.load("./resources/64/heros_64.png").convert_alpha()

def affiche_labyrinthe(ecran, labyrinthe):
    for x in range(0, 10):
        for y in range(0, 10):
            if labyrinthe[y][x] == mur:
                ecran.blit(image_mur, (x * 64, y * 64))
            elif labyrinthe[y][x] == sol:
                ecran.blit(image_sol, (x * 64, y * 64))
            elif labyrinthe[y][x] == out:
                ecran.blit(image_sol, (x * 64, y * 64))
                ecran.blit(image_out, (x * 64, y * 64))

boucle = True
pause = False
horloge = pygame.time.Clock()
while boucle:
    horloge.tick(60)
    affiche_labyrinthe(ecran, labyrinthe)
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
    pygame.display.flip()

pygame.quit()
