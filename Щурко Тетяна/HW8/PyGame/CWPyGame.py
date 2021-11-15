import CWPyGamesetting as s
import pygame
pygame.init()
COORD_X = 50
COORD_Y = 50
sprite=pygame.image.load('img.png')
gameDisplay = pygame.display.set_mode((s.WIDTH_DISPLAY, s.HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("My first game")
run = True
clock = pygame.time.Clock()
while run:
    pygame.time.delay(100)
    gameDisplay.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        COORD_X = COORD_X - s.DELTA_STEP
    if keys[pygame.K_RIGHT]:
        COORD_X = COORD_X + s.DELTA_STEP
    if keys[pygame.K_UP]:
        COORD_Y = COORD_Y - s.DELTA_STEP
    if keys[pygame.K_DOWN]:
        COORD_Y = COORD_Y + s.DELTA_STEP
    gameDisplay.blit(sprite, [COORD_X,COORD_Y])
    pygame.display.update()
    clock.tick(s.FPS)