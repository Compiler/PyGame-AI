

import pygame

from GridObject import GridObject


class Grid:

    _divisor = 10

    def __init__(self, width, height):
        self.map_width = (int)(width / self._divisor)
        self.map_height = (int)(height / self._divisor)
        self.grid = [[None]*self.map_height for x in range(self.map_width)]

    
    def add(self, gridType):
        if not isinstance(gridType, GridObject):
            raise TypeError
        
        x = (int)(gridType.getX() / self._divisor)
        y = (int)(gridType.getY() / self._divisor)
        self.grid[x][y] = gridType


    def add_new(self, x, y, gridType):
        if not isinstance(gridType, GridObject):
            raise TypeError
        self.grid[x][y] = gridType

    def render(self, screen):
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                if isinstance(self.grid[x][y], GridObject):
                    self.grid[x][y].render(screen, self._divisor, self._divisor)
                elif x == 5 and y == 5:
                  
                    a = x * self._divisor
                    b = y * self._divisor
                    w = self._divisor
                    pygame.draw.rect(screen, (200, 255, 200), pygame.Rect(a, b, w, w))
