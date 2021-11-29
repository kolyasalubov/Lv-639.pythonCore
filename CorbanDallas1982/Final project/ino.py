import pygame

class Ino(pygame.sprite.Sprite):
    """klass odnogo zelenskogo"""

    def __init__(self, screen):
        """nachalnaja pozicija"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(('ze.png'))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """vivod zeli na ekran"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """peremeschenije ze armii"""
        self.y += 0.1
        self.rect.y = self.y
