

import pygame

class Grid:

    _divisor = 10
    def __init__(self, width, height):
        self.map_width = (int)(width / _divisor)
        self.map_height = (int)(height / _divisor)
        self.grid = [[None]*self.map_width for x in range(self.map_height)]
    

