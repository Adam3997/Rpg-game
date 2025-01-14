#import pygame
#from pygame.sprite import _Group, Sprite

import pygame
from pygame.sprite import Sprite
from sprite_sheet_animater import Sprite_loader
from physics_stats import Physics_stats
import math

class Player(Sprite,Physics_stats):
    """This is the player in the game. You have a sprite and a location on screen. No animations yet. """
    def __init__(self,rpg):
        """"""
        Physics_stats.__init__(self)
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()
        
        self.movement_delay = 200
        self.mass = 2 # this represents 84 kilograms
        self.min_acc = 30
        self.max_acc = 150

        # 10 low 90 high is slow
        # 30 and 90 might be faster
        # 30 and 150 is fast

        self.impact_delay = 40
        self.impact_delay_old = self.impact_delay

        ## # this stuff will be used for attack logic
        self.attack_direct_1_counter = 6
        self.attack_direct_1_counter_old = self.attack_direct_1_counter


        self.attack_active = False

        self.attack_length = 5


        


        #
        
        #self.something = pygame.draw.circle(self.screen,((10),(100),(200)),radius=5)

        self.highest = 'right'
        self.animation_last = 'right'
        n = 0
        m = 8
        self.image_list_right = []
        self.image_list_left = []
        while n < 9:
            load_string = '_internal\img\player_right_'
            added = str(n)
            added2 = '.bmp'
            load_string += added
            load_string += added2
            image_hold = pygame.image.load(load_string)
            image_hold = pygame.transform.scale2x(image_hold)
            self.image_list_right.append(image_hold)
            n += 1
        n = 0
        while n < 9:
            load_string = '_internal\img\player_left_'
            added = str(n)
            added2 = '.bmp'
            load_string += added
            load_string += added2
            image_hold = pygame.image.load(load_string)
            image_hold = pygame.transform.scale2x(image_hold)
            self.image_list_left.append(image_hold)
            n += 1
        #self.image = pygame.image.load("_internal\img\ch_1.bmp")
        #self.image_resized = pygame.transform.scale(self.image,(150,250))
        self.image_resized = pygame.transform.scale2x(self.image_list_right[0])
        #self.rect = self.image_resized.get_rect()
        #self.holder = pygame.Rect(top=0,left=0,height=50,width=50)
        size = 500, 200
        red = (255, 0, 0)
        gray = (150, 150, 150)
        self.rect = pygame.Rect(0,0,120,120)

        #self.rect = self.holder.get_rect()
        self.rect_2 = self.rect
        self.rect.centerx = 0
        self.rect.centery = 0

        #print(self.rect.height,self.rect.width, ' is height and width')
        #print(self.rect.centerx,self.rect.centery, ' is x and y ')

        self.rect.center = self.screen_rect.center

        self.x = self.rect.x
        self.y = self.rect.y
        self.last_attack = False

        self.animation_counter = 0
        self.animation_delay = 2

        self.animation_delay_start = self.animation_delay

        self.animation_length_walk = 7

        self.sprite_sheet_player_1 = Sprite_loader('images1\sheet_1_player.png',3)
        

    def animation(self):
        """This performs the animation of the player."""

    def movement_test(self,rpg):
        """This is a test"""
        self.movement_delay -= 1
        if self.movement_delay <= 0:
            self.change_accelleration()
            #print('acc changed')
            self.movement_delay = 200
        self.update_speed(rpg)
        self.rect.x += self.velocity[0] * rpg.dt
        self.rect.y += self.velocity[1] * rpg.dt
    
    def check_particle_hit(self,rpg):
        """"""
        rect_particle = pygame.Rect(0,0,70,70)
        rect_particle.centerx = rpg.particle_list_1[1].particle_x_location + 45
        rect_particle.centery = rpg.particle_list_1[1].particle_y_location + 40
        #pygame.draw.rect(self.screen,'black',rect_particle) this works!@
        #pygame.draw.rect(self.screen,'cyan',self.rect_2)

        n = 0
        m = len(rpg.enemy_list) - 1
        while n <= m:
            collisions_test  = pygame.Rect.colliderect(rect_particle,rpg.enemy_list[n])
            if collisions_test:
                #print('hit with particle')
                rpg.enemy_list[n].health -= rpg.particle_list_1[1].damage
                rpg.particle_list_1[1].damage -= rpg.particle_list_1[1].damage
                if rpg.particle_list_1[1].damage < 0:
                    rpg.particle_list_1[1].damage = 0
                rpg.particle_list_1[1].reset_particle(rpg)

            n += 1


    def attack_particle(self,rpg):
        """This wlil be the first particle attack.
        This will launch a projectile, that if it hits the enemy,
        will do damage."""

    def attack_particle_surround(self,rpg):
        """This is the second particle attack. This will be a particle that is animated.
        This particle will start small and simple and grow larger and more complicated.
        The enemies it touches will receive damage.""" # this will most likely need a second rect which is reshaped to make the hit box grow so everything is smooth. 

    def attack_sword_1(self,rpg):
        """ this is the direct attack in front of the character.""" # my plan is to create a new  rect in front of the character, and if its touching the monster
        # then 
        self.rect_attack_right = pygame.Rect.copy(self.rect)
        self.rect_attack_left = pygame.Rect.copy(self.rect)
        self.rect_attack_up = pygame.Rect.copy(self.rect)
        self.rect_attack_down = pygame.Rect.copy(self.rect)
        
        
        self.rect_attack_right.centerx += 90
        self.rect_attack_right.centery += 10
        
        self.rect_attack_left.centerx -= 80
        #self.rect_attack_left.centery -= 40

        self.rect_attack_down.centery += 90
        #self.rect_attack_down.centerx += 65

        self.rect_attack_up.centery -= 90
        self.rect_attack_up.centerx += 10
        match self.highest:
            case 'right':
                """"""
                #pygame.draw.circle(self.screen,('red'),radius=50,center = (self.rect_attack_right.centerx,self.rect_attack_right.centery))
                # collsion here for now. this will be refactored later
                n = 0
                m = len(rpg.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_right.colliderect(rpg.enemy_list[n])
                    if collisions_test:
                        #print('hit right')
                        rpg.enemy_list[n].health -= 10
                    n += 1


            case 'left':
                """"""
                #pygame.draw.circle(self.screen,('yellow'),radius=50,center = (self.rect_attack_left.centerx,self.rect_attack_left.centery))
                n = 0
                m = len(rpg.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_left.colliderect(rpg.enemy_list[n])
                    if collisions_test:
                        #print('hit left')
                        rpg.enemy_list[n].health -= 10
                    n += 1
            case 'up':
                """"""
                #pygame.draw.circle(self.screen,('cyan'),radius=50,center = (self.rect_attack_up.centerx,self.rect_attack_up.centery))
                n = 0
                m = len(rpg.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_up.colliderect(rpg.enemy_list[n])
                    if collisions_test:
                        #print('hit up')
                        rpg.enemy_list[n].health -= 10
                    n += 1
            case 'down':
                """"""
                #pygame.draw.circle(self.screen,('brown'),radius=50,center = (self.rect_attack_down.centerx,self.rect_attack_down.centery))
                n = 0
                m = len(rpg.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_down.colliderect(rpg.enemy_list[n])
                    if collisions_test:
                        #print('hit down')
                        rpg.enemy_list[n].health -= 10
                    n += 1
                    
                #collisions_test = self.rect_attack_down.colliderect(rpg.enemy_list)
                
        #pygame.draw.circle(self.screen,('red'),radius=50,center = (self.rect_attack_right.centerx,self.rect_attack_right.centery))
        #pygame.draw.circle(self.screen,('yellow'),radius=50,center = (self.rect_attack_left.centerx,self.rect_attack_left.centery))
        #pygame.draw.circle(self.screen,('cyan'),radius=50,center = (self.rect_attack_up.centerx,self.rect_attack_up.centery))
        #pygame.draw.circle(self.screen,('brown'),radius=50,center = (self.rect_attack_down.centerx,self.rect_attack_down.centery))

        #pygame.draw.rect(self.screen,'black',rect=self.rect)

        
        #collisions_test = pygame.sprite.spritecollide(rpg.player_1_test,rpg.enemy_list,False)
         
    def attack_cycle(self,rpg):
        """This will be the loops for the attack animation and damage"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_n]:
            """n will be for attack direct 1 for now."""
            if self.attack_active == False:
                self.attack_animation(rpg)
                if self.animation_last == 'right':
                    """"""
                    self.animation_counter = 63
                if self.animation_last == 'left':
                    """"""
                    self.animation_counter = 45
                if self.animation_last == 'down':
                    """"""
                    self.animation_counter = 54
                if self.animation_last == 'up':
                    """"""
                    self.animation_counter = 36
                
                if self.attack_direct_1_counter == self.attack_direct_1_counter_old:
                    self.attack_direct_1_counter -= 1

        if self.attack_direct_1_counter < self.attack_direct_1_counter_old:
            if self.attack_direct_1_counter < self.attack_direct_1_counter_old - 3:
                self.attack_sword_1(rpg)
                
            if self.animation_delay <=0:
                self.attack_direct_1_counter -= 1
                
            if self.attack_direct_1_counter <= 0:
                self.attack_direct_1_counter = self.attack_direct_1_counter_old



    def draw_me(self,rpg):
        """"""
        
        hypotenuse = ((self.velocity[0]**2) + (self.velocity[1]**2))**0.5
        #angle = ((-1)*self.velocity[1]) / hypotenuse
        """if angle > 1:
            angle = 1
        if angle < -1:
            angle = -1"""
        #angle = math.degrees(math.asin(angle))
        #print(angle,' is degrees')
        #print(self.velocity[0],hypotenuse)        
        # this is where the 
        
        a = self.velocity[0]**2
        b = self.velocity[1]**2
        highest = max(a,b)

        speed_trigger = 50
        if highest == a:
            
            if self.velocity[0] >= 0:
                """"""
                self.highest = 'right'
            if self.velocity[0] < 0:
                """"""
                self.highest = 'left'
        if highest == b:
            if self.velocity[1] >= 0:
                """"""
                self.highest = 'down'
            if self.velocity[1] < 0:
                """"""
                self.highest = 'up'
                # dop this

        right_start = 99
        left_start = 81
        up_start = 72
        down_start = 90
        if self.attack_active == False:
            match self.highest:
                case 'right':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'right':
                            if self.animation_counter  < (right_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (right_start + self.animation_length_walk):
                                self.animation_counter = right_start
                        if self.animation_last != 'right':
                            self.animation_counter = right_start
                            self.animation_last = 'right'
                    
                case 'left':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'left':
                            if self.animation_counter  < (left_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (left_start + self.animation_length_walk):
                                self.animation_counter = left_start
                                
                        if self.animation_last != 'left':
                            self.animation_counter = left_start
                            self.animation_last = 'left'
                    
            # right is 27, left is 9, down is 18, up is 0
                case 'down':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'down':
                            if self.animation_counter  < (down_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (down_start + self.animation_length_walk):
                                self.animation_counter = down_start
                        if self.animation_last != 'down':
                            self.animation_counter = down_start
                            self.animation_last = 'down'
                    
                case 'up':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'up':
                            if self.animation_counter  < (up_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (up_start + self.animation_length_walk):
                                self.animation_counter = up_start
                        if self.animation_last != 'up':
                            self.animation_counter = up_start
                            self.animation_last = 'up'
        right_start = 63
        left_start = 45
        up_start = 36
        down_start = 54
        if self.attack_active == True:
            """Then the attack happens"""
            
            match self.highest:
                case 'right':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'right':
                            if self.animation_counter  < (right_start + self.attack_length):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (right_start + self.attack_length):
                                self.animation_counter = right_start + 36
                                self.attack_active = False
                                #print('attack ends', self.animation_counter, left_start, self.attack_length)
                        if self.animation_last != 'right':
                            self.animation_counter = right_start 
                            self.animation_last = 'right'
                    
                case 'left':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'left':
                            if self.animation_counter  < (left_start +self.attack_length):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (left_start + self.attack_length):
                                self.animation_counter = left_start + 36
                                #print('attack ends', self.animation_counter, left_start, self.attack_length)
                                self.attack_active = False
                        if self.animation_last != 'left':
                            self.animation_counter = left_start
                            self.animation_last = 'left'
                    
            # right is 27, left is 9, down is 18, up is 0
                case 'down':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'down':
                            if self.animation_counter  < (down_start + self.attack_length):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (down_start + self.attack_length):
                                self.animation_counter = down_start + 36
                                self.attack_active = False
                                #print('attack ends', self.animation_counter, left_start, self.attack_length)
                        if self.animation_last != 'down':
                            self.animation_counter = down_start
                            self.animation_last = 'down'
                    
                case 'up':
                    """"""
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'up':
                            if self.animation_counter  < (up_start + self.attack_length):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (up_start + self.attack_length):
                                self.animation_counter = up_start + 36
                                self.attack_active = False
                                #print('attack ends', self.animation_counter, left_start, self.attack_length)

                        if self.animation_last != 'up':
                            self.animation_counter = up_start
                            self.animation_last = 'up'
            
                
                #self.screen.blit(self.up_moving_sprite[self.animation_counter],self.rect)
        self.screen.blit(self.sprite_sheet_player_1.surface_list[self.animation_counter],self.rect_2)
        #print(self.animation_counter)
        #self.screen.blit(self.down_moving_sprite[0],self.rect)
        



    def attack_animation(self,rpg):
        """this will be the logic for the attack animation"""
        # this will later be refactored into its own class
        # then each object with an attack can inherit it.
        if self.attack_direct_1_counter < self.attack_direct_1_counter_old:
            self.attack_active = True


