import pygame
from pygame.sprite import Sprite
import random
from sprite_sheet_animater import Sprite_loader


class In_game_map(Sprite):
    """This is the world the character exists in. This also holds the graphics for most of these things."""
    def __init__(self,rpg):
        """This is the world map the character walks around in. This also has the other in game sprites like trees and grass and their animations. """
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()
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
        self.animation_limit = 0
        self.animation_delay_total = 24
        self.animation_count_reverse = 0
        self.animation_delay = self.animation_delay_total
        while i <= limit:
            pick = random.randint(1,300)
            q = pick
            match q:
                case 1:
                    n = pygame.image.load("_internal\img\\tree1.bmp")
                    n2 = pygame.transform.scale2x(n)
                    self.flowers.append(n2)
                    m = n2.get_rect()
                    self.rect_list.append(m)
                    x = random.randint(-15000,15000)
                    y = random.randint(-15000,15000)
                    self.rect_list[flowers_count].center = (x,y)
                    flowers_count += 1
                case 2:
                    n = pygame.image.load("_internal\img\\tree1.bmp")
                    n2 = pygame.transform.scale2x(n)
                    self.flowers.append(n2)
                    m = n2.get_rect()
                    self.rect_list.append(m)
                    x = random.randint(-15000,15000)
                    y = random.randint(-15000,15000)
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
                    x = random.randint(-16000,16000)
                    y = random.randint(-16000,16000)
                    self.rect_list2[grass_count].center = (x,y)
                    grass_count += 1
                    self.animation_limit = len(inside_list)

                    self.animation_limit -= 1
                    self.animation_count_reverse = (self.animation_limit * 2) - self.animation_count
            i += 1

    def draw_grass(self):
        """This draws the grass on the screen and animates it"""
        finish = len(self.grass) - 2
        i = 0
        while i <= finish:
            idea = self.grass[i]
            idea2 = idea[self.animation_count]
            self.screen.blit(idea2,self.rect_list2[i])
            if self.animation_delay <= 0:
                self.animation_delay = self.animation_delay_total
                if self.animation_count_reverse > self.animation_limit:
                    self.animation_count += 1
                self.reset_animation()
            i += 1
        self.animation_delay -= 1

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

class Clouds():
    """This is the class for in game clouds.
    The clouds will float accross the screen and have a shadow below them.
    They will only have a shadow at night."""

    def __init__(self,rpg,number):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        
        self.cloud_rect_list = []
        self.cloud_list = []
        self.shadow_surfaces = []
        self.screen_width = self.screen_rect.width
        self.screen_height= self.screen_rect.height

        self.cloud_speed_x = random.randint(-70,-30)
        self.cloud_speed_y = random.randint(-40,-10)

        self.cloud_rect_list_for_shadows = []
        #print('before')
        self.cloud_images = Sprite_loader('_internal\\img\\clouds_small.png',7)
        #print('after')
        
        n = 0
        while n <= number:
            a = random.choice([self.cloud_images.surface_list[0],self.cloud_images.surface_list[1],self.cloud_images.surface_list[2],self.cloud_images.surface_list[3]])
            b = a.get_rect()
            
            b.centerx = random.randint(-3 * self.screen_width ,3 * self.screen_width )
            b.centery = random.randint(-3 * self.screen_height, 3 * self.screen_height  )

            self.cloud_rect_list.append(b)
            b.inflate(-200,-200)
            #a.center = b.center
            self.cloud_rect_list[n].center = b.center
            b = b.scale_by(-0.55)
            self.cloud_rect_list_for_shadows.append(b)
            c = pygame.Surface((self.cloud_rect_list_for_shadows[n].width,self.cloud_rect_list_for_shadows[n].height),pygame.SRCALPHA)
            c.fill((255,255,255,0))
            pygame.draw.ellipse(c,(20,20,20,50),c.get_rect())
            self.shadow_surfaces.append(c)
            self.cloud_list.append(a)
            #print('create cloud')
            n += 1

    def cloud_loop(self,rpg):
        self.update_clouds(rpg)
        self.draw_clouds()

    def move_clouds_for_player(self,rpg):
        """this moves the clouds as the player moves"""
        n = 0
        m = len(self.cloud_rect_list)- 1

        while n <= m:
            self.cloud_rect_list[n].centerx -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            self.cloud_rect_list[n].centery -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            self.cloud_rect_list_for_shadows[n].centerx -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            self.cloud_rect_list_for_shadows[n].centery -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            n += 1

    def update_clouds(self,rpg):
        """This moves the clouds"""
        n = 0
        m = len(self.cloud_rect_list)- 1
        #print('updating clouds')
        while n <= m:
            self.cloud_rect_list[n].centerx += self.cloud_speed_x * rpg.dt
            self.cloud_rect_list[n].centery += self.cloud_speed_y * rpg.dt
            self.cloud_rect_list_for_shadows[n].centerx = self.cloud_rect_list[n].centerx 
            self.cloud_rect_list_for_shadows[n].centery = self.cloud_rect_list[n].centery
            if self.cloud_rect_list[n].centerx >= (3.5 * self.screen_width):
                self.cloud_rect_list[n].centerx = random.randint(-3 * self.screen_width, -1 *self.screen_width  )
                self.cloud_rect_list[n].centery = random.randint(-2 * self.screen_height, 2 * self.screen_height )
                self.cloud_rect_list_for_shadows[n].centerx = self.cloud_rect_list[n].centerx 
                self.cloud_rect_list_for_shadows[n].centery = self.cloud_rect_list[n].centery 
            if self.cloud_rect_list[n].centerx <= (-3.5 * self.screen_width):
                self.cloud_rect_list[n].centerx = random.randint(self.screen_width + 200,3 * self.screen_width )
                self.cloud_rect_list[n].centery = random.randint(-2 * self.screen_height, 2 * self.screen_height)
                self.cloud_rect_list_for_shadows[n].centerx = self.cloud_rect_list[n].centerx 
                self.cloud_rect_list_for_shadows[n].centery = self.cloud_rect_list[n].centery
            if self.cloud_rect_list[n].centery >= (3.5 * self.screen_height):
                self.cloud_rect_list[n].centerx = random.randint(-3 * self.screen_width, -1 *self.screen_width  )
                self.cloud_rect_list[n].centery = random.randint(-2 * self.screen_height, 2 * self.screen_height )
                self.cloud_rect_list_for_shadows[n].centerx = self.cloud_rect_list[n].centerx 
                self.cloud_rect_list_for_shadows[n].centery = self.cloud_rect_list[n].centery
            if self.cloud_rect_list[n].centery <= (-3.5 * self.screen_height):
                self.cloud_rect_list[n].centerx = random.randint(self.screen_width + 200,3 * self.screen_width )
                self.cloud_rect_list[n].centery = random.randint(-2 * self.screen_height, 2 * self.screen_height)
                self.cloud_rect_list_for_shadows[n].centerx = self.cloud_rect_list[n].centerx 
                self.cloud_rect_list_for_shadows[n].centery = self.cloud_rect_list[n].centery
            n += 1


    def draw_clouds(self):
        """This draws the clouds on screen"""

        n = 0
        m = len(self.cloud_rect_list)- 1
        while n <= m:
            #self.cloud_rect_list_for_shadows[n].center = self.cloud_rect_list[n].center
            self.screen.blit(self.shadow_surfaces[n],self.cloud_rect_list_for_shadows[n])
            self.screen.blit(self.cloud_list[n],self.cloud_rect_list[n])  
            n += 1  







class Grass_Sprites():
    """"""

    def __init__(self,rpg,number):
        """"""

        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        

        self.rect_list = []
        self.grass_sprite_list = []
        

        number_of_stuff = number
        n = 0
        while n <= number_of_stuff:
            """"""

            hold = random.choice([pygame.image.load("_internal\\img\\bush_1.png"),(pygame.image.load("_internal\\img\\bush_2.png")),(pygame.image.load("_internal\\img\\bush_3.png")),(pygame.image.load("_internal\\img\\leaves_2.png")),(pygame.image.load("_internal\\img\\leaves_1.png")),(pygame.image.load("_internal\\img\\flower_rect.png"))])
            hold = pygame.transform.scale_by(hold,2)
            self.grass_sprite_list.append(hold)
            hold_rect = hold.get_rect()
            #surface_hold = pygame.Surface((hold.get_rect().width,hold.get_rect().height))
            #surface_hold
            a = random.randint(-10000,10000)
            hold_rect.x = a
            a = random.randint(-10000,10000)
            hold_rect.y = a
            self.rect_list.append(hold_rect)
            n += 1

    def update_location(self,rpg):
        """This updates location as player moves"""
        n = 0
        m = len(self.grass_sprite_list) - 1
        while n <= m:
            self.rect_list[n].x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            self.rect_list[n].y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            
            n += 1


    def draw_grass(self,rpg):
        """"""
        n = 0
        m = len(self.grass_sprite_list) - 1
        while n <= m:
            self.screen.blit(self.grass_sprite_list[n],self.rect_list[n])
            
            n += 1

                
                