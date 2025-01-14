import pygame
import math
import random
from enemy_logic import Overworld_person

class Boss(Overworld_person):
    """This is the class for creating a boss. These will be stronger than regular enemies.
    Will also have unique attacks."""
    def __init__(self,rpg):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__(rpg)

        self.attack_animation_delay = 4
        self.attack_animation_delay_old = self.attack_animation_delay
        self.animation_lenth_attack_1 = 4
        self.attack_count = 0
        self.delay_1 = 15
        self.delay_1_old = self.delay_1
        self.hit_limit = 1
        self.hit_limit_old = self.hit_limit

        self.hit_1_knockback = 3000


        self.highest = 'right'
        n = 0
        m = 9
        
        self.image_list_right = []
        self.image_list_left = []

        self.attack = False

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

        self.load_and_rescale("images1\spider11.png",6)
      
        
        self.animation_counter = 0
        self.animation_delay = 20

        self.animation_delay_start = self.animation_delay

        self.animation_length = 6

        x = -1000
        y = 2500
        #self.rect = self.image_list_right[0].get_rect()
        self.rect = pygame.Rect(0,0,200,300)
        self.rect.center = (x,y)
        #self.rect.x += 600
        #self.rect.y += 600
        self.rect_2 = pygame.Rect(0,0,200,300)
        self.rect_2.center = (x,y)
        self.rect_2.x += 200
        self.rect_2.y += 180

        self.rect_attack_right = pygame.Rect(0,0,100,200)
        self.rect_attack_left = pygame.Rect(0,0,100,200)
        self.rect_attack_up = pygame.Rect(0,0,200,100)
        self.rect_attack_down = pygame.Rect(0,0,200,100)

        self.rect_attack_right.center = (x,y)
        self.rect_attack_right.x += 400
        self.rect_attack_right.y += 180

        self.rect_attack_left.center = (x,y)
        self.rect_attack_left.x -= 20
        self.rect_attack_left.y += 180

        self.rect_attack_up.center = (x,y)
        self.rect_attack_up.x += 200
        self.rect_attack_up.y -= 50

        self.rect_attack_down.center = (x,y)
        self.rect_attack_down.x += 200
        self.rect_attack_down.y += 400
        


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
        self.boss_attack_delay = self.animation_length
        #self.boss_attack_delay = self.animation_length
        self.boss_attack_timer = 10
        self.boss_attack_timer_old =self.boss_attack_timer

        #self.rect_5 = pygame.Rect(0,0,120,120)
        p0 = 0
        end = 30
        while p0 <= end:
            """"""
            p0 += 1



    def draw_me(self):
        """draws the enemy from the surface to the screen. """
        if self.animation_counter >= len(self.sprite_enemy.surface_list):
            self.animation_counter = len(self.sprite_enemy.surface_list) - 1
        self.screen.blit(self.sprite_enemy.surface_list[self.animation_counter],(self.rect))
        pygame.draw.rect(self.screen,'cyan',self.rect_2)
        pygame.draw.rect(self.screen,'red',self.rect_attack_down)
        pygame.draw.rect(self.screen,'yellow',self.rect_attack_left)
        pygame.draw.rect(self.screen,'green',self.rect_attack_right)
        pygame.draw.rect(self.screen,'purple',self.rect_attack_up)
        #self.animation_counter += 1
        """self.animation_delay -= 1
        if self.boss_attack_delay >= 0:
            if self.animation_delay <= 0:
                if self.attack == True:
                    self.animation_counter += 1
                    print('counter added in draw me')
                self.boss_attack_delay -= 1
                #self.boss_attack_delay -= 1
                self.animation_delay = self.animation_delay_old
                if (self.animation_counter_old + self.animation_length) <= self.animation_counter:
                    self.animation_counter = self.animation_counter_old 
                    #self.boss_attack_delay = 0 """
                    


    def check_direct_attack_hit(self,rpg):
        """""" # 0up , 10 left, 20 down, 30 right,
        if self.animation_counter == 2:
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_up,rpg.player_1.rect)
            if collisions_test:
                """"""
                if self.hit_limit > 0:
                    print('boss hits player')
                    rpg.player_1.velocity[1] -= self.hit_1_knockback
                    self.hit_limit -=1
        if self.animation_counter == 12:
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_left,rpg.player_1.rect)
            if collisions_test:
                """"""
                if self.hit_limit > 0:
                    print('boss hits player')
                    rpg.player_1.velocity[0] -= self.hit_1_knockback
                    self.hit_limit -=1
        if self.animation_counter == 22:
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_down,rpg.player_1.rect)
            if collisions_test:
                """"""
                if self.hit_limit > 0:
                    print('boss hits player')
                    rpg.player_1.velocity[1] += self.hit_1_knockback
                    self.hit_limit -=1
        if self.animation_counter == 32:
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_right,rpg.player_1.rect)
            if collisions_test:
                """"""
                if self.hit_limit > 0:
                    print('boss hits player')
                    rpg.player_1.velocity[0] += self.hit_1_knockback
                    self.hit_limit -=1




    def set_animation_direction(self,rpg):
        """This will make the animation face in the correct direction.
        It will also make the animation count through a loop"""
        
        x_calc = rpg.player_1.rect.centerx - self.rect_2.centerx
        y_calc = rpg.player_1.rect.centery - self.rect_2.centery
        hypotenuse_boss_player_1 = ((x_calc**2) +(y_calc**2))**0.5
        angle_to_calc = (-1)*( y_calc / hypotenuse_boss_player_1)

        angle_boss_player_1 = math.degrees(math.asin(angle_to_calc))
        #print(round(angle_boss_player_1,2),round(x_calc,2),round(y_calc,2),' is angle, x, y')


        if self.attack == False:
            if x_calc >= 0:
                if 0 <= angle_boss_player_1 <= 45:
                    self.animation_counter = 34
                    self.animation_counter_old = self.animation_counter 

                
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < angle_boss_player_1 <= 90:
                    self.animation_counter = 4
                    self.animation_counter_old = self.animation_counter
                if -45 <= angle_boss_player_1 < 0:
                    self.animation_counter = 34
                    self.animation_counter_old = self.animation_counter
                if -90 <= angle_boss_player_1 < -45:
                    self.animation_counter = 24
                    self.animation_counter_old = self.animation_counter

            if x_calc < 0:
                """"""
                if 0 <= angle_boss_player_1 <= 45:
                    self.animation_counter = 14
                    self.animation_counter_old = self.animation_counter 

                
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < angle_boss_player_1 <= 90:
                    self.animation_counter = 4
                    self.animation_counter_old = self.animation_counter
                if -45 <= angle_boss_player_1 < 0:
                    self.animation_counter = 14
                    self.animation_counter_old = self.animation_counter
                if -90 <= angle_boss_player_1 < -45:
                    self.animation_counter = 24
                    self.animation_counter_old = self.animation_counter



        if self.attack == True:
            """"""
            #self.check_direct_attack_hit(rpg)
            if x_calc >= 0:
                if 0 <= angle_boss_player_1 <= 45:
                    self.animation_counter = 30
                    self.animation_counter_old = self.animation_counter 

                
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < angle_boss_player_1 <= 90:
                    self.animation_counter = 0
                    self.animation_counter_old = self.animation_counter
                if -45 <= angle_boss_player_1 < 0:
                    self.animation_counter = 30
                    self.animation_counter_old = self.animation_counter
                if -90 <= angle_boss_player_1 < -45:
                    self.animation_counter = 20
                    self.animation_counter_old = self.animation_counter

            if x_calc < 0:
                """"""
                if 0 <= angle_boss_player_1 <= 45:
                    self.animation_counter = 10
                    self.animation_counter_old = self.animation_counter 

                
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < angle_boss_player_1 <= 90:
                    self.animation_counter = 0
                    self.animation_counter_old = self.animation_counter
                if -45 <= angle_boss_player_1 < 0:
                    self.animation_counter = 10
                    self.animation_counter_old = self.animation_counter
                if -90 <= angle_boss_player_1 < -45:
                    self.animation_counter = 20
                    self.animation_counter_old = self.animation_counter



    def boss_check(self,rpg):
        """This holds the boss loop and activities"""
        rpg.physics_active.update_boss(rpg)
        #print(self.animation_counter, self.boss_attack_timer, ' is counter and timer')
        #pygame.draw.rect(self.screen,'black',rect=self.rect)
        if self.boss_attack_timer > 0:
            #self.animation_length = 6
            #print('greater than 0 attack timer')
            if self.attack == False:
                #print('not self.attack', self.attack)
                self.set_animation_direction(rpg)
                #if self.boss_attack_delay <= 0:
                #print('set direction')
                #self.set_animation_direction(rpg)
                self.boss_attack_delay = self.animation_length
                #attack gets triggered to start
                self.boss_attack_timer -= 1
                #print(self.boss_attack_timer,' is boss attack timer')
            #self.boss_attack_delay -= 1
            #print(self.boss_attack_delay,' is boss attack delay')
            if self.attack == True:
                self.check_direct_attack_hit(rpg)
                #print('self.attack is true')
                self.boss_attack_delay -= 1
                if self.attack_count < self.animation_lenth_attack_1:
                    """"""
                    
                    self.delay_1 -=1
                    if self.delay_1 <= 0:
                        self.attack_count += 1
                        self.animation_counter += 1
                        self.delay_1 = self.delay_1_old
                    #print(self.attack_count, 'is attack count')
                if self.attack_count >= self.animation_lenth_attack_1:
                    self.attack = False
                    self.attack_count = 0

                """self.attack_animation_delay -= 1
                if self.attack_animation_delay <= 0:

                    #self.animation_counter += 1
                    self.attack_animation_delay = self.attack_animation_delay_old
                    print(self.animation_counter, 'added')"""
                
            """if self.boss_attack_delay <= 0:
                self.attack = False"""
            #self.draw_me()
                
        if self.boss_attack_timer <=0:
            """then the boss attacks"""
            #print('boss starts attack')
            self.attack = True
            self.hit_limit = self.hit_limit_old
            #self.boss_attack_primary(rpg)
            self.set_animation_direction(rpg)
            self.boss_attack_delay = self.animation_lenth_attack_1
            self.boss_attack_timer = self.boss_attack_timer_old
            #self.animation_length = 4
            #self.attack = True
            #self.animation_counter
            #print(self.attack, 'is after setting to true.')

    def check_hitbox_for_direct_attack_1(self,rpg):
        """this is for checking the hit box during part of the animation."""
    def boss_attack_primary(self,rpg):
        """This is the bosses primary attack"""
        self.set_animation_direction(rpg)
        # next i need attack 

    
    def boss_attack_secondary(Self,rpg):
        """This is the bosses secondary attack"""
    def boss_spawn_ally(Self,rpg):
        """This spawns an ally with a velocity in a random direction"""
