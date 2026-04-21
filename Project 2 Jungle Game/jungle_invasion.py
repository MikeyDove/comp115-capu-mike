import sys
import pygame
from settings import Settings
from player import Player
from enemy import Enemy
from dagger import Dagger
from bush import Bush

    
class JungleInvasion: 
    def __init__ (self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.dagger_sheet = pygame.image.load('dagger2.bmp').convert_alpha()
        self.player = Player(self) 
        self.enemies= pygame.sprite.Group()
        self.enemy_daggers = pygame.sprite.Group()
        self._create_enemies()
        self.obstacles = pygame.sprite.Group()
        bush = Bush(400, 300, 80, 80)
        self.obstacles.add(bush)
    def _create_enemies(self):
        for _ in range (20):
            new_enemy = Enemy(self)
            self.enemies.add(new_enemy)
    def _check_enemy_collisions(self):
        if self.player.attacking:
            collisions = pygame.sprite.spritecollide(self.player, self.enemies, True)
            
            if collisions:
                print("You've gotten one!")
        if pygame.sprite.spritecollideany(self.player, self.enemy_daggers):
            print("Yikes!")


    def run_game(self):
       while True:
            self._check_events()
            self.player.update()
            self.enemies.update()

            for enemy in self.enemies:
                enemy.throw_dagger(self.enemy_daggers, self.dagger_sheet)

            self._check_enemy_collisions()
            self.enemy_daggers.update()
            self._update_screen()
            self.clock.tick(60)

      
           
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.moving_right = True
                    elif event.key == pygame.K_UP:
                        self.player.moving_up = True
                    elif event.key == pygame.K_LEFT:
                        self.player.moving_left = True
                    elif event.key == pygame.K_DOWN:
                        self.player.moving_down = True
                    elif event.key == pygame.K_SPACE:
                        if not self.player.attacking:
                                self.player.attacking = True
                                self.player.attack_timer = 20
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player.moving_right = False
                    elif event.key == pygame.K_UP:
                        self.player.moving_up = False
                    elif event.key == pygame.K_LEFT:
                        self.player.moving_left = False
                    elif event.key == pygame.K_DOWN:
                        self.player.moving_down = False
                


    def _update_screen(self):
        self.screen.blit(self.settings.bg_image, (0 , 0))
        self.player.blitme()
        for enemy in self.enemies.sprites():
            enemy.blitme()
        self.enemy_daggers.draw(self.screen)
        self.obstacles.draw(self.screen)
        pygame.display.flip()            

if __name__ == '__main__':
    ji = JungleInvasion()
    ji.run_game()