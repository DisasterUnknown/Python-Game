import pygame, os
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('Code', '..', 'Resources', 'rock.png')).convert_alpha()  # Getting the file
        self.image = pygame.transform.smoothscale(self.image, (ZOOMSIZE, ZOOMSIZE))                          # Setting the file size
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-15)    # Hitbox Size