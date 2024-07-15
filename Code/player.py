import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('Code', '..', 'Resources', 'player.png')).convert_alpha()   # Getting the file
        self.image = pygame.transform.smoothscale(self.image, (ZOOMSIZE - 10, ZOOMSIZE - 5))                             # Setting the file size
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0)    # Hitbox Size
        
        self.direction = pygame.math.Vector2()
        self.speed = SPEED                            # Player Speen
        
        self.obstacle_sprites = obstacle_sprites
        
    # Checking the user Inputs
    def input(self):
        keys = pygame.key.get_pressed()   # Getting the pressed keys
        
        # Giving the functions for the pressed keys
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            
    # Checking if the plyers moving
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed  # Setting the speed with the dirrection
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed  # Setting the speed with the dirrection
        self.collision('vertical')
        self.rect.center = self.hitbox.center  # Making the center of the player to the center of the hitbox
        
    # Adding mecanisims for blocks that cann't be overlap
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # Moving left
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom
                        
                    
    # Updating the funtions in the screen
    def update(self):
        self.input()
        self.move(self.speed)
        