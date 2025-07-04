import pygame
from pygame import *
import sys

pygame.init()
pygame.mixer.init()

LARGEUR_ECRAN = 1900
HAUTEUR_ECRAN = 1200

fenetre = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption("PACMAN")

joueur_image = pygame.image.load("C:\\Users\\Qadis\\OneDrive\\Documents\\Python Games\\pacman.png").convert_alpha()
joueur_rect = joueur_image.get_rect()
joueur_rect.topleft = (100, 100)
pygame.mixer.music.load("C:\\Users\\Qadis\\OneDrive\\Documents\\Python Games\\pacman-music.ogg")
pygame.mixer.music.play(loops=0)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    touche = pygame.key.get_pressed()
    vitesse = 5

    if touche[pygame.K_LEFT]:
        joueur_rect.x -= vitesse
    if touche[pygame.K_RIGHT]:
        joueur_rect.x += vitesse
    if touche[pygame.K_UP]:
        joueur_rect.y -= vitesse
    if touche[pygame.K_DOWN]:
        joueur_rect.y += vitesse


    fenetre.fill((0, 0, 0))
    fenetre.blit(joueur_image, joueur_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



