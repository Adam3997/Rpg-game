import pygame
from player import Player
from characters import Character
#import images1
from button import Button
from map_logic import In_game_map
from enemy_logic import Overworld_person
#from polygon_parametric import Create_polygon
#from fighting_logic import Fighting_logcic
from particles import Particle
from physics import Physics
from boss import Boss
#from sprite_sheet_animater import Sprite_loader
from trees_builder import Tree_collection

class RPG_game:
    """This is an rpg game with a world to explore. working on the world now."""
   

    # this makes the game loop and run
    def run_game(self):
        """main loop for the game"""
        pygame.init()

        # set up the screen
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        # set up the ingame clock/framerate
        self.clock = pygame.time.Clock()
        # this is the physics class
        self.physics_active = Physics(self)

        self.target_framerate = 60
        self.tree_set = Tree_collection(self)

        
        # this is the game active boolian
        self.game = True
        # this is variables 
        self.deck_spot = 0
        self.start_menu = False
        self.turn = 0
        self.campagne_fight = False
        self.dt = 0
        
        
        
         # this will be used for the momentum. ill redo this later with linear algrebra. 
        self.fire_attack = 0
        self.opening_menu = True

        # fonts and screen background color.
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (30,30,30)
        self.bg_color = (250,250,250)
        self.screen_rect = self.screen.get_rect()
        self.screen_color = (190,200,200)

        fps_words = 'FPS: '
        # words for display 
        words1 = 'Game over!!'
        self.game_over = self.font.render(words1,True,self.text_color,'gray')
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.game_over_rect.centery -= 100
        # temporary animation stuff
        self.animation_timer = 401
        self.animation_timer2 = 401
        self.animation_length = 400
        self.interval = 80
        # stuff that will be displayed on the map like trees
        self.map_1 = False
        self.world1 = In_game_map(self)
        #self.world2 = In_game_map(self)
        #self.world3 = In_game_map(self)
        #self.world4 = In_game_map(self)
        # the player
        self.player_1 = Player(self)
        # the enemies on the map
        self.try1 = Overworld_person(self)
        # these are for the card-game style battle mode.
        self.starter_character = Character(self,10,10,10,10,20)
        #self.enemy1 = Character(self,10,10,10,10,20)
        #self.enemy1.rect.x += (self.screen_width / 4)*3
        #self.enemy1.x = self.enemy1.rect.x
        self.starter_character.rect.x += self.screen_width / 10
        self.starter_character.x = self.starter_character.rect.x
        # this builds up a list of enemies for the ingame world. This will be refactored later. 
        enemy_count = 0
        self.enemy_list = []
        #self.eneny_characters = []
        enemy_total = 20
        while enemy_count <= enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            n = Overworld_person(self)
            n.id_number = enemy_count
            #m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            #self.eneny_characters.append(m)
            enemy_count += 1
        # this builds up a list of particles. again will be refactored as needed. This should get its own class soon 
        self.particle_list_1 = []
        n = 0
        particle_total = 2
        while n < particle_total:
            """This creates a list of particles that can be used."""
            f = Particle(self)
            self.particle_list_1.append(f)
            n += 1
        # this is the boss for the level
        self.level_1_boss = Boss(self)
        # fight logic for the demo battle
        #self.fight_demo = Fighting_logcic(self,1,2)
        # this is for the demo
        self.start_demo_button = Button(self,'Start Demo',1)
        self.start_demo_button.rect.center = self.screen_rect.center
        self.start_demo_button.prep_msg('Start Demo')
        # this is for the campagne with map and enemies and bosses. 
        self.campagne_mode = False

        self.start_campagne_button = Button(self,'',1)
        self.start_campagne_button.rect.center = self.screen_rect.center
        self.start_campagne_button.rect.y -= 200
        
        self.start_campagne_button.prep_msg('Start new single player game')

        

        #self.fight_demo.update_infoboard(self)


        # this is the sprite sheet animater
        



# refactor below soon.
        # this is where the game loop is 
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # this checks if you click to start game, or demo. demo currently does not work. will remove later. 
                    self._check_campagne_button(mouse_pos)
                    #self._check_start_demo_button(mouse_pos)
            self.clock.tick(self.target_framerate)
            self.screen.fill(self.screen_color)
            if self.opening_menu:
                # this is the starting screen.
                self.screen.fill(self.screen_color)
                #self.start_demo_button.draw_button()
                self.start_campagne_button.draw_button()
            if self.start_menu:
                # this is the demo battle. was used for testing code early on.
                for event in pygame.event.get():
                    #print('here')
                    if event.type == pygame.QUIT:
                        self.game = False
                        #print('here')
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        #print('here')
                        mouse_pos = pygame.mouse.get_pos()
                        """self.fight_demo._check_attack_1_button(self,mouse_pos)
                        self.fight_demo._check_attack_2_button(self,mouse_pos)
                        self.fight_demo._check_attack_3_button(self,mouse_pos)
                        self.fight_demo._check_attack_4_button(self,mouse_pos)"""
                self.screen.fill(self.screen_color)
                #self.fight_demo.health_check(self)
                self.starter_character.draw_me(self)
                self.starter_character.update_deck(self)
                """self.fight_demo.attack_1_button.draw_button()
                self.fight_demo.attack_2_button.draw_button()
                self.fight_demo.attack_3_button.draw_button()
                self.fight_demo.attack_4_button.draw_button()"""
                #self.enemy1.draw_me(self)
                #self.fight_demo.draw_infoboard(self)
                """if self.animation_timer <= self.animation_length: # this will be given its own function to shrink it. 
                    self.starter_character.attack_animation()
                    self.animation_timer += 1
                    if self.animation_timer % self.interval == 0:
                        self.starter_character.animation_tracker += 1
                        if self.starter_character.animation_tracker >= 5:
                            self.starter_character.animation_tracker = 0
                if self.animation_timer2 <= self.animation_length:
                    self.enemy1.attack_animation_r()
                    self.animation_timer2 += 1
                    if self.animation_timer2 % self.interval == 0:
                        self.enemy1.animation_tracker_r += 1
                        if self.enemy1.animation_tracker_r >= 5:
                            self.enemy1.animation_tracker_r = 0
                if self.fire_attack > 0:
                    self.starter_character.animation_countdown -= 1
                    if self.starter_character.animation_countdown % 20 == 0:
                        self.starter_character.animation_spark_track += 1
                        if self.starter_character.animation_spark_track >= len(self.starter_character.fire_sprites):
                            self.starter_character.animation_spark_track = len(self.starter_character.fire_sprites) - 1
                    self.starter_character.draw_fire(self)
                    #print('here')
                    self.fire_attack -= 1"""
                #self.combat() 
                # 
                # # the campagne begins here#!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            if self.campagne_mode:
                """This means the player is walking around the game world."""
                self.screen.fill(self.screen_color)
                if not self.campagne_fight:
                    # this stops physics and attacks while you battle in the card-style battle mode. This is not fighting, and thus physics active.
                    self.physics_active.movement_2(self)
                    #self.check_attack_in_game()
                while self.campagne_fight:
                    """The game will stay in a fight loop until you finish fighting"""
                    # while fighting no physics or attacks.
                    self.screen.fill('white')
                    """self.fight_demo.check_events_fight(self)
                    self.fight_demo.draw_fight_screen(self)"""
                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                # this is the map section.
                if self.map_1:
                    self.world1.draw_map()
                    self.try1.draw_me()
                    self.world1.draw_grass()
                    #self.world2.draw_grass()
                    #self.world3.draw_grass()
                    #self.world4.draw_grass()
                    #self.world1.draw_flowers()
                    
                    self.physics_active.detect_collisions_bounce(self)
                    self.physics_active.detect_collisions_bounce_trees(self)
                    self.physics_active.enemy_loop(self)
                    
                    self.level_1_boss.draw_me()
                    self.level_1_boss.boss_check(self)

                    self.check_attack_in_game()

                    x = len(self.enemy_list)
                    i = 0
                    while i < x:
                        """This draws all of the enemies in the list"""
                        self.enemy_list[i].draw_me()
                        i += 1
                    #self.world1.draw_flowers()
                    self.player_1.draw_me(self)
                    self.player_1.check_particle_hit(self)
                    
                    self.player_1.attack_cycle(self)
                    self.tree_set.draw_trees()
                    self.particle_list_1[1].check_particle(self)
                    #print(self.clock.get_fps())
                    fps_words = 'FPS: '
                    fps_words += str(int(self.clock.get_fps()))
                    self.fps_data = self.font.render(fps_words,True,self.text_color,'gray')
                    self.fps_data_rect = self.fps_data.get_rect()
                    self.fps_data_rect.topleft = self.screen_rect.topleft
                    self.screen.blit(self.fps_data,self.fps_data_rect)
                    


            pygame.display.flip() #update screen.

    def check_attack_in_game(self):
        """When you press the space bar this will activate a particle to be drawn on screen and move with momentum to attack enemies with"""
        keys = pygame.key.get_pressed()
        '''
        for event in pygame.event.get():
             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    self.game = False
                if event.key == pygame.K_SPACE:
                    self.particle_list_1[1].spawn_particle(self)
        '''
        if keys[pygame.K_q]:
            self.game = False
        if keys[pygame.K_SPACE]:
            """"""
            self.particle_list_1[1].spawn_particle(self)
            
        
    def _check_campagne_button(self,mouse_pos):
        """This checks if you want to start a campagne demo"""
        button_clicked = self.start_campagne_button.rect.collidepoint(mouse_pos)
       
        if button_clicked and self.opening_menu == True:
            """"""
            self.campagne_mode = True
            self.opening_menu = False
            self.map_1 = True 

   

    def _check_start_demo_button(self,mouse_pos):
        """This starts the battle demo"""
        button_clicked = self.start_demo_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.opening_menu:
            """"""
            self.start_menu = True
            self.opening_menu = False

   
    # function level
    def combat(self):
        """Allows the combat to end when enemy health reaches 0 or less. """ 
        if self.enemy1.health <=0:
            """"""
            game = False
            #print('game over enemy reaches 0 health')

            


#  game runs here

if __name__ == '__main__':
    rpg = RPG_game()
    rpg.run_game()