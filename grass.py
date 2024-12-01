import pygame
import random

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/grassHalf.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def scroll(self, change):
        self.rect.top += change
        screen_info = pygame.display.Info()
        if self.rect.top > screen_info.current_h:
            self.rect.top = -50
            self.rect.centerx = random.randint(5, (screen_info.current_w - 50) // 10) * 10