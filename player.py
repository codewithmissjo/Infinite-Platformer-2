import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/p1_jump.png')
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(0, 0)
        self.facing = "R"
        self.rect.center = [200, 200]
        self.jump_speed = -14
    
    def update(self, platforms):
        self.rect.move_ip(self.speed)
        self.speed[0] = 0

        # infinite x axis
        if self.rect.right < 0:
            self.rect.left = 400
        elif self.rect.left > 400:
            self.rect.right = 0
        
        # y speed stuff
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for p in hit_list:
            # look for player landing on top of platform
            if self.speed[1] > 0 and abs(self.rect.bottom - p.rect.top) <= self.speed[1]:
                self.rect.bottom = p.rect.top
                self.speed[1] = self.jump_speed
        
        # scrolling platforms
        if self.rect.top < 100:
            self.rect.top = 100
            for pl in platforms.sprites():
                pl.scroll(-1 * self.speed[1])

        # gravity
        self.speed[1] += 0.5
        

    def move_right(self):
        self.speed[0] = 2
        if self.facing != "R":
            self.facing = "R"
            self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.left > 400:
            self.rect.right = 0
    
    def move_left(self):
        self.speed[0] = -2
        if self.facing != "L":
            self.facing = "L"
            self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.right < 0:
            self.rect.left = 400



# setting up player speed with a vector!
# -- define speed: self.speed = pygame.math.Vector2(1, 0)
# -- apply speed: self.rect.move_ip(self.speed)
# -- call in main game loop

# infinite x axis movement

# player key based movement
# player facing