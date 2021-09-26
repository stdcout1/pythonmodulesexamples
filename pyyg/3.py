import pygame, sys
x= 0
y = 0
hd = 1
vd = 1
v = 10
pygame.init()
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
img = pygame.image.load('imj.png')
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((60,60,80))

    if x>=700-img.get_width(): x = 1
    x+=hd*3


    pygame.display.update()
    clock.tick(60)