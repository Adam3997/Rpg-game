import pygame
from pygame.sprite import Sprite
import random


class In_game_map(Sprite):
    """"""
    def __init__(self,rpg):
        """This is the world map the character walks around in. This also has the other in game sprites like trees and grass and their animations. """

        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()

        self.image = pygame.image.load("_internal\img\map_assets_1.bmp")
        self.image_rescaled = pygame.transform.scale2x(self.image)
        self.rect = self.image_rescaled.get_rect()
        self.image2 = pygame.image.load("_internal\img\ckground_1.bmp")
        self.rect2 = self.image2.get_rect()
        self.x2 = self.rect2.x
        self.y2 = self.rect2.y
        self.animation_list = []
        i = 0
        limit = 6000
        
        
        self.flowers = []
        self.rect_list = []
        self.rect_list2 = []
        self.grass = []
        grass_count = 0
        flowers_count = 0
        choices_animation = [0,1,2,3,4]
        self.animation_count = random.choice(choices_animation)
        #print(self.animation_count)
        self.animation_limit = 0

        #self.animation_delay = 24
        
        self.animation_delay_total = 24
        self.animation_count_reverse = 0
        self.animation_delay = self.animation_delay_total

        while i <= limit:
            pick = random.randint(1,300)
            #q = random.choice(pick)
            q = pick
            #print(i,len(self.rect_list))
            match q:
                
                case 1:
                    n = pygame.image.load("_internal\img\\tree1.bmp")
                    n2 = pygame.transform.scale2x(n)
                    
                    self.flowers.append(n2)
                    m = n2.get_rect()
                    self.rect_list.append(m)
                    x = random.randint(-2300,3500)
                    y = random.randint(-2300,3500)
                    self.rect_list[flowers_count].center = (x,y)
                    flowers_count += 1
                case 2:
                    n = pygame.image.load("_internal\img\\tree1.bmp")
                    n2 = pygame.transform.scale2x(n)
                    self.flowers.append(n2)
                    m = n2.get_rect()
                    self.rect_list.append(m)
                    x = random.randint(-2300,3500)
                    y = random.randint(-2300,3500)
                    self.rect_list[flowers_count].center = (x,y)
                    flowers_count += 1
                case num if num > 2:
                    n = pygame.image.load("_internal\img\grass2.bmp")
                    n2 = pygame.image.load("_internal\img\grass2_1.bmp")
                    n3 = pygame.image.load("_internal\img\grass2_25.bmp")
                    n4 = pygame.image.load("_internal\img\grass2_50.bmp")
                    n5 = pygame.image.load("_internal\img\grass2_88.bmp")
                    inside_list = []
                    inside_list.append(n)
                    inside_list.append(n2)
                    inside_list.append(n3)
                    inside_list.append(n4)
                    inside_list.append(n5)
                    
                    self.grass.append(inside_list)
                    m = n.get_rect()
                    self.rect_list2.append(m)
                    x = random.randint(-2300,3500)
                    y = random.randint(-2300,3500)
                    self.rect_list2[grass_count].center = (x,y)
                    grass_count += 1
                    self.animation_limit = len(inside_list)

                    self.animation_limit -= 1
                    self.animation_count_reverse = (self.animation_limit * 2) - self.animation_count

                
            #n = pygame.image.load("images1\lower_clear.bmp")
            
        


            
            i += 1






        self.rect.center = self.screen_rect.center
        self.rect2.center = self.screen_rect.center
        self.x = self.rect.x
        self.y = self.rect.y    

    def draw_flowers(self):
        finish = len(self.flowers) - 2
        i = 0
        while i <= finish:
            
            
            self.screen.blit(self.flowers[i],self.rect_list[i])
            
            
            i += 1

    def draw_grass(self):
        """"""
        finish = len(self.grass) - 2
        i = 0
        
        while i <= finish:
            idea = self.grass[i]
            #print(idea)
            #print(len(idea))
            #print(self.animation_count)
            #print(self.animation_limit)
            idea2 = idea[self.animation_count]
            self.screen.blit(idea2,self.rect_list2[i])
            
            if self.animation_delay <= 0:
                self.animation_delay = self.animation_delay_total
                if self.animation_count_reverse > self.animation_limit:
                    self.animation_count += 1
                
                self.reset_animation()
                #self.animation_count += 1

            i += 1
        self.animation_delay -= 1

    def draw_map(self):
        """"""
        self.screen.blit(self.image2,self.rect2)
        self.screen.blit(self.image_rescaled,self.rect)

    
    def reset_animation(self):
        """if above limit then = 0 again.""" # here i stoppeedd
        if self.animation_count_reverse >= 0:
            #self.animation_limit *= 2
            if self.animation_count_reverse <= self.animation_limit:
                self.animation_count -= 1
            self.animation_count_reverse -= 1
            if self.animation_count_reverse <= 0:

                self.animation_count = 0
                
                self.animation_count_reverse = self.animation_limit * 2
                
                