import pygame



class GridObject:

    def __init__(self, xpos, ypos, color):
        self.x = xpos
        self.y = ypos
        self.color = color

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getPos(self):
        return (self.x, self.y)

    def getColor(self):
        return self.color
