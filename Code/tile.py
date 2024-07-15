import pygame, os
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((29, 29))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface                                                                                 # Getting the file
        # self.image = pygame.transform.smoothscale(self.image, (ZOOMSIZE, ZOOMSIZE))                          # Setting the file size
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0)    # Hitbox Size