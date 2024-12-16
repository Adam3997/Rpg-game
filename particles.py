import pygame
from pygame.sprite import Sprite
from  polygon_parametric import Create_polygon

class Particle():
    """this is a class that allows particles to exist for various reasons. """

    def __init__(self,rpg):
        """This will initialize the particle in game. it will have a location and stuff"""
        self.screen_rect = rpg.screen.get_rect()
        self.mass = 1
        self.V_x = 1
        self.V_y = 1
        self.dvx_dt = 0
        self.dvy_dt = 0
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

        self.particle_1 = Create_polygon(rpg)
        self.particle_1.create_third_shape()
        #try_particle = pygame.draw.polygon(self.screen,color=(red,green,blue),points=self.test.nested_polygon_list[self.counter_test])
        self.particle_color = (100,100,250)
        self.particle_animation_counter = 0
        self.particle_counter_animation_limit = len(self.particle_1.nested_polygon_list) - 1
        self.particle_rect = pygame.draw.polygon(rpg.screen,color=(self.particle_color),points=self.particle_1.nested_polygon_list[1])

        # this is the variables used by a particle. in theory. 

    def check_particle(self,rpg):
        """this draws the particle and proves its possible to move it. the while loop moves it. the draw makes it appear on screen."""
        #print(self.draw_me,self.particle_1.nested_polygon_list[1][1][0], self.V_x,self.V_y)
        
        if self.draw_me == True:
            self.change_velocity(rpg)
            if -1 < self.V_x < 1:
                    if -1 < self.V_y < 1:
                        self.reset_particle(rpg)
                        self.draw_me = False
                        self.V_x = 0
                        self.V_y = 0
                        return
                        
            o = len (self.particle_1.nested_polygon_list[1])
            n = 0
            
            while n < o:
                
            
                self.particle_1.nested_polygon_list[1][n][0] += (self.V_x ) * rpg.dt
                self.particle_1.nested_polygon_list[1][n][1] += (self.V_y ) * rpg.dt
                
                      
                n += 1
            self.distance_x += (self.V_x ) * rpg.dt
            self.distance_y +=  (self.V_y ) * rpg.dt
            #if 1 < self.V_x < 1:
            #    self.V_x = 0
            #if 1 < self.V_y < 1:
            #    self.V_y = 0
            pygame.draw.polygon(rpg.screen,(self.particle_color),self.particle_1.nested_polygon_list[1])
        
    def reset_particle(self,rpg):
        """"""
        o = len (self.particle_1.nested_polygon_list[1])
        n = 0
        print(self.distance_x)
        
        while n < o:
                
            
            self.particle_1.nested_polygon_list[1][n][0] -= self.distance_x
            self.particle_1.nested_polygon_list[1][n][1] -= self.distance_y
            if n == 20:
                print('particle reset')
                      
            n += 1
        self.distance_x = 0
        self.distance_y = 0

    def player_movement_particle(self,rpg,up,down,left,right):
        """"""     
        if up:
            """"""
            #elf.enemy_list[n].rect.y += self.movement_speed * self.dt
            if self.draw_me == True:
                o = len (self.particle_1.nested_polygon_list[1])
                n = 0
                while n < o:
                    
                
                #self.particle_1.nested_polygon_list[1][n][0] +=  rpg.movement_speed * rpg.dt
                    self.particle_1.nested_polygon_list[1][n][1] +=  rpg.movement_speed * rpg.dt
                    
                    #self.distance_y +=  rpg.movement_speed * rpg.dt
                        
                    n += 1
        
            
        if down:
            """"""
            if self.draw_me == True:
                o = len (self.particle_1.nested_polygon_list[1])
                n = 0
                while n < o:
                    
                
                #self.particle_1.nested_polygon_list[1][n][0] +=  rpg.movement_speed * rpg.dt
                    self.particle_1.nested_polygon_list[1][n][1] -=  rpg.movement_speed * rpg.dt
                    
                    #self.distance_y -=  rpg.movement_speed * rpg.dt
                        
                    n += 1
        if left:
            """"""
            if self.draw_me == True:
                o = len (self.particle_1.nested_polygon_list[1])
                n = 0
                while n < o:
                    
                
                #self.particle_1.nested_polygon_list[1][n][0] +=  rpg.movement_speed * rpg.dt
                    self.particle_1.nested_polygon_list[1][n][0] +=  rpg.movement_speed * rpg.dt
                    #self.distance_x +=  rpg.movement_speed * rpg.dt
                        
                    n += 1
        if right:
            """""" 
            if self.draw_me == True:
                o = len (self.particle_1.nested_polygon_list[1])
                n = 0
                while n < o:
                    
                
                #self.particle_1.nested_polygon_list[1][n][0] +=  rpg.movement_speed * rpg.dt
                    self.particle_1.nested_polygon_list[1][n][0] -=  rpg.movement_speed * rpg.dt
                    #self.distance_x -=  rpg.movement_speed * rpg.dt
                        
                    n += 1
        
    def change_velocity(self,rpg):
        """"""
        #velocity = rpg.moving_right + rpg.moving_left + rpg.moving_up + rpg.moving_down
        if  self.V_x > 0.1 or self.V_x < -0.1: 
            self.V_x *= (1 - self.drag)
        if  self.V_y > 0.1 or self.V_y < -0.1: 
            self.V_y *= (1 - self.drag)

    def accellerate_when_spawned(self,rpg):
        """"""
        if rpg.moving_right > 0:
            self.V_x += rpg.moving_right
        if rpg.moving_left > 0:
            self.V_x -= rpg.moving_left
        if rpg.moving_up > 0:
            self.V_y -= rpg.moving_up
        if rpg.moving_down > 0:
            self.V_y += rpg.moving_down

    def spawn_particle(self,rpg):
        """"""
        self.change_velocity(rpg)
        self.accellerate_when_spawned(rpg)
        self.draw_me = True
        self.particle_creation = False
        


    def check_life(self):
        if self.particle_alive == False:
            del self
    
    
   
        '''
        n = 0
        m = len(self.enemy_list)
        while n < m:
            if up:
                self.enemy_list[n].rect.y += self.movement_speed * self.dt
            if down:
                self.enemy_list[n].rect.y -= self.movement_speed * self.dt
            if left:
                self.enemy_list[n].rect.x += self.movement_speed * self.dt
            if right:
                self.enemy_list[n].rect.x -= self.movement_speed * self.dt
        
            n += 1
            

        n = 0
        m = len(rpg.particle_set_1)
        while n < m:
            if up:
                rpg.particle_set_1[n].rect.y += rpg.movement_speed * rpg.dt
            if down:
                rpg.particle_set_1[n].rect.y -= rpg.movement_speed * rpg.dt
            if left:
                rpg.particle_set_1[n].rect.x += rpg.movement_speed * rpg.dt
            if right:
                rpg.particle_set_1[n].rect.x -= rpg.movement_speed * rpg.dt
            
            n += 1
        '''
    
    def set_new_location(self):
        """This changes the particle location and will remove any velocity. """
    
    
    
    
    

