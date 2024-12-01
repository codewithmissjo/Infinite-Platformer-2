import sys
import pygame
from pygame.locals import *
from player import Player
from grass import Platform
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))

screen_info = pygame.display.Info()
size = (width, height) =  (screen_info.current_w,
screen_info.current_h)

bg = (255, 224, 179)
pl = pygame.sprite.GroupSingle()
gr = pygame.sprite.Group()

def setup():
    pl.add(Player())

    for i in range(height // 100):
        for j in range(width // 200):
            gr.add(Platform( random.randint(5, (width - 50) // 10) * 10, 120 * i))

def main():
    setup()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        
        # Events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pl.sprite.move_right()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pl.sprite.move_left()


        # Update Sprites
        pl.update(gr)

        # Draw Sprites
        screen.fill(bg)
        pl.draw(screen)
        gr.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()