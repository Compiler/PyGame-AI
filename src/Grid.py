

import pygame

from GridObject import GridObject


class Grid:

    _divisor = 10
    def __init__(self, width, height):
        self.map_width = (int)(width / _divisor)
        self.map_height = (int)(height / _divisor)
        self.grid = [[GridObject]*self.map_width for x in range(self.map_height)]
    


    def render():
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                self.grid[x][y].render()
