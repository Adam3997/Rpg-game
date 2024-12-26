import numpy as np
from pygame.sprite import Sprite
import pygame

class Create_polygon(Sprite):
    """This creates a polygon using a parametric equation. 3 shapes so far. """
    def __init__(self,rpg):
        """"""
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
        self.particle_color = (100,100,250)
        self.polygon_surface.set_colorkey((0,0,0))

        self.rect = self.polygon_surface.get_rect()
       

        #player_rect = player_img.get_rect(topleft=(100, 300))
    
    def create_second_shape_new(self):
        """this is the test to see if this works. It works well!"""
        start = -3
        finish = 3
       
        animation_count = 0
        animation_total = 1000
        start_position_x = 100 
        start_position_y = 100

        color_start = 0
        color_end = 250 
        while animation_count < animation_total:
            """"""
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
            """"""
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
        """this is the test to see if this works. It works well!"""
        
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

    
    def create_first_shape(self):
        """this is the test to see if this works. It works well!"""
        
        start = -10
        finish = 10
       
        animation_count = 0
        animation_total = 400

        color_start = 0
        color_end = 250 
        while animation_count < animation_total:
            """"""
            start_position_x = self.screen_rect.centerx
            start_position_y = self.screen_rect.centery
            t = start
            end = finish
            
            hold_list = []

            color = (np.sin(animation_count/24) + 1)*100
            #self.colors.append((color_start,color_end - color_start,animation_total - color_start))
            self.colors.append((color,100,color))
            #print(color)
            color_start += 1

            while t <= end:
                """math done here"""
                if animation_count >= (animation_total / 2):
                    """"""
                    offset_x = start_position_x  -(animation_total ) + animation_count
                    offset_y = start_position_y  -(animation_total ) + animation_count
                    scale = 110 - (animation_total )+ animation_count
                else:
                    offset_x = start_position_x - animation_count
                    offset_y = start_position_y - animation_count
                    scale = 110 - animation_count
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
            self.nested_polygon_list.append(hold_list)
            #print(self.polygon_list)
            #start += 0.01
            #finish -= 0.01
            
            #self.polygon_list.clear()
            animation_count += 1
        #print(self.nested_polygon_list[animation_total - 1])






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
        self.rect = pygame.draw.polygon(self.polygon_surface,(self.particle_color),self.nested_polygon_list[1],4)




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