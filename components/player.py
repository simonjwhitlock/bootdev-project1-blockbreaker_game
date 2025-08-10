import pygame
from components.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, y, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/player_paddle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.y, self.x)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.move(dt)
        if keys[pygame.K_LEFT]:
            self.move(-dt)
            
    def move(self, dt):
        if (self.y <= 0 and dt < 0):
            print("left edge")
        elif (self.y >= (SCREEN_WIDTH - PLAYER_WIDTH) and dt > 0):
            print("right edge")
        else:
            self.y += PLAYER_VELOCITY * dt
            self.rect.center = (self.y, self.x)
            
    def collision(self, other):
        if pygame.sprite.spritecollide(self, other, False):
            if pygame.sprite.spritecollide(self, other, False, pygame.sprite.collide_mask):
                print("collide")
                return True
        return False
        