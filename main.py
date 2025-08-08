import pygame
from components.constants import *
from components.player import *
from components. ball import *

def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable, balls)
    
    player = Player(SCREEN_HEIGHT - GAME_PADDING - PLAYER_HEIGHT, (SCREEN_WIDTH/2) - (PLAYER_WIDTH/2))
    ball = Ball(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
	main()