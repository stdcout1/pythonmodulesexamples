import pygame, sys
x= 0
y = 0
hd = 1
vd = 1
v = 10
pygame.init()
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((60,60,80))
    player = pygame.draw.rect(screen,(255,100,130),(x,y,30,30))
    # if x<=0: hd = 1
    # if x>=700: hd = -1
    # x+=hd*3
    # if y<=0: vd = 1
    # if y>=700: vd = -1
    # y+=vd*20
    # move
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
        v = 2
    else:
        v = 10


    pygame.display.update()
    clock.tick(60)