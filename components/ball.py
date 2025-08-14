import pygame
from components.constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/ball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = pygame.Vector2(0, BALL_START_VELOCITY)
        
    def reflect(self, NV):
        self.velocity = self.velocity.reflect(pygame.math.Vector2(NV))

    def update(self, dt):
        self.rect.center += self.velocity * dt
        
        if self.rect.left <= 0:
            self.reflect((1, 0))
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.reflect((-1, 0))
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.reflect((0, 1))
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.reflect((0, -1))
            self.rect.bottom = SCREEN_HEIGHT
    
