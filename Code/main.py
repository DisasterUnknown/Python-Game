import pygame, sys
from settings import *
from level import Level
from debug import debug

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        pygame.display.set_caption("Zelda")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Level()

    # Rinning environment 
    def run(self):
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                
                if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black') # Background color
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

# Checking if the program is running from the main or other modules 
if __name__ == '__main__':
    game = Game()
    game.run()