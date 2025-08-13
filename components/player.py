import pygame
from components.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/player_paddle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, 0)
        self.rect.bottom = y
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = 0

    def update(self, dt):
        self.velocity = 0
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            print('right')
            self.move(dt)
        if keys[pygame.K_LEFT]:
            print('left')
            self.move(-dt)
        
        self.x += self.velocity
        print(self.x)
        self.rect.center = (self.x, self.y)
            
    def move(self, dt):
        if (self.rect.left <= 0 and dt < 0):
            print("left edge")
            self.velocity = 0
        elif (self.rect.right >= SCREEN_WIDTH and dt > 0):
            print("right edge")
            self.velocity = 0
        else:
            self.velocity = PLAYER_VELOCITY * dt
            
    def collision(self, other):
        if pygame.sprite.spritecollide(self, other, False):
            if pygame.sprite.spritecollide(self, other, False, pygame.sprite.collide_mask):
                return True
        return False
        