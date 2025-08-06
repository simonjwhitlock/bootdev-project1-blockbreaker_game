import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, other):
        distance_to = self.position.distance_to(other.position)
        if (self.radius + other.radius) >= distance_to:
            return True
        return False
    
class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x, y, width, height)
        
    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass
    
    def collision(self, other):
        pass