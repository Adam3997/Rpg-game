import numpy as np
import random


class Physics_stats():
    """"""


    def __init__(self):
        """"""

        # this will use i,j,k vector notation. i=x, j=y, k=z. Things can be resized slightly to make things jump for example. 
        self.id_number = 0

        self.V_x = 0
        self.V_y = 0

        #self.dV_dt = 0

        self.velocity = np.array([[0.0],[0.0]]) # i,j,k or x,y
        self.dv_dt = np.array([[0.0],[0.0]])
        self.mass = 10
        self.temp = 1
        self.max_speed = 400
        #print(self.velocity,'in init')
        self.friction_slowdown = 0.95

        self.max_acc = 60
        self.min_acc = 5
        self.acc_timer = 1
        self.acc_timer_limit = 80

        self.low = -10
        self.high = 10

        self.scaler = 8



        #m = 5
        #answer = self.Velocity + self.dV_dt
        

        #print(self.Velocity, answer)
    

    def update_speed(self,rpg):
        """"""
        
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
        self.velocity[0] = self.velocity[0] * self.friction_slowdown  
        self.velocity[1] = self.velocity[1] * self.friction_slowdown 
        
    
    def check_acc_timer_limit(self):
        print(self.acc_timer)
        if self.acc_timer > self.acc_timer_limit:
            self.acc_timer = self.acc_timer_limit
    
    def accellerate_up(self,rpg):
        """"""
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
                                        

    

