import pygame
from pygame import*

LARGEUR_ECRAN = 1900
HAUTEUR_ECRAN = 1200

class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 0, 0))



class Personnage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)


pygame.init()

pygame.display.set_caption("Test pour un nouveau jeu")

ecran = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])

continuer = True
while continuer:
    
    for event in pygame.event.get():
        if event == pygame.QUIT:
            continuer = False


pygame.quit()



