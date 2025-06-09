
from pygame.sprite import Sprite
from  polygon_parametric import Create_polygon
from physics_stats import Physics_stats
import random
import math
import pygame


class Particle(Sprite,Physics_stats):
    """this is a class that allows particles to exist for various reasons. """

    def __init__(self,rpg,cut_scene,total):
        """This will initialize the particle in game. it will have a location and stuff"""
        Physics_stats.__init__(self,rpg)
        super().__init__()
        self.screen_rect = rpg.screen.get_rect()
        self.screen = rpg.screen
        self.mass = 1
        self.damage = 10
        self.damage_start = self.damage
        
        self.drag = 0.1
        self.friction_threshold = 0.1
        self.lifespan = 200
        self.particle_alive = True
        self.speed_animation_2 = 1/2
        self.speed_animation = self.speed_animation_2
        self.speed_animation_start = self.speed_animation
        self.draw_me = False
        self.animation_active = False
        self.distance_x = 0
        self.distance_y = 0
        self.particle_creation = True
        self.particle_heartbeat = 1000
        self.start_location_x = self.screen_rect.centerx  - 45 # i will try 45
        self.start_location_y = self.screen_rect.centery - 70
        self.shape_2_counter = 500
        self.particle_damage = 15
        
        if cut_scene:
            """then change its location"""
            m = random.randrange(0,total*2)
            number = math.pi / ((total + 1)/2)
            
            x_adjust = 200 * math.cos(  (number * m))
            
            y_adjust = 200 * (math.sin( (number * m)))
            
            self.start_location_x = x_adjust + 500
            self.start_location_y = y_adjust + 500

        self.particle_x_location = self.start_location_x
        self.particle_y_location = self.start_location_y
        

        self.post_hit_particle_active = False
        self.post_hit_particle__timer = 45
        self.post_hit_particle__timer_old = self.post_hit_particle__timer

        self.cut_scene_timer_active_countdown = 120
        self.cut_scene_timer_active_countdown_old = self.cut_scene_timer_active_countdown
        self.cut_scene_particle_active = False
        
        
            
        self.post_impact_particle_list = []
        q = 0
        r = 10
        while q < r:
            """creates the particles for post impact."""
            #print('starting')
            s = Create_polygon(rpg,cut_scene=cut_scene)
            try:
                #print('try load')
                s.load_first_shape('small')
                #print('load')
            except:
                s.create_first_shape('small')
                #print('create small')
            self.post_impact_particle_list.append(s)
            #print('creating list')
            q += 1

        
        self.speed_scale = 6
        #print('before')
        self.particle_1 = Create_polygon(rpg,cut_scene=cut_scene)
        #self.particle_1.create_third_shape()
        #print('after')
        try:
            self.particle_1.load_first_shape('big')
        except:
            self.particle_1.create_first_shape('big')
        #self.particle_1.create_second_shape_new()
        self.rect = self.particle_1.polygon_surface.get_rect(center=(self.particle_x_location,self.particle_y_location))
        #try_particle = pygame.draw.polygon(self.screen,color=(red,green,blue),points=self.test.nested_polygon_list[self.counter_test])
        
        self.particle_animation_counter = 0
        self.particle_counter_animation_limit = len(self.particle_1.nested_polygon_list) - 1
        #self.particle_rect = self.particle_1.polygon_surface.get_rect()

        # this is the variables used by a particle. in theory. 

        # adding a shadow here.

        self.shadow_surface = pygame.Surface((50,50), pygame.SRCALPHA)
        self.shadow_rect = self.shadow_surface.get_rect()
        self.shadow_surface.set_colorkey((0,255,0))
        self.shadow_surface.fill((0,255,0))
        #pygame.draw.ellipse(self.shadow_surface,(2, 48, 32,150),self.shadow_rect)
        pygame.draw.ellipse(self.shadow_surface,(2,48,32,150),self.shadow_rect)

    def set_particle_active_cut_scene(self,x_acc,y_acc):
        self.post_hit_particle__timer = self.post_hit_particle__timer_old
        self.cut_scene_particle_active = True
        self.velocity[0] = x_acc
        self.velocity[1] = y_acc

    def check_particle(self,rpg):
        """this draws the particle and proves its possible to move it. the while loop moves it. the draw makes it appear on screen."""
        self.draw_post_hit_particles(rpg)
        self.player_movement_particle(rpg)
        if -1 < self.velocity[0] < 1:
                    if -1 < self.velocity[1] < 1:
                        if self.draw_me == True:
                            self.reset_particle(rpg)
                            self.draw_me = False
                            self.velocity[0] = 0
                            self.velocity[1] = 0
                            return
        if self.draw_me == True:
            self.particle_heartbeat -= 1
            if self.particle_heartbeat <= 0:
                self.reset_particle(rpg)
                self.particle_heartbeat = 1000
            self.change_velocity(rpg)
            self.move_particle(rpg)
            self.particle_x_location = int(self.particle_x_location)
            self.particle_y_location = int(self.particle_y_location)
            

            #rpg.screen.blit(self.particle_1.surface_list[self.shape_2_counter],(self.particle_x_location,self.particle_y_location))
            rpg.screen.blit(self.shadow_surface,(self.particle_x_location + 10,self.particle_y_location + 10))
            rpg.screen.blit(self.particle_1.polygon_surface,(self.particle_x_location,self.particle_y_location))

            
            self.shape_2_counter -= 1
            if self.shape_2_counter <= 450:
                self.shape_2_counter = 450
    # that had to be set to surface to list work for the particle 2 new. for particle 3, it was the self.polygon surface

    def move_particle_for_cut_scene(self,rpg):
        """This moves the particle for the cut scene"""
        
        if self.cut_scene_particle_active == True:
            
            
            self.particle_x_location += self.velocity[0] * rpg.dt
            self.particle_1.rect.x += self.velocity[0] * rpg.dt
                
              
            self.particle_y_location += self.velocity[1] * rpg.dt
            self.particle_1.rect.y += self.velocity[1] * rpg.dt


            self.cut_scene_timer_active_countdown -= 1
            if self.cut_scene_timer_active_countdown <= 0:
                """Then particle explodes"""
                self.accellerate_post_hit_particles(rpg)
                self.cut_scene_timer_active_countdown = self.cut_scene_timer_active_countdown_old
                self.post_hit_particle_active = True
                self.reset_particle_cut_scene(rpg)


    def move_particle(self,rpg):
        """"""
        
        if self.draw_me == True:
            rpg.level_stuff.player_1.check_particle_hit(rpg)
            rpg.overlay.display_attack_2 = False
            self.particle_x_location += self.velocity[0] * rpg.dt
            self.particle_1.rect.x += self.velocity[0] * rpg.dt
            
            self.particle_y_location += self.velocity[1] * rpg.dt
            self.particle_1.rect.y += self.velocity[1] * rpg.dt
    
    def draw_particle_for_cut_scene(self,rpg):
        """This draws the particle for a cut scene"""
        self.move_particle_for_cut_scene(rpg)
        if self.post_hit_particle_active == False:
            if self.cut_scene_particle_active:
                rpg.screen.blit(self.particle_1.polygon_surface,(self.particle_x_location,self.particle_y_location))
                self.change_velocity(rpg)
        if self.post_hit_particle_active:
            self.draw_post_hit_particles_for_cut_scene(rpg)

    def reset_particle_cut_scene(self,rpg):
        """This resets the particle for the cut scene"""
        self.particle_x_location = self.start_location_x
        self.particle_y_location = self.start_location_y
        self.particle_1.rect.x = self.start_location_x
        self.particle_1.rect.y = self.start_location_y
        self.velocity[0] = 0
        self.velocity[1] = 0

    def reset_particle(self,rpg):
        """"""
        rpg.overlay.display_attack_2 = True
        self.particle_x_location = self.start_location_x
        self.particle_y_location = self.start_location_y
        self.particle_1.rect.x = self.start_location_x
        self.particle_1.rect.y = self.start_location_y
        self.velocity[0] = 0
        self.velocity[1] = 0
        self.shape_2_counter = 500
        self.damage = self.damage_start
        
        
     

    def player_movement_particle(self,rpg):
        """"""     
        
        if self.draw_me == True:
            
            self.particle_y_location -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            self.particle_1.rect.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
        
            self.particle_x_location -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            self.particle_1.rect.x -= rpg.level_stuff.player_1.velocity[0]* rpg.dt

        if self.post_hit_particle_active == True:
            #print('adjust')
            q = 0
            r = len(self.post_impact_particle_list) - 1
            while q <= r:
                
                
                self.post_impact_particle_list[q].rect.x -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
                self.post_impact_particle_list[q].rect.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
                q += 1



    def change_velocity(self,rpg):
        """"""
        #velocity = rpg.moving_right + rpg.moving_left + rpg.moving_up + rpg.moving_down
        
        if  self.velocity[0] > 0.1 or self.velocity[0] < -0.1: 
            self.velocity[0] *= (1 - self.drag)
        if  self.velocity[1] > 0.1 or self.velocity[1] < -0.1: 
            self.velocity[1] *= (1 - self.drag)

    def accellerate_when_spawned(self,rpg):
        """This accellerates the particle according to your momentum multiplied by 10. """
        #print('accellerating')
        
        self.velocity[0] += (rpg.level_stuff.player_1.velocity[0] * self.speed_scale)
        
        self.velocity[1] += (rpg.level_stuff.player_1.velocity[1] * self.speed_scale)
        

    def spawn_particle(self,rpg):
        """"""
        if self.draw_me == False:
            
            self.reset_particle(rpg)
            self.particle_heartbeat = 1000
            self.change_velocity(rpg)
            self.accellerate_when_spawned(rpg)
            self.draw_me = True
            self.particle_creation = False
            if rpg.level_stuff.sound_logic.click_1_sound.get_volume() > rpg.settings_hold.max_volume:
                rpg.level_stuff.sound_logic.click_1_sound.set_volume(rpg.settings_hold.max_volume)
            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.click_1_sound)
            

    def accellerate_post_hit_particles(self,rpg):
        """This accellerates the particles after they hit something"""

        q = 0
        r = len(self.post_impact_particle_list) - 1
        while q <= r:

            s = random.randrange(-80,100)
            s = s/100
            t = random.randrange(20,100)
            t = t / 10
            s2 = random.randrange(-80,100)
            s2 = s2/100
            #t2 = random.randrange(5,12)
            #t2 = t2 / 10
            u = random.randrange(-150,150)
            u2 = random.randrange(-150,150)
            self.post_impact_particle_list[q].velocity[0] += (u + (self.velocity[0] * s ))#* #t))
            self.post_impact_particle_list[q].velocity[1] += (u2 + (self.velocity[1] * s2)) #* t2))
            self.post_impact_particle_list[q].rect.center = (self.particle_x_location + 55,self.particle_y_location + 55)
            #print(self.post_impact_particle_list[q].velocity[0], '  is after collision ')
            #print(self.velocity[1], '  is velocity ')
            q += 1
    
    def draw_post_hit_particles(self,rpg):
        """This draws the particles after it hits something"""
        # this can be done in random direction, or based upon original direction.
        # or some reflect back others just move.
        # i could also resize stuff.
        if self.post_hit_particle__timer <= 0:
            self.post_hit_particle_active = False
            #print('made false')
            self.post_hit_particle__timer = self.post_hit_particle__timer_old
        if self.post_hit_particle_active == True:
            self.post_hit_particle__timer -= 1
            q = 0
            r = len(self.post_impact_particle_list) - 1
            #print(self.post_impact_particle_list[0].velocity[0],' is velocity')
            while q <= r:
                #self.post_impact_particle_list[q].update_location(rpg)
                self.post_impact_particle_list[q].rect.x += (self.post_impact_particle_list[q].velocity[0] * rpg.dt)
                self.post_impact_particle_list[q].rect.y += (self.post_impact_particle_list[q].velocity[1] * rpg.dt)
                self.friction_slowdown_small = 0.9
                self.post_impact_particle_list[q].velocity[0] *= self.friction_slowdown_small
                self.post_impact_particle_list[q].velocity[1] *= self.friction_slowdown_small
                #print(self.location[0],self.location[1])
                #print(self.particle_x_location,self.particle_y_location)
                rpg.screen.blit(self.post_impact_particle_list[q].polygon_surface,(self.post_impact_particle_list[q].rect))
                q += 1



    def draw_post_hit_particles_for_cut_scene(self,rpg):
        """This draws the particles after it hits something"""
        # this can be done in random direction, or based upon original direction.
        # or some reflect back others just move.
        # i could also resize stuff.
        if self.post_hit_particle__timer <= 0:
            self.post_hit_particle_active = False
            #print('made false')
            self.post_hit_particle__timer = self.post_hit_particle__timer_old
            self.reset_particle_cut_scene(rpg)
            self.cut_scene_particle_active = False
        if self.post_hit_particle_active == True:
            self.post_hit_particle__timer -= 1
            q = 0
            r = len(self.post_impact_particle_list) - 1
            #print(self.post_impact_particle_list[0].velocity[0],' is velocity')
            while q <= r:
                #self.post_impact_particle_list[q].update_location(rpg)
                self.post_impact_particle_list[q].rect.x += (self.post_impact_particle_list[q].velocity[0] * rpg.dt)
                self.post_impact_particle_list[q].rect.y += (self.post_impact_particle_list[q].velocity[1] * rpg.dt)
                self.friction_slowdown_small = 0.9
                self.post_impact_particle_list[q].velocity[0] *= self.friction_slowdown_small
                self.post_impact_particle_list[q].velocity[1] *= self.friction_slowdown_small
                #print(self.location[0],self.location[1])
                #print(self.particle_x_location,self.particle_y_location)
                rpg.screen.blit(self.post_impact_particle_list[q].polygon_surface,(self.post_impact_particle_list[q].rect))
                q += 1



    def check_life(self):
        if self.particle_alive == False:
            del self
    
    
   
