import pygame
from components.constants import *
from components.Rectshape import *

class Block(Rectshape):
    def __init__(self, x, y, health=4):
        super().__init__(x, y)
        self.image = pygame.image.load("assets/blue_block.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        
    def update(self,dt):
        
        if (self.health == 4):
            self.image = pygame.image.load("assets/blue_block.png")
        elif (self.health == 3):
            self.image = pygame.image.load("assets/green_block.png")
        elif (self.health == 2):
            self.image = pygame.image.load("assets/yellow_block.png")
        elif (self.health == 1):
            self.image = pygame.image.load("assets/red_block.png")
            
    def collision(self, other):
        if pygame.sprite.spritecollide(self, other, False):
            if pygame.sprite.spritecollide(self, other, False, pygame.sprite.collide_mask):
                return True
        return False
    
    
class BlockRow(pygame.sprite.Sprite):
    def __init__(self, y, blockhealth):
        self.y = y
        self.rowlen = BLOCK_PER_ROW
        self.blockhealth = blockhealth
        self.blockspace = 48

        i = 0
        x = self.blockspace /2
        while (i < self.rowlen):
            block = Block(x, self.y, self.blockhealth)
            x = x + self.blockspace
            i = i + 1
            
class BlockArray(pygame.sprite.Sprite):
    def __init__(self, y, rowcount, rowspace):
        self.y = y
        self.rowspace = rowspace
        self.rowcount = rowcount
        
        j = 0
        while (j < self.rowcount):
            row = BlockRow(self.y, 4)
            self.y = self.y + self.rowspace
            j = j + 1
        