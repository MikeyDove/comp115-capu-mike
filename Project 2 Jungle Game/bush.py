import pygame 
from pygame.sprite import Sprite

class Bush(Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((34, 139, 34)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y