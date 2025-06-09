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

#from wolf import Wolf

class test_platform():
    """this will be used for testing new code without having
    to use the full game code. """

    def test_code(self):
        """initializes"""
        pygame.init()
        #print(pygame.font.get_fonts())
        # sets up the screen.
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        # clock for framerate.
        
        #font in case its needed
        """self.font = pygame.font.SysFont(None,48)
        self.text_color = (30,30,30)
        self.bg_color = (255,255,255)
        """
        #self.map_1 = In_game_map(self,100,100,(21,20,50))
        self.game = True
        #self.cut_scene_1 = Scenes(self)
        #self.cut_scene_1.cut_scene_test.cut_scene_part_1 = True

        # level logic and player_1 needed for boss to work since they refrence each other.
        #self.level_stuff = Level_logic(self)

        #self.player_1 = Player(self)

        #self.level_1_boss = Boss(self,100,200,100,200,False,'one')
        # both of these are needed 
        self.sprite_sheet_player_1 = Sprite_loader('_internal\\img\\player_image.png',3)
        
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.dt = self.clock.tick(60) / 1000

        #self.night = Night_cycle(self)

        #self.hue = Shadow_gfx(self,'test')

        #self.wolf_test = Wolf(self)

        #from shadow_gfx import Shadow_gfx
        #self.shadow_test = Shadow_gfx(self)
        #self.shadow_test.draw_shadowy_overlay()
        self.wolf_boss = Wolf_boss(self,(800,500),10)


        # test code can go here and then be deleted when done
        # test code above. and below as needed to blit to screen. 
        while self.game:
            #mouse_pos = pygame.mouse.get_pos()
            self.clock.tick(60)

            self.screen.fill((150,150,100))
            #self.level_1_boss.draw_me(self)
            #self.level_stuff.player_1.draw_me(self)
            #self.hue.draw_shadowy_overlay_2()
            #self.map_1.update_map(self)
            #self.map_1.draw_map(self)
            #self.wolf_test.draw_for_credits((200,500))
            #self.screen.blit(self.wolf_test.sprite_enemy.surface_list[30],(50,335)) # walk right or stand
            #self.screen.blit(self.wolf_test.sprite_enemy.surface_list[35],(250,335)) # run right
            #self.screen.blit(self.wolf_test.sprite_enemy.surface_list[40],(550,335)) # walk left
            #self.screen.blit(self.wolf_test.sprite_enemy.surface_list[50],(750,335)) # run left
            #self.screen.blit(self.wolf_test.sprite_enemy.surface_list[30],(950,835))
            #self.screen.blit(self.wolf_test.sprite_enemy.surface_list[25],(1150,835))
            #print(pygame.font.SysFont)
            """n = 0
            m = len(self.wolf_boss.wolf_list) - 1
            while n <= m:
                self.wolf_boss.wolf_list[n].draw_me(self)
                n += 1"""
            
            n = 55
            o = n
            m = len(self.wolf_boss.wolf_list[0].sprite_enemy.surface_list) - 1
            #print(m, n)
            #print(len(self.wolf_boss.wolf_list))
            #print(m, ' is m')
            while n <= m:
                #self.wolf_test.sprite_enemy.surface_list[n]
                self.screen.blit(self.wolf_boss.wolf_list[0].sprite_enemy.surface_list[n],((n-o)* 100,(n-o)*65))
                n += 1
            pygame.display.flip()

if __name__ == '__main__':
    testing = test_platform()
    testing.test_code()