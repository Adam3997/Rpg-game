import pygame
import math
import random
from enemy_logic import Overworld_person
from physics_stats import Physics_stats
from sprite_sheet_animater import Sprite_loader
from projectile_attack import Projectile_class
#from polygon_parametric import Create_polygon
from fire_ritual import Fire_ritual
from wolf import Wolf

class Boss(Overworld_person,Physics_stats):
    """This is the class for creating a boss. These will be stronger than regular enemies.
    Will also have unique attacks."""
    def __init__(self,rpg,x_min,x_max,y_min,y_max,cut_scene,level,type_of_boss):
        self.one_switch = True
        if cut_scene == False:
            x = random.randint(x_min,x_max)
            y = random.randint(y_min,y_max)
        if cut_scene == True:
            x = 200
            y = 200
        Physics_stats.__init__(self,rpg)
        Overworld_person(rpg,'spider')
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        #super().__init__(rpg)
        self.mass = 5000
        self.attack_animation_delay = 4
        self.attack_animation_delay_old = self.attack_animation_delay
        self.animation_lenth_attack_1 = 4
        self.attack_count = 0
        self.delay_1 = 15
        self.delay_1_old = self.delay_1
        self.hit_limit = 1
        self.hit_limit_old = self.hit_limit
   
        self.fire_ball_limit = 1
        self.fire_active_1 = False
        self.hit_1_knockback = 3000
        self.hit_1_damage = 10
        self.fire_distance_active = 1000
        self.level = level
        self.a = 0

        self.fireball_x_attack_active = False
        j = 0
        k = 15
        self.fireball_list_x =[]
        while j <= k:
            a = Projectile_class(rpg,3,4)
            a.fire_ball_rect.center = (x,y)
            self.fireball_list_x.append(a)
            j += 1


        # below is fireball for 0 attack
        p = 0
        q = 4
        self.fireball_list = []
        while p <= q:
            a = Projectile_class(rpg,3,2)
            a.fire_ball_rect.center = (x,y)
            self.fireball_list.append(a)
            p += 1
        self.highest = 'right'
        if type_of_boss == 'regular':
            n = 0
            m = 9
            self.image_list_right = []
            self.image_list_left = []
            self.attack = False
            while n < 9:
                load_string = '_internal\\spiderboss_right_'
                added = str(n)
                added2 = '.bmp'
                load_string += added
                load_string += added2
                image_hold = pygame.image.load(load_string)
                image_hold = pygame.transform.scale_by(image_hold,8)
                self.image_list_right.append(image_hold)
                n += 1
            self.load_and_rescale("_internal\\spider11.png",6)
        if type_of_boss == 'Second':
            """"""
            self.load_and_rescale('_internal\\spider04.png',6)
            #self.sprite_loaded = Sprite_loader
        
        self.score_value = 5000
        self.animation_counter = 0
        self.animation_delay = 20
        self.animation_delay_start = self.animation_delay
        self.animation_length = 6
        self.rect = pygame.Rect(0,0,200,300)
        self.rect.center = (x,y)
        self.rect_2 = pygame.Rect(0,0,200,300)
        self.rect_2.center = (x,y)
        self.rect_2.x += 200
        self.rect_2.y += 180

        self.map_x_location = x
        self.map_y_location = y

        
        #self.fire_circle_start_up()
        match level:
            case 'one':
                self.fire_circle_level_1 = Fire_ritual(rpg)
                self.fire_circle_level_1.fire_circle_start_up(x,y) # this is correct, i am testing something
                #self.fire_circle_level_1.fire_shape_start_up(rpg,x,y)
                #self.fire_circle_level_1.spawn_rocket(rpg,x,y)
                self.fire_distance_active = 10000
                self.armor = 80
                self.armor_old = self.armor
            case 'two':
                self.fire_circle_level_1 = Fire_ritual(rpg)
                self.fire_circle_level_1.fire_box_start_up(rpg,x,y)
                self.armor = 200
                self.armor_old = self.armor
            case 'three':
                self.fire_circle_level_1 = Fire_ritual(rpg)
                
                self.fire_circle_level_1.spawn_both(rpg,x,y)
                self.armor = 200
                self.armor_old = self.armor
            case 'four':
                self.fire_circle_level_1 = Fire_ritual(rpg)
                self.fire_circle_level_1.spawn_both(rpg,x,y)
                self.armor = 200
                self.armor_old = self.armor
            case 'five':
                self.fire_circle_level_1 = Fire_ritual(rpg)
                self.fire_circle_level_1.spawn_both(rpg,x,y)
                self.armor = 200
                self.armor_old = self.armor
            case 'six':
                self.fire_circle_level_1 = Fire_ritual(rpg)
                self.fire_circle_level_1.spawn_rocket(rpg,x,y)
                self.armor = 400
                self.armor_old = self.armor
        
        self.weakness_rect = pygame.Rect(0,0,250,250)
        self.weakness_rect.center = (x,y)

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
        self.surface_rect = self.surface.blit(self.image_list_right[0],(-50,0))
        self.V_x = 0
        self.V_y = 0
        self.dydt = 10
        self.dxdt = 10
        self.dVdt = random.randint(30,100)
        timer = random.randint(50,110)
        self.accelleration_timer = timer
        self.fire_attack_scale = 10
        self.x = self.rect.x
        self.y = self.rect.y
        self.health = 2 #300   # 120 is decent amount
        self.helper_list = []
        self.boss_attack_delay = self.animation_length
        self.boss_attack_timer = 10
        self.boss_attack_timer_old =self.boss_attack_timer
        if cut_scene == False:
            self.x_calc = rpg.player_1.rect.centerx - self.rect_2.centerx
            self.y_calc = rpg.player_1.rect.centery - self.rect_2.centery
        if cut_scene:
            self.x_calc = self.x_calc = rpg.cut_scene_player.rect.centerx - self.rect_2.centerx
            self.y_calc = self.y_calc = rpg.cut_scene_player.rect.centery - self.rect_2.centery
        self.hypotenuse_boss_player_1 = ((self.x_calc**2) +(self.y_calc**2))**0.5
        angle_to_calc = (-1)*( self.y_calc / self.hypotenuse_boss_player_1)
        self.angle_boss_player_1 = math.degrees(math.asin(angle_to_calc))
        self.x_amount =   10 # this is hypoenuse
        self.y_amount =   20
        self.alternate_death_method = False
        self.invoke_life = False
        self.invoke_knowledge = False
        self.invoke_war_attack = False # this will be for the new boss attack
        j = 0
        k = 30
        self.fireball_list_war_invoke =[]
        while j <= k:
            a = Projectile_class(rpg,3,1000000)
            a.fire_ball_rect.center = (x,y)
            a.mass = 0.1
            self.fireball_list_war_invoke.append(a)

            j += 1
        
        j = 0
        k = 60
        self.fireball_list_war_invoke_2 =[]
        while j <= k:
            a = Projectile_class(rpg,'smoke',100)
            a.fire_ball_rect.center = (x,y)
            a.mass = 0.01
            self.fireball_list_war_invoke_2.append(a)
            j += 1
        self.war_attack_active = False # this is for when you can see and be hurt by the fireballs
        self.war_attack_smoke_active = False
        self.war_attack_timer_active = 50
        self.war_attack_timer_active_old = self.war_attack_timer_active 

        self.reset_fireball_war_attack()
        self.reset_fireball()
        self.reset_fireball_x()


    def spawn_war_attack(self,rpg):
        """The war attack will be drawn on screen"""
        speed_scale = 10
        x_distance = (rpg.level_stuff.player_1.rect.centerx - self.rect_2.centerx) * speed_scale
        y_distance = (rpg.level_stuff.player_1.rect.centery - self.rect_2.centery) * speed_scale
        
        x_distance += (rpg.level_stuff.player_1.velocity[0] * 2)
        y_distance += (rpg.level_stuff.player_1.velocity[1] * 2)
        self.war_attack_timer_active = self.war_attack_timer_active_old

        n = 0
        m = len(self.fireball_list_war_invoke)
        self.war_attack_active = True
        a = random.choice([rpg.level_stuff.sound_logic.fire_sound_1,rpg.level_stuff.sound_logic.fire_sound_2])
        rpg.level_stuff.sound_logic.screach_sound.set_volume(rpg.settings_hold.max_volume)
        pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.screach_sound)
        pygame.mixer.Sound.play(a)
        
        while n < m:
            o = random.randrange(-50,50)
            p = random.randrange(-50,50)
            self.fireball_list_war_invoke[n].fire_ball_active = True
            self.fireball_list_war_invoke[n].hit_limit = 1
            self.fireball_list_war_invoke[n].fire_ball_animation_counter = 0
            self.fireball_list_war_invoke[n].fire_damage = self.fireball_list_war_invoke[n].fire_damage_old
            self.fireball_list_war_invoke[n].dv_dt[0] = x_distance 
            self.fireball_list_war_invoke[n].dv_dt[1] = y_distance 
            self.fireball_list_war_invoke[n].fire_ball_rect.x += o
            self.fireball_list_war_invoke[n].fire_ball_rect.y += p
            n += 1

        n = 0
        m = len(self.fireball_list_war_invoke_2)
        while n < m:
            o = random.randrange(-50,50)
            p = random.randrange(-50,50)
            self.fireball_list_war_invoke_2[n].fire_ball_active = True
            self.fireball_list_war_invoke_2[n].hit_limit = 1
            self.fireball_list_war_invoke_2[n].fire_ball_animation_counter = 0
            self.fireball_list_war_invoke_2[n].fire_damage = self.fireball_list_war_invoke_2[n].fire_damage_old
            self.fireball_list_war_invoke_2[n].dv_dt[0] = x_distance 
            self.fireball_list_war_invoke_2[n].dv_dt[1] = y_distance 
            self.fireball_list_war_invoke_2[n].fire_ball_rect.x += o
            self.fireball_list_war_invoke_2[n].fire_ball_rect.y += p
            n += 1
        
    def move_war_attack(self,rpg):
        """This moves the war attack."""
        if self.war_attack_active:
            i = 0
            j = len(self.fireball_list_war_invoke)
            #print('moving war attack')

            while i < j:
                self.fireball_list_war_invoke[i].update_speed_stats(rpg)
                self.fireball_list_war_invoke[i].fire_ball_rect.x += self.fireball_list_war_invoke[i].velocity[0] * rpg.dt
                self.fireball_list_war_invoke[i].fire_ball_rect.y += self.fireball_list_war_invoke[i].velocity[1] * rpg.dt
                i += 1

            i = 0
            j = len(self.fireball_list_war_invoke_2)
            #print('moving war attack')

            while i < j:
                self.fireball_list_war_invoke_2[i].update_speed_stats(rpg)
                self.fireball_list_war_invoke_2[i].fire_ball_rect.x += self.fireball_list_war_invoke_2[i].velocity[0] * rpg.dt
                self.fireball_list_war_invoke_2[i].fire_ball_rect.y += self.fireball_list_war_invoke_2[i].velocity[1] * rpg.dt
                i += 1
    
    def reset_fireball_war_attack(self):
        """This returns the fireball to its start and removes any velocity""" # this must  be called at first to stop it being in corner for first use.
        i = 0
        j = len(self.fireball_list_war_invoke)
        self.war_attack_active = False
        #print('resetting')
        while i < j:
            self.fireball_list_war_invoke[i].velocity[0] = 0
            self.fireball_list_war_invoke[i].velocity[1] = 0
            self.fireball_list_war_invoke[i].fire_ball_rect.center = self.rect.center
            self.fireball_list_war_invoke[i].fire_ball_rect.x += self.fireball_list_war_invoke[i].x_offset
            self.fireball_list_war_invoke[i].fire_ball_rect.y += self.fireball_list_war_invoke[i].y_offset
            i += 1
        i = 0
        j = len(self.fireball_list_war_invoke_2)
        self.war_attack_active = False
        #print('resetting')
        while i < j:
            self.fireball_list_war_invoke_2[i].velocity[0] = 0
            self.fireball_list_war_invoke_2[i].velocity[1] = 0
            self.fireball_list_war_invoke_2[i].fire_ball_rect.center = self.rect.center
            self.fireball_list_war_invoke_2[i].fire_ball_rect.x += self.fireball_list_war_invoke_2[i].x_offset
            self.fireball_list_war_invoke_2[i].fire_ball_rect.y += self.fireball_list_war_invoke_2[i].y_offset
            i += 1

    def draw_war_attack(self,rpg):
        """This draws the war attack on the screen."""
        if self.war_attack_active:
            self.war_attack_timer_active -= 1
            
            # fire is below
            i = 0
            j = len(self.fireball_list_war_invoke)
            while i < j:
                if self.fireball_list_war_invoke[i].fire_ball_active:
                    self.fireball_list_war_invoke[i].check_fire_hit(rpg)
                    self.screen.blit(self.fireball_list_war_invoke[i].fire_ball.surface_list[self.fireball_list_war_invoke[i].fire_ball_animation_counter],(self.fireball_list_war_invoke[i].fire_ball_rect))
                
                    self.fireball_list_war_invoke[i].fire_ball_animation_delay -= 1
                    if self.fireball_list_war_invoke[i].fire_ball_animation_delay <= 0:
                        self.fireball_list_war_invoke[i].fire_ball_animation_counter += 1
                        self.fireball_list_war_invoke[i].fire_ball_animation_delay = self.fireball_list_war_invoke[i].fire_ball_animation_delay_old
                    if self.fireball_list_war_invoke[i].fire_ball_animation_counter >= (len(self.fireball_list_war_invoke[i].fire_ball.surface_list)):
                        self.fireball_list_war_invoke[i].fire_ball_animation_counter = 0
                
                i += 1
            # smoke is below: _2 is smoke
            i = 0
            j = len(self.fireball_list_war_invoke_2)
            while i < j:
                if self.fireball_list_war_invoke_2[i].fire_ball_active:
                    #self.fireball_list_war_invoke_2[i].check_fire_hit(rpg)
                    self.screen.blit(self.fireball_list_war_invoke_2[i].fire_ball.surface_list[self.fireball_list_war_invoke_2[i].fire_ball_animation_counter],(self.fireball_list_war_invoke_2[i].fire_ball_rect))
                
                    self.fireball_list_war_invoke_2[i].fire_ball_animation_delay -= 1
                    if self.fireball_list_war_invoke_2[i].fire_ball_animation_delay <= 0:
                        self.fireball_list_war_invoke_2[i].fire_ball_animation_counter += 1
                        self.fireball_list_war_invoke_2[i].fire_ball_animation_delay = self.fireball_list_war_invoke_2[i].fire_ball_animation_delay_old
                    if self.fireball_list_war_invoke_2[i].fire_ball_animation_counter >= (len(self.fireball_list_war_invoke_2[i].fire_ball.surface_list)):
                        self.fireball_list_war_invoke_2[i].fire_ball_animation_counter = 0
                
                i += 1

    def boss_overlay(self,rpg):
        """This will show the boss health""" # this can be modified to add a weakness for certian situations.
        if self.hypotenuse_boss_player_1 <= 1000:
            color = int(self.health)
            color_2 = int(self.health) - 20
            if color > 120:
                color = 120
                color_2 = 100
            if color < 0 :
                color = 0
            if color_2 < 0:
                color_2 = 0
            pygame.draw.line(self.screen,(100,color,color_2),(self.rect_2.centerx - (2 * self.health/2),self.rect_2.centery - 50),(self.rect_2.centerx + (2 * self.health / 2),self.rect_2.centery - 50),20)

    def war_attack_loop(self,rpg):
        """This is the war attack code"""
        self.move_war_attack(rpg)
        self.draw_war_attack(rpg)
        if self.war_attack_timer_active <= 0:
            self.war_attack_timer_active = self.war_attack_timer_active_old
            self.war_attack_active = False # reset stuff too.
            self.reset_fireball_war_attack()



    def detect_collision_fire_circle_level_1(self,rpg):
        """This checks if the player walks inside the circle"""
        a = 0
        b = len(self.fire_circle_level_1.fire_circle_active_list) - 1
        
        while a <= b :
            collisions_test  = pygame.Rect.colliderect(self.fire_circle_level_1.rect_circle_spell_list[a],rpg.level_stuff.player_1.rect)
            if collisions_test:
                #print(a)
                if self.fire_circle_level_1.fire_circle_active_list[a] == False:
                    self.fire_circle_level_1.fire_circle_active_list[a] = True
                    self.armor -= 10
                    rpg.level_stuff.sound_logic.fire_crackle_sound.set_volume(rpg.settings_hold.max_volume)
                    pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.fire_crackle_sound)
                
            a += 1

    def delete_me(self,rpg):
        """deletes the enemy. The location change is nessecary for other code checking its location to not trigger."""
        rpg.level_stuff.player_1.score += self.score_value
        x = -10000
        y = -10000
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        del self

    def spawn_x_fireball(self,rpg):
        """This spawns the fireballs for an attack in an X shape"""
        if self.fireball_x_attack_active == False:
            self.fireball_x_attack_active = True
            a = random.choice([rpg.level_stuff.sound_logic.fire_sound_1,rpg.level_stuff.sound_logic.fire_sound_2])
            rpg.level_stuff.sound_logic.fire_sound_1.set_volume(rpg.settings_hold.max_volume)
            rpg.level_stuff.sound_logic.fire_sound_2.set_volume(rpg.settings_hold.max_volume)
            rpg.level_stuff.sound_logic.bang_sound_1.set_volume(rpg.settings_hold.max_volume)
            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.bang_sound_1)
            pygame.mixer.Sound.play(a)
            # this now activated the fireballs
            i = 0
            j = len(self.fireball_list_x)
            while i < j:
                """This sets them all active"""
                r = random.uniform(500,4000)
                s = random.choice([-1,1])
                s2 = random.choice([-1,1])
                self.fireball_list_x[i].fire_ball_active = True
                self.fireball_list_x[i].hit_limit = 1
                self.fireball_list_x[i].fire_ball_animation_counter = 0
                self.fireball_list_x[i].fire_damage = self.fireball_list_x[i].fire_damage_old
                self.fireball_list_x[i].dv_dt[0] +=  r * s
                self.fireball_list_x[i].dv_dt[1] +=  r * s2
                i += 1

    def spawn_fireball(self,rpg):
        """This spawns the fireball for an attack by the boss."""
        if self.fire_ball_limit > 0:
            self.fire_active_1  = True
            a = random.choice([rpg.level_stuff.sound_logic.fire_sound_1,rpg.level_stuff.sound_logic.fire_sound_2])
            
            x_distance = rpg.level_stuff.player_1.rect.centerx - self.rect_2.centerx
            y_distance = rpg.level_stuff.player_1.rect.centery - self.rect_2.centery
            self.hypotenuse_boss_player_1 = ((self.x_calc**2) +(self.y_calc**2))**0.5
            angle_to_calc = ( self.y_calc / self.hypotenuse_boss_player_1)
            self.angle_boss_player_1 = math.degrees(math.asin(angle_to_calc))

            sound_volume =  (0.2 + (1/self.hypotenuse_boss_player_1))
            sound_volume = sound_volume * 100
            if sound_volume > 1:
                sound_volume = 1
            if sound_volume < 0:
                sound_volume = 0
            rpg.level_stuff.sound_logic.bang_sound_1.set_volume(sound_volume)
            rpg.level_stuff.sound_logic.fire_sound_1.set_volume(rpg.settings_hold.max_volume)
            rpg.level_stuff.sound_logic.fire_sound_2.set_volume(rpg.settings_hold.max_volume)
            rpg.level_stuff.sound_logic.bang_sound_1.set_volume(rpg.settings_hold.max_volume)
            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.bang_sound_1)
            pygame.mixer.Sound.play(a)

            i = 0
            j = len(self.fireball_list)
            while i < j:
                """This sets them all active"""
                r = random.uniform(0.5,2)
                s = random.uniform(0.5,2)
                self.fireball_list[i].fire_ball_active = True
                self.fireball_list[i].hit_limit = 1
                self.fireball_list[i].fire_ball_animation_counter = 0
                self.fireball_list[i].fire_damage = self.fireball_list[i].fire_damage_old
                self.fireball_list[i].dv_dt[0] += x_distance * self.fire_attack_scale * r
                self.fireball_list[i].dv_dt[1] += y_distance * self.fire_attack_scale * s
                i += 1

    def move_fireball(self,rpg):
        """This will move the fireball"""
        if self.fire_active_1  == True:
            x_distance = rpg.level_stuff.player_1.rect.centerx - self.fireball_list[1].fire_ball_rect.centerx
            y_distance = rpg.level_stuff.player_1.rect.centery - self.fireball_list[1].fire_ball_rect.centery
            hypotenuse_fireball_player_1 = ((x_distance**2) +(y_distance**2))**0.5
            sound_volume =  (1/hypotenuse_fireball_player_1)
            sound_volume = sound_volume * 100
            if sound_volume > 1:
                sound_volume = 1
            if sound_volume < 0:
                sound_volume = 0
            i = 0
            j = len(self.fireball_list)
            rpg.level_stuff.sound_logic.fire_sound_1.set_volume(sound_volume)
            rpg.level_stuff.sound_logic.fire_sound_2.set_volume(sound_volume)
            
            while i < j:
                self.fireball_list[i].update_speed_stats(rpg)
                self.fireball_list[i].fire_ball_rect.x += self.fireball_list[i].velocity[0] * rpg.dt
                self.fireball_list[i].fire_ball_rect.y += self.fireball_list[i].velocity[1] * rpg.dt
                i += 1
            
    def reset_fireball(self):
        """This returns the fireball to its start and removes any velocity"""
        i = 0
        j = len(self.fireball_list)
        while i < j:
            """This sets them all active"""
            self.fireball_list[i].velocity[0] = 0
            self.fireball_list[i].velocity[1] = 0
            self.fireball_list[i].fire_ball_rect.center = self.rect.center
            self.fireball_list[i].fire_ball_rect.x += self.fireball_list[i].x_offset
            self.fireball_list[i].fire_ball_rect.y += self.fireball_list[i].y_offset
            i += 1

    def reset_fireball_x(self):
        """"""
        i = 0
        j = len(self.fireball_list_x)
        while i < j:
            """This sets them all active"""
            self.fireball_list_x[i].velocity[0] = 0
            self.fireball_list_x[i].velocity[1] = 0
            self.fireball_list_x[i].fire_ball_rect.center = self.rect.center
            self.fireball_list_x[i].fire_ball_rect.x += self.fireball_list_x[i].x_offset
            self.fireball_list_x[i].fire_ball_rect.y += self.fireball_list_x[i].y_offset
            i += 1
    
    def fireball_check_and_draw(self,rpg):
        """This checks for the activity of fireball and draws it on screen if its active"""
        if self.fire_active_1  == True:
            self.move_fireball(rpg)
            i = 0
            j = len(self.fireball_list)
            while i < j:
                """This sets them all active"""
                if self.fireball_list[i].fire_ball_active:
                    self.fireball_list[i].check_fire_hit(rpg)
                    self.screen.blit(self.fireball_list[i].fire_ball.surface_list[self.fireball_list[i].fire_ball_animation_counter],(self.fireball_list[i].fire_ball_rect))
                    self.fireball_list[i].fire_ball_animation_delay -= 1
                    if self.fireball_list[i].fire_ball_animation_delay <= 0:
                        self.fireball_list[i].fire_ball_animation_counter += 1
                        self.fireball_list[i].fire_ball_animation_delay = self.fireball_list[i].fire_ball_animation_delay_old
                    if self.fireball_list[i].fire_ball_animation_counter >= (len(self.fireball_list[i].fire_ball.surface_list)):
                        self.fireball_list[i].fire_ball_animation_counter = 0
                i += 1

    def move_fireball_x(self,rpg):
        """This will move the fireball"""
        if self.fireball_x_attack_active == True:
            i = 0
            j = len(self.fireball_list_x)
            while i < j:
                self.fireball_list_x[i].update_speed_stats(rpg)
                self.fireball_list_x[i].fire_ball_rect.x += self.fireball_list_x[i].velocity[0] * rpg.dt
                self.fireball_list_x[i].fire_ball_rect.y += self.fireball_list_x[i].velocity[1] * rpg.dt
                i += 1
    
    def fireball_x_check_and_draw(self,rpg):
        """This checks for the activity of fireball and draws it on screen if its active"""
        if self.fireball_x_attack_active  == True:
            self.move_fireball_x(rpg)
            i = 0
            j = len(self.fireball_list_x)
            while i < j:
                """This sets them all active"""
                if self.fireball_list_x[i].fire_ball_active:
                    #self.fireball_list_x[i].check_fire_hit(rpg)
                    self.fireball_list_x[i].check_fire_hit(rpg)
                    self.screen.blit(self.fireball_list_x[i].fire_ball.surface_list[self.fireball_list_x[i].fire_ball_animation_counter],(self.fireball_list_x[i].fire_ball_rect))
                    self.fireball_list_x[i].fire_ball_animation_delay -= 1
                    if self.fireball_list_x[i].fire_ball_animation_delay <= 0:
                        self.fireball_list_x[i].fire_ball_animation_counter += 1
                        self.fireball_list_x[i].fire_ball_animation_delay = self.fireball_list_x[i].fire_ball_animation_delay_old
                    if self.fireball_list_x[i].fire_ball_animation_counter >= (len(self.fireball_list_x[i].fire_ball.surface_list)):
                        self.fireball_list_x[i].fire_ball_animation_counter = 0
                i += 1

    def draw_circle_spots(self,rpg):
        """This draws the fire in a 6 pointes circle around the boss"""
        i = 0
        j = len(self.fire_circle_level_1.rect_circle_spell_list) - 1
        while i <= j:
            #print(i)
            #print(len(self.rect_circle_spell_list))
            if self.hypotenuse_boss_player_1 >= self.fire_distance_active: # this hides the circle if far away
                self.fire_circle_level_1.fire_circle_active_list[i] = False
                self.armor = 80
                self.armor_old = self.armor
            if self.fire_circle_level_1.fire_circle_active_list[i] == True:
                #pygame.draw.circle(self.screen,'red',(self.rect_circle_spell_list[i].centerx,self.rect_circle_spell_list[i].centery),50)
                self.screen.blit(self.fire_circle_level_1.fire_circle.surface_list[self.fire_circle_level_1.fire_circle_animation_counter_list[i]],self.fire_circle_level_1.rect_circle_spell_list[i].center)
                self.fire_circle_level_1.animation_circle_delay_list[i] -= 1
                if self.fire_circle_level_1.animation_circle_delay_list[i] <= 0:
                    self.fire_circle_level_1.fire_circle_animation_counter_list[i] += 1
                    self.fire_circle_level_1.animation_circle_delay_list[i] =self.fire_circle_level_1.animation_circle_delay_old_list[i]
                if self.fire_circle_level_1.fire_circle_animation_counter_list[i] >= self.fire_circle_level_1.fire_circle_animation_limit_list[i]:
                    self.fire_circle_level_1.fire_circle_animation_counter_list[i] = 0
            i += 1

    def draw_me_for_cut_scene_1(self,rpg):
        """draws the boss from the surface to the screen. """
       
        self.screen.blit(self.sprite_enemy.surface_list[34],(self.rect))
        
    def drawing_stuff(self,rpg):
        """Holds the draw specific stuff"""
        self.x_calc = rpg.level_stuff.player_1.rect.centerx - self.rect_2.centerx
        self.y_calc = rpg.level_stuff.player_1.rect.centery - self.rect_2.centery
        self.hypotenuse_boss_player_1 = ((self.x_calc**2) +(self.y_calc**2))**0.5
        angle_to_calc = ( self.y_calc / self.hypotenuse_boss_player_1)
        self.angle_boss_player_1 = math.degrees(math.asin(angle_to_calc))
        self.x_rect = pygame.Rect(0,0,abs(self.x_amount),10)
        self.y_rect = pygame.Rect(0,0,10,abs(self.y_amount))
        self.x_rect.topleft = self.rect_2.center
        self.y_rect.topleft = self.rect_2.center
        self.check_boss_health(rpg)
                       
        if self.fire_active_1:
            self.fireball_list[0].fire_ball_lifespan -= 1
        if self.fireball_list[0].fire_ball_lifespan <= 0:
            self.fireball_list[0].fire_ball_lifespan = self.fireball_list[0].fire_ball_lifespan_old
            self.fire_active_1 = False
            self.reset_fireball()
        if self.fireball_x_attack_active:
            self.fireball_list_x[0].fire_ball_lifespan -= 1
        if self.fireball_list_x[0].fire_ball_lifespan <= 0:
            self.fireball_list_x[0].fire_ball_lifespan = self.fireball_list_x[0].fire_ball_lifespan_old
            self.fireball_x_attack_active = False
            self.reset_fireball_x()

        if self.animation_counter >= len(self.sprite_enemy.surface_list):
            self.animation_counter = len(self.sprite_enemy.surface_list) - 1
        if self.hypotenuse_boss_player_1 <= 1000: 
                    
            self.fireball_list[0].fire_ball_countdown -= 1
            if self.fireball_list[0].fire_ball_countdown == 30:
                rpg.level_stuff.sound_logic.splat_rev_sound.set_volume(rpg.settings_hold.max_volume)

                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.splat_rev_sound)
            if self.fireball_list[0].fire_ball_countdown <= 0:
                
                self.a = random.choice([0,1])
                if self.invoke_war_attack:
                    self.a = random.choice([0,1,2,2,2])
                if self.a == 0:
                    self.spawn_x_fireball(rpg) # i added this, it needs testing. this line may be casuing a bug if this is read later. 2/19/25 # i dont think there is a bug. 6/14/25
                if self.a == 1:
                    self.spawn_fireball(rpg)
                if self.a == 2:
                    self.spawn_war_attack(rpg)
                self.fireball_list[0].fire_ball_countdown = self.fireball_list[0].fire_ball_countdown_old

    def check_boss_health(self,rpg):
        """This checks the health of the boss.""" # this works for when alternate ddeath method is false. when true needs to be added next. 
        if self.health <= 0 and self.alternate_death_method == False:    # this is where the boss dies i need to make it a function soon # i must remake this into a function now.
            #rpg.campagne_mode = False
            rpg.loading_screen.draw_loading_screen()
            pygame.display.update()
            self.delete_me(rpg)
            if rpg.level_stuff.level_1:
                if self.one_switch:
                    rpg.level_stuff.first_to_second_level_switch(rpg)
                    self.one_switch = False
                    #print('level 1 switch')
            if rpg.level_stuff.level_2:
                if self.one_switch:
                    self.one_switch = False
                    rpg.level_stuff.second_to_third_level_switch(rpg)
                    #print('level 2 switch')
            if rpg.level_stuff.level_3:
                if self.one_switch:
                    rpg.level_stuff.third_to_fourth_level_switch(rpg)
                    self.one_switch = False
                    #print('level 3 switch')
            if rpg.level_stuff.level_4:
                if self.one_switch:
                    rpg.level_stuff.fourth_to_fifth_level_switch(rpg)
                    self.one_switch = False
            if rpg.level_stuff.level_5:
                if self.one_switch:
                    rpg.level_stuff.fifth_to_sixth_level_switch(rpg)
                    self.one_switch = False
            if rpg.level_stuff.level_6:
                if self.one_switch:
                    rpg.high_score_stuff.add_score(rpg.level_stuff.player_1.score)
                    rpg.win_game_screen = True
                    rpg.campagne_mode = False
                    self.one_switch = False
        
        if self.health <= 0 and self.alternate_death_method:    # this is where the boss dies i need to make it a function soon # i must remake this into a function now.
            #rpg.campagne_mode = False
            if rpg.level_stuff.player_1.health <= 0:
                self.delete_me(rpg)
                if rpg.level_stuff.level_1:
                    if self.one_switch:
                        rpg.level_stuff.first_to_second_level_switch(rpg)
                        self.one_switch = False
                        #print('level 1 switch')
                if rpg.level_stuff.level_2:
                    if self.one_switch:
                        self.one_switch = False
                        rpg.level_stuff.second_to_third_level_switch(rpg)
                        #print('level 2 switch')
                if rpg.level_stuff.level_3:
                    if self.one_switch:
                        rpg.level_stuff.third_to_fourth_level_switch(rpg)
                        self.one_switch = False
                        #print('level 3 switch')
                if rpg.level_stuff.level_4:
                    if self.one_switch:
                        rpg.level_stuff.fourth_to_fifth_level_switch(rpg)
                        self.one_switch = False
                if rpg.level_stuff.level_5:
                    if self.one_switch:
                        rpg.level_stuff.fifth_to_sixth_level_switch(rpg)
                        self.one_switch = False
                if rpg.level_stuff.level_6:
                    if self.one_switch:
                        rpg.high_score_stuff.add_score(rpg.level_stuff.player_1.score)
                        rpg.win_game_screen = True
                        rpg.campagne_mode = False
                        self.one_switch = False

    def draw_me(self,rpg):
        """draws the boss from the surface to the screen. """
        
        self.drawing_stuff(rpg)
        #pygame.draw.rect(self.screen,(200,0,0),self.weakness_rect)
        self.screen.blit(self.sprite_enemy.surface_list[self.animation_counter],(self.rect))
        #pygame.draw.rect(self.screen,(0,200,200),self.weakness_rect)
        self.detect_collision_fire_circle_level_1(rpg)
        self.boss_overlay(rpg)
        self.draw_circle_spots(rpg)
        self.fireball_check_and_draw(rpg)
        self.fireball_x_check_and_draw(rpg)
        self.war_attack_loop(rpg)
    
    def check_direct_attack_hit(self,rpg):
        """""" # 0up , 10 left, 20 down, 30 right,
        if self.animation_counter == 2:
            #pygame.draw.rect(self.screen,'purple',self.rect_attack_up)
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_up,rpg.level_stuff.player_1.rect)
            if collisions_test:
                if self.hit_limit > 0:
                    
                    rpg.level_stuff.player_1.velocity[1] -= self.hit_1_knockback
                    # must add damage armor check. will set damage as its own stat?
                    if self.hit_1_damage > rpg.level_stuff.player_1.armor:
                        rpg.level_stuff.player_1.health -= self.hit_1_damage
                        rpg.overlay.create_damage_for_overlay(self.hit_1_damage,self.rect_attack_up.center,'red')
                        rpg.level_stuff.sound_logic.player_hit_sound.set_volume(rpg.settings_hold.max_volume)
                        pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_hit_sound)
                        self.hit_limit -=1
        if self.animation_counter == 12:
            #pygame.draw.rect(self.screen,'yellow',self.rect_attack_left)
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_left,rpg.level_stuff.player_1.rect)
            if collisions_test:
                if self.hit_limit > 0:
                    if self.hit_1_damage > rpg.level_stuff.player_1.armor:
                        rpg.level_stuff.player_1.velocity[0] -= self.hit_1_knockback
                        rpg.level_stuff.player_1.health -= self.hit_1_damage
                        rpg.overlay.create_damage_for_overlay(self.hit_1_damage,self.rect_attack_left.center,'red')
                        rpg.level_stuff.sound_logic.player_hit_sound.set_volume(rpg.settings_hold.max_volume)
                        pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_hit_sound)
                        self.hit_limit -=1
        if self.animation_counter == 22:
            #pygame.draw.rect(self.screen,'red',self.rect_attack_down)
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_down,rpg.level_stuff.player_1.rect)
            if collisions_test:
                if self.hit_limit > 0:
                    if self.hit_1_damage > rpg.level_stuff.player_1.armor:
                        rpg.level_stuff.player_1.velocity[1] += self.hit_1_knockback
                        rpg.level_stuff.player_1.health -= self.hit_1_damage
                        rpg.overlay.create_damage_for_overlay(self.hit_1_damage,self.rect_attack_down.center,'red')
                        rpg.level_stuff.sound_logic.player_hit_sound.set_volume(rpg.settings_hold.max_volume)
                        pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_hit_sound)
                        self.hit_limit -=1
        if self.animation_counter == 32:
            #pygame.draw.rect(self.screen,'green',self.rect_attack_right)
            collisions_test  = pygame.Rect.colliderect(self.rect_attack_right,rpg.level_stuff.player_1.rect)
            if collisions_test:
                if self.hit_limit > 0:
                    if self.hit_1_damage > rpg.level_stuff.player_1.armor:
                        rpg.level_stuff.player_1.velocity[0] += self.hit_1_knockback
                        rpg.level_stuff.player_1.health -= self.hit_1_damage
                        rpg.overlay.create_damage_for_overlay(self.hit_1_damage,self.rect_attack_right.center,'red')
                        rpg.level_stuff.sound_logic.player_hit_sound.set_volume(rpg.settings_hold.max_volume)
                        pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_hit_sound)
                        self.hit_limit -=1
        
    def set_animation_direction(self,rpg):
        """This will make the animation face in the correct direction.
        It will also make the animation count through a loop"""
        self.x_calc = rpg.level_stuff.player_1.rect.centerx - self.rect_2.centerx
        self.y_calc = rpg.level_stuff.player_1.rect.centery - self.rect_2.centery
        self.hypotenuse_boss_player_1 = ((self.x_calc**2) +(self.y_calc**2))**0.5
        angle_to_calc = (-1)*( self.y_calc / self.hypotenuse_boss_player_1)
        self.angle_boss_player_1 = math.degrees(math.asin(angle_to_calc))
        if self.attack == False:
            if self.x_calc >= 0:
                if 0 <= self.angle_boss_player_1 <= 45:
                    self.animation_counter = 34
                    self.animation_counter_old = self.animation_counter 
                    self.weakness_rect.center = self.rect_attack_left.center
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < self.angle_boss_player_1 <= 90:
                    self.animation_counter = 4
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_down.center
                if -45 <= self.angle_boss_player_1 < 0:
                    self.animation_counter = 34
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_left.center
                if -90 <= self.angle_boss_player_1 < -45:
                    self.animation_counter = 24
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_up.center
            if self.x_calc < 0:
                if 0 <= self.angle_boss_player_1 <= 45:
                    self.animation_counter = 14
                    self.animation_counter_old = self.animation_counter 
                    self.weakness_rect.center = self.rect_attack_right.center
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < self.angle_boss_player_1 <= 90:
                    self.animation_counter = 4
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_down.center
                if -45 <= self.angle_boss_player_1 < 0:
                    self.animation_counter = 14
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_right.center
                if -90 <= self.angle_boss_player_1 < -45:
                    self.animation_counter = 24
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_up.center
        if self.attack == True:
            #self.check_direct_attack_hit(rpg)
            if self.x_calc >= 0:
                if 0 <= self.angle_boss_player_1 <= 45:
                    self.animation_counter = 30
                    self.animation_counter_old = self.animation_counter 
                    self.weakness_rect.center = self.rect_attack_left.center
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < self.angle_boss_player_1 <= 90:
                    self.animation_counter = 0
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_down.center
                if -45 <= self.angle_boss_player_1 < 0:
                    self.animation_counter = 30
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_left.center
                if -90 <= self.angle_boss_player_1 < -45:
                    self.animation_counter = 20
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_up.center
            if self.x_calc < 0:
                if 0 <= self.angle_boss_player_1 <= 45:
                    self.animation_counter = 10
                    self.animation_counter_old = self.animation_counter 
                    self.weakness_rect.center = self.rect_attack_right.center
                    # 4up , 14 left, 24 down, 34 right, 
                if 45 < self.angle_boss_player_1 <= 90:
                    self.animation_counter = 0
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_down.center
                if -45 <= self.angle_boss_player_1 < 0:
                    self.animation_counter = 10
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_right.center
                if -90 <= self.angle_boss_player_1 < -45:
                    self.animation_counter = 20
                    self.animation_counter_old = self.animation_counter
                    self.weakness_rect.center = self.rect_attack_up.center

    def boss_check(self,rpg):
        """This holds the boss loop and activities"""
        rpg.level_stuff.physics_active.update_boss(rpg)
    
        if self.boss_attack_timer > 0:
            if self.attack == False:
                self.set_animation_direction(rpg)
                self.boss_attack_delay = self.animation_length
                #attack gets triggered to start
                self.boss_attack_timer -= 1
            if self.attack == True:
                self.check_direct_attack_hit(rpg)
                #pygame.mixer.Sound.play(rpg.bite_attack_sound)
                self.boss_attack_delay -= 1
                if self.attack_count < self.animation_lenth_attack_1:
                    self.delay_1 -=1
                    if self.delay_1 <= 0:
                        self.attack_count += 1
                        self.animation_counter += 1
                        self.delay_1 = self.delay_1_old
                if self.attack_count >= self.animation_lenth_attack_1:
                    self.attack = False
                    self.attack_count = 0
        if self.boss_attack_timer <=0:
            """then the boss attacks"""
            #pygame.mixer.Sound.play(rpg.bite_attack_sound)            
            self.attack = True
            self.hit_limit = self.hit_limit_old
            #self.boss_attack_primary(rpg)
            self.set_animation_direction(rpg)
            self.boss_attack_delay = self.animation_lenth_attack_1
            self.boss_attack_timer = self.boss_attack_timer_old
            if self.hypotenuse_boss_player_1 <= 1200:
                rpg.level_stuff.sound_logic.bite_sound.set_volume(rpg.settings_hold.max_volume)
                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.bite_sound)
    
    def boss_attack_primary(self,rpg):
        """This is the bosses primary attack"""
        self.set_animation_direction(rpg)

class Wolf_boss():
    """This is the overall wolf boss class. its holds the logic for wolf bosses. """

    def __init__(self,rpg,location,number_of_wolves):
        """"""
        self.one_switch = True
        self.health = 100
        self.score_value = 266
        #Physics_stats.__init__(self,rpg)
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        #super().__init__(rpg,location)

        self.rect = pygame.Rect(0,0,200,300)
        #self.rect.center = (x,y)
        self.rect_2 = pygame.Rect(0,0,200,300)
        #self.rect_2.center = (x,y)
        self.rect_2.x += 200
        self.rect_2.y += 180

        #rpg.level_stuff.boss_type = 'wolf'
        self.wolf_list = []

        n = 0

        self.map_x_location = location[0]
        self.map_y_location = location[1]

        m = number_of_wolves 
        while n <= m:
            a = Wolf(rpg,((location[0] + random.randint(-400,400)),(location[1] + random.randint(-400,400))),'boss')
            a.load_and_rescale_wolf("_internal\\img\\wolf_1_cropped_side.png",2)
            #a.rect_picture.centerx = (location[0] + random.randint(-400,400))
            #a.rect_picture.centery = (location[1] + random.randint(-400,400))
            self.wolf_list.append(a)
            n += 1

    def delete_me(self,rpg):
        """deletes the enemy. The location change is nessecary for other code checking its location to not trigger."""
        rpg.level_stuff.player_1.score += self.score_value
        x = -10000
        y = -10000
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        del self

    def check_for_end_of_boss(self,rpg):
        """This checks to see if all the wolves have been defeated."""  
        if len(self.wolf_list) == 0:
            """The boss is defeated."""
            
            #self.delete_me(rpg)
            if rpg.level_stuff.level_1:
                if self.one_switch:
                    rpg.level_stuff.first_to_second_level_switch(rpg)
                    self.one_switch = False
                    #print('level 1 switch')
            if rpg.level_stuff.level_2:
                if self.one_switch:
                    self.one_switch = False
                    rpg.level_stuff.second_to_third_level_switch(rpg)
                        #print('level 2 switch')
            if rpg.level_stuff.level_3:
                if self.one_switch:
                    rpg.level_stuff.third_to_fourth_level_switch(rpg)
                    self.one_switch = False
                        #print('level 3 switch')
            if rpg.level_stuff.level_4:
                if self.one_switch:
                    rpg.level_stuff.fourth_to_fifth_level_switch(rpg)
                    self.one_switch = False
            if rpg.level_stuff.level_5:
                if self.one_switch:
                    rpg.level_stuff.fifth_to_sixth_level_switch(rpg)
                    self.one_switch = False
            if rpg.level_stuff.level_6:
                if self.one_switch:
                    rpg.high_score_stuff.add_score(rpg.level_stuff.player_1.score)
                    rpg.win_game_screen = True
                    rpg.campagne_mode = False
                    self.one_switch = False
                
            
    def draw_wolves_for_boss(self,rpg):

        self.check_for_end_of_boss(rpg)
        self.n_for_draw = 0
        self.m_for_draw = len(self.wolf_list) - 1
        #print(m)

        while self.n_for_draw <= self.m_for_draw:
            self.wolf_list[self.n_for_draw].update_speed_stats(rpg)
            self.wolf_list[self.n_for_draw].draw_me(rpg)
            self.n_for_draw += 1

    



