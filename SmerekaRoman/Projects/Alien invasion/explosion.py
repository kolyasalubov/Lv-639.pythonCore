import pygame 
from os import path
from pygame.sprite import Sprite   
from pygame.transform import scale


class Explosion(Sprite):
    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.rect = pygame.Rect(x, y, 40, 40)
            self.images = []
            self.index = 0

            for i in range(8):
                image = scale(pygame.image.load(rf"images\Explosions_kenney\regularExplosion0{i}.png"), (40, 40))
                self.images.append(image)

    def draw(self, screen):
        if self.index < 8:
                screen.blit(self.images[self.index],self.rect)
                self.index += 1












# EXPLOSION_IMGS = [pygame.image.load(path.join('images\Explosions_kenney', img)).convert_alpha()
#                   for img in range('images\Explosions_kenney')]
# # "C:\Users\super\Desktop\Alien invasion\images\Explosions_kenney\regularExplosion00.png"
# class Explosion(Sprite):
#     def __init__(self, center):
#         super(Explosion, self).__init__()
#         self.image = EXPLOSION_IMGS[0]
#         self.rect = self.image.get_rect(center=center)
#         self.frame = 0
#         self.last_update = pygame.time.get_ticks()
#         self.frame_rate = 50

#     def update(self):
#         now = pygame.time.get_ticks()
#         if now - self.last_update > self.frame_rate:
#             self.last_update = now
#             self.frame += 1
#         if self.frame == len(EXPLOSION_IMGS):
#             self.kill()
#         else:
#             self.image = EXPLOSION_IMGS[self.frame]
#             self.rect = self.image.get_rect(center=self.rect.center)
    
    
# # class Explosion(Sprite):
# #     def __init__(self, center, size):
# #         super(Explosion, self).__init__()
# #         self.size = size
# #         self.image = explosion_anim[self.size][0]
# #         self.rect = self.image.get_rect()
# #         self.rect.center = center
# #         self.frame = 0
# #         self.last_update = pygame.time.get_ticks()
# #         self.frame_rate = 50

# #     def update(self):
# #         now = pygame.time.get_ticks()
# #         if now - self.last_update > self.frame_rate:
# #             self.last_update = now
# #             self.frame += 1
# #             if self.frame == len(explosion_anim[self.size]):
# #                 self.kill()
# #             else:
# #                 center = self.rect.center
# #                 self.image = explosion_anim[self.size][self.frame]
# #                 self.rect = self.image.get_rect()
# #                 self.rect.center = center
    
    
# explosion_anim = {}
# explosion_anim['lg'] = []
# for i in range(9):
#         filename = 'regularExplosion0{}.png'.format(i)
#         img = pygame.image.load(path.join(r"C:\Users\super\Desktop\Alien invasion\images\Explosions_kenney", filename)).convert()
#         # img.set_colorkey()
#         img_lg = pygame.transform.scale(img, (75, 75))
#         explosion_anim['lg'].append(img_lg)
 