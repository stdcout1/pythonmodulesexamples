import pygame, sys, random
x= 0
y = 0
hd = 1
vd = 1
v = 10
point = 1
one,two,three = 60,60,80
pygame.init()
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
img = pygame.image.load('imj.png')
imgp = pygame.image.load('imgp2.jpg')
img3 = pygame.image.load('img3.png')
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((one, two, three))
    a = screen.blit(img,(x,y))
    b = screen.blit(imgp, (250, 50))
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
        one,two,three = random.randint(0,100),random.randint(0,100),random.randint(0,100)
    if key[pygame.K_LCTRL]:
        pygame.quit()
    else:
        v = 10
    if a.colliderect(b):
        print('crash')


    pygame.display.update()
    clock.tick(60)