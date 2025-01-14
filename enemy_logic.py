import pygame
from pygame.sprite import  Sprite
import random
from sprite_sheet_animater import Sprite_loader
from physics_stats import Physics_stats

class Overworld_person(Sprite,Physics_stats):
    """This is the image of the enemy that shows up on the world map when you move around the game world."""

    def __init__(self,rpg):
        """loads the images and gives random location. Also random image"""
        
        Physics_stats.__init__(self)
        # sets up the screen.
        self.mass = 2 # 20 kilogram spider, why not.
         

        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        #brings in sprite
        super().__init__()
        # picks a image for the enemy
        a = [1,2,3,4]
        pick = random.choice(a)
        scale = 1
        match pick:
            case 1:
                Overworld_person.load_and_rescale(self,"images1\spider06.png",scale)
            case 2:
                Overworld_person.load_and_rescale(self,"images1\spider07.png",scale)
            case 3:
                Overworld_person.load_and_rescale(self,"images1\spider08.png",scale)
            case 4:
                Overworld_person.load_and_rescale(self,"images1\spider10.png",scale)
        #self.image = pygame.image.load("images1\peacock.bmp")
        # does rect stuff
        self.rect = self.sprite_enemy.surface_list[0].get_rect()

        #self.rect.center = self.screen_rect.center
        # location on map established. 
        x = random.randint(-2300,3500)
        y = random.randint(-2300,3500)
        self.rect.center = (x,y)
        # established a surface 
        self.surface = pygame.Surface((100,100))
        self.surface.fill((0,0,0))
        self.surface.set_colorkey((0,0,0))
        
        #self.surface_rect = self.surface.blit(self.image,(-25,-20))
        # variables for velocity and accelleration and movement timer.
        self.V_x = 0
        self.V_y = 0

        self.dydt = 10
        self.dxdt = 10
        self.dVdt = random.randint(30,100)
        timer = random.randint(50,110)
        self.accelleration_timer = timer

        # centering the rect on image.
        self.x = self.rect.x
        self.y = self.rect.y

        self.health = 30

        # animation timer
        self.animation_counter = 0
        self.animation_counter_old = self.animation_counter
        self.animation_delay = 6
        self.animation_delay_old = self.animation_delay
        self.animation_direction = 'right'
        self.animation_length = 6


    def load_and_rescale(self,directory,size):
        self.sprite_enemy = Sprite_loader(directory,2)
        #self.image = pygame.image.load("_internal\img\spider_1.bmp")
        n = 0
        m = len(self.sprite_enemy.surface_list) - 1
        while n <= m:
            """"""
            self.sprite_enemy.surface_list[n] = pygame.transform.scale_by(self.sprite_enemy.surface_list[n],size)
            n += 1
    
    def change_accelleration(self):
        """Changes the velocity by a random one time accelleration."""
        self.dVdt = random.randint(30,100)
        


    def delete_me(self):
        """deletes the enemy. The location change is nessecary for other code checking its location to not trigger."""
        x = -10000
        y = -10000
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        del self

    def draw_me(self):
        """draws the enemy from the surface to the screen. """
        if self.health <= 0:
            self.delete_me()
        if self.animation_counter >= len(self.sprite_enemy.surface_list):
            self.animation_counter = len(self.sprite_enemy.surface_list) - 1
        self.screen.blit(self.sprite_enemy.surface_list[self.animation_counter],(self.rect.x,self.rect.y))
        #self.animation_counter += 1
        self.animation_delay -= 1
        if self.animation_delay <= 0:
            self.animation_counter += 1
            self.animation_delay = self.animation_delay_old
            if (self.animation_counter_old + self.animation_length) <= self.animation_counter:
                self.animation_counter = self.animation_counter_old

    def set_animation_direction(self):
        """This will make the animation face in the correct direction.
        It will also make the animation count through a loop"""
        #print(len(self.sprite_enemy.surface_list))
        value_x = abs(self.V_x)
        value_y = abs(self.V_y)
        if value_x >= value_y:
            """"""
            if self.V_x >=0:
                """right"""
                self.animation_counter = 34
                self.animation_counter_old = self.animation_counter

            if self.V_x < 0:
                """left"""
                self.animation_counter = 14
                self.animation_counter_old = self.animation_counter
        if value_y > value_x:
            """"""
            if self.V_y >=0:
                """down"""
                self.animation_counter = 24
                self.animation_counter_old = self.animation_counter
            if self.V_y < 0:
                """up"""
                self.animation_counter = 4
                self.animation_counter_old = self.animation_counter

    