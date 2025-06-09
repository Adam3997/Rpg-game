import numpy as np
from pygame.sprite import Sprite
import pygame
from physics_stats import Physics_stats
import json
from pathlib import Path

class Create_polygon(Sprite,Physics_stats):
    """This creates a polygon using a parametric equation. 3 shapes so far. """
    def __init__(self,rpg,cut_scene):
        """Initialize the polygon"""
        Physics_stats.__init__(self,rpg)
        super().__init__()
        self.polygon_surface = pygame.Surface((80,80))
        self.polygon_list = []
        self.nested_polygon_list = []
        self.nested_polygon_list_backup = []
        self.surface_list = []
        self.rect_list = []
        self.colors = []
        self.screen_rect = rpg.screen.get_rect()
        self.screen = rpg.screen
        self.particle_color = (160,82,45)
        if cut_scene:
            self.particle_color = (255,100,50)
        self.polygon_surface.set_colorkey((0,0,0))

        self.rect = self.polygon_surface.get_rect()

        self.path = Path('polygon_data.json')
       
       

        #player_rect = player_img.get_rect(topleft=(100, 300))
    
    def save_shape_info(self):
        """this saves the list used to draw the shape."""

        contents = json.dumps(self.nested_polygon_list)
        self.path.write_text(contents)
        

    def load_shape_info(self):
        """"""

        try:
            """"""

            contents = self.path.read_text()
            information = json.loads(contents)
            self.nested_polygon_list = information[0]
        except:
            """"""
            pass # i am doing the try except somewhere else since it is more customizable



    def create_second_shape_new(self):
        """This is shape number 2. This is a ball turning into a wave. a famous equation with a name.
        When a = 0 then the equation is a ball. as a is positive it turns into a wave moving into positive
        direction. it is mirrored about the y axis. very slow to do math since it has 1000 animation frames.
        The new part refers to it having the addded effect of the color changing as it animates. note,
        This part of the code does not have the logic to play back the animation, this only creates it.
        to play the animation, iterate through the list. The backup is incase you rescale the original list"""
        start = -3
        finish = 3
       
        animation_count = 0
        animation_total = 1000
        start_position_x = 100 
        start_position_y = 100

        color_start = 0
        color_end = 250 
        while animation_count < animation_total:
            """number of animation frames"""
            #start_position_x = self.screen_rect.centerx
            #start_position_y = self.screen_rect.centery
            t = start
            end = finish
            
            hold_list = []

            color = (np.sin(animation_count/100) + 1)*100
            #self.colors.append((color_start,color_end - color_start,animation_total - color_start))
            self.colors.append((color,100,color))
            #print(color)
            color_start += 1
            scale = 40
            while t <= end:
                """math done here"""
                
                #y = np.sin( 2 * t ) * 100 + offset
                #x = offset  + 100 * np.cos(t)
                slower = 100
                a = ((-animation_total / 2) + animation_count ) / slower 
                x = (scale * (a + np.cos(t))  ) + start_position_x
                y = (scale * (a * np.tan(t)  + np.sin(t)) ) + start_position_y
                if y >= 4000:
                    y = 4000
                if y < -4000:
                    y = -4000

                x = round(x,2)
                y = round(y,2)
                #print(y)
                #z = (x,y)
                
                hold_list.append([x,y])
                #print(x)
                t += 0.01
            self.nested_polygon_list.append(hold_list)
            self.nested_polygon_list_backup.append(hold_list)
            #print(self.polygon_list)
            #start += 0.01
            #finish -= 0.01
            
            #self.polygon_list.clear()
            animation_count += 1
        n = 0
        m = len(self.nested_polygon_list)
        while n < m:
            polygon_surface_temp = pygame.Surface((200,200))
            polygon_surface_temp.fill((0,0,0))
            polygon_surface_temp.set_colorkey((0,0,0)) # this will make background invisible
            rect_temp = pygame.draw.polygon(polygon_surface_temp,(self.particle_color),self.nested_polygon_list[n])

            self.surface_list.append(polygon_surface_temp)
            self.rect_list.append(rect_temp)


            n += 1
        #self.polygon_surface.fill((0,0,0))
        #self.rect = pygame.draw.polygon(self.polygon_surface,(self.particle_color),self.nested_polygon_list[1],4)
        
        
        
        
    def create_second_shape(self):
        """this is the same as the other but it stays one color"""
        
        start = -3
        finish = 3
       
        animation_count = 0
        animation_total = 1000

        color_start = 0
        color_end = 250 
        while animation_count < animation_total:
            """"""
            start_position_x = self.screen_rect.centerx
            start_position_y = self.screen_rect.centery
            t = start
            end = finish
            
            hold_list = []

            color = (np.sin(animation_count/100) + 1)*100
            #self.colors.append((color_start,color_end - color_start,animation_total - color_start))
            self.colors.append((color,100,color))
            #print(color)
            color_start += 1
            scale = 100
            while t <= end:
                """math done here"""
                
                #y = np.sin( 2 * t ) * 100 + offset
                #x = offset  + 100 * np.cos(t)
                slower = 100
                a = ((-animation_total / 2) + animation_count ) / slower 
                x = (scale * (a + np.cos(t))  ) + start_position_x
                y = (scale * (a * np.tan(t)  + np.sin(t)) ) + start_position_y
                if y >= 4000:
                    y = 4000
                if y < -4000:
                    y = -4000

                x = round(x,2)
                y = round(y,2)
                #print(y)
                z =list(x,y)
                
                hold_list.append(z)
                #print(x)
                t += 0.01
            self.nested_polygon_list.append(hold_list)
            #print(self.polygon_list)
            #start += 0.01
            #finish -= 0.01
            
            #self.polygon_list.clear()
            animation_count += 1

    def load_first_shape(self,size):
        """This is a spikey ball"""
        
        
        
        
        self.surface_list_1 = []
        self.surface_list_1_rect = []
        
      
        self.load_shape_info()
        
        self.polygon_surface = pygame.Surface((70,70))
        self.polygon_surface.fill((255,255,255))
        self.polygon_surface.set_colorkey((255,255,255))
        self.rect = pygame.draw.polygon(self.polygon_surface,(self.particle_color),self.nested_polygon_list)
        if size == 'small':
            self.polygon_surface = pygame.transform.scale_by(self.polygon_surface,0.25)
            #self.rect.x += 35
            #self.rect.y += 35
        #self.save_shape_info()
       

    def create_first_shape(self,size):
        """This is a spikey ball"""
        
        start = -10
        finish = 10
       

        
        
        self.surface_list_1 = []
        self.surface_list_1_rect = []
        
        #start_position_x = self.screen_rect.centerx
        #start_position_y = self.screen_rect.centery
        t = start
        end = finish
            
        hold_list = []

        
        #self.colors.append((color_start,color_end - color_start,animation_total - color_start))
        
        #print(color)
        offset_x = 35
        offset_y = 35
        

        while t <= end:
                
            
            
            #offset_x = start_position_x 
            #offset_y = start_position_y 
            scale = 10 
            #y = np.sin( 2 * t ) * 100 + offset
            #x = offset  + 100 * np.cos(t)
            x = scale * (2.3 * np.cos(10 * t) + np.cos(23 * t)) + offset_x
            y = scale * (2.3 * np.sin(10 * t) - np.sin(23 * t)) + offset_y


            x = round(x,2)
            y = round(y,2)
            #print(y)
                
            hold_list.append((x,y))
                
            #print(x)
            t += 0.001
        #print(hold_list)
        self.nested_polygon_list.append(hold_list)
        self.polygon_surface = pygame.Surface((70,70))
        self.polygon_surface.fill((255,255,255))
        self.polygon_surface.set_colorkey((255,255,255))
        self.rect = pygame.draw.polygon(self.polygon_surface,(self.particle_color),hold_list)
        if size == 'small':
            self.polygon_surface = pygame.transform.scale_by(self.polygon_surface,0.25)
            #self.rect.x += 35
            #self.rect.y += 35
        self.save_shape_info()
       



    def create_third_shape(self):
        """this is the test to see if this works. It works well!"""
        
        start = -3.15
        finish = 3.15
       
        animation_count = 0
        animation_total = 1000

        color_start = 0
        color_end = 250 
        slower = 2
        while animation_count < animation_total:
            """"""
            start_position_x = 290 
            start_position_y = 40
            #start_position_x = 0
            #start_position_y = 0
            t = start
            end = finish
            
            hold_list = []

            color = (np.sin(animation_count/100) + 1)*100
            #self.colors.append((color_start,color_end - color_start,animation_total - color_start))
            self.colors.append((color,100,color))
            #print(color)
            color_start += 1
            scale = 30
            while t <= end:
                """math done here"""
                
                #y = np.sin( 2 * t ) * 100 + offset
                #x = offset  + 100 * np.cos(t)
                
                a = ((-animation_total / 2) + animation_count ) / slower 
                x = scale * (np.sin(2*t)) + a + start_position_x
                y = scale * (np.sin(t + np.sin(2*t))) + start_position_y
                if y >= 4000:
                    y = 4000
                if y < -4000:
                    y = -4000

                x = round(x,8)
                y = round(y,8)
                #print(y)
                
                hold_list.append([x,y])
                #print(x)
                t += 0.01
            self.nested_polygon_list.append(hold_list)
            self.nested_polygon_list_backup.append(hold_list)
            #print(self.polygon_list)
            #start += 0.01
            #finish -= 0.01
            
            #self.polygon_list.clear()
            animation_count += 1
        self.polygon_surface.fill((0,0,0))
        self.rect = pygame.draw.polygon(self.polygon_surface,(self.particle_color),self.nested_polygon_list[1])




    def create_fourth_shape(self):
        """this is the test to see if this works. It works well!
        This will be the cool looking spiral portal. """
        
        start = -3.15
        finish = 3.15
       
        animation_count = 0
        animation_total = 1000

        color_start = 0
        color_end = 250 
        slower = 2
        while animation_count < animation_total:
            """"""
            start_position_x = 290 
            start_position_y = 40
            #start_position_x = 0
            #start_position_y = 0
            t = start
            end = finish
            
            hold_list = []

            color = (np.sin(animation_count/100) + 1)*100
            #self.colors.append((color_start,color_end - color_start,animation_total - color_start))
            self.colors.append((color,100,color))
            #print(color)
            color_start += 1
            scale = 30
            while t <= end:
                """math done here"""
                
                #y = np.sin( 2 * t ) * 100 + offset
                #x = offset  + 100 * np.cos(t)
                
                a = ((-animation_total / 2) + animation_count ) / slower 
                x = scale * (np.sin(2*t)) + a + start_position_x
                y = scale * (np.sin(t + np.sin(2*t))) + start_position_y
                if y >= 4000:
                    y = 4000
                if y < -4000:
                    y = -4000

                x = round(x,8)
                y = round(y,8)
                #print(y)
                
                hold_list.append([x,y])
                #print(x)
                t += 0.01
            self.nested_polygon_list.append(hold_list)
            self.nested_polygon_list_backup.append(hold_list)
            #print(self.polygon_list)
            #start += 0.01
            #finish -= 0.01
            
            #self.polygon_list.clear()
            animation_count += 1
        self.polygon_surface.fill((0,0,0))
        self.rect = pygame.draw.polygon(self.polygon_surface,(self.particle_color),self.nested_polygon_list[1],4)