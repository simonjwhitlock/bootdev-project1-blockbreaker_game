import pygame
from components.constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/ball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = pygame.Vector2(0, BALL_START_VELOCITY)
        
        
    def update(self, dt):
        self.rect.center += self.velocity * dt
        
