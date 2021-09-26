import pygame
import random,sys
p =[]
pressed = False
class Maze():
    def __init__(self):
        self.M = 15
        self.N = 15
        self.maze = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        ]

    def draw(self):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                p.append(pygame.draw.rect(screen,(255,0,0),(bx * 44, by * 44,44,44)))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1



pygame.init()
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
r,a,n,d,o,m = (random.randint(0, 700)),(random.randint(0, 700)),(random.randint(0, 700)),(random.randint(0, 700)),(random.randint(0, 700)),(random.randint(0, 700))
x = 50
y = 313
v = 10
while 1:
    p =[]
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    for i in range(3):
        p.append(pygame.draw.rect(screen, (255, 100, 130), (r,a, 44, 44)))
        p.append(pygame.draw.rect(screen, (100, 50, 80), (n, d, 44, 44)))
        p.append(pygame.draw.rect(screen, (200, 30, 200), (o, m, 44, 44)))

    r += 10
    n += 10
    m += 10
    if r >= 700: r=0
    if n >= 700: n = 0
    if m >= 700: m = 0



    player = pygame.draw.rect(screen,(0,225,0),(x,y,30,30))
    finish = pygame.draw.rect(screen, (0,0,225), (300,313,35,35))
    button = pygame.draw.rect(screen, (225, 0, 225), (200, 513, 35, 35))

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[ord('a')]:
        x += -v
    if key[pygame.K_RIGHT] or key[ord('d')]:
        x += v
    if key[pygame.K_UP] or key[ord('w')]:
        y += -v
    if key[pygame.K_DOWN] or key[ord('s')]:
        y += v
    if key[pygame.K_LCTRL]:
        v = 1
    if key[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        v = 10

    if not pressed:
        finish = pygame.draw.rect(screen, (0,0,225), (230,313,40,40))


    Maze().draw()


    for i in p:
        if player.colliderect(i):
            x = 55
            y = 313
    if player.colliderect(button):
        pressed = True


    pygame.display.update()
    clock.tick(60)
