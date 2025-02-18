import pygame
from .image import Image

class Tile:

    def __init__(self,
    
        # optional parameters
        name=None,
        image=None,
        solid=False
    
    ):
    
        self.name = name
        self.image = image
        self.solid = solid
    
    # just draws the tile to the surface provided
    def draw(self, scene, x, y, size, alpha=255):
        if self.image is None:
            return
        scene.renderer.add(Image(
            self.image,
            x, y,
            size, size,
            alpha = alpha
        ))

    # renders the map for all entities with a camera
    def render(self, scene, x, y, size, alpha=255):
        if self.image is None:
            return
        scene.renderer.add(Image(
            self.image,
            x, y,
            size, size,
            alpha = alpha
        ), scene = False)
