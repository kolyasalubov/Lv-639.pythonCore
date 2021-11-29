import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """pulja v pozicii puski"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 150, 12)
        self.color = 139, 195, 74
        self.speed = 4.5
        """skorost puli 4.5"""
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """peremeschenije puli"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """otrisovka puli na ekrane"""
        pygame.draw.rect(self.screen, self.color, self.rect)