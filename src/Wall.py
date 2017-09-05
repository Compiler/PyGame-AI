import pygame
from GridObject import GridObject

class Wall(GridObject):

    
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, ((150, 22, 11)))


