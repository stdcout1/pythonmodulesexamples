import pygame, sys, random
x= 0
y = 0
hd = 1
vd = 1
v = 10
one,two,three = 60,60,80
pygame.init()
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
img = pygame.image.load('imj.png')

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((one, two, three))
    screen.blit(img,(x,y))
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[ord('a')]:
        x += -v
    if key[pygame.K_RIGHT] or key[ord('d')]:
        x += v
    if key[pygame.K_UP] or key[ord('w')]:
        y += -v
    if key[pygame.K_DOWN] or key[ord('s')]:
        y += v
    if key[pygame.K_LSHIFT]:
        pass
    else:
        v = 10


    pygame.display.update()
    clock.tick(60)