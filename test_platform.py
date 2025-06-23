import pygame

import random
from scenes import Scenes
from boss import Boss
from player import Player
from level_logic import Level_logic
from night_cycle import Night_cycle
from shadow_gfx import Shadow_gfx
from in_game_map import In_game_map
from sprite_sheet_animater import Sprite_loader

from boss import Wolf_boss
from wolf import Golem

#from wolf import Wolf

class test_platform():
    """this will be used for testing new code without having
    to use the full game code. """

    def test_code(self):
        """initializes"""
        pygame.init()
        
        # sets up the screen.
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        
        self.game = True
        
        self.sprite_sheet_player_1 = Sprite_loader('_internal\\img\\player_image.png',3)
        
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.dt = self.clock.tick(60) / 1000

        
        self.golem = Golem(self,(300,300),200)

        # test code can go here and then be deleted when done
        # test code above. and below as needed to blit to screen. 
        while self.game:
            #mouse_pos = pygame.mouse.get_pos()
            self.clock.tick(60)

            self.screen.fill((150,150,100))
            self.golem.draw_me(self)
            
            """n = 28
            o = n
            m = len(self.golem.sprite_enemy.surface_list) - 1
            #print(m)
            #print(m, n)
            #print(len(self.wolf_boss.wolf_list))
            #print(m, ' is m')
            while n <= m:
                #self.wolf_test.sprite_enemy.surface_list[n]
                self.screen.blit(self.golem.sprite_enemy.surface_list[n],((n-o)* 100,(n-o)*65))
                n += 1"""
            pygame.display.flip()


if __name__ == '__main__':
    testing = test_platform()
    testing.test_code()