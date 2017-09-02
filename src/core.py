import pygame










def init():
    pygame.init()
    screen = pygame.display.set_mode((400,300))

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        update()
        render()
        pygame.display.flip()






def update():
    print("damn")



def render():
    print("god")



init()
