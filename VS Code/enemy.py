import pygame
from pygame.sprite import Sprite
import random 
import math
class Enemy(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.player = ai_game.player
        self.sheet = pygame.image.load('goblineverything.bmp').convert_alpha()
        self.pics = {
            'down':  self.sheet.subsurface((0, 0, 64, 64)),
            'up':    self.sheet.subsurface((0, 64, 64, 64)),
            'left':  self.sheet.subsurface((64, 0, 64, 64)),
            'right': self.sheet.subsurface((64, 64, 64, 64)),
        }
        for gobface in self.pics:
            self.pics[gobface] = pygame.transform.scale(self.pics[gobface], (100, 100))
        self.image = self.pics['down']
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.screen_width - 150
        self.rect.y = 100
        self.speed = 1
        self.detection_range = 150 
        self.direction_x = 0
        self.direction_y = 0
        self.wander_timer = 0
        self.shoot_cooldown = 0
        
    def throw_dagger(self, dagger_group, dagger_sheet):
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance < 300 and self.shoot_cooldown <= 0:
            from dagger import Dagger

            tx = self.direction_x
            ty = self.direction_y

            if tx == 0 and ty == 0:
                tx = -1

            new_dagger = Dagger(self.rect.centerx, self.rect.centery, tx, ty, dagger_sheet)
            

            dagger_group.add(new_dagger)
            self.shoot_cooldown = 120 

    def update(self):
        if self.wander_timer <= 0:
            self.direction_x = random.choice([-1, 0, 0, 1])
            self.direction_y = random.choice([-1, 0 , 0,  1])
            self.wander_timer = random.randint(120, 240)

        self.wander_timer -= 1
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    

        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance < self.detection_range:
            if dx > 0:
                self.direction_x = 1
            elif dx < 0:
                self.direction_x = -1
            else:
                self.direction_x = 0

            if dy > 0:
                self.direction_y = 1
            elif dy < 0:
                self.direction_y = -1
            else:
                self.direction_y = 0
        else:
            if self.wander_timer <= 0:
                self.direction_x = random.choice([-1, 0, 0, 0, 1])
                self.direction_y = random.choice([-1, 0, 0, 0, 1])
                self.wander_timer = random.randint(120, 240)



        self.rect.x += self.direction_x * self.speed
        self.rect.y += self.direction_y * self.speed

        if self.direction_y < 0:
            self.image = self.pics['up']
        elif self.direction_y > 0:
            self.image = self.pics['down']
        elif self.direction_x < 0:
            self.image = self.pics['left']
        elif self.direction_x > 0:
            self.image = self.pics['right']


        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction_x *= -1 
        elif self.rect.right >= self.settings.screen_width:
            self.rect.right = self.settings.screen_width
            self.direction_x *= -1
        

        
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction_y *= -1 
        elif self.rect.bottom >= self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height
            self.direction_y *= -1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
 