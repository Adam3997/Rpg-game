import pygame

class Shadow_gfx():
    """This will create a shadowy overlay. the overlay is static with a bright spot in the middle."""
    # i will add a function that slowly changes the overlay to create a day/night cycle.



    def __init__(self,rpg,type):
        if type == 'shadow':

            self.screen = rpg.screen
            self.screen_rect = rpg.screen.get_rect()

            self.color_key = (0,0,0,200)
            self.fill_in = ()
            self.width = self.screen.get_rect().width
            self.height = self.screen.get_rect().height
            self.location = (0,0)
            self.location_2 = (120 + self.width/2,0)

            self.counter = 0
            self.counter_limit = 20 # this must  be one less than f which is below
            self.delay = 200
            self.delay_old = self.delay

            self.shadow_list = [] # this is for holding different shades of gray

            self.backwards = False
            
            #self.shadow_surface = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
            #self.shadow_surface_2 = pygame.Surface((self.height,self.width),pygame.SRCALPHA)
            e = 0
            f = 50 # f
            while e < f:
                surface_temp = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
                surface_temp_2 =  pygame.Surface((self.height,self.width),pygame.SRCALPHA)
                for i in range(self.width):
                    z = 0.1 + (e/2)# smaller gets ligher faster
                    step_max = 3  # bigger number makes everything darker at end of animation. smaller numbers leaves bright spot in middle
                    # 5 ends really dark but things are still visible.
                    # 5: extremely dark, 4: very dark, 3: mostly dark, 2.5: default dark 2; bright spot in middle, 1: rim of darkness around edge
                    if z > step_max:
                        z = step_max
                    max = 2 # lower ends more light, higher ends darker
                    if 255 -( i //z) < (max ):
                        pygame.draw.line(surface_temp, (0,0,0,max ), (i,0), (i,self.height))
                        pygame.draw.line(surface_temp_2, (0,0,0,max ), (i,0), (i,self.width))
                    elif 255 - (i // z) > 255:
                        pygame.draw.line(surface_temp, (0,0,0,255 ), (i,0), (i,self.height))
                        pygame.draw.line(surface_temp_2, (0,0,0,255 ), (i,0), (i,self.width))
                    else:
                        #print(i,z)
                        pygame.draw.line(surface_temp, (0,0,0,255 - i//(z)), (i,0), (i,self.height))
                        pygame.draw.line(surface_temp_2, (0,0,0,255 - i//(z)), (i,0), (i,self.width))
                a = surface_temp
                b = pygame.transform.flip(surface_temp,flip_x=True,flip_y=False)
                c = pygame.transform.rotate(surface_temp_2,90)
                d = pygame.transform.flip(c,flip_x=False,flip_y=True)
                self.shadow_list.append((a,b,c,d))
                e += 1
        if type == 'test':

            self.screen = rpg.screen
            self.screen_rect = rpg.screen.get_rect()

            self.color_key = (0,0,0,200)
            self.fill_in = ()
            self.width = self.screen.get_rect().width
            self.height = self.screen.get_rect().height
            self.location = (0,0)
            self.location_2 = (120 + self.width/2,0)

            self.counter = 0
            self.counter_limit = 20 # this must  be one less than f which is below
            self.delay = 200
            self.delay_old = self.delay

            self.shadow_list = [] # this is for holding different shades of gray

            self.backwards = False
            
            #self.shadow_surface = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
            #self.shadow_surface_2 = pygame.Surface((self.height,self.width),pygame.SRCALPHA)
            e = 0
            f = 50 # f
            while e < f:
                surface_temp = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
                surface_temp_2 =  pygame.Surface((self.height,self.width),pygame.SRCALPHA)
                for i in range(self.width):
                    z = 0.1 + (e/2)# smaller gets ligher faster
                    step_max = 2  # bigger number makes everything darker at end of animation. smaller numbers leaves bright spot in middle
                    # 5 ends really dark but things are still visible.
                    # 5: extremely dark, 4: very dark, 3: mostly dark, 2.5: default dark 2; bright spot in middle, 1: rim of darkness around edge
                    if z > step_max:
                        z = step_max
                    max = 2 # lower ends more light, higher ends darker
                    if 255 -( i //z) < (max ):
                        pygame.draw.line(surface_temp, (93,63,211,max ), (i,0), (i,self.height)) #93, 63, 211 is a cool purple glow
                        pygame.draw.line(surface_temp_2, (93, 63, 211,max ), (i,0), (i,self.width))
                    elif 255 - (i // z) > 255:
                        pygame.draw.line(surface_temp, (93, 63, 211,255 ), (i,0), (i,self.height))
                        pygame.draw.line(surface_temp_2, (93, 63, 211,255 ), (i,0), (i,self.width))
                    else:
                        #print(i,z)
                        pygame.draw.line(surface_temp, (93, 63, 211,255 - i//(z)), (i,0), (i,self.height))
                        pygame.draw.line(surface_temp_2, (93, 63, 211,255 - i//(z)), (i,0), (i,self.width))
                a = surface_temp
                b = pygame.transform.flip(surface_temp,flip_x=True,flip_y=False)
                c = pygame.transform.rotate(surface_temp_2,90)
                d = pygame.transform.flip(c,flip_x=False,flip_y=True)
                self.shadow_list.append((a,b,c,d))
                e += 1
        
    def draw_shadowy_overlay_2(self):
        """This draws it to the screen."""

        self.screen.blit(self.shadow_list[19][0],self.location)
        self.screen.blit(self.shadow_list[19][1],self.location)
        self.screen.blit(self.shadow_list[19][2],self.location)
        self.screen.blit(self.shadow_list[19][3],self.location)

    def draw_shadowy_overlay(self,rpg):
        """This draws it to the screen."""

        self.screen.blit(self.shadow_list[self.counter][0],self.location)
        self.screen.blit(self.shadow_list[self.counter][1],self.location)
        self.screen.blit(self.shadow_list[self.counter][2],self.location)
        self.screen.blit(self.shadow_list[self.counter][3],self.location)
        self.delay -= 1
        if self.delay <= 0:
            self.delay = self.delay_old
            if self.backwards:
                self.counter -= 1
                if self.counter < 0:
                    self.counter = 0
                    self.backwards = False
                    rpg.night.night_time = False
            if self.backwards == False: 
                self.counter += 1
            if self.counter > self.counter_limit:
                self.counter = self.counter_limit