import pygame

class Sprite_loader():
    """This is the Sprite loader. This will load in a sprite sheet. 
    It then will divide the sprite sheet into pieces and then 
    apply those to a surface and save them in a list. The list will then be
    iterated through by a animation function."""


    def __init__(self,file_name,number):
        """initializes the variable, this can be rectored to use a dict
        to seperate different animations."""
        # the x and y offset counter will be n and m. 
        n = 0
        m = 11
        

        sheet_large = 'images1\character_sheet.bmp'
        #image_temp = pygame.image.load(sheet_large)
        image_temp = pygame.image.load(file_name)
        wide = image_temp.get_width()
        high = image_temp.get_height()
        size_info = image_temp.get_size()
        y_count = 0
        # the step size multiplied by the counter gets you to the destination pixel.
        self.offset_x = 0 # this is for the player. i will make it its own code like number == 3
        offset_y = -10
        self.image_wide = 60
        self.image_high = self.image_wide
        step_size_x = 64
        step_size_y = 64
        self.surface_list = []

        self.y_count_total = 4
        if number == 2:
            # number 2 is the spiders
            self.image_wide = 50
            self.image_high = self.image_wide
            self.offset_x = -5
            offset_y = -6
            m = 12
        if number == 3:
            # number 3 is for the new player sheet
            """"""
            self.y_count_total = 80
            
        #'''
        while n <= m:
            # creates a surface to save the image to.
            surface_1 = pygame.Surface((self.image_wide,self.image_high))
            rect_hold = surface_1.get_rect()
            #surface_1.rect = surface_1.get_rect()
            surface_1.fill((0,0,0))
            surface_1.set_colorkey((0,0,0))
            x = self.offset_x + (step_size_x * n * (-1))
            y = offset_y + (step_size_y * y_count * (-1))
            #print(x,y)
            # adds the part of the image to the surface
            # the surface is smaller than the image so it will only show a piece of the total image.
            surface_1.blit(image_temp,(x,y))
            surface_1.get_rect()

            # this is a list that holds all of the surfaces.
            # each surface will have a image on it. if it works.
            surface_1 = pygame.transform.scale2x(surface_1) 
            self.surface_list.append(surface_1)
            # the below should work to scan across image
            if n <(m - 1):
                n += 1
            if n == (m - 2):
                # when we reach the right side, we move down a step and back to the left side.
                y_count += 1
                n = 0
                if y_count >=self.y_count_total:
                    n = m + 1
                
        #'''

    def draw_sprite(self,rpg):
        """This will be the function to draw stuff on the screen."""