import pygame
from .component import Component

class ColliderComponent(Component):

    def __init__(self, offsetX, offsetY, w, h, collisionResponse=None):
        
        self.key = 'collider'
        self.rect = pygame.Rect(offsetX, offsetY, w, h)
        
        # function that is called when colliding with other entities or the map
        self.collisionResponse = collisionResponse
    
    def collidingWith(self, otherEntity):
        
        if self.rect is None or otherEntity.rect is None:
            return False
        return self.rect.colliderect(otherEntity.rect)