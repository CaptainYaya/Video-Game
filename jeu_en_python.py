import pygame as pg
from pygame import *

LARGEUR_ECRAN = 1900
HAUTEUR_ECRAN = 1200

pg.init()

class Vaisseau(pg.sprite.Sprite):

    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pg.Surface((50, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(-5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN

pg.display.set_caption("Test pour le jeu")

ecran = pg.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])
vaisseau = Vaisseau()
continuer = True

while continuer:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuer = False
    
    ecran.fill((0, 0, 0))
    touche_appuyee = pg.key.get_pressed()
    vaisseau.update(touche_appuyee)    
    ecran.blit(vaisseau.surf, vaisseau.rect)
    
    pg.display.flip()

pg.quit()