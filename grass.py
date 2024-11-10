import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/grassHalf.png')
        self.rect = self.image.get_rect()