import pygame

class Player:
  def __init__(self, ai_game):
       self.facing = 'front'
       self.screen = ai_game.screen
       self.screen_rect = ai_game.screen.get_rect()
       self.attacking = False
       self.attack_timer = 0
       self.moving_right = self.moving_left = self.moving_up = self.moving_down = False
  
       self.image_original = pygame.transform.scale(pygame.image.load('frogmanf.bmp').convert_alpha(), (100, 100))
       self.image_left = pygame.image.load('frogmanl.bmp').convert_alpha()
       self.image_left = pygame.transform.scale(self.image_left, (100, 100))
       self.image_right = pygame.image.load('frogmanright.bmp').convert_alpha()
       self.image_right = pygame.transform.scale(self.image_right, (100, 100))
       self.image_back = pygame.image.load('frogmanb.bmp').convert_alpha()
       self.image_back = pygame.transform.scale(self.image_back, (100, 100))
       self.image = self.image_original
       self.rect = self.image.get_rect()
       self.rect.center = self.screen_rect.center

       self.image_ba1 = pygame.transform.scale(pygame.image.load('frogmanattack1.bmp'), (100,150))
       self.image_ba2 = pygame.transform.scale(pygame.image.load('frogmanattack2.bmp'), (100,130))
       self.image_fa1 = pygame.transform.scale(pygame.image.load('frogmanfa1.bmp'), (100,150))
       self.image_fa2 = pygame.transform.scale(pygame.image.load('frogmanfa2.bmp'), (100,150))
       self.image_la1 = pygame.transform.scale(pygame.image.load('frogmanla1.bmp'), (125,100))
       self.image_la2 = pygame.transform.scale(pygame.image.load('frogmanla2.bmp'), (100,100))
       self.image_ra1 = pygame.transform.scale(pygame.image.load('frogmanra1.bmp'), (140,100))
       self.image_ra2 = pygame.transform.scale(pygame.image.load('frogmanra2.bmp'), (100,100))




      
  def update(self):
    if self.attacking: #initial attack
          old_center = self.rect.center
          old_feet = self.rect.midbottom
          if self.facing == 'back':
            self.image = self.image_ba1 if self.attack_timer > 10 else self.image_ba2
          elif self.facing =='front':
            self.image = self.image_fa1 if self.attack_timer > 10 else self.image_fa2
          elif self.facing == 'left':

                self.image = self.image_la1 if self.attack_timer > 10 else self.image_la2
          elif self.facing =='right':
                self.image = self.image_ra1 if self.attack_timer > 10 else self.image_ra2

          self.attack_timer -= 1 #after frog attacks, go back to direction you were facing
          if self.attack_timer <= 0:
              self.attacking = False
              chillin_frog = {'back' : self.image_back , 'front' : self.image_original , 'left' : self.image_left , 'right' : self.image_right }
              self.image = chillin_frog[self.facing]
      
          self.rect = self.image.get_rect()
          self.rect.center = old_center
    else: #Barrier stuff
      if self.moving_right and self.rect.right < self.screen_rect.right:
        self.rect.x += 3
        self.image , self.facing = self.image_right, 'right'
      if self.moving_left and self.rect.left > 0:
        self.rect.x -= 3
        self.image , self.facing = self.image_left , 'left'
      if self.moving_up and self.rect.top > 0:
        self.rect.y -= 3
        self.image , self.facing = self.image_back , 'back'
      if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        self.rect.y += 3
        self.image , self.facing = self.image_original , 'front'

  def blitme(self):
    self.screen.blit(self.image, self.rect)