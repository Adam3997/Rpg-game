import numpy as np
import random


class Physics_stats():
    """This holds the individual exogenous variables used by the physics system. Each thing in the physics simulation inherits this."""


    def __init__(self,rpg):
        # this will use i,j,k vector notation. i=x, j=y, k=z. Things can be resized slightly to make things jump for example. 
        self.id_number = 0

        self.V_x = 0
        self.V_y = 0
        
        self.location = np.array([0.0,0.0]) # location
        self.velocity = np.array([0.0,0.0]) # i,j,k or x,y since 2D
        self.dv_dt = np.array([0.0,0.0]) # accelleration
        self.mass = 10
        self.temp = 1
        self.max_speed = 400
        self.friction_slowdown = 0.9
        self.max_acc = 60
        self.min_acc = 5
        self.acc_timer = 1
        self.acc_timer_limit = 80

        self.low = -10
        self.high = 10

        self.scaler = 8

        # this is used for the in game map
        self.map_x_location = 0
        self.map_y_location = 0

   

    def update_location(self,rpg):
        """This updates the location for some particles that use this function"""

        #print(self.velocity[0])
        self.location[0] +=  self.velocity[0] * rpg.dt
        self.location[1] +=  self.velocity[1] * rpg.dt
        self.velocity[0] -= self.velocity[0] * self.friction_slowdown  * rpg.dt # i added delta time to make this framerate dependent.
        self.velocity[1] -= self.velocity[1] * self.friction_slowdown * rpg.dt
        #print(self.location[1], ' is x')
        #print(rpg.dt, ' is rpg.dt')

    def update_speed_stats(self,rpg):
        """This updates the speed"""
        
        #print(self.dv_dt, 'in update speed before')

        self.velocity[0] = self.velocity[0] + self.dv_dt[0] 
        self.velocity[1] = self.velocity[1] + self.dv_dt[1]
        #self.dv_dt[0] = 0
        #self.dv_dt[1] = 0
        self.dv_dt = 0 * self.dv_dt
        #print(self.dv_dt, 'in update speed after') 
        #print(self.velocity, ' is velocity')
        vector = ((self.velocity[0]**2) + (self.velocity[1]**2))**(0.5)
        if vector > self.max_speed:
            self.velocity[0] = 0.9 * self.velocity[0]
            self.velocity[1] = 0.9 * self.velocity[1]
        self.velocity[0] -= self.velocity[0] * self.friction_slowdown   * rpg.dt # i added the dt to make this framerate dependent.
        self.velocity[1] -= self.velocity[1] * self.friction_slowdown  * rpg.dt
        if abs(self.velocity[0]) < 190: # this makes stuff stop.
            self.velocity[0] = 0
        if abs(self.velocity[1]) < 190:
            self.velocity[1] = 0 # if below doesnt work i can use the old setup.
        #print(vector,self.dv_dt)

        """if vector <= 50:
            self.velocity[0] = 0
            self.velocity[1] = 0"""
        
    
    def check_acc_timer_limit(self):
        #print(self.acc_timer)
        if self.acc_timer > self.acc_timer_limit:
            self.acc_timer = self.acc_timer_limit
    
    def accellerate_up(self,rpg):
        """causes a upward accelleration"""
        #self.check_acc_timer_limit()
       
        self.dv_dt[1] -= ( random.randint(self.min_acc,self.max_acc))  
       
        #print(self.dv_dt)
    
    def accellerate_down(self,rpg):
        """"""
        #self.check_acc_timer_limit()
        self.dv_dt[1] += ( random.randint(self.min_acc,self.max_acc))  
        
        #print(self.dv_dt)
    
    def accellerate_left(self,rpg):
        """"""
        #self.check_acc_timer_limit()
        self.dv_dt[0] -= ( random.randint(self.min_acc,self.max_acc))  
         
        #print(self.dv_dt)

    def accellerate_right(self,rpg):
        """"""
        #self.check_acc_timer_limit()
        self.dv_dt[0] += ( random.randint(self.min_acc,self.max_acc))  
        
        #print(self.dv_dt)
                                        

    

