import pygame
from components.constants import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, health=4):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/blue_block.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        
    def update(self,dt):
        
        if self.health == 4:
            self.image = pygame.image.load("assets/blue_block.png").convert_alpha()
        elif self.health == 3:
            self.image = pygame.image.load("assets/green_block.png").convert_alpha()
        elif self.health == 2:
            self.image = pygame.image.load("assets/yellow_block.png").convert_alpha()
        elif self.health == 1:
            self.image = pygame.image.load("assets/red_block.png").convert_alpha()
        elif self.health == 0:
            self.kill()
            
    def collision(self, other):
        if pygame.sprite.spritecollide(self, other, False):
            if pygame.sprite.spritecollide(self, other, False, pygame.sprite.collide_mask):
                self.health -= 1
                print(self.health)
                return True
        return False