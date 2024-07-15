import pygame
import os
from suport import *
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Sprit setup
        self.create_map()
        
    # Creating the map
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout(os.path.join('Code', '../Resources/World/Dot Map/', 'Coliders.csv'))
        }
        
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * (FLOOR_WIDTH / 100)
                        y = row_index * (FLOOR_HIGHT / 106)
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')

        #         # Displaying the imgs
        #         if col == 'x':
        #             Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
        #         if col == 'p':
        #             self.Player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)    
        self.Player = Player((1500, 2900),[self.visible_sprites], self.obstacle_sprites)
        
                

    def run(self):
        # Update and draw the game
        self.visible_sprites.custom_draw(self.Player)
        self.visible_sprites.update()
        debug(self.Player.direction)



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        # General setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        # Creating the map
        self.floor_surf = pygame.image.load(os.path.join('Code', '../Resources/World/Map', 'Map.png')).convert()
        
        self.floor_surf = pygame.transform.smoothscale(self.floor_surf, (FLOOR_WIDTH, FLOOR_HIGHT))
        self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))
        
    def custom_draw(self, player):
        
        # Getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        # Drawing the flow 
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)