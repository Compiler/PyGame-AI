import pygame



class GridObject:

    def __init__(self, xpos, ypos, color):
        self.x = xpos
        self.y = ypos
        self.color = color
    

    def render(self, screen, w, h):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * w, self.y * h, w, h))

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getPos(self):
        return (self.x, self.y)

    def getColor(self):
        return self.color
