import pygame
from components.constants import *
from components.shapes import RectangleShape

class Player(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
         
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect, border_radius=PLAYER_CORNERS)