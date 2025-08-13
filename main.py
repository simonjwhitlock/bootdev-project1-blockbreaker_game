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
    
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT - GAME_PADDING)
    ball1 = Ball(SCREEN_WIDTH /2, 20)
    
    updatable.add(player,ball1)
    drawable.add(player,ball1)
    balls.add(ball1)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        
        collisions = pygame.sprite.spritecollide(player,balls,False,pygame.sprite.collide_mask)
        if len(collisions) > 0:
            for ball in collisions:
                print(ball)
                print(player.velocity)
                ball.reflect((player.velocity, -1))
        
        if player.collision(balls):
            print("ball colliding with player")
        
        screen.fill("black")
        
        drawable.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
	main()