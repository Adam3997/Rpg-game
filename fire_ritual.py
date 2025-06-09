import math
import pygame
from sprite_sheet_animater import Sprite_loader

class Fire_ritual():
    """This is the class for the fire ritual to fight bosses"""

    def __init__(self,rpg):
        """"""

    def fire_circle_start_up(self,x,y):
        
        self.fire_circle = Sprite_loader('_internal\\explosion\expl_01_000',-2)
        self.fire_circle_animation_counter_list = []
        self.fire_circle_animation_limit_list = []
        self.rect_circle_spell_list = []
        self.fire_circle_active_list = []
        self.last_fire_circle = -1
        self.counting_up = True
        self.animation_circle_delay_list = []
        self.animation_circle_delay_old_list = []
        self.animation_circle_delay = 4
        self.animation_circle_delay_old = self.animation_circle_delay

        #self.armor = 80 # armor for boss is here. self.armor
        # i can refactor armor later.
        
        n = 0
        m = 7

        self.armor = (m + 1) * 10

        while n <= m:
            number = math.pi / ((m + 1)/  2)
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(23) #always -1 the number of frames
            self.fire_circle_active_list.append(False)
            n += 1


    def fire_box_start_up(self,rpg,x,y):
        self.fire_circle = Sprite_loader('_internal\\explosion\expl_06_000',-4) # 6 has 32 frames and needs -4 key
        self.fire_circle_animation_counter_list = []
        self.fire_circle_animation_limit_list = []
        self.rect_circle_spell_list = []
        self.fire_circle_active_list = []
        self.last_fire_circle = -1
        self.counting_up = True
        self.animation_circle_delay_list = []
        self.animation_circle_delay_old_list = []
        self.animation_circle_delay = 4
        self.animation_circle_delay_old = self.animation_circle_delay

        #self.armor = 80
        
        n = 0
        m = 23
        #rpg.level_stuff.level_1_boss.armor = (m + 1) * 10
        # 7 then 15 then 23 and 31

        while n <= m:

            
            #number = (2 * math.pi) / (n + 1)
            number = n * (2 * math.pi/(m + 1))
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            x_adjust = 500 * (abs(math.cos(number)) * math.cos(number) + abs(math.sin(number)) * math.sin(number))
            #x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = 500 * (abs(math.cos(number)) * math.cos(number) - abs(math.sin(number)) * math.sin(number))
            #y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(31) #always -1 the number of frames # this sets the animation limit for fire
            self.fire_circle_active_list.append(False)
            n += 1


    def fire_shape_start_up(self,rpg,x,y):
        self.fire_circle = Sprite_loader('_internal\\explosion\expl_06_000',-4) # 6 has 32 frames and needs -4 key
        self.fire_circle_animation_counter_list = []
        self.fire_circle_animation_limit_list = []
        self.rect_circle_spell_list = []
        self.fire_circle_active_list = []
        self.last_fire_circle = -1
        self.counting_up = True
        self.animation_circle_delay_list = []
        self.animation_circle_delay_old_list = []
        self.animation_circle_delay = 4
        self.animation_circle_delay_old = self.animation_circle_delay

        #self.armor = 80
        
        n = -11
        m = 11
        #rpg.level_stuff.level_1_boss.armor = (m + 1) * 10
        # 7 then 15 then 23 and 31

        while n <= m:

            
            #number = (2 * math.pi) / (n + 1)
            number = n * (2 * math.pi/(2*m + 1))
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            # equations below
            x_adjust = 500 * math.sin(number)  # equations go here
            #x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = 500 * math.cos(number**2)
            #y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(31) #always -1 the number of frames # this sets the animation limit for fire
            self.fire_circle_active_list.append(False)
            n += 1


    def spawn_both(self,rpg,x,y):
        """This does both in the same one."""

        self.fire_circle = Sprite_loader('_internal\\explosion\expl_01_000',-2)
        self.fire_circle_animation_counter_list = []
        self.fire_circle_animation_limit_list = []
        self.rect_circle_spell_list = []
        self.fire_circle_active_list = []
        self.last_fire_circle = -1
        self.counting_up = True
        self.animation_circle_delay_list = []
        self.animation_circle_delay_old_list = []
        self.animation_circle_delay = 4
        self.animation_circle_delay_old = self.animation_circle_delay

        #self.armor = 80 # armor for boss is here. self.armor
        # i can refactor armor later.
        
        n = 0
        m = 7

        self.armor = (m + 1) * 10

        while n <= m:
            number = math.pi / ((m + 1)/  2)
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(23) #always -1 the number of frames
            self.fire_circle_active_list.append(False)
            n += 1
        self.fire_circle = Sprite_loader('_internal\\explosion\expl_06_000',-4)
        n = 0
        m = 23
        #rpg.level_stuff.level_1_boss.armor = (m + 1) * 10
        # 7 then 15 then 23 and 31

        while n <= m:

            
            #number = (2 * math.pi) / (n + 1)
            number = n * (2 * math.pi/(m + 1))
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            x_adjust = 500 * (abs(math.cos(number)) * math.cos(number) + abs(math.sin(number)) * math.sin(number))
            #x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = 500 * (abs(math.cos(number)) * math.cos(number) - abs(math.sin(number)) * math.sin(number))
            #y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(31) #always -1 the number of frames # this sets the animation limit for fire
            self.fire_circle_active_list.append(False)
            n += 1
        n = -11
        m = 11
        #rpg.level_stuff.level_1_boss.armor = (m + 1) * 10
        # 7 then 15 then 23 and 31

        while n <= m:

            
            #number = (2 * math.pi) / (n + 1)
            number = 2 *n * ( math.pi/(2*m + 1))
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            # equations below
            x_adjust = 500 * math.sin(number)  # equations go here
            #x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = 500 * math.cos(number**2)
            #y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(31) #always -1 the number of frames # this sets the animation limit for fire
            self.fire_circle_active_list.append(False)
            n += 1



    def spawn_rocket(self,rpg,x,y):
        """This does both in the same one."""

        #self.fire_circle = Sprite_loader('_internal\\explosion\expl_01_000',-2)
        self.fire_circle = Sprite_loader('_internal\\explosion\expl_06_000',-4)
        self.fire_circle_animation_counter_list = []
        self.fire_circle_animation_limit_list = []
        self.rect_circle_spell_list = []
        self.fire_circle_active_list = []
        self.last_fire_circle = -1
        self.counting_up = True
        self.animation_circle_delay_list = []
        self.animation_circle_delay_old_list = []
        self.animation_circle_delay = 4
        self.animation_circle_delay_old = self.animation_circle_delay

        #self.armor = 80 # armor for boss is here. self.armor
        # i can refactor armor later.

        total_scale = 200
        self.start = -40
        self.finish = 40
        n = self.start
        m = self.finish

        self.armor = 3*2*(m + 1) * 10 - 20

        while n <= m:
            number = n * ( math.pi/(m + 1))
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            x_adjust = total_scale * (5*math.sin(number) + math.sin(7*number))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = total_scale * (5*math.cos(number) + math.cos(7*number))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(23) #always -1 the number of frames
            self.fire_circle_active_list.append(False)
            n += 1
        
        n = self.start
        m = self.finish
        #rpg.level_stuff.level_1_boss.armor = (m + 1) * 10
        # 7 then 15 then 23 and 31

        while n <= m:

            
            #number = (2 * math.pi) / (n + 1)
            number = n * ( math.pi/(m + 1))
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            x_adjust = total_scale * (5*math.sin(number))
            #x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = total_scale * (5*math.cos(2*number) + math.cos(7*number))
            #y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(31) #always -1 the number of frames # this sets the animation limit for fire
            self.fire_circle_active_list.append(False)
            n += 1
        n = self.start
        m = self.finish
        #rpg.level_stuff.level_1_boss.armor = (m + 1) * 10
        # 7 then 15 then 23 and 31

        while n <= m:

            
            #number = (2 * math.pi) / (n + 1)
            number = n * ( math.pi/(2*m + 1))
            o = pygame.Rect(0,0,100,100)
            o.center = (x,y)
            # equations below
            x_adjust = total_scale * (2.3*math.cos(10*number)+ math.cos(23*number))  # equations go here
            #x_adjust = 500 * (math.cos((-1 * math.pi) + (number * n)))
            o.centerx += x_adjust
            o.centerx += 180
            y_adjust = total_scale * (2.3*math.sin(10*number))
            #y_adjust = 500 * (math.sin((-1 * math.pi) + (number * n)))
            o.centery += y_adjust
            o.centery += 175
            self.rect_circle_spell_list.append(o)
            self.animation_circle_delay_list.append(4)
            self.animation_circle_delay_old_list.append(4)

            
            self.fire_circle_animation_counter_list.append(0)
            self.fire_circle_animation_limit_list.append(31) #always -1 the number of frames # this sets the animation limit for fire
            self.fire_circle_active_list.append(False)
            n += 1

