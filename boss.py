import pygame
from pygame.sprite import Sprite
import random
from enemy_logic import Overworld_person

class Boss(Overworld_person):

    def __init__(self,rpg):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__(rpg)

        self.highest = 'right'
        n = 0
        m = 9
        del self.image
        self.image_list_right = []
        self.image_list_left = []

        while n < 9:
            load_string = '_internal\img\\spiderboss_right_'
            added = str(n)
            added2 = '.bmp'
            load_string += added
            load_string += added2
            image_hold = pygame.image.load(load_string)
            image_hold = pygame.transform.scale_by(image_hold,8)
            self.image_list_right.append(image_hold)
            n += 1

        
      
        
        self.animation_counter = 0
        self.animation_delay = 20

        self.animation_delay_start = self.animation_delay



        x = -1000
        y = 2500
        self.rect.center = (x,y)

        self.surface = pygame.Surface((300,300))
        self.surface.fill((0,0,0))
        #self.surface.set_colorkey((0,0,0))
        
        self.surface_rect = self.surface.blit(self.image_list_right[0],(-50,0))

        self.V_x = 0
        self.V_y = 0

        self.dydt = 10
        self.dxdt = 10
        self.dVdt = random.randint(30,100)
        timer = random.randint(50,110)
        self.accelleration_timer = timer


        self.x = self.rect.x
        self.y = self.rect.y

        self.health = 3000

        self.helper_list = []

    def boss_attack_primary(self,rpg):
        """This is the bosses primary attack"""
    
    def boss_attack_secondary(Self,rpg):
        """This is the bosses secondary attack"""
    def boss_spawn_ally(Self,rpg):
        """This spawns an ally with a velocity in a random direction"""
