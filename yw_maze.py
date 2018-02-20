#!/usr/bin/env python
import pygame
from pygame import locals as pl

pygame.init()

X = 0
Y = 1
sol = 0
mur = 1
out = 2
labyrinthe = [[mur, mur, mur, mur, mur, mur, mur, mur, mur, mur],
              [mur, sol, mur, sol, sol, sol, mur, mur, out, mur],
              [mur, sol, mur, sol, mur, sol, mur, sol, sol, mur],
              [mur, sol, sol, sol, mur, sol, mur, sol, mur, mur],
              [mur, sol, mur, mur, mur, mur, mur, sol, sol, mur],
              [mur, sol, sol, mur, sol, sol, sol, mur, sol, mur],
              [mur, mur, sol, sol, sol, mur, sol, mur, sol, mur],
              [mur, sol, mur, mur, mur, mur, sol, mur, sol, mur],
              [mur, sol, sol, sol, sol, sol, sol, sol, sol, mur],
              [mur, mur, mur, mur, mur, mur, mur, mur, mur, mur]]

ecran = pygame.display.set_mode((640, 640), pl.FULLSCREEN)
pygame.mouse.set_visible(False)

image_mur = pygame.image.load("./resources/64/mur_64.jpg").convert()
image_sol = pygame.image.load("./resources/64/sol_64.jpg").convert()
image_out = pygame.image.load("./resources/64/sortie_64.png").convert_alpha()
image_heros = pygame.image.load("./resources/64/heros_64.png").convert_alpha()
image_bravo = pygame.image.load("./resources/bravo.png").convert_alpha()


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


def affiche_heros(ecran, heros):
    ecran.blit(image_heros, (heros[X] * 64, heros[Y] * 64))


def affiche_bravo(ecran):
    ecran.blit(image_bravo, (0, 0))


heros = [1, 1]
boucle = True
pause = False
horloge = pygame.time.Clock()
gagne = False
while boucle:
    horloge.tick(60)
    affiche_labyrinthe(ecran, labyrinthe)
    affiche_heros(ecran, heros)
    if gagne:
        affiche_bravo(ecran)
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            boucle = False
        elif evenement.type == pygame.KEYDOWN:
            if not gagne:
                if evenement.key == pygame.K_DOWN:
                    heros[Y] += 1
                    if labyrinthe[heros[Y]][heros[X]] == mur:
                        heros[Y] -= 1
                elif evenement.key == pygame.K_LEFT:
                    heros[X] -= 1
                    if labyrinthe[heros[Y]][heros[X]] == mur:
                        heros[X] += 1
                elif evenement.key == pygame.K_RIGHT:
                    heros[X] += 1
                    if labyrinthe[heros[Y]][heros[X]] == mur:
                        heros[X] -= 1
                elif evenement.key == pygame.K_UP:
                    heros[Y] -= 1
                    if labyrinthe[heros[Y]][heros[X]] == mur:
                        heros[Y] += 1
                elif evenement.key == pygame.K_p:
                    print("PAUSE !")
                    pause = not pause
                if labyrinthe[heros[Y]][heros[X]] == out:
                    gagne = True
            if evenement.key == pygame.K_ESCAPE:
                boucle = False
    pygame.display.flip()

pygame.quit()
