import pygame
from components.constants import *
from components.shapes import CircleShape

class Ball(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        