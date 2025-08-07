import pygame
from components.constants import *
from components.shapes import RectangleShape

class Player(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
         
    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.posy, self.posx, self.width, self.height), border_radius=PLAYER_CORNERS)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.move(dt)
        if keys[pygame.K_LEFT]:
            self.move(-dt)
            
    def move(self, dt):
        if (self.posy <= 0 and dt < 0):
            print("left edge")
        elif (self.posy >= (SCREEN_WIDTH - PLAYER_WIDTH) and dt > 0):
            print("right edge")
        else:
            self.posy += PLAYER_VELOCITY * dt