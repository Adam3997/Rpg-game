import pygame
import random

class In_game_items():
    """This will be the simple in game items. They can be seen on screen. and when touched
    There will be a sound and a monologue and then the player gets a bonus"""

    def __init__(self,rpg,name):
        """Initialize the various items"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()

        self.name = name


        self.font_items = pygame.font.SysFont('vinerhanditc',32)
        self.display_interaction_possible = True
        self.first = ''
        self.second = ''
        self.third = ''
        self.fourth = ''
        self.current_spot_in_ritual_code = 0

        region_lower = -10000
        region_higher = 10000


        match name:
            case 'stone':
                # t his loads the stone
                """"""
                
                self.image = pygame.image.load("_internal\\img\\stone.png")
                self.rect = self.image.get_rect()
                
                self.image = pygame.transform.scale_by(self.image,4)
                #self.interact_rect = pygame.Rect(0,0,400,400)
                self.interact_rect = self.image.get_rect()
                self.interact_rect = self.interact_rect.inflate(100,100)
                self.rect.centerx = random.randint(region_lower,region_higher)
                self.rect.centery = random.randint(region_lower,region_higher)
                
                self.item_magic_active = False
            case 'rock_words':
                # t his loads the stone
                """"""
                
                self.image = pygame.image.load("_internal\\img\\rock_words.png")
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale_by(self.image,4)
                #self.interact_rect = pygame.Rect(0,0,400,400)
                self.interact_rect = self.image.get_rect()
                self.interact_rect = self.interact_rect.inflate(100,100)
                self.rect.centerx = random.randint(region_lower,region_higher)
                self.rect.centery = random.randint(region_lower,region_higher)
            case 'cross':
                """"""
                self.image = pygame.image.load("_internal\\img\\cross.png")
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale_by(self.image,4)
                #self.interact_rect = pygame.Rect(0,0,400,400)
                self.interact_rect = self.image.get_rect()
                self.interact_rect = self.interact_rect.inflate(100,100)
                #self.rect.centerx = random.randint(-8000,-7000)
                #self.rect.centery = random.randint(-8000,-7000)
                self.rect.centerx = random.randint(region_lower,region_higher)
                self.rect.centery = random.randint(region_lower,region_higher)
                self.item_magic_active = False
            case 'bowl':
                """"""
                self.image = pygame.image.load("_internal\\img\\bowl.png")
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale_by(self.image,4)
                self.image_2 = pygame.image.load("_internal\\img\\bowl_water.png")
                self.image_2 = pygame.transform.scale_by(self.image_2,4)


                self.rect.centerx = random.randint(region_lower,region_higher)
                self.rect.centery = random.randint(region_lower,region_higher)
                #self.interact_rect = pygame.Rect(0,0,400,400)
                self.interact_rect = self.image.get_rect()
                self.interact_rect = self.interact_rect.inflate(100,100)
                self.item_magic_active = False
            case 'plant':
                """"""
                self.image = pygame.image.load("_internal\\img\\plant_full.png")  
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale_by(self.image,4)
                self.rect.centerx = random.randint(region_lower,region_higher)
                self.rect.centery = random.randint(region_lower,region_higher)
                #self.interact_rect = pygame.Rect(0,0,400,400)
                self.interact_rect = self.image.get_rect()
                self.interact_rect = self.interact_rect.inflate(100,100)
                self.item_magic_active = False
            case 'pond':
                """"""
                self.image = pygame.image.load("_internal\\img\\pond.png")
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale_by(self.image,4)
                self.rect.centerx = random.randint(region_lower,region_higher)
                self.rect.centery = random.randint(region_lower,region_higher)
                #self.interact_rect = pygame.Rect(0,0,400,400)
                self.interact_rect = self.image.get_rect()
                self.interact_rect = self.interact_rect.inflate(100,100)
                self.item_magic_active = False
            case 'pillar':
                """"""
                self.image = pygame.image.load("_internal\\img\\pillar_empty.png")
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale_by(self.image,4)
                self.image_2 = pygame.image.load("_internal\\img\\pillar_growth.png")
                self.image_2 = pygame.transform.scale_by(self.image_2,4)
                self.rect.centerx = random.randint(region_lower,region_higher)
                self.rect.centery = random.randint(region_lower,region_higher)
                self.interact_rect = self.image.get_rect()
                self.interact_rect = self.interact_rect.inflate(100,100)
                self.item_magic_active = False

        self.map_x_location = self.rect.centerx
        self.map_y_location = self.rect.centery

    def check_button_to_interact(self,rpg):
        """This checks if the player presses a button."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            """Then the player interacts""" # rpg.level_stuff.ritual_logic
            
            if self.item_magic_active == False:
                self.item_magic_active = True
                self.display_interaction_possible = False
                if rpg.level_stuff.ritual_logic.current_spot_in_ritual_code == 0:
                    rpg.level_stuff.ritual_logic.first = self.name
                    pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_interact_sound)
                    rpg.level_stuff.ritual_logic.current_spot_in_ritual_code += 1
                elif rpg.level_stuff.ritual_logic.current_spot_in_ritual_code == 1:
                    rpg.level_stuff.ritual_logic.second = self.name
                    pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_interact_sound)
                    rpg.level_stuff.ritual_logic.current_spot_in_ritual_code += 1
                elif rpg.level_stuff.ritual_logic.current_spot_in_ritual_code == 2:
                    rpg.level_stuff.ritual_logic.third = self.name
                    pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_interact_sound)
                    rpg.level_stuff.ritual_logic.current_spot_in_ritual_code += 1
                elif rpg.level_stuff.ritual_logic.current_spot_in_ritual_code == 3:
                    rpg.level_stuff.ritual_logic.fourth = self.name
                    pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.player_interact_sound)
                    rpg.level_stuff.ritual_logic.current_spot_in_ritual_code += 1


    def check_player_interact(self,rpg):
        """This allows the player to interact.
        If the player is clos enough, a prompt to click will appear.
        Then if the player clicks then the interaction will occur. """
        if self.display_interaction_possible:
            collisions_test = pygame.Rect.colliderect(rpg.level_stuff.player_1.rect,self.interact_rect)
            
            if collisions_test:
                """Then the player is able to touch the thing."""

                words = 'Interaction possible'
                display_words = self.font_items.render(words,True,(226,223,210),rpg.bg_color)
                rect_words = display_words.get_rect()
                rect_words.topleft = rpg.level_stuff.player_1.rect.bottomleft
                self.screen.blit(display_words,rect_words)
                self.check_button_to_interact(rpg)
            

    def draw_me(self,rpg):
        """This draws the object"""
        
        self.interact_rect.centerx = self.rect.centerx
        self.interact_rect.centery = self.rect.centery
        a = self.image.get_rect().width
                
        self.interact_rect.x += (a/2)
        a = self.image.get_rect().height
        self.interact_rect.y += (a/2)
        
        
        self.screen.blit(self.image,self.rect.center)
        self.check_player_interact(rpg)
        

class generic_items():
    """"""

    def __init__(self,rpg,number):

        """"""
        n = 0
        self.item_list_generic = []
        while n <= number:
            a = random.randint(-8000,8000)
            b = random.randint(-8000,8000)
            c = item_for_use(rpg,'food_plant',(a,b))
            self.item_list_generic.append(c)
            n += 1

    def draw_items_generic(self,rpg):
        """"""
        n = 0
        m = len(self.item_list_generic)- 1
        while n <= m:
            self.item_list_generic[n].draw_item_generic(rpg)
            n += 1
        
class item_for_use():

    def __init__(self,rpg,type_of_item,location):

        self.item_type = type_of_item
        self.plant_full = False
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()

        self.font_items = pygame.font.SysFont('vinerhanditc',22)

        match type_of_item:
            case 'food_plant':
                self.image = pygame.image.load("_internal\\img\\food_plant.png")
                self.image = pygame.transform.scale_by(self.image,4)
                self.image_empty = pygame.image.load("_internal\\img\\food_plant_empty.png")
                self.image_empty = pygame.transform.scale_by(self.image_empty,4)
                self.rect = self.image.get_rect()
                self.rect.centerx = location[0]
                self.rect.centery = location[1]
                self.plant_full = True
                self.plant_refil_timer = 1000
                self.plant_refil_timer_old = self.plant_refil_timer
                self.plant_health_bonus = 10

    def check_button_to_interact(self,rpg):
        """This checks if the player presses a button."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            """Then the player interacts""" # rpg.level_stuff.ritual_logic
            if self.item_type == 'food_plant' and self.plant_full:
                """"""

                rpg.level_stuff.player_1.health += self.plant_health_bonus
                self.plant_full = False
            
                



    def check_player_interact(self,rpg):
        """This allows the player to interact.
        If the player is clos enough, a prompt to click will appear.
        Then if the player clicks then the interaction will occur. """
        
        collisions_test = pygame.Rect.colliderect(rpg.level_stuff.player_1.rect,self.rect)
            
        if collisions_test:
            """Then the player is able to touch the thing."""

            words = 'Interaction possible'
            display_words = self.font_items.render(words,True,(226,223,210),rpg.bg_color)
            rect_words = display_words.get_rect()
            rect_words.topleft = rpg.level_stuff.player_1.rect.bottomleft
            self.screen.blit(display_words,rect_words)
            self.check_button_to_interact(rpg)



    def draw_item_generic(self,rpg):
        if self.item_type == 'food_plant':
            
            if self.plant_full:
                rpg.screen.blit(self.image,self.rect)  
                self.check_player_interact(rpg)    
            else:
                rpg.screen.blit(self.image_empty,self.rect)
                self.plant_refil_timer -= 1
                if self.plant_refil_timer <= 0:
                    self.plant_refil_timer = self.plant_refil_timer_old
                    self.plant_full = True
                    



