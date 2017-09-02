import pygame


class Wall(GridObject):

    
    def __init__(self, xpos, ypos):
        super.__init__(xpos, ypos, (30, 30, 30))
