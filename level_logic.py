from enemy_logic import Overworld_person
from in_game_items import In_game_items
from story_text import Story_text
#from info_overlay import Info_overlay
from trees_builder import Tree_collection
from boss import Boss
from physics import Physics
from particles import Particle
from player import Player
from button import Button
from ritual_recipe import Ritual_recipe
from sounds_logic import Sound_logic
from in_game_map import In_game_map
from wolf import Wolf
import random
import pygame
from map_logic import Grass_Sprites
from map_logic import Clouds
from boss import Wolf_boss
from in_game_items import generic_items
from town import Town
from enemy_intelligence import History_for_AI
#from wolf import Golem




class Level_logic():
    """This holds the logic that organizes the levels. There are 6 levels. """

    def __init__(self,rpg):
        """Initialize the variable"""
        
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.player_1 = Player(rpg)
        self.physics_active = Physics(self)
        self.history_log = History_for_AI(self)
        self.particle_list_1 = []
        n = 0
        particle_total = 2
        while n < particle_total:
            """This creates a list of particles that can be used."""
            f = Particle(self,False,1)
            self.particle_list_1.append(f)
            n += 1

        self.level_1 = False
        self.level_2 = False
        self.level_3 = False
        self.level_4 = False
        self.level_5 = False
        self.level_6 = False

        self.town_exists = False

        self.boss_type = 'spider'

        self.level_1_boss = Boss(self,-8000,-6000,9000,11000,False,'one','regular')

        self.level_1_to_2_button = Button(rpg,'Next',1)
        self.level_1_to_2_button.rect.y += 100
        self.level_1_to_2_button.prep_msg('Next')

        self.ritual_delay = 1000
        self.ritual_delay_old = self.ritual_delay

        self.sound_logic = Sound_logic(rpg)

        self.play_sound = True

        self.generic_items = generic_items(rpg,50,'normal')

        self.map_color = (150,105,25)
        self.map_size = 200

        self.current_level_tracker = 0

        self.grass_decorations = Grass_Sprites(rpg,200)

        self.cloud_stuff =  Clouds(rpg,50)


        self.town_1 = Town(rpg,(1000,1000))

        self.level_design = Level_design(rpg)


        self.base_difficult = 1.0
        self.difficulty = 'normal'

        if self.difficulty == 'easy':
            self.base_difficult = 0.5
        if self.difficulty == 'hard':
            self.base_difficult = 2.0
        if self.difficulty == 'extreme':
            self.base_difficult = 5.0

    def change_difficulty(self,change):
        """"""
        change = str(change)
        if change == 'easy':
            """"""
        if change == 'normal':
            """"""
        if change == 'hard':
            """"""
        else:
            return



    def load_game_skip(self,rpg):
        """This is the load game logic for skipping to level the player was on."""
        rpg.save_file_1.load_game(rpg)
        #print(self.current_level_tracker, ' is current tracker')
        #print(type(self.current_level_tracker))
        if self.current_level_tracker == 1:
            self.load_level_2(rpg)
            #print('level 2 loaded')
        if self.current_level_tracker == 2:
            self.load_level_3(rpg)
        if self.current_level_tracker == 3:
            self.load_level_4(rpg)
        if self.current_level_tracker == 4:
            self.load_level_5(rpg)
        if self.current_level_tracker == 5:
            self.load_level_6(rpg)
        rpg.campagne_mode = True
        rpg.main_menu_stuff.opening_menu = False


    def display_win_game_screen(self,rpg):
        """the screen that shows when the player wins in some way"""
        winning = 'You have won!'

        self.winning = rpg.font.render(winning,True,rpg.text_color,'red')
        self.winning_rect = self.winning.get_rect()
        self.winning_rect.center = self.screen_rect.center
        score = 'Score: '
        score += str(int(self.player_1.score))
        self.score = rpg.font.render(score,True,rpg.text_color,'red')
        self.score_rect = self.score.get_rect()
        self.score_rect.midbottom = self.winning_rect.midtop
        self.screen.blit(self.winning,self.winning_rect)
        self.screen.blit(self.score,self.score_rect)
        #rpg.return_campagne_screen_button.prep_msg('Return to start screen.')
        rpg.return_campagne_screen_button.draw_button()

    def reset_player(self,rpg):
        """resets the player and his score"""
        self.player_1 = Player(rpg)

    def first_to_second_level_switch(self,rpg):
        """This switches from first to second level."""
        self.load_level_2(rpg)
        
        rpg.switch_first_to_second_level_screen = True
        rpg.campagne_mode = False
        self.current_level_tracker += 1
        pygame.mouse.set_visible(True)
        #self.level_1 = False

    def second_to_third_level_switch(self,rpg):
        """This switches from first to second level."""
        self.load_level_3(rpg)
        rpg.switch_2_to_3_level_screen = True
        rpg.campagne_mode = False
        self.current_level_tracker += 1
        pygame.mouse.set_visible(True)

    
    def third_to_fourth_level_switch(self,rpg):
        """This switches from first to second level."""
        self.load_level_4(rpg)
        rpg.switch_3_to_4_level_screen = True
        rpg.campagne_mode = False
        self.current_level_tracker += 1
        pygame.mouse.set_visible(True)
    
    def fourth_to_fifth_level_switch(self,rpg):
        """This switches from first to second level."""
        self.load_level_5(rpg)
        rpg.switch_4_to_5_level_screen = True
        rpg.campagne_mode = False
        self.current_level_tracker += 1
        pygame.mouse.set_visible(True)
    
    def fifth_to_sixth_level_switch(self,rpg):
        """This switches from first to second level."""
        self.load_level_6(rpg)
        rpg.switch_5_to_6_level_screen = True
        rpg.campagne_mode = False
        self.current_level_tracker += 1
        pygame.mouse.set_visible(True)
    
    def ritual_loop(self,rpg):
        """this is the loop"""
        self.ritual_logic.check_for_finished_ritual()
        self.ritual_delay -= 1
        if self.ritual_delay <= 0:
            #print('delay done')
            self.ritual_logic.perform_glory(rpg)
            self.ritual_logic.perform_knowledge(rpg)
            self.ritual_logic.perform_life(rpg)
            self.ritual_logic.perform_war(rpg)
            self.ritual_delay = self.ritual_delay_old

    
    def load_level_1(self,rpg):
        """creates objects for level"""
        self.level_design.setup_forest_level()
        self.map = In_game_map(rpg,self.map_size,self.map_size,self.map_color)
        self.physics_active = Physics(self)
        self.tree_set = Tree_collection(self,400,20000,20000)
        self.grass_decorations = Grass_Sprites(rpg,600)
        self.story = Story_text(rpg)
        #self.story.setup_second_story()
        self.level_1_boss = Boss(self,-8000,-6000,9000,11000,False,'one','regular')
        self.boss_type = 'spider'
        #self.level_1_boss = Wolf_boss(rpg,(200,200),(int(self.base_difficult * 1)))
        #self.level_1_boss = Wolf_boss(rpg,(200,200),(1))
        #self.boss_type = 'wolf'
        self.cloud_stuff =  Clouds(rpg,50)

        self.generic_items = generic_items(rpg,50,'normal')

        #self.town_1 = Town(rpg,(2000,2000))
        #self.town_exists = True

        self.ritual_logic = Ritual_recipe(rpg)
        rpg.game_over_screen = False
        self.level_1 = True

        enemy_count = 0
        self.enemy_list = []
        self.enemy_total = 140
        while enemy_count <= self.enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            spot_x = random.randint(-8000,8000)
            spot_y = random.randint(-8000,8000)
            n = random.choice([Wolf(rpg,(spot_x,spot_y),'lone'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider')])
            #n = Golem(rpg,(200,200),100)
            #n = Overworld_person(self,'spider')
            #n = Wolf(rpg)
            #n = Overworld_person(rpg) # i changed this from self to rpg, i hope nothing breaks
            n.id_number = enemy_count
            #m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            #self.eneny_characters.append(m)
            enemy_count += 1

        self.item_list = []
        
        w = In_game_items(self,'stone')
        self.item_list.append(w)
        w = In_game_items(self,'cross')
        self.item_list.append(w)
        w = In_game_items(self,'bowl')
        self.item_list.append(w)
        w = In_game_items(self,'plant')
        self.item_list.append(w)
        w = In_game_items(self,'pond')
        self.item_list.append(w)
        w = In_game_items(self,'pillar')
        self.item_list.append(w)
    
    def load_level_2(self,rpg):
        """this will be level 2"""
        self.level_design.setup_lava_level()
        self.level_design.load_objects_for_lava_level(700,20000)
        self.map = In_game_map(rpg,self.map_size,self.map_size,self.map_color)
        self.physics_active = Physics(self)
        #self.tree_set = Tree_collection(self,400,20000,20000)
        #self.grass_decorations = Grass_Sprites(rpg,200)
        self.story = Story_text(rpg)
        self.story.setup_second_story()
        self.level_1_boss = Boss(self,2000,10000,5000,9000,False,'two','regular')
        self.cloud_stuff =  Clouds(rpg,50)
        self.boss_type = 'spider'

        #self.generic_items = generic_items(rpg,50,'normal')

        self.ritual_logic = Ritual_recipe(rpg)
        self.level_2 = True
        self.level_1 = False

        enemy_count = 0
        self.enemy_list = []
        self.enemy_total = 300 # this will be tied to difficulty.
        while enemy_count <= self.enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            spot_x = random.randint(-8000,8000)
            spot_y = random.randint(-8000,8000)
            n = random.choice([Wolf(rpg,(spot_x,spot_y),'lone'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider')])
            
            
            #n = Overworld_person(self,'spider')
            n.id_number = enemy_count
            #m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            #self.eneny_characters.append(m)
            enemy_count += 1

        #self.physics_active = Physics(self)


        self.item_list = []
        #print('level 2')
        w = In_game_items(self,'stone')
        self.item_list.append(w)
        w = In_game_items(self,'cross')
        self.item_list.append(w)
        w = In_game_items(self,'bowl')
        self.item_list.append(w)
        w = In_game_items(self,'plant')
        self.item_list.append(w)
        w = In_game_items(self,'pond')
        self.item_list.append(w)
        w = In_game_items(self,'pillar')
        self.item_list.append(w)

    def load_level_3(self,rpg):
        """"""
        self.level_design.setup_forest_level()
        self.map = In_game_map(rpg,self.map_size,self.map_size,self.map_color)
        self.physics_active = Physics(self)
        self.tree_set = Tree_collection(self,400,20000,20000)
        self.grass_decorations = Grass_Sprites(rpg,200)
        self.story = Story_text(rpg)
        self.story.setup_third_story()
        self.level_1_boss = Boss(self,-12000,-5000,-9000,-5000,False,'three','regular')
        self.cloud_stuff =  Clouds(rpg,50)
        self.boss_type = 'spider'

        self.generic_items = generic_items(rpg,50,'normal')

        self.ritual_logic = Ritual_recipe(rpg)

        self.level_3 = True
        self.level_2 = False
        enemy_count = 0
        self.enemy_list = []
        self.enemy_total = 300
        while enemy_count <= self.enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            spot_x = random.randint(-8000,8000)
            spot_y = random.randint(-8000,8000)
            n = random.choice([Wolf(rpg,(spot_x,spot_y),'lone'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider')])
            
            
            #n = Overworld_person(self,'spider')
            n.id_number = enemy_count
            #m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            #self.eneny_characters.append(m)
            enemy_count += 1

        self.item_list = []
        #print('level 3')
        w = In_game_items(self,'stone')
        self.item_list.append(w)
        w = In_game_items(self,'cross')
        self.item_list.append(w)
        w = In_game_items(self,'bowl')
        self.item_list.append(w)
        w = In_game_items(self,'plant')
        self.item_list.append(w)
        w = In_game_items(self,'pond')
        self.item_list.append(w)
        w = In_game_items(self,'pillar')
        self.item_list.append(w)
    
    def load_level_4(self,rpg):
        """"""
        self.level_design.setup_forest_level()
        self.map = In_game_map(rpg,self.map_size,self.map_size,self.map_color)
        self.physics_active = Physics(self)
        self.tree_set = Tree_collection(self,400,20000,20000)
        self.grass_decorations = Grass_Sprites(rpg,200)
        self.story = Story_text(rpg)
        self.story.setup_fourth_story()
        self.level_1_boss = Boss(self,-1200,-1000,500,900,False,'four','regular')
        self.cloud_stuff =  Clouds(rpg,50)
        self.boss_type = 'spider'

        self.generic_items = generic_items(rpg,50,'normal')

        self.ritual_logic = Ritual_recipe(rpg)
        self.level_4 = True
        self.level_3 = False

        #print('level 4')
        enemy_count = 0
        self.enemy_list = []
        self.enemy_total = 400
        while enemy_count <= self.enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            
            spot_x = random.randint(-8000,8000)
            spot_y = random.randint(-8000,8000)
            n = random.choice([Wolf(rpg,(spot_x,spot_y),'lone'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider')])
            
            
            #n = Overworld_person(self,'spider')
            n.id_number = enemy_count
            #m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            #self.eneny_characters.append(m)
            enemy_count += 1

        self.item_list = []
        
        w = In_game_items(self,'stone')
        self.item_list.append(w)
        w = In_game_items(self,'cross')
        self.item_list.append(w)
        w = In_game_items(self,'bowl')
        self.item_list.append(w)
        w = In_game_items(self,'plant')
        self.item_list.append(w)
        w = In_game_items(self,'pond')
        self.item_list.append(w)
        w = In_game_items(self,'pillar')
        self.item_list.append(w)


    def load_level_5(self,rpg):
        """"""
        self.level_design.setup_forest_level()
        self.map = In_game_map(rpg,self.map_size,self.map_size,self.map_color)
        self.physics_active = Physics(self)
        self.tree_set = Tree_collection(self,400,20000,20000)
        self.grass_decorations = Grass_Sprites(rpg,200)
        self.story = Story_text(rpg)
        self.story.setup_fifth_story()
        self.level_1_boss = Wolf_boss(rpg,(1200,6000),(int(self.base_difficult * 15)))
        self.cloud_stuff =  Clouds(rpg,50)
        self.boss_type = 'wolf'

        self.generic_items = generic_items(rpg,5,'normal')

        self.ritual_logic = Ritual_recipe(rpg)
        self.level_5 = True
        self.level_4 = False

        #print('level 5')
        enemy_count = 0
        self.enemy_list = []
        self.enemy_total = 350
        while enemy_count <= self.enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            
            spot_x = random.randint(-8000,8000)
            spot_y = random.randint(-8000,8000)
            #n = random.choice([Wolf(rpg,(spot_x,spot_y),'lone'),Golem(rpg,(200,200),100),Golem(rpg,(200,200),100),Golem(rpg,(200,200),100),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider')])
            #n = Golem(rpg,(200,200),100)
            n = random.choice([Wolf(rpg,(spot_x,spot_y),'lone'),Overworld_person(rpg,'spider'),Overworld_person(rpg,'spider')])
            #
            #n = Overworld_person(self,'spider')
            n.id_number = enemy_count
            #m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            #self.eneny_characters.append(m)
            enemy_count += 1

        self.item_list = []
        
        w = In_game_items(self,'stone')
        self.item_list.append(w)
        w = In_game_items(self,'cross')
        self.item_list.append(w)
        w = In_game_items(self,'bowl')
        self.item_list.append(w)
        w = In_game_items(self,'plant')
        self.item_list.append(w)
        w = In_game_items(self,'pond')
        self.item_list.append(w)
        w = In_game_items(self,'pillar')
        self.item_list.append(w)



    def load_level_6(self,rpg):
        """"""
        self.level_design.setup_forest_level()
        self.map = In_game_map(rpg,self.map_size,self.map_size,self.map_color)
        self.physics_active = Physics(self)
        self.tree_set = Tree_collection(self,400,20000,20000)
        self.grass_decorations = Grass_Sprites(rpg,200)
        self.story = Story_text(rpg)
        self.story.setup_sixth_story()
        self.level_1_boss = Boss(self,-1200,-1000,500,900,False,level='six')
        self.cloud_stuff =  Clouds(rpg,50)
        self.boss_type = 'spider'

        self.generic_items = generic_items(rpg,50,'normal')

        self.ritual_logic = Ritual_recipe(rpg)
        self.level_6 = True
        self.level_5 = False
        #print('level 6')

        enemy_count = 0
        self.enemy_list = []
        self.enemy_total = 600
        while enemy_count <= self.enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            spot_x = random.randint(-8000,8000)
            spot_y = random.randint(-8000,8000)
            n = random.choice([Wolf(rpg,(spot_x,spot_y),'lone'),Overworld_person(rpg,'spider')])
            
            
            #n = Overworld_person(self,'spider')
            n.id_number = enemy_count
            #m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            #self.eneny_characters.append(m)
            enemy_count += 1

        self.item_list = []
        
        w = In_game_items(self,'stone')
        self.item_list.append(w)
        w = In_game_items(self,'cross')
        self.item_list.append(w)
        w = In_game_items(self,'bowl')
        self.item_list.append(w)
        w = In_game_items(self,'plant')
        self.item_list.append(w)
        w = In_game_items(self,'pond')
        self.item_list.append(w)
        w = In_game_items(self,'pillar')
        self.item_list.append(w)


class Loading_screen_and_logic():
    """This class holds the logic for the loading screen and anything else as needed."""
    def __init__(self,rpg):
        """temp"""
        self.screen = rpg.screen
        self.screen_rect = self.screen.get_rect()

        self.loading_screen_color = (138,154,91)

        self.loading_screen_font_color = (54,69,79)

        self.loading_screen_font = pygame.font.SysFont('vinerhanditc',90)

        self.loading_words = self.loading_screen_font.render('Loading...',True,self.loading_screen_font_color,self.loading_screen_color)
        self.loading_words_rect = self.loading_words.get_rect()
        self.loading_words_rect.center = self.screen_rect.center

    
    def draw_loading_screen(self):
        """This draws the loading screen for the player to look at."""
        self.screen.fill(self.loading_screen_color)
        self.screen.blit(self.loading_words,self.loading_words_rect)




class Level_design():
    """This will hold the specific info for having 2 different level types. 
    The two types will be a forest, and the lava level. """


    def __init__(self,rpg):
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()


        #self.lava_level_background_color = (110,38,14) # this is burnt umber
        #self.lava_level_background_color = (54,69,79) # this is charcoal
        #self.lava_level_background_color = (57,53,53) 
        #self.lava_level_background_color = (53,57,53) # onyx
        self.lava_level_background_color = (15,5,2) 

        self.forest_level_background_color = (47,129,54)

        self.current_background_color = self.forest_level_background_color

        self.level_type = 'forest'

        self.rocks_list = []
        self.rocks_rect_list = []

        self.lava_list = []
        self.lava_rect_list = []

        self.lava_damage_rect_list = []
        self.damage_delay = 5
        self.damage_delay_old = self.damage_delay

        

        #
    
    def draw_objects_for_lava_level(self,rpg):
        """This draws the objects for the lava level"""
        self.check_for_lava_damage(rpg)
        if self.damage_delay != 5:
            self.damage_delay -= 1
            if self.damage_delay <= 0:
                self.damage_delay = self.damage_delay_old
        
        n = 0
        m = len(self.lava_list)
        while n < m:
            self.screen.blit(self.lava_list[n],self.lava_rect_list[n])
            self.screen.blit(self.rocks_list[n],self.rocks_rect_list[n])
            #pygame.draw.rect(self.screen,'red',self.lava_damage_rect_list[n])


            n += 1

    def check_for_lava_damage(self,rpg):
        """This checks if the lava damages the player."""
        n = 0
        m = len(self.lava_damage_rect_list)
        while n < m:

            collisions_test  = pygame.Rect.colliderect(self.lava_damage_rect_list[n],rpg.level_stuff.player_1.rect)
            if collisions_test:
                """"""
                if self.damage_delay == 5:
                    rpg.level_stuff.player_1.health -= 1
                    rpg.overlay.create_damage_for_overlay(1,rpg.level_stuff.player_1.rect.center,'red')
                    self.damage_delay -= 1
                
            n += 1

    def load_objects_for_lava_level(self,amount,max_distance_to_spawn):
        """This loads up the rocks and lava for the lava level."""

        n = 0
        while n <= amount//2:
            m = random.choice([pygame.image.load("_internal\\img\\lava_1.png"),pygame.image.load("_internal\\img\\lava_2.png"),pygame.image.load("_internal\\img\\lava_3.png")])
            m = pygame.transform.scale_by(m,3)
            
            image_temp = m
            rect_temp = image_temp.get_rect()
            rect_temp.center = ((random.randrange(-max_distance_to_spawn//2,max_distance_to_spawn//2)),(random.randrange(-max_distance_to_spawn//2,max_distance_to_spawn//2)))

            damage_rect_temp = pygame.Rect.scale_by(rect_temp,0.6)
            
            self.lava_list.append(image_temp)
            self.lava_rect_list.append(rect_temp)
            self.lava_damage_rect_list.append(damage_rect_temp)

            n += 1

        n = 0
        while n <= amount//2:
            m = random.choice([pygame.image.load("_internal\\img\\rubble_1.png"),pygame.image.load("_internal\\img\\rubble_2.png"),pygame.image.load("_internal\\img\\rubble_3.png"),pygame.image.load("_internal\\img\\rubble_4.png"),pygame.image.load("_internal\\img\\rubble_5.png")])
            #m = pygame.transform.scale_by(m,3)
            
            image_temp = m
            rect_temp = image_temp.get_rect()
            rect_temp.center = ((random.randrange(-max_distance_to_spawn//2,max_distance_to_spawn//2)),(random.randrange(-max_distance_to_spawn//2,max_distance_to_spawn//2)))

            #damage_rect_temp = pygame.Rect.scale_by(rect_temp,0.6)
            
            self.rocks_list.append(image_temp)
            self.rocks_rect_list.append(rect_temp)
            

            n += 1
    
    def setup_forest_level(self):
        """This sets up the forest level."""
        self.current_background_color = self.forest_level_background_color
        self.level_type = 'forest'


    

    def setup_lava_level(self):
        """This sets up the lava level. """
        self.current_background_color = self.lava_level_background_color
        self.level_type = 'lava'
        