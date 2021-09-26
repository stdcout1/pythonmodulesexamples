import pygame, sys
pygame.init()
screen = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(60)