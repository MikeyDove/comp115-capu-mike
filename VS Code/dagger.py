import pygame

class Dagger(pygame.sprite.Sprite):
    def __init__(self, x, y, dir_x, dir_y, dagger_sheet):
        super().__init__()
        

        if dir_y != 0:
            mini_dagger = dagger_sheet.subsurface(pygame.Rect(0, 0, 64, 64))
            self.image = pygame.transform.scale(mini_dagger, (100, 140))
            
            if dir_y < 0:
                self.image = pygame.transform.flip(self.image, False, True)
        else:
            mini_dagger = dagger_sheet.subsurface(pygame.Rect(0, 192, 64, 64))
            self.image = pygame.transform.scale(mini_dagger, (140, 100)) # Wide for horizontal
            
            if dir_x > 0: 
                self.image = pygame.transform.flip(self.image, True, False) 

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3
        self.dir_x = dir_x
        self.dir_y = dir_y

    def update(self):
        self.rect.x += self.speed * self.dir_x
        self.rect.y += self.speed * self.dir_y

        if self.rect.right < 0 or self.rect.left > 1000 or self.rect.bottom < 0 or self.rect.top > 800: 
            self.kill()