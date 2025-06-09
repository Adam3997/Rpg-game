import pygame

class Sprite_loader():
    """This is the Sprite loader. This will load in a sprite sheet. 
    It then will divide the sprite sheet into pieces and then 
    apply those to a surface and save them in a list. The list will then be
    iterated through by a animation function."""

    def __init__(self,file_name,number,*args):
        """initializes the variable, this can be rectored to use a dict
        to seperate different animations."""
        # the x and y offset counter will be n and m. 
        n = 0
        m = 11
        #image_temp = pygame.image.load(sheet_large)
        if type(number) == int:
            if number >= 0:
                image_temp = pygame.image.load(file_name)
            y_count = 0
            # the step size multiplied by the counter gets you to the destination pixel.
            self.offset_x = 0 
            offset_y = -10
            self.image_wide = 60
            self.image_high = self.image_wide
            step_size_x = 64
            step_size_y = 64
            self.surface_list = []
            set_colorkey = (0,0,0)
            fill_in = (0,0,0)
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
                self.y_count_total = 80
            if number == 4:
                self.image_high = 40
                self.image_wide = 40
                m = 13
                self.y_count_total = 10
                set_colorkey = (0,0,0) # 255 is white 0 is black
                fill_in = (0,0,0)
                self.offset_x = -5
                offset_y = -5
                step_size_x = 50
                step_size_y = 50
            if number == 7: # 7 is for clouds
                #print('inside 7')
                self.image_high = 184
                self.image_wide = 300
                m = 4
                self.y_count_total = 3
                #set_colorkey = (47,129,54,0)
                #fill_in = (47,129,54,0)
                fill_in = (220,220,220,0)
                set_colorkey = (220,220,220,0)
                step_size_x = 300
                step_size_y = 184
                self.offset_x = 0
                offset_y = 0
            if number == -1:
                """This will not be a sprite sheet.""" # the negatives are for the fire effects
                n = 0 
                m = 23
                set_colorkey = (79,121,66) # 255 is white 0 is black
                fill_in = (79,121,66,0)
                self.image_high = 80
                self.image_wide = self.image_high
            if number == -2:
                n = 1 
                m = 23
                set_colorkey = (79,121,66) # 255 is white 0 is black
                fill_in = (79,121,66,0)
                self.image_high = 80
                self.image_wide = self.image_high
            if number == -3:
                n = 0 
                m = 31
                set_colorkey = (79,121,66) # 255 is white 0 is black
                fill_in = (79,121,66,0)
                self.image_high = 80
                self.image_wide = self.image_high
                self.opach = 150
            if number == -10:
                n = 0 
                m = 31
                set_colorkey = (79,121,66) # 255 is white 0 is black
                fill_in = (79,121,66,0)
                self.image_high = 80
                self.image_wide = self.image_high
                self.opach = 150
            if number == -4:
                n = 0 
                m = 31
                set_colorkey = (79,121,66) # 255 is white 0 is black
                fill_in = (79,121,66,0)
                self.image_high = 120
                self.image_wide = self.image_high
            

            if number < 0:
                while n <=m:
                    
                    surface_1 = pygame.Surface((self.image_wide,self.image_high),pygame.SRCALPHA)
                    surface_1.fill(fill_in)
                    #surface_1.set_colorkey(set_colorkey)
                    j = len(file_name) - 1
                    name_temp = file_name[0:j]
                    if n < 10:
                        name_temp = file_name
                    name_temp += str(n)
                    name_temp += '.png'
                    image_temp = pygame.image.load(name_temp)
                    
                    if number == -10:
                        image_temp.set_alpha(200)
                        #print('alpha set')
                    
                    surface_1.blit(image_temp,(0,0))
                    surface_1.get_rect()
                    self.surface_list.append(surface_1)
                    n += 1
            if number >= 0 and number != 7:
                while n <= m:
                    # creates a surface to save the image to.
                    #print(n)
                    surface_1 = pygame.Surface((self.image_wide,self.image_high))
                    surface_1.fill(fill_in)
                    surface_1.set_colorkey(set_colorkey)
                    x = self.offset_x + (step_size_x * n * (-1))
                    y = offset_y + (step_size_y * y_count * (-1))
                    # adds the part of the image to the surface
                    # the surface is smaller than the image so it will only show a piece of the total image.
                    surface_1.blit(image_temp,(x,y))
                    surface_1.get_rect()
                    # this is a list that holds all of the surfaces.
                    # each surface will have a image on it. if it works.
                    if number != 4:
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
            if number == 7:
                while n <= m:
                    # creates a surface to save the image to.
                    #print(n)
                    surface_1 = pygame.Surface((self.image_wide,self.image_high),pygame.SRCALPHA)
                    
                    surface_1.fill(fill_in)
                    #surface_1.set_colorkey(set_colorkey)
                    x = self.offset_x + (step_size_x * n * (-1))
                    y = offset_y + (step_size_y * y_count * (-1))
                    # adds the part of the image to the surface
                    # the surface is smaller than the image so it will only show a piece of the total image.
                    surface_1.blit(image_temp,(x,y))
                    surface_1.get_rect()
                    # this is a list that holds all of the surfaces.
                    # each surface will have a image on it. if it works.
                    if number != 4:
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
        if type(number) == str:
            if number == 'wolf_2':
                """This is for the wolf"""
                image_temp = pygame.image.load(file_name)
                set_colorkey = (0,0,255) # 255 is white 0 is black
                fill_in = (0,0,255)
                self.image_wide = 63
                self.image_high = 33
                self.offset_x = 0
                offset_y = -95
                step_size_x = 63
                step_size_y = 33

                y_count = 0
                self.surface_list = []

                #set_colorkey = (0,0,0)
                #fill_in = (0,0,0)
                self.y_count_total = 4 # this is the number of downward steps

                n = 0
                m = 5 # this is the number of eastward steps

                while n <= m:
                    # creates a surface to save the image to.
                    surface_1 = pygame.Surface((self.image_wide,self.image_high))
                    surface_1.fill(fill_in)
                    surface_1.set_colorkey(set_colorkey)
                    x = self.offset_x + (step_size_x * n * (-1))
                    y = offset_y + (step_size_y * y_count * (-1))
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

            if number == 'wolf': # this will have a *args usage
                """This is for the wolf"""
                image_temp = pygame.image.load(file_name)
                set_colorkey = (0,0,255) # 255 is white 0 is black
                fill_in = (0,0,255)
                self.image_wide = 63
                self.image_high = 33
                self.offset_x = 0
                offset_y = -95
                step_size_x = 63
                step_size_y = 33

                y_count = 0
                self.surface_list = []

                #set_colorkey = (0,0,0)
                #fill_in = (0,0,0)
                self.y_count_total = 10 # this is the number of downward steps

                n = 0
                m = 5 # this is the number of eastward steps

                while n <= m:
                    # creates a surface to save the image to.
                    surface_1 = pygame.Surface((self.image_wide,self.image_high))
                    surface_1.fill(fill_in)
                    surface_1.set_colorkey(set_colorkey)
                    x = self.offset_x + (step_size_x * n * (-1))
                    y = offset_y + (step_size_y * y_count * (-1))
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

                # this is the second chunk
                image_temp = pygame.image.load(file_name)
                set_colorkey = (0,0,255) # 255 is white 0 is black
                fill_in = (0,0,255)
                self.image_wide = 63
                self.image_high = 33
                self.offset_x = 0
                offset_y = -95
                step_size_x = 63
                step_size_y = 33

                y_count = 0
                self.surface_list = []

                #set_colorkey = (0,0,0)
                #fill_in = (0,0,0)
                self.y_count_total = 4 # this is the number of downward steps

                n = 0
                m = 5 # this is the number of eastward steps

                while n <= m:
                    # creates a surface to save the image to.
                    surface_1 = pygame.Surface((self.image_wide,self.image_high))
                    surface_1.fill(fill_in)
                    surface_1.set_colorkey(set_colorkey)
                    x = self.offset_x + (step_size_x * n * (-1))
                    y = offset_y + (step_size_y * y_count * (-1))
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
                
                
                self.offset_x = 0
                offset_y = -287
                y_count = 0

                n = 0
                m = 5

                while n <= m:
                    # creates a surface to save the image to.
                    surface_1 = pygame.Surface((self.image_wide,self.image_high))
                    surface_1.fill(fill_in)
                    surface_1.set_colorkey(set_colorkey)
                    x = self.offset_x + (step_size_x * n * (-1))
                    y = offset_y + (step_size_y * y_count * (-1))
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
                
                 # this is the third one
                self.offset_x = 3
                offset_y = 0
                y_count = 0
                self.image_wide = 30
                self.image_high = 65
                step_size_x = 32
                step_size_y = 65

                n = 0
                m = 11
                self.y_count_total = 5
                image_temp = pygame.image.load(*args)


                while n <= m:
                    # creates a surface to save the image to.
                    surface_1 = pygame.Surface((self.image_wide,self.image_high))
                    surface_1.fill(fill_in)
                    surface_1.set_colorkey(set_colorkey)
                    x = self.offset_x + (step_size_x * n * (-1))
                    y = offset_y + (step_size_y * y_count * (-1))
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
