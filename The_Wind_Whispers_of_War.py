import pygame
import random
from info_overlay import Info_overlay
from level_logic import Level_logic
from button import Button
from map_logic import In_game_map
from scenes import Scenes
from night_cycle import Night_cycle
from pause_menu import Pause_menu
from save_load_game import Save_and_load_game
from opening import Opening
from opening import Top_Scores
from Settings import Settings
from level_logic import Loading_screen_and_logic



class RPG_game:
    """This is an rpg game with a world to explore. There is a run game loop that starts the game. 
    There is also functions invovled in the game operation."""
    # this makes the game loop and run
    def run_game(self):
        """The game is started with this function"""
        pygame.init()
        

        self.game = True

        # setting up the fonts

        self.text_color =  (82, 54, 31)
        self.bg_color = (31, 59, 82)
        self.font = pygame.font.SysFont('vinerhanditc',48)
        
        # set up the settings.
        
        self.settings_hold = Settings(self)
        
        # set up the screen
        
        if self.settings_hold.resolution_1080p:
            if self.settings_hold.full_screen:
                self.screen = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
            if self.settings_hold.full_screen == False:
                self.screen = pygame.display.set_mode((1920, 1080))
        if self.settings_hold.resolution_720p:
            if self.settings_hold.full_screen:
                self.screen = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)
            if self.settings_hold.full_screen == False:
                self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('The Wind Whispers of War')
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.settings_hold.create_setting_screen(self)
    
        # set up the ingame clock/framerate

        self.clock = pygame.time.Clock()


        # going to add a load screen here
        
        # creating the highscores, main menu, save files stuff, level logic, pause menu, night cycle and framerate info.
        # it is currently locked to 60 framerate.

        self.loading_screen = Loading_screen_and_logic(self)
        self.loading_screen_active = False

        # this is an attempt at a loading screen.
        """self.screen.fill((255,255,255))
        self.loading_screen.draw_loading_screen()
        pygame.display.update()"""
        
        self.high_score_stuff = Top_Scores(self)

        self.main_menu_stuff = Opening(self)
        
        self.save_file_1 = Save_and_load_game(self,'1')
        
        self.level_stuff = Level_logic(self)

        self.pause_menu = Pause_menu(self)

        self.night = Night_cycle(self)
        self.target_framerate = 60
        
        self.time_tracker = 0

        self.clock.tick(self.target_framerate)
        
        # this is the game active boolian
        
        # this is the test cut screne that made it into the game

        self.cut_scene_1 = Scenes(self)
        self.first_time_cut_scene = False

        # this is variables 

        self.deck_spot = 0
        self.start_menu = False
        self.turn = 0
        self.campagne_fight = False
        self.dt = 0
        self.game_over_screen = False
        self.campagne_story_1 = False
        self.win_game_screen = False
        self.campagne_story_2 = False
        self.campagne_story_3 = False
        self.boss_intro_1 = False
        self.boss_defeated_1 = False
        self.setting_screen = False
        #self.pause_menu = False
        self.switch_first_to_second_level_screen = False
        self.switch_2_to_3_level_screen = False
        self.switch_3_to_4_level_screen = False
        self.switch_4_to_5_level_screen = False
        self.switch_5_to_6_level_screen = False
        
        self.fire_attack = 0
        self.opening_menu = True
        
        # fonts and screen background color.
        
        self.font = pygame.font.SysFont('vinerhanditc',48)
        self.font_fps = pygame.font.SysFont('vinerhanditc',20)
        #self.text_color = (234,221,202)
        self.text_color =  (82, 54, 31)
        #self.bg_color = (74,4,4) # text background
        self.bg_color = (31, 59, 82)
        #self.screen_color = (79,121,66) # grass background
        #self.screen_color =(33, 82, 31) # this is a nice dark green. 
        self.screen_color = (47,129,54) # this should match sprites.
        #self.screen_background = (128,70,27)
        self.screen_background = (82, 54, 31)
        #fps_words = 'FPS: '
        # words for display 
        
        # below is in  game texts for display

        words1 = 'Game over!!'
        self.game_over = self.font.render(words1,True,self.text_color,self.bg_color)
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.game_over_rect.centery -= 100
        
        # temporary animation stuff
        
        self.animation_timer = 401
        self.animation_timer2 = 401
        self.animation_length = 400
        self.interval = 80
        
        # this is the in game map for display on the bottom of the screen so the player does not get lost.
        
        self.map_1 = False
        self.world1 = In_game_map(self)
        
        # this is for the campagne with map and enemies and bosses. 
        
        self.campagne_mode = False
        
        # overlay for information during gameplay

        self.overlay = Info_overlay(self)
        
        # button for return to main menu.
        self.return_campagne_screen_button = Button(self,'',1)
        self.return_campagne_screen_button.rect.center = self.screen_rect.center
        self.return_campagne_screen_button.rect.y += 200
        self.return_campagne_screen_button.prep_msg('Return to main menu')
        
        # this is where the game loop is, and order of calculations.
         
        while self.game:
            if self.loading_screen_active:
                self.loading_screen.draw_loading_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN: # i might get rid of this, it does not seem to be used currently.
                    mouse_pos = pygame.mouse.get_pos()
                    # this checks if you click to start game. 
                    #self.main_menu_stuff._check_campagne_button(self,mouse_pos)      
            self.clock.tick(self.target_framerate)
            self.level_system()
            if self.campagne_mode:
                """This means the player is walking around the game world."""
                self.screen.fill(self.level_stuff.level_design.current_background_color)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                # this is the map section.
                self.physics_system()
                self.drawing_system()
                self.background_sounds()
                self.check_for_first_cut_scene()
                self.level_stuff.ritual_loop(self)
                while self.pause_menu.pause_active:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.game = False 
                            self.pause_menu.pause_active = False  
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            self.pause_menu.check_to_save(self,mouse_pos)
                            self.pause_menu.check_to_unpause(mouse_pos)
                            self.pause_menu.check_hint_button(mouse_pos)        
                    self.pause_menu.draw_pause_screen()
                    pygame.display.flip()
            if self.game_over_screen:
                """This is where the player ends up after a game over"""
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False   
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        self._check_return_campagne_button(mouse_pos)
                self.screen.fill(self.screen_background)
                self.display_game_over_screen()
            if self.win_game_screen:
                """The player has won. celebrate him or her."""
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False   
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        self._check_return_campagne_button(mouse_pos)
                self.screen.fill(self.screen_background)
                self.level_stuff.display_win_game_screen(self) 
            
            pygame.display.flip() #update screen.

    #################### The game is above. 
    def physics_system(self):
        """Holds physics code for render order"""
        if self.level_stuff.player_1.death_animation_active == False:
            self.level_stuff.physics_active.movement_2(self)  
        self.level_stuff.physics_active.momentum_3(self)
        self.level_stuff.player_1.death_animation_logic(self)  
        self.level_stuff.physics_active.detect_collisions_bounce(self)
        if self.level_stuff.level_design.level_type == 'forest':
            self.level_stuff.physics_active.detect_collisions_bounce_trees(self)
        if self.level_stuff.level_design.level_type == 'lava':
            self.level_stuff.physics_active.update_lava(self)
        if self.level_stuff.boss_type == 'spider':
            self.level_stuff.physics_active.detect_collisions_bounce_boss(self)
        if self.level_stuff.boss_type == 'wolf':
            self.level_stuff.physics_active.detect_collisions_bounce_wolf(self)
        self.level_stuff.physics_active.enemy_loop(self)
        #self.level_stuff.physics_active.update_town(self)
        self.check_attack_in_game()

    def level_system(self):
        """This will hold the level stuff for update cycle"""
    
        # # the campagne begins here#!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if self.main_menu_stuff.start_stuff:
            self.main_menu_stuff.intro_screen_logic(self)
            pygame.display.flip()
        if self.main_menu_stuff.opening_menu:
            self.main_menu_stuff.draw_opening_menu(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # this checks if you click to start game. 
                    self.main_menu_stuff._check_campagne_button(self,mouse_pos) 
                    self.main_menu_stuff._check_credits_button(self,mouse_pos)
                    self.main_menu_stuff._check_load_button(self,mouse_pos)
                    self.main_menu_stuff._check_quit_game_button(self,mouse_pos)
                    self.main_menu_stuff._check_settings_button(self,mouse_pos)
                    self.main_menu_stuff._check_top_scores_button(self,mouse_pos)
            pygame.display.flip()
        if self.main_menu_stuff.top_scores_menu:
            self.main_menu_stuff.draw_top_scores_screen(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.main_menu_stuff._check_return_button(self,mouse_pos)
            pygame.display.flip()
        if self.main_menu_stuff.credits_screen:
            self.main_menu_stuff.draw_credits_screen(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.main_menu_stuff._check_return_button(self,mouse_pos)
                    #print('here we check for credit screen')
            pygame.display.flip()
        if self.main_menu_stuff.settings_menu:
            self.main_menu_stuff.draw_settings_screen(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.main_menu_stuff._check_return_button(self,mouse_pos)
                    self.settings_hold._check_button_background_minus_1(self,mouse_pos)
                    self.settings_hold._check_button_background_minus_10(self,mouse_pos)
                    self.settings_hold._check_button_background_plus_1(self,mouse_pos)
                    self.settings_hold._check_button_background_plus_10(self,mouse_pos)
                    self.settings_hold._check_button_dialogue_minus_1(self,mouse_pos)
                    self.settings_hold._check_button_dialogue_minus_10(self,mouse_pos)
                    self.settings_hold._check_button_dialogue_plus_1(self,mouse_pos)
                    self.settings_hold._check_button_dialogue_plus_10(self,mouse_pos)
                    self.settings_hold._check_button_volume_plus_1(self,mouse_pos)
                    self.settings_hold._check_button_volume_plus_10(self,mouse_pos)
                    self.settings_hold._check_button_volume_minus_1(self,mouse_pos)
                    self.settings_hold._check_button_volume_minus_10(self,mouse_pos)
            pygame.display.flip()
        if self.campagne_story_1:
            """This displays the story before the player enters the game world"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.level_stuff.story._check_continue_button(self,mouse_pos)
            self.screen.fill(self.screen_background)
            self.level_stuff.story.display_story_1()
        if self.switch_first_to_second_level_screen:
            """This is between 1 and 2"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.level_stuff.story._check_start_level_2_button(self,mouse_pos)
            self.screen.fill(self.screen_background)
            self.level_stuff.story.display_story_2()
        if self.switch_2_to_3_level_screen:
            """This is between 2 and 3"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.level_stuff.story._check_start_level_3_button(self,mouse_pos)
            self.screen.fill(self.screen_background)
            self.level_stuff.story.display_story_2()
        if self.switch_3_to_4_level_screen:
            """This is between 3 and 4"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.level_stuff.story._check_start_level_4_button(self,mouse_pos)
            self.screen.fill(self.screen_background)
            self.level_stuff.story.display_story_2()
        if self.switch_4_to_5_level_screen:
            """This is between 4 and 5"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.level_stuff.story._check_start_level_5_button(self,mouse_pos)
            self.screen.fill(self.screen_background)
            self.level_stuff.story.display_story_2()
        if self.switch_5_to_6_level_screen:
            """This is between 5 and 6"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.level_stuff.story._check_start_level_6_button(self,mouse_pos)
            self.screen.fill(self.screen_background)
            self.level_stuff.story.display_story_2()
        
        if self.cut_scene_1.cut_scene_test.cut_scene_active == True:
            """This will be the cut scene stuff."""
            self.cut_scene_1.perform_cut_scene_1(self)
            self.night.day_night_cycle(self)

    def drawing_system(self):
        """Holds stuff that gets drawn on screen."""
        if self.level_stuff.level_design.level_type == 'forest':
            self.level_stuff.grass_decorations.draw_grass(self)
            #self.world1.draw_grass() 
        if self.level_stuff.level_design.level_type == 'lava':
            self.level_stuff.level_design.draw_objects_for_lava_level(self)
        
        x = len(self.level_stuff.enemy_list)
        i = 0
        while i < x:
            """This draws all of the enemies in the list"""
            self.level_stuff.enemy_list[i].draw_me(self)
            x = len(self.level_stuff.enemy_list)
            i += 1
            #self.world1.draw_flowers()
        if self.level_stuff.boss_type == 'spider':
            self.level_stuff.level_1_boss.draw_me(rpg)
        if self.level_stuff.boss_type == 'wolf':
            self.level_stuff.level_1_boss.draw_wolves_for_boss(self)
        if self.level_stuff.boss_type == 'spider':
            self.level_stuff.level_1_boss.boss_check(self)
        if self.level_stuff.town_exists:
            self.level_stuff.town_1.draw_town()
        self.draw_items()
        if self.level_stuff.level_design.level_type == 'forest':
            self.level_stuff.generic_items.draw_items_generic(self)
        if self.level_stuff.player_1.death_animation_active == False:
            self.level_stuff.player_1.draw_me(self)
        if self.level_stuff.player_1.death_animation_active:
            self.level_stuff.player_1.draw_death_stuff()
        if self.level_stuff.level_design.level_type == 'forest':
            self.level_stuff.tree_set.draw_trees()  
        self.level_stuff.player_1.attack_cycle(self)
        
        self.level_stuff.particle_list_1[1].check_particle(self)
        self.level_stuff.cloud_stuff.cloud_loop(self)

        #self.shadow_test.draw_shadowy_overlay()
        self.night.day_night_cycle(self)
        fps_words = 'FPS: '
        fps_words += str(int(self.clock.get_fps()))
        self.fps_data = self.font_fps.render(fps_words,True,self.text_color,self.bg_color)
        self.fps_data_rect = self.fps_data.get_rect()
        self.fps_data_rect.topleft = self.screen_rect.topleft

        self.screen.blit(self.fps_data,self.fps_data_rect)
        self.overlay.update_overlay(self)
        self.overlay.draw_overlay(self)
        self.level_stuff.map.update_map(self)
        self.level_stuff.map.draw_map()
        #self.level_stuff.player_1.draw_death_stuff()

    def draw_items(self):
        """draws items on screen"""
        u = 0
        v = len(self.level_stuff.item_list) - 1
        while u <= v:
            self.level_stuff.item_list[u].draw_me(self)
            u += 1

    def check_for_first_cut_scene(self):
        """This checks to see if the first cut scene should become active.
        When it does, self.first_time_cut_scene will become true then 
        the scene will no longer trigger when its over."""
        if self.level_stuff.boss_type == 'spider':
            #print(self.level_stuff.boss_type)
            if self.level_stuff.level_1_boss.hypotenuse_boss_player_1 < 1000:
                """then scene becomes active"""
                if self.first_time_cut_scene == False:
                    self.first_time_cut_scene = True
                    self.cut_scene_1.cut_scene_test.cut_scene_active = True
                    self.campagne_mode = False
                    self.level_stuff.sound_logic.before_boss_1_dialogue.set_volume(self.settings_hold.dialogue_volume)
                    pygame.mixer.Sound.play(self.level_stuff.sound_logic.before_boss_1_dialogue)
                    pygame.mouse.set_visible(True)
        
    def display_game_over_screen(self):
        """This is game over"""
        game_over_words = 'Game Over!'
        self.game_over = self.font.render(game_over_words,True,self.text_color,self.bg_color)
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.screen.blit(self.game_over,self.game_over_rect)
        # buttons
        self.return_campagne_screen_button.draw_button()
 
    def _check_return_campagne_button(self,mouse_pos):
        """checks the return button to see if the player would like to play again after win/lose"""
        button_clicked = self.return_campagne_screen_button.msg_image_rect.collidepoint(mouse_pos) #
        #print('checking', button_clicked)
        if button_clicked and (self.win_game_screen):
            """This means the player won"""
            #print('button clicked')
            self.reset_campagne()
            self.main_menu_stuff.opening_menu = True
            self.game_over_screen = False
            self.win_game_screen = False
            pygame.mixer.music.stop()
        if button_clicked and (self.game_over_screen):
            """This means the player lost"""
            #print('button clicked')
            self.reset_campagne()
            self.main_menu_stuff.opening_menu = True
            self.game_over_screen = False
            self.win_game_screen = False
            pygame.mixer.music.stop()
               
    def background_sounds(self):
        """Makes noises and sounds in the background."""
        n = random.randint(0,1800)
        if n == 50:
            m = random.randint(1,100)
            m = m / 100
            if m <= self.settings_hold.background_volume * self.settings_hold.max_volume:
                self.level_stuff.sound_logic.spooky_sound.set_volume(m * self.settings_hold.max_volume)
            else:
                self.level_stuff.sound_logic.spooky_sound.set_volume(self.settings_hold.background_volume * self.settings_hold.max_volume)
            pygame.mixer.Sound.play(self.level_stuff.sound_logic.spooky_sound)
        
        n = random.randint(0,1400)
        if n == 50:
            m = random.randint(1,100)
            m = m / 100
            if m <= self.settings_hold.background_volume * self.settings_hold.max_volume:
                self.level_stuff.sound_logic.spooky_sound_2.set_volume(m * self.settings_hold.max_volume)
            else:
                self.level_stuff.sound_logic.spooky_sound_2.set_volume(self.settings_hold.background_volume * self.settings_hold.max_volume)
            pygame.mixer.Sound.play(self.level_stuff.sound_logic.spooky_sound_2)
       
        n = random.randint(0,1200)
        if n == 50:
            m = random.randint(1,100)
            m = m / 100
            #print(m, ' is for sound')
            if m <= self.settings_hold.background_volume * self.settings_hold.max_volume:
                self.level_stuff.sound_logic.owl_background_noise.set_volume(m * self.settings_hold.max_volume)
            else:
                self.level_stuff.sound_logic.owl_background_noise.set_volume(self.settings_hold.background_volume * self.settings_hold.max_volume)
            pygame.mixer.Sound.play(self.level_stuff.sound_logic.owl_background_noise)

        n = random.randint(0,1100)
        if n == 50:
            m = random.randint(50,100)
            m = m / 100
            #print(m, ' is for sound')
            if m <= self.settings_hold.background_volume * self.settings_hold.max_volume:
                self.level_stuff.sound_logic.wind_2_sound.set_volume(m * self.settings_hold.max_volume)
            else:
                self.level_stuff.sound_logic.wind_2_sound.set_volume(self.settings_hold.background_volume * self.settings_hold.max_volume)
            pygame.mixer.Sound.play(self.level_stuff.sound_logic.wind_2_sound)
        
        n = random.randint(100,1200)
        if n == 150:
            m = random.randint(50,100)
            m = m / 100
            #print(m, ' is for sound')
            if m <= self.settings_hold.background_volume * self.settings_hold.max_volume:
                self.level_stuff.sound_logic.wind_1_sound.set_volume(m * self.settings_hold.max_volume)
            else:
                self.level_stuff.sound_logic.wind_1_sound.set_volume(self.settings_hold.background_volume * self.settings_hold.max_volume)
            pygame.mixer.Sound.play(self.level_stuff.sound_logic.wind_1_sound)

        n = random.randint(100,12000)
        if n == 1500:
            m = random.randint(50,100)
            m = m / 100
            #print(m, ' is for sound')
            if m <= self.settings_hold.background_volume * self.settings_hold.max_volume:
                self.level_stuff.sound_logic.whistle_sound.set_volume(m * self.settings_hold.max_volume)
            else:
                self.level_stuff.sound_logic.whistle_sound.set_volume(self.settings_hold.background_volume * self.settings_hold.max_volume)
            pygame.mixer.Sound.play(self.level_stuff.sound_logic.whistle_sound)

    def check_attack_in_game(self):
        """When you press the space bar this will activate a particle to be drawn on screen and move with momentum to attack enemies with"""
        self.level_stuff.player_1.block_cycle()
        self.level_stuff.player_1.check_throw_timer()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_m]:
            if self.level_stuff.player_1.block_active == False and self.level_stuff.player_1.throw_timer_delay == self.level_stuff.player_1.throw_timer_delay_old:
                self.level_stuff.particle_list_1[1].spawn_particle(self)
                self.level_stuff.player_1.throw_timer_delay -= 1
        if keys[pygame.K_TAB]:
            self.pause_menu.pause_active = True
            pygame.mixer.pause()
            pygame.mouse.set_visible(True)
        if keys[pygame.K_COMMA]:
            """comma is the block."""
            if self.level_stuff.player_1.block_active == False: 
                self.level_stuff.player_1.block_active = True

    def reset_campagne(self):
        """This resets the stuff for the game to work when restarting"""
        # resets start here
        self.loading_screen_active = True
        self.loading_screen.draw_loading_screen()
        pygame.display.update()

        self.level_stuff.load_level_1(self)
        self.level_stuff.reset_player(self)
        self.level_stuff.current_level_tracker = 0
        self.game_over_screen = False
        self.win_game_screen = False 
        self.campagne_mode = False
        self.map_1 = False
        self.overlay_test = Info_overlay(self)
        self.loading_screen_active = False
    
   

  
#  game runs here
if __name__ == '__main__':
    rpg = RPG_game()
    rpg.run_game()