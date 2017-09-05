import pygame
from Grid import Grid
from Wall import Wall
from GridObject import GridObject







def init():
    pygame.init()
    screen = pygame.display.set_mode((400,300))

    done = False
    grid = Grid(2000, 1000)
    x = Wall(5,5)
    grid.add(x)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        update()
        render()
        grid.render(screen)
        pygame.display.flip()






def update():
    pass


def render():
    pass


init()
