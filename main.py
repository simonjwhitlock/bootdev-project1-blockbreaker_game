import pygame
from components.constants import *
from components.player import *
from components.ball import *
from components.blocks import *

def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Ball.containers = (updatable,drawable,balls)
    Block.containers = (updatable,drawable,blocks)
    
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT - GAME_PADDING)
    ball1 = Ball(SCREEN_WIDTH /2, 400)
    
    block1 = Block(SCREEN_WIDTH /2, 200)
    
    #updatable.add(player,ball1,block1)
    #drawable.add(player,ball1,block1)
    #balls.add(ball1)
    #blocks.add
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        player_collisions = pygame.sprite.spritecollide(player,balls,False,pygame.sprite.collide_mask)
        if len(player_collisions) > 0:
            for ball in player_collisions:
                print(ball)
                print(player.velocity)
                ball.reflect((player.velocity, -1))
                
        for block in blocks:
            block_collisions = pygame.sprite.spritecollide(block,balls,False,pygame.sprite.collide_mask)
            if len(block_collisions) > 0:
                for ball in block_collisions:
                    print(ball)
                    ball.reflect((0, -1))
                    
        
        
        screen.fill("black")
        
        drawable.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
	main()