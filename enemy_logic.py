import pygame
from pygame.sprite import  Sprite
import random
from sprite_sheet_animater import Sprite_loader
from physics_stats import Physics_stats
from enemy_intelligence import Enemy_intelligence

class Overworld_person(Sprite,Physics_stats,Enemy_intelligence):
    """This is the image of the enemy that shows up on the world map when you move around the game world."""

    def __init__(self,rpg,type_of_character):
        """loads the images and gives random location. Also random image"""
        Physics_stats.__init__(self,rpg)
        Enemy_intelligence.__init__(self,type_of_character)
        # sets up the screen.
        self.mass = 2 # 20 kilogram spider, why not.
        self.score_value = 1
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        #brings in sprite
        super().__init__()
        # picks a image for the enemy
        a = [1,2,3,4]
        pick = random.choice(a)
        scale = 1
        match pick:
            case 1:
                Overworld_person.load_and_rescale(self,"_internal\\img\\spider06.png",scale)
            case 2:
                Overworld_person.load_and_rescale(self,"_internal\\img\\spider07.png",scale)
            case 3:
                Overworld_person.load_and_rescale(self,"_internal\\img\\spider08.png",scale)
            case 4:
                Overworld_person.load_and_rescale(self,"_internal\\img\\spider10.png",scale)
        # does rect stuff
        self.rect_picture = self.sprite_enemy.surface_list[0].get_rect()
        self.rect = pygame.Rect(0,0,30,30)
        # location on map established. 
        x = random.randint(-10000,10000)
        y = random.randint(-10000,10000)
        self.rect.center = (x,y)
        self.rect_picture.center = (x,y)
        # established a surface 
        self.surface = pygame.Surface((100,100))
        self.surface.fill((0,0,0))
        self.surface.set_colorkey((0,0,0))
        # variables for velocity and accelleration and movement timer.
        self.V_x = 0
        self.V_y = 0
        self.dydt = 10
        self.dxdt = 10
        self.dVdt = random.randint(30,100)
        timer = random.randint(150,310)
        self.accelleration_timer = timer # this determins how often they move
        self.acc_timer_old = self.accelleration_timer
        # centering the rect on image.
        self.x = self.rect.x
        self.y = self.rect.y
        self.health = 30
        self.damage = 5
        self.damage_old = self.damage
        self.min_acc = 80
        self.max_acc = 200
        # animation timer
        self.animation_counter = 0
        self.animation_counter_old = self.animation_counter
        self.animation_delay = 5
        self.animation_delay_old = self.animation_delay
        self.animation_direction = 'up'
        self.animation_length = 5
        self.previous_direction = 'up'
        self.animation_last = 'up'
        self.attack_active_timer = 0
        self.attack_active = False
        self.attack_delay = random.randint(40,80) # 40 works great for backup
        self.hit_limit = 1
        self.attack_length = 3
        self.attack_delay_old = self.attack_delay
        self.rect_attack_right = pygame.Rect(0,0,80,80)
        self.rect_attack_left = pygame.Rect(0,0,80,80)
        self.rect_attack_up = pygame.Rect(0,0,80,80)
        self.rect_attack_down = pygame.Rect(0,0,80,80)
        self.rect_attack_right.center = (x,y)
        self.rect_attack_right.x += 50
        self.rect_attack_right.y += 0
        self.rect_attack_left.center = (x,y)
        self.rect_attack_left.x -= 50
        self.rect_attack_left.y += 0
        self.rect_attack_up.center = (x,y)
        self.rect_attack_up.x += 0
        self.rect_attack_up.y -= 50
        self.rect_attack_down.center = (x,y)
        self.rect_attack_down.x += 0
        self.rect_attack_down.y += 50



        self.shadow_surface = pygame.Surface((50,50), pygame.SRCALPHA)
        self.shadow_rect = self.shadow_surface.get_rect()
        #self.shadow_rect.centery += 10
        self.shadow_surface.fill((10,10,10))
        self.shadow_surface.set_colorkey((10,10,10))
        pygame.draw.ellipse(self.shadow_surface,(2, 48, 32,150),self.shadow_rect)
        


        



    

    def check_attack(self,rpg):
        """This checks if the attack delay is below 0. if it is, then the enemy will attack whatever is in front"""
        if self.hypotenuse <= 1200:
            self.attack_delay -=1
            #print(self.attack_delay, ' is attack delay', self.animation_counter, self.animation_delay, 'is animation counter and delay')
            if self.attack_delay <= 0:
                #print('attack activates')
                self.damage = self.damage_old
                self.attack_active = True
                self.attack_delay = self.attack_delay_old
                volume_hold = 0.2 - (self.hypotenuse / 5000)
                if volume_hold > 0.2:
                    volume_hold = 0.2
                if volume_hold < 0:
                    volume_hold = 0
                

    def check_attack_hit(self,rpg):
        """This checks if the spider hits the player"""
        match self.highest:
            case 'up':
                collisions_test  = pygame.Rect.colliderect(self.rect_attack_up,rpg.level_stuff.player_1)
            case 'right':
                collisions_test  = pygame.Rect.colliderect(self.rect_attack_right,rpg.level_stuff.player_1)
            case 'down':
                collisions_test  = pygame.Rect.colliderect(self.rect_attack_down,rpg.level_stuff.player_1)
            case 'left':
                collisions_test  = pygame.Rect.colliderect(self.rect_attack_left,rpg.level_stuff.player_1)

        #collisions_test  = pygame.Rect.colliderect(self.rect,rpg.level_stuff.player_1)
        if collisions_test:
            if self.damage > rpg.level_stuff.player_1.armor:
                rpg.level_stuff.player_1.health -= self.damage
                rpg.overlay.create_damage_for_overlay(self.damage,rpg.level_stuff.player_1.rect.center,'red')
                self.damage -= self.damage
                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_hit_sound)
                if self.damage < 0:
                    self.damage = 0

    def load_and_rescale(self,directory,size):
        """This loads the sprite sheet and scales it size. the list of sprites
        will be saved as surfaces in surface list. iterate through the surface list to animate the image."""
        self.sprite_enemy = Sprite_loader(directory,2)
        n = 0
        m = len(self.sprite_enemy.surface_list) - 1
        while n <= m:
            self.sprite_enemy.surface_list[n] = pygame.transform.scale_by(self.sprite_enemy.surface_list[n],size)
            n += 1

    def delete_me(self,rpg):
        """deletes the enemy. The location change is nessecary for other code checking its location to not trigger."""
        rpg.level_stuff.player_1.score += self.score_value
        pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.cracking_noise)
        #self.score_value = 0
        x = -10000
        y = -10000
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        #self.kill()
        
        rpg.level_stuff.enemy_list.remove(self)
        del self

    def check_health_for_death(self,rpg):
        if self.health <= 0:
            self.delete_me(rpg)
    def draw_me(self,rpg):
        """draws the enemy from the surface to the screen. """
        self.check_health_for_death(rpg)
        self.set_animation_direction(rpg)


    def draw_for_credits(self,location):
        """this draws the art for credit screen"""
        self.screen.blit(self.sprite_enemy.surface_list[1],(location[0],location[1]))
    
    def check_highest(self):
        """"""
        a = self.velocity[0]**2
        b = self.velocity[1]**2
        highest = max(a,b)
        #speed_trigger = 30
        if highest == a:
            if self.velocity[0] >= 0:
                self.highest = 'right'
                self.previous_direction = self.highest
            if self.velocity[0] < 0:
                self.highest = 'left'
                self.previous_direction = self.highest
            
        if highest == b:
            if self.velocity[1] >= 0:
                self.highest = 'down'
                self.previous_direction = self.highest
            if self.velocity[1] < 0:
                self.highest = 'up'
                self.previous_direction = self.highest
        if self.velocity[0] == 0 and self.velocity[1] == 0:
            self.highest = self.previous_direction # i might chnage this to down.

    def check_animation_attack(self,rpg,direction):
        """"""
        if self.animation_delay <=0:
            self.animation_counter += 1
            if self.animation_counter == (direction + 2):
                self.check_attack_hit(rpg)
            self.animation_delay = self.animation_delay_old
        if self.animation_delay > 0:
            self.animation_delay -= 1

        

    def attack_active_true_nest(self,rpg):
        """"""
        right_start = 30 # trash code ends
        left_start = 10
        up_start = 0
        down_start = 20
        if self.attack_active == True:
            """Then the attack happens"""
            match self.highest:
                case 'right':
                    if self.animation_last == 'right':
                        if self.animation_counter  < (right_start + self.attack_length):
                            self.check_animation_attack(rpg,right_start)
                        if self.animation_counter >= (right_start + self.attack_length):
                            self.animation_counter = right_start  
                            self.attack_active = False
                    if self.animation_last != 'right':
                        self.animation_counter = right_start 
                        self.animation_last = 'right'
                case 'left':
                    if self.animation_last == 'left':
                        if self.animation_counter  < (left_start +self.attack_length):
                            self.check_animation_attack(rpg,left_start)
                        if self.animation_counter >= (left_start + self.attack_length):
                            self.animation_counter = left_start 
                            self.attack_active = False
                    if self.animation_last != 'left':
                        self.animation_counter = left_start
                        self.animation_last = 'left'
            # right is 30, left is 10, down is 20, up is 0
                case 'down':
                    if self.animation_last == 'down':
                        if self.animation_counter  < (down_start + self.attack_length):
                            self.check_animation_attack(rpg,down_start)
                        if self.animation_counter >= (down_start + self.attack_length):
                            self.animation_counter = down_start 
                            self.attack_active = False
                    if self.animation_last != 'down':
                        self.animation_counter = down_start
                        self.animation_last = 'down'
                case 'up':
                    if self.animation_last == 'up':
                        if self.animation_counter  < (up_start + self.attack_length):
                            self.check_animation_attack(rpg,up_start)
                        if self.animation_counter >= (up_start + self.attack_length):
                            self.animation_counter = up_start 
                            self.attack_active = False
                    if self.animation_last != 'up':
                        self.animation_counter = up_start
                        self.animation_last = 'up'

    def check_animation_delay(self):
        """"""
        if self.animation_delay <=0:
            self.animation_counter += 1
            self.animation_delay = self.animation_delay_old
        if self.animation_delay > 0:
            self.animation_delay -= 1                        
        


    def attack_active_false_nest(self):
        """"""
        hypotenuse = ((self.velocity[0]**2) + (self.velocity[1]**2))**0.5
        speed_trigger = 30
        right_start = 34
        left_start = 14
        up_start = 4
        down_start = 24 
        if self.attack_active == False:
            match self.highest:
                case 'right':
                    if hypotenuse >= speed_trigger:
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
                    if hypotenuse >= speed_trigger:
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
                    if hypotenuse >= speed_trigger:
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
                    if hypotenuse >= speed_trigger:
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



    def set_animation_direction(self,rpg):
        """This will make the animation face in the correct direction.
        It will also make the animation count through a loop"""
        self.check_attack(rpg)
        self.check_highest()
        self.attack_active_false_nest()
        self.attack_active_true_nest(rpg) 
        self.perform_draw()

    def perform_draw(self):
        """"""  
        self.screen.blit(self.shadow_surface,(self.rect_picture.centerx - 20,self.rect_picture.centery - 8))
        if self.animation_counter > (len(self.sprite_enemy.surface_list)-1):
            self.animation_counter = 0
        self.screen.blit(self.sprite_enemy.surface_list[self.animation_counter],self.rect_picture) 
        

    