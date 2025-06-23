from enemy_logic import Overworld_person as OP
from sprite_sheet_animater import Sprite_loader
import pygame
import random

class Wolf(OP):

    def __init__(self,rpg,location_to_spawn,type_of_wolf):
        """"""
        OP.__init__(self,rpg,'wolf')
        self.load_and_rescale_wolf("_internal\\img\\wolf_1_cropped_side.png",2)
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.damage = 20
        self.damage_old = self.damage
        self.animation_length = 5
        self.attack_length = 3
        self.down_animation_length = 4
        self.attack_hit = 0

        self.rect = pygame.Rect(0,0,200,300)
        #self.rect.center = (x,y)
        self.rect_2 = pygame.Rect(0,0,200,300)
        #self.rect_2.center = (x,y)
        self.rect_2.x += 200
        self.rect_2.y += 180
        
        self.right_start_animation = 0
        self.left_start_animation = 12
        self.up_start_animation = 47
        self.down_start_animation = 42

        self.rect_picture = self.sprite_enemy.surface_list[0].get_rect()
        self.rect_picture.centerx , self.rect_picture.centery = location_to_spawn[0], location_to_spawn[1]
        self.rect = pygame.Rect(0,0,80,80)

        self.attack_delay = random.randint(40,80) 
        self.attack_delay_old = self.attack_delay

        self.shadow_surface = pygame.Surface((50,150), pygame.SRCALPHA)
        self.shadow_rect = self.shadow_surface.get_rect()
        #self.shadow_rect.centery += 10
        self.shadow_surface.fill((10,10,10))
        self.shadow_surface.set_colorkey((10,10,10))
        pygame.draw.ellipse(self.shadow_surface,(2, 48, 32,150),self.shadow_rect)

        self.shadow_surface_2 = pygame.Surface((150,50), pygame.SRCALPHA)
        self.shadow_rect_2 = self.shadow_surface_2.get_rect()
        #self.shadow_rect.centery += 10
        self.shadow_surface_2.fill((10,10,10))
        self.shadow_surface_2.set_colorkey((10,10,10))
        pygame.draw.ellipse(self.shadow_surface_2,(2, 48, 32,150),self.shadow_rect_2)

        self.rect_attack_down.center = self.rect_picture.center
        self.rect_attack_down.centery += 100
        self.rect_attack_down.centerx += 20
        self.rect_attack_right.center = self.rect_picture.center
        self.rect_attack_right.centerx += 120
        
        self.rect_attack_left.center = self.rect_picture.center
        self.rect_attack_left.centerx -= 80
        self.rect_attack_up.center = self.rect_picture.center
        self.rect_attack_up.centery -= 100
        self.rect_attack_up.centerx += 20

        self.rect.center = self.rect_picture.center


        timer = random.randint(80,210)
        self.accelleration_timer = timer # this determins how often they move
        self.acc_timer_old = self.accelleration_timer

        self.type_of_wolf = type_of_wolf

        self.L_scale = 7
        self.reg_scale = 6
        

        

    def perform_draw(self):
        """"""
        #pygame.draw.rect(self.screen,(200,100,100),self.rect_attack_left)    
        #pygame.draw.rect(self.screen,(100,200,100),self.rect_attack_right)
        #pygame.draw.rect(self.screen,(100,100,200),self.rect_attack_up)
        #pygame.draw.rect(self.screen,(100,150,150),self.rect_attack_down)
        if self.animation_counter > (len(self.sprite_enemy.surface_list)-1):
            self.animation_counter = 0
        if self.animation_last == ('right') or self.animation_last == 'left':  
            self.screen.blit(self.shadow_surface_2,(self.rect_picture.centerx - 60,self.rect_picture.centery  + 20))
            self.screen.blit(self.sprite_enemy.surface_list[self.animation_counter],self.rect_picture)
        if self.animation_last == ('up') or self.animation_last == 'down':
            self.screen.blit(self.shadow_surface,(self.rect_picture.centerx ,self.rect_picture.centery ))
            self.screen.blit(self.sprite_enemy.surface_list[self.animation_counter],(self.rect_picture.centerx - 30,self.rect_picture.centery - 100))
        #pygame.draw.rect(self.screen,(255,255,255),self.rect)
        
        
        #print('this draw')


    def attack_active_false_nest(self):
        """"""
        #hypotenuse = ((self.x_dist**2) + (self.y_dist**2))**0.5
        speed_trigger = 30
        right_start = 0
        left_start = 12
        up_start = 47
        down_start = 42 # old is 41 
        if self.attack_active == False:
            #print('wolf')
            match self.highest:
                case 'right':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'right':
                            if self.animation_counter  < (right_start + self.animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (right_start + self.animation_length):
                                self.animation_counter = right_start
                            if self.animation_counter < right_start:
                                self.animation_counter = right_start
                        if self.animation_last != 'right':
                            self.animation_counter = right_start
                            self.animation_last = 'right'
                case 'left':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'left':
                            if self.animation_counter  < (left_start + self.animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (left_start + self.animation_length):
                                self.animation_counter = left_start
                            if self.animation_counter < left_start:
                                self.animation_counter = left_start
                        if self.animation_last != 'left':
                            self.animation_counter = left_start
                            self.animation_last = 'left'
            # right is 27, left is 9, down is 18, up is 0
                case 'down':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'down':
                            if self.animation_counter  < (down_start + self.down_animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (down_start + self.down_animation_length):
                                self.animation_counter = down_start
                            if self.animation_counter < down_start:
                                self.animation_counter = down_start
                        if self.animation_last != 'down':
                            self.animation_counter = down_start
                            self.animation_last = 'down'
                case 'up':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'up':
                            if self.animation_counter  < (up_start + self.down_animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (up_start + self.down_animation_length):
                                self.animation_counter = up_start
                            if self.animation_counter < up_start:
                                self.animation_counter = up_start
                        if self.animation_last != 'up':
                            self.animation_counter = up_start
                            self.animation_last = 'up'
        if self.hypotenuse < 300:
            self.attack_active = True

    def attack_active_true_nest(self,rpg): # must find bug here for up and down.
        """"""
        #hypotenuse = ((self.velocity[0]**2) + (self.velocity[1]**2))**0.5
        speed_trigger = 1
        right_start = 6 # trash code ends
        left_start = 18
        up_start = 66
        down_start = 60
        if self.attack_active == True:
            """Then the attack happens"""
            match self.highest:
                case 'right':
                    if self.animation_last == 'right':
                        if self.animation_counter  < (right_start + self.attack_length):#and self.animation_counter >= right_start:
                            self.check_animation_attack(rpg,right_start)
                        if self.animation_counter >= (right_start + self.attack_length):
                            self.animation_counter = self.right_start_animation 
                            self.attack_active = False
                    if self.animation_last != 'right':
                        self.animation_counter = right_start 
                        self.animation_last = 'right'
                case 'left':
                    if self.animation_last == 'left':
                        if self.animation_counter  < (left_start +self.attack_length):
                            self.check_animation_attack(rpg,left_start)
                        if self.animation_counter >= (left_start + self.attack_length):
                            self.animation_counter = self.left_start_animation 
                            self.attack_active = False
                    if self.animation_last != 'left':
                        self.animation_counter = left_start
                        self.animation_last = 'left'
            # right is 30, left is 10, down is 20, up is 0
                case 'down':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'down':
                            if self.animation_counter < down_start:
                                self.animation_counter = down_start
                            if self.animation_counter  < (down_start + self.attack_length):
                                self.check_animation_attack(rpg,down_start)
                            if self.animation_counter >= (down_start + self.attack_length):
                                self.animation_counter = self.down_start_animation
                                self.attack_active = False 
                        if self.animation_last != 'down':
                            self.animation_counter = down_start
                            self.animation_last = 'down'
                    '''if self.animation_last == 'down':
                        if self.animation_counter  < (down_start + self.attack_length):
                            self.check_animation_attack(rpg,down_start)
                        if self.animation_counter >= (down_start + self.attack_length):
                            self.animation_counter = self.down_start_animation 
                            self.attack_active = False
                    if self.animation_last != 'down':
                        self.animation_counter = down_start
                        self.animation_last = 'down'''
                case 'up':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'up':
                            if self.animation_counter < up_start:
                                self.animation_counter = up_start
                            if self.animation_counter  < (up_start + self.attack_length):
                                self.check_animation_attack(rpg,up_start)
                            if self.animation_counter >= (up_start + self.attack_length):
                                self.animation_counter = self.up_start_animation
                                self.attack_active = False 
                        if self.animation_last != 'up':
                            self.animation_counter = down_start
                            self.animation_last = 'up'


   
    def check_animation_attack(self,rpg,direction):
        """"""

        self.check_animation_delay()
        if self.animation_counter == (direction + self.attack_hit):
            self.check_attack_hit(rpg)
            
    def draw_me(self,rpg):
        """draws the enemy from the surface to the screen. """
        self.check_health_for_death(rpg)
        self.set_animation_direction(rpg)

    def delete_me(self,rpg):
        """deletes the enemy. The location change is nessecary for other code checking its location to not trigger."""
        rpg.level_stuff.player_1.score += self.score_value
        #pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.cracking_noise)
        #self.score_value = 0
        x = -10000
        y = -10000
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        #self.kill()
        if self.type_of_wolf == 'lone':
            rpg.level_stuff.enemy_list.remove(self)
        if self.type_of_wolf == 'boss':
            rpg.level_stuff.level_1_boss.wolf_list.remove(self)
            rpg.level_stuff.level_1_boss.m_for_draw -= 1
        #del self

    def load_and_rescale_wolf(self,directory,size):
        """This loads the sprite sheet and scales it size. the list of sprites
        will be saved as surfaces in surface list. iterate through the surface list to animate the image."""
        self.sprite_enemy = Sprite_loader(directory,'wolf','_internal\\img\\wolf_1_cropped.png') # this will be its own number. 
        n = 0
        m = len(self.sprite_enemy.surface_list) - 1
        while n <= m:
            self.sprite_enemy.surface_list[n] = pygame.transform.scale_by(self.sprite_enemy.surface_list[n],size)
            n += 1

from projectile_attack import Projectile_class

class Golem(OP):
    """This will be a new enemy type that is a golem."""


    def __init__(self,rpg,location_to_spawn,health):
        OP.__init__(self,rpg,'golem')
        self.health = health
        self.load_and_rescale_golem(2)
        self.animation_length = 7

        self.rect_picture = self.sprite_enemy.surface_list[0].get_rect()
        self.rect_picture.centerx , self.rect_picture.centery = location_to_spawn[0], location_to_spawn[1]


        self.damage = 20
        self.damage_old = self.damage
        #self.animation_length = 5
        self.attack_length = 7
        #self.down_animation_length = 4
        self.attack_hit = 0

        self.rect = pygame.Rect(0,0,200,300)
        #self.rect.center = (x,y)
        self.rect_2 = pygame.Rect(0,0,200,300)
        #self.rect_2.center = (x,y)
        self.rect_2.x += 200
        self.rect_2.y += 180
        
        self.right_start_animation = 20
        self.left_start_animation = 7
        self.up_start_animation = 0
        self.down_start_animation = 14

        self.rect_picture = self.sprite_enemy.surface_list[0].get_rect()
        self.rect_picture.centerx , self.rect_picture.centery = location_to_spawn[0], location_to_spawn[1]
        self.rect = pygame.Rect(0,0,80,80)

        self.attack_delay = random.randint(40,80) 
        self.attack_delay_old = self.attack_delay

        self.shadow_surface = pygame.Surface((50,150), pygame.SRCALPHA)
        self.shadow_rect = self.shadow_surface.get_rect()
        #self.shadow_rect.centery += 10
        self.shadow_surface.fill((10,10,10))
        self.shadow_surface.set_colorkey((10,10,10))
        pygame.draw.ellipse(self.shadow_surface,(2, 48, 32,150),self.shadow_rect)

        self.shadow_surface_2 = pygame.Surface((150,50), pygame.SRCALPHA)
        self.shadow_rect_2 = self.shadow_surface_2.get_rect()
        #self.shadow_rect.centery += 10
        self.shadow_surface_2.fill((10,10,10))
        self.shadow_surface_2.set_colorkey((10,10,10))
        pygame.draw.ellipse(self.shadow_surface_2,(2, 48, 32,150),self.shadow_rect_2)

        self.rect_attack_down.center = self.rect_picture.center
        self.rect_attack_down.centery += 100
        self.rect_attack_down.centerx += 20
        self.rect_attack_right.center = self.rect_picture.center
        self.rect_attack_right.centerx += 120
        
        self.rect_attack_left.center = self.rect_picture.center
        self.rect_attack_left.centerx -= 80
        self.rect_attack_up.center = self.rect_picture.center
        self.rect_attack_up.centery -= 100
        self.rect_attack_up.centerx += 20

        self.rect.center = self.rect_picture.center


        timer = random.randint(80,210)
        self.accelleration_timer = timer # this determins how often they move
        self.acc_timer_old = self.accelleration_timer

        #self.type_of_wolf = type_of_wolf

        self.L_scale = 7
        self.reg_scale = 6

        self.fire_ball_list_aoe = []   
        self.fire_ball_aoe_active = False 
        self.fire_ball_aoe_timer = 1000
        self.fire_ball_aoe_timer_old = self.fire_ball_aoe_timer

        
    def decide_L_or_l_movement(self,rpg): # this should work.
        """This is where the npc decides to make an 
        L manuever or move in a stright line towards player."""
        scale = self.L_scale
        
        if self.first_movement == ('left' or 'right'):
            if self.first_movement == 'left':
                self.dv_dt[0] += (self.x_dist * scale)
                #self.first_movement = ''
            if self.first_movement == 'right':
                self.dv_dt[1] += (self.y_dist * scale)
                #self.first_movement = ''
            self.first_movement = ''
            return
        choice_to_move = random.choice(['L','1','targeting','aoe'])
        
        match choice_to_move:
            case 'L':
                """"""
                choice_left_or_right = random.choice(['right','left'])
                if choice_left_or_right == 'right':
                    self.dv_dt[0] += (self.x_dist * scale)
                    self.first_movement = 'right'
                if choice_left_or_right == 'left':
                    self.dv_dt[1] += (self.y_dist * scale)
                    self.first_movement = 'left'
            case '1':
                """"""
                self.make_decision(rpg)
            case 'targeting':
                """This targets the player.
                This means it adds the distance vector to the players velocity vector.
                Multiply the number of seconds it takes to arrive by the vector to
                make it arrive in 1 second. """
                movement_x = self.x_dist + rpg.level_stuff.player_1.velocity[0]
                movement_y = self.y_dist + rpg.level_stuff.player_1.velocity[1]

                self.dv_dt[0] += movement_x
                self.dv_dt[1] += movement_y
            case 'aoe':
                """This will activate the aoe attack"""
                self.spawn_aoe_fireball(rpg)

    def prepare_aoe_attack(self,rpg,number_of_fireballs):
        """This will be aoe attack setup that creates all the assets."""
        n = 0
        m = number_of_fireballs

        while n < m:
            a = Projectile_class(rpg,'fireball',0)
            a.fire_ball_rect.center = self.rect_2.center
            self.fire_ball_list_aoe.append(a)
            n += 1

    def reset_aoe_attack(self):
        """This resets the aoe attack back to its starter location"""
        
        n = 0
        m = len(self.fire_ball_list_aoe)
        while n < m:
            self.fire_ball_list_aoe[n].fire_ball_rect.x = self.rect.x
            self.fire_ball_list_aoe[n].fire_ball_rect.y = self.rect.y
            n += 1
        self.fire_ball_aoe_active = False

    def move_fireball_aoe(self,rpg):
        """This will move the fireball"""
        if self.fire_ball_aoe_active:
            i = 0
            j = len(self.fire_ball_list_aoe)
            while i < j:
                self.fire_ball_list_aoe[i].update_speed_stats(rpg)
                self.fire_ball_list_aoe[i].fire_ball_rect.x += rpg.level_stuff.player_1.velocity[0] * rpg.dt
                self.fire_ball_list_aoe[i].fire_ball_rect.y += rpg.level_stuff.player_1.velocity[1] * rpg.dt
                i += 1

    def fireball_aoe_draw(self,rpg):
        """This checks for the activity of fireball and draws it on screen if its active"""
        
        i = 0
        j = len(self.fire_ball_list_aoe)
        while i < j:
            """This sets them all active"""
            if self.fire_ball_list_aoe[i].fire_ball_active:
                #self.fire_ball_list_aoe[i].check_fire_hit(rpg)
                self.fire_ball_list_aoe[i].check_fire_hit(rpg)
                self.screen.blit(self.fire_ball_list_aoe[i].fire_ball.surface_list[self.fire_ball_list_aoe[i].fire_ball_animation_counter],(self.fire_ball_list_aoe[i].fire_ball_rect))
                self.fire_ball_list_aoe[i].fire_ball_animation_delay -= 1
                if self.fire_ball_list_aoe[i].fire_ball_animation_delay <= 0:
                    self.fire_ball_list_aoe[i].fire_ball_animation_counter += 1
                    self.fire_ball_list_aoe[i].fire_ball_animation_delay = self.fire_ball_list_aoe[i].fire_ball_animation_delay_old
                if self.fire_ball_list_aoe[i].fire_ball_animation_counter >= (len(self.fire_ball_list_aoe[i].fire_ball.surface_list)):
                    self.fire_ball_list_aoe[i].fire_ball_animation_counter = 0
            i += 1

    def spawn_aoe_fireball(self,rpg):
        """This spawns the fireballs for an attack in an X shape"""
        if self.fire_ball_aoe_active == False:
            self.fire_ball_aoe_active = True

            x_distance = rpg.level_stuff.player_1.rect.centerx - self.rect_2.centerx
            y_distance = rpg.level_stuff.player_1.rect.centery - self.rect_2.centery

            a = random.choice([rpg.level_stuff.sound_logic.fire_sound_1,rpg.level_stuff.sound_logic.fire_sound_2])
            rpg.level_stuff.sound_logic.fire_sound_1.set_volume(rpg.settings_hold.max_volume)
            rpg.level_stuff.sound_logic.fire_sound_2.set_volume(rpg.settings_hold.max_volume)
            #rpg.level_stuff.sound_logic.bang_sound_1.set_volume(rpg.settings_hold.max_volume)
            #pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.bang_sound_1)
            pygame.mixer.Sound.play(a)
            # this now activated the fireballs
            i = 0
            j = len(self.fire_ball_list_aoe)
            while i < j:
                """This sets them all active"""
                #r = random.uniform(500,4000)
                r = random.uniform(500)
                s = random.choice([0,1,-1,0])
                s2 = random.choice([0,1,-1,0])
                #s = random.choice([-1,1])
                #s2 = random.choice([-1,1])
                self.fire_ball_list_aoe[i].fire_ball_active = True
                self.fire_ball_list_aoe[i].hit_limit = 1
                self.fire_ball_list_aoe[i].fire_ball_animation_counter = 0
                self.fire_ball_list_aoe[i].fire_damage = self.fire_ball_list_aoe[i].fire_damage_old
                self.fire_ball_list_aoe[i].fire_ball_rect.x =  rpg.level_stuff.player_1.rect.centerx + r * s #r * s
                self.fire_ball_list_aoe[i].fire_ball_rect.y =  rpg.level_stuff.player_1.rect.centery + r * s2 #r * s2

                i += 1



    def area_attack_loop(self,rpg):
        """This will be the aoe attack"""
        if self.fire_ball_aoe_active:
            """Then loop is here."""
            self.fireball_aoe_draw(rpg)
            self.move_fireball_aoe(rpg)
            self.fire_ball_aoe_timer -= 1
            if self.fire_ball_aoe_timer <= 0:
                self.fire_ball_aoe_timer = self.fire_ball_aoe_timer_old
                self.reset_aoe_attack()
                
    def draw_me(self,rpg):
        """draws the enemy from the surface to the screen. """
        self.check_health_for_death(rpg)
        self.set_animation_direction(rpg)
        self.area_attack_loop(rpg)


    def load_and_rescale_golem(self,size):
        """This loads the golem and resizes it"""
        self.sprite_enemy = Sprite_loader('_internal\\img\\golem-walk.png','golem','_internal\\img\\golem-atk.png')
        n = 0
        m = len(self.sprite_enemy.surface_list)
        while n < m:
            self.sprite_enemy.surface_list[n] = pygame.transform.scale_by(self.sprite_enemy.surface_list[n],size)
            n += 1

    def attack_active_false_nest(self):
        """This is for the animation when not attacking"""
        #hypotenuse = ((self.x_dist**2) + (self.y_dist**2))**0.5
        speed_trigger = 30
        right_start = 20
        left_start = 7
        up_start = 0
        down_start = 14 # old is 41 
        if self.attack_active == False:
            #print('wolf')
            match self.highest:
                case 'right':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'right':
                            if self.animation_counter  < (right_start + self.animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (right_start + self.animation_length):
                                self.animation_counter = right_start
                            if self.animation_counter < right_start:
                                self.animation_counter = right_start
                        if self.animation_last != 'right':
                            self.animation_counter = right_start
                            self.animation_last = 'right'
                case 'left':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'left':
                            if self.animation_counter  < (left_start + self.animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (left_start + self.animation_length):
                                self.animation_counter = left_start
                            if self.animation_counter < left_start:
                                self.animation_counter = left_start
                        if self.animation_last != 'left':
                            self.animation_counter = left_start
                            self.animation_last = 'left'
            # right is 27, left is 9, down is 18, up is 0
                case 'down':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'down':
                            if self.animation_counter  < (down_start + self.animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (down_start + self.animation_length):
                                self.animation_counter = down_start
                            if self.animation_counter < down_start:
                                self.animation_counter = down_start
                        if self.animation_last != 'down':
                            self.animation_counter = down_start
                            self.animation_last = 'down'
                case 'up':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'up':
                            if self.animation_counter  < (up_start + self.animation_length):
                                self.check_animation_delay()
                            if self.animation_counter >= (up_start + self.animation_length):
                                self.animation_counter = up_start
                            if self.animation_counter < up_start:
                                self.animation_counter = up_start
                        if self.animation_last != 'up':
                            self.animation_counter = up_start
                            self.animation_last = 'up'
        if self.hypotenuse < 300:
            self.attack_active = True
    
    def attack_active_true_nest(self,rpg): # must find bug here for up and down.
        """This is for when the golem attacks"""
        #hypotenuse = ((self.velocity[0]**2) + (self.velocity[1]**2))**0.5
        speed_trigger = 1
        right_start = 48 # trash code ends
        left_start = 34
        up_start = 28
        down_start = 41
        if self.attack_active == True:
            """Then the attack happens"""
            match self.highest:
                case 'right':
                    if self.animation_last == 'right':
                        if self.animation_counter  < (right_start + self.attack_length):#and self.animation_counter >= right_start:
                            self.check_animation_attack(rpg,right_start)
                        if self.animation_counter >= (right_start + self.attack_length):
                            self.animation_counter = self.right_start_animation 
                            self.attack_active = False
                    if self.animation_last != 'right':
                        self.animation_counter = right_start 
                        self.animation_last = 'right'
                case 'left':
                    if self.animation_last == 'left':
                        if self.animation_counter  < (left_start +self.attack_length):
                            self.check_animation_attack(rpg,left_start)
                        if self.animation_counter >= (left_start + self.attack_length):
                            self.animation_counter = self.left_start_animation 
                            self.attack_active = False
                    if self.animation_last != 'left':
                        self.animation_counter = left_start
                        self.animation_last = 'left'
            # right is 30, left is 10, down is 20, up is 0
                case 'down':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'down':
                            if self.animation_counter < down_start:
                                self.animation_counter = down_start
                            if self.animation_counter  < (down_start + self.attack_length):
                                self.check_animation_attack(rpg,down_start)
                            if self.animation_counter >= (down_start + self.attack_length):
                                self.animation_counter = self.down_start_animation
                                self.attack_active = False 
                        if self.animation_last != 'down':
                            self.animation_counter = down_start
                            self.animation_last = 'down'
                    '''if self.animation_last == 'down':
                        if self.animation_counter  < (down_start + self.attack_length):
                            self.check_animation_attack(rpg,down_start)
                        if self.animation_counter >= (down_start + self.attack_length):
                            self.animation_counter = self.down_start_animation 
                            self.attack_active = False
                    if self.animation_last != 'down':
                        self.animation_counter = down_start
                        self.animation_last = 'down'''
                case 'up':
                    if self.hypotenuse >= speed_trigger:
                        if self.animation_last == 'up':
                            if self.animation_counter < up_start:
                                self.animation_counter = up_start
                            if self.animation_counter  < (up_start + self.attack_length):
                                self.check_animation_attack(rpg,up_start)
                            if self.animation_counter >= (up_start + self.attack_length):
                                self.animation_counter = self.up_start_animation
                                self.attack_active = False 
                        if self.animation_last != 'up':
                            self.animation_counter = down_start
                            self.animation_last = 'up'
