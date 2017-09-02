

import pygame

from GridObject import GridObject


class Grid:

    _divisor = 10

    def __init__(self, width, height):
        self.map_width = (int)(width / self._divisor)
        self.map_height = (int)(height / self._divisor)
        self.grid = [[GridObject]*self.map_width for x in range(self.map_height)]


    def render(self, screen):
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                if isinstance(self.grid[x][y], GridObject) :
                    self.grid[x][y].render(screen, self._divisor, self._divisor)
