import pygame
from Grid import Grid









def init():
    pygame.init()
    screen = pygame.display.set_mode((400,300))

    done = False
    grid = Grid(100, 100)
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
