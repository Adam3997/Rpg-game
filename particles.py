import pygame
from pygame.sprite import Sprite
from  polygon_parametric import Create_polygon
from physics_stats import Physics_stats

class Particle(Sprite,Physics_stats):
    """this is a class that allows particles to exist for various reasons. """

    def __init__(self,rpg):
        """This will initialize the particle in game. it will have a location and stuff"""
        Physics_stats.__init__(self)
        super().__init__()
        self.screen_rect = rpg.screen.get_rect()
        self.screen = rpg.screen
        self.mass = 1
        self.damage = 10
        self.damage_start = self.damage
        
        self.drag = 0.2
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
        self.start_location_x = self.screen_rect.centerx  - 38
        self.start_location_y = self.screen_rect.centery - 40
        self.shape_2_counter = 500
        self.particle_damage = 15

        self.particle_x_location = self.start_location_x
        self.particle_y_location = self.start_location_y

        
        self.speed_scale = 6
        self.particle_1 = Create_polygon(rpg)
        self.particle_1.create_third_shape()
        #self.particle_1.create_second_shape_new()
        self.rect = self.particle_1.polygon_surface.get_rect(center=(self.particle_x_location,self.particle_y_location))
        #try_particle = pygame.draw.polygon(self.screen,color=(red,green,blue),points=self.test.nested_polygon_list[self.counter_test])
        self.particle_color = (100,100,250)
        self.particle_animation_counter = 0
        self.particle_counter_animation_limit = len(self.particle_1.nested_polygon_list) - 1
        #self.particle_rect = self.particle_1.polygon_surface.get_rect()

        # this is the variables used by a particle. in theory. 

    def check_particle(self,rpg):
        """this draws the particle and proves its possible to move it. the while loop moves it. the draw makes it appear on screen."""
        #print(self.draw_me,self.particle_1.nested_polygon_list[1][1][0], self.V_x,self.V_y)
        #print(self.velocity)
        #rpg.screen.blit(self.particle_1.polygon_surface,(self.particle_x_location,self.particle_y_location))
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
            
                        
           
            self.player_movement_particle(rpg)
            self.move_particle(rpg)
            
           
            #if 1 < self.V_x < 1:
            #    self.V_x = 0
            #if 1 < self.V_y < 1:
            #    self.V_y = 0
            #pygame.draw.polygon(rpg.screen,(self.particle_color),self.particle_1.nested_polygon_list[1],5)
            #print(self.particle_x_location,self.particle_y_location,' is the x, y')
            self.particle_x_location = int(self.particle_x_location)
            self.particle_y_location = int(self.particle_y_location)
            

            #rpg.screen.blit(self.particle_1.surface_list[self.shape_2_counter],(self.particle_x_location,self.particle_y_location))
            rpg.screen.blit(self.particle_1.polygon_surface,(self.particle_x_location,self.particle_y_location))
            
            self.shape_2_counter -= 1
            if self.shape_2_counter <= 450:
                self.shape_2_counter = 450
    # that had to be set to surface to list work for the particle 2 new. for particle 3, it was the self.polygon surface

    def move_particle(self,rpg):
        """"""
        
        if self.draw_me == True:
                
            self.particle_x_location += self.velocity[0] * rpg.dt
            self.particle_1.rect.x += self.velocity[0] * rpg.dt
                
        
        
            
                
            self.particle_y_location += self.velocity[1] * rpg.dt
            self.particle_1.rect.y += self.velocity[1] * rpg.dt
        


    def reset_particle(self,rpg):
        """"""
        self.particle_x_location = self.start_location_x
        self.particle_y_location = self.start_location_y
        self.particle_1.rect.x = self.start_location_x
        self.particle_1.rect.y = self.start_location_y
        self.velocity[0] = 0
        self.velocity[1] = 0
        self.shape_2_counter = 500
        self.damage = self.damage_start
        
        '''
        while n < o:
                
            
            self.particle_1.nested_polygon_list[1][n][0] -= self.distance_x
            self.particle_1.nested_polygon_list[1][n][1] -= self.distance_y
            if n == 20:
                print('particle reset')
                      
            n += 1
        '''
        

        #self.particle_1.create_third_shape()
        

    def player_movement_particle(self,rpg):
        """"""     
        
        if self.draw_me == True:
            
            self.particle_y_location -= rpg.player_1.velocity[1] * rpg.dt
            self.particle_1.rect.y -= rpg.player_1.velocity[1] * rpg.dt
        
            self.particle_x_location -= rpg.player_1.velocity[0] * rpg.dt
            self.particle_1.rect.x -= rpg.player_1.velocity[0]* rpg.dt



        


    


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
        
        self.velocity[0] += (rpg.player_1.velocity[0] * self.speed_scale)
        
        self.velocity[1] += (rpg.player_1.velocity[1] * self.speed_scale)
        
        

    def spawn_particle(self,rpg):
        """"""
        if self.draw_me == False:
            
            self.reset_particle(rpg)
            self.particle_heartbeat = 1000
            self.change_velocity(rpg)
            self.accellerate_when_spawned(rpg)
            self.draw_me = True
            self.particle_creation = False
        


    def check_life(self):
        if self.particle_alive == False:
            del self
    
    
   
    
    def set_new_location(self):
        """This changes the particle location and will remove any velocity. """
    
    
    
    
    

