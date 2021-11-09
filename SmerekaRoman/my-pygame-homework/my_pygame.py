import pygame
from pygame import display
from pygame.constants import RESIZABLE

# added background music, changed screen color, added ambluance icon

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGTH_GREEN = (98, 206, 63)

pygame.init()
 
screen = pygame.display.set_mode([800, 600], pygame.RESIZABLE)
 
pygame.display.set_caption('Fly Ambluance')
 
clock = pygame.time.Clock()

pygame.display.update()
 
background_position = [0, 0]
 
player_image = pygame.image.load(r"C:\Users\super\Desktop\python_work\Lv-639.pythonCore\SmerekaRoman\my-pygame-homework\image_1.png").convert()

player_image.set_colorkey(BLACK)

pygame.mixer.music.load('lp-numb.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    screen.fill(LIGTH_GREEN)          
 
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    screen.blit(player_image, [x, y])
 
    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()