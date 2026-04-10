import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_image = pygame.image.load('swamp_background.bmp')
        self.bg_image = pygame.transform.scale(self.bg_image, 
                        (self.screen_width, self.screen_height))
        
 