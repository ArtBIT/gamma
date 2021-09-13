import pygame

from .component import Component
from .colours import *

class EmoteComponent(Component):

    def __init__(self,
    
        # required parameters
        image,

        # optional parameters
        timed=True,
        timer=200,
        backgroundColour=WHITE
    
    ):

        self.key = 'emote'
        
        # store the passed parameters
        self.image = image
        self.timed = timed
        self.timer = timer
        self.backgroundColour = backgroundColour

        # set additional component properties
        self.bottomMargin = 10
        self.imagePadding = 2
        self.pointerWidth = 4
        self.pointerHeight = 4
        self.destroy = False
    
    def update(self):

        # decrement timer
        if self.timed:
            self.timer -= 1
            
            # destroy if timer reaches 0
            if self.timer <= 0:
                self.destroy = True


