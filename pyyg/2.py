import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
img = pygame.image.load('imj.png')
imgr = img.get_rect ()
imgr.center = 250,250
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(img,imgr)

    pygame.display.update()
    clock.tick(60)