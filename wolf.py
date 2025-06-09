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



