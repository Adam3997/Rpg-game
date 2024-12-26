#import pygame
#from pygame.sprite import _Group, Sprite
import images1
import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """This is the player in the game. You have a sprite and a location on screen. No animations yet. """
    def __init__(self,rpg):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()

        n = 0
        m = 9
        # i am here

        sheet_large = 'images1\character_sheet.bmp'
        image_temp = pygame.image.load(sheet_large)
        wide = image_temp.get_width()
        high = image_temp.get_height()
        size_info = image_temp.get_size()
        step_size_x = wide/9
        step_size_y = high/9
        '''
        while n <= m:
            

            # the below should work to scan across image
            if n <8:
                n += 1
            if n == 8:
                n = 0
                
        '''


        self.highest = 'right'
        n = 0
        m = 9
        self.image_list_right = []
        self.image_list_left = []
        while n < 9:
            load_string = '_internal\img\player_right_'
            added = str(n)
            added2 = '.bmp'
            load_string += added
            load_string += added2
            image_hold = pygame.image.load(load_string)
            image_hold = pygame.transform.scale2x(image_hold)
            self.image_list_right.append(image_hold)
            n += 1
        n = 0
        while n < 9:
            load_string = '_internal\img\player_left_'
            added = str(n)
            added2 = '.bmp'
            load_string += added
            load_string += added2
            image_hold = pygame.image.load(load_string)
            image_hold = pygame.transform.scale2x(image_hold)
            self.image_list_left.append(image_hold)
            n += 1
        #self.image = pygame.image.load("_internal\img\ch_1.bmp")
        #self.image_resized = pygame.transform.scale(self.image,(150,250))
        self.image_resized = pygame.transform.scale2x(self.image_list_right[0])
        self.rect = self.image_resized.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = self.rect.x
        self.y = self.rect.y

        self.animation_counter = 0
        self.animation_delay = 20

        self.animation_delay_start = self.animation_delay

    def animation(self):
        """This performs the animation of the player."""

    def draw_me(self,rpg):
        """"""
        total = [rpg.moving_right , rpg.moving_left , rpg.moving_down , rpg.moving_up]
        highest = max(total)
        #print(total)
        if highest >= 1:
            match highest:
                case rpg.moving_right:
                    ''''''
                    self.highest = 'right'
                    self.animation_delay -= int(1 + (rpg.movement_speed / 80))
            
            
                    if self.animation_delay <= 0:
                        self.animation_counter += 1
                        self.animation_delay = self.animation_delay_start
                        if self.animation_counter > 8:
                            self.animation_counter = 0
                    self.screen.blit(self.image_list_right[self.animation_counter],self.rect)
                case rpg.moving_left:
                    ''''''
                    self.highest = 'left'
                    self.animation_delay -= int(1 + (rpg.movement_speed / 80))
            
            
                    if self.animation_delay <= 0:
                        self.animation_counter += 1
                        self.animation_delay = self.animation_delay_start
                        if self.animation_counter > 8:
                            self.animation_counter = 0
                    self.screen.blit(self.image_list_left[self.animation_counter],self.rect)
                case rpg.moving_up:
                    self.screen.blit(self.image_list_left[self.animation_counter],self.rect)
                case rpg.moving_down:
                    self.screen.blit(self.image_list_left[self.animation_counter],self.rect)
                

        
        
        if highest < 1:

            if self.highest == 'right':
                self.screen.blit(self.image_list_right[self.animation_counter],self.rect)
            if self.highest == 'left':
                self.screen.blit(self.image_list_right[self.animation_counter],self.rect)
            if self.highest == 'up':
                self.screen.blit(self.image_list_right[self.animation_counter],self.rect)
            if self.highest == 'down':
                self.screen.blit(self.image_list_right[self.animation_counter],self.rect)
        
        
        
        
        '''
        if rpg.moving_right > 1:

            self.animation_delay -= int(1 + (rpg.movement_speed / 80))
            
            
            if self.animation_delay <= 0:
                self.animation_counter += 1
                self.animation_delay = self.animation_delay_start
                if self.animation_counter > 8:
                    self.animation_counter = 0
        self.screen.blit(self.image_list[self.animation_counter],self.rect)
        '''
