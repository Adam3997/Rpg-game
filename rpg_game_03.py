import pygame
from player import Player
from characters import Character
import images1
from button import Button
from map_logic import In_game_map
from enemy_logic import Overworld_person
#from polygon_parametric import Create_polygon
from fighting_logic import Fighting_logcic
from particles import Particle
from physics import Physics
from boss import Boss

class RPG_game:
    """This is an rpg game with a world to explore. working on the world now."""
   

    # this makes the game loop and run
    def run_game(self):
        """main loop for the game"""
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        
        self.clock = pygame.time.Clock()

        self.physics_active = Physics(self)
        

        self.game = True
        #self.screen = screen.rect
        self.deck_spot = 0
        self.start_menu = False
        self.turn = 0
        self.campagne_fight = False
        self.dt = 0
        self.movement_speed = 50
        self.default_speed = self.movement_speed
        self.accelleration = 20
        self.deccelleration = 5
        self.speed_limit = 400
        self.moving_up = 0
        self.moving_down = 0
        self.moving_left = 0
        self.moving_right  = 0 # this will be used for the momentum. ill redo this later with linear algrebra. 
        self.fire_attack = 0
        self.opening_menu = True

      
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (30,30,30)
        self.bg_color = (250,250,250)
        self.screen_rect = self.screen.get_rect()
        self.screen_color = (190,200,200)
        words1 = 'Game over!!'
        self.game_over = self.font.render(words1,True,self.text_color,'gray')
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.game_over_rect.centery -= 100
        self.animation_timer = 401
        self.animation_timer2 = 401
        self.animation_length = 400
        self.interval = 80
        
        self.map_1 = False
        self.world1 = In_game_map(self)
        self.world2 = In_game_map(self)
        self.world3 = In_game_map(self)
        self.world4 = In_game_map(self)
        
        self.player1 = Player(self)

        self.try1 = Overworld_person(self)

        self.starter_character = Character(self,10,10,10,10,20)
        self.enemy1 = Character(self,10,10,10,10,20)
        self.enemy1.rect.x += (self.screen_width / 4)*3
        self.enemy1.x = self.enemy1.rect.x
        self.starter_character.rect.x += self.screen_width / 10
        self.starter_character.x = self.starter_character.rect.x
        
        enemy_count = 0
        self.enemy_list = []
        self.eneny_characters = []
        enemy_total = 20
        while enemy_count <= enemy_total:
            """This creates the enemies on the map and gives them some stats."""
            n = Overworld_person(self)
            m = Character(self,10,10,10,10,50)
            self.enemy_list.append(n)
            self.eneny_characters.append(m)
            enemy_count += 1
        
        self.particle_list_1 = []
        n = 0
        particle_total = 2
        while n < particle_total:
            """This creates a list of particles that can be used."""
            f = Particle(self)
            self.particle_list_1.append(f)
            n += 1

        self.level_1_boss = Boss(self)
        self.fight_demo = Fighting_logcic(self,1,2)

        self.start_demo_button = Button(self,'Start Demo',1)
        self.start_demo_button.rect.center = self.screen_rect.center
        self.start_demo_button.prep_msg('Start Demo')

        self.campagne_mode = False

        self.start_campagne_button = Button(self,'',1)
        self.start_campagne_button.rect.center = self.screen_rect.center
        self.start_campagne_button.rect.y -= 200
        
        self.start_campagne_button.prep_msg('Start new single player game')

        

        self.fight_demo.update_infoboard(self)



# stopped here. must do combat engine next. while combat is true stuff goes in loop
        # this is where the game loop is 
        while self.game:
            for event in pygame.event.get():
                #print('here')
                if event.type == pygame.QUIT:
                    self.game = False
                    #print('here')
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_campagne_button(mouse_pos)
                    self._check_start_demo_button(mouse_pos)
            self.clock.tick(60)
            self.screen.fill(self.screen_color)
            if self.opening_menu:
                self.screen.fill(self.screen_color)
                self.start_demo_button.draw_button()
                self.start_campagne_button.draw_button()
            if self.start_menu:
                for event in pygame.event.get():
                    #print('here')
                    if event.type == pygame.QUIT:
                        self.game = False
                        #print('here')
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        #print('here')
                        mouse_pos = pygame.mouse.get_pos()
                        self.fight_demo._check_attack_1_button(self,mouse_pos)
                        self.fight_demo._check_attack_2_button(self,mouse_pos)
                        self.fight_demo._check_attack_3_button(self,mouse_pos)
                        self.fight_demo._check_attack_4_button(self,mouse_pos)
                self.screen.fill(self.screen_color)
                self.fight_demo.health_check(self)
                self.starter_character.draw_me(self)
                self.starter_character.update_deck(self)
                self.fight_demo.attack_1_button.draw_button()
                self.fight_demo.attack_2_button.draw_button()
                self.fight_demo.attack_3_button.draw_button()
                self.fight_demo.attack_4_button.draw_button()
                self.enemy1.draw_me(self)
                self.fight_demo.draw_infoboard(self)
                if self.animation_timer <= self.animation_length:
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
                    self.fire_attack -= 1
                #self.combat() # the campagnme behgins here#!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            if self.campagne_mode:
                """This means the player is walking around the game world."""
                self.screen.fill(self.screen_color)
                if not self.campagne_fight:
                    self.physics_active.movement(self)
                    self.check_attack_in_game()
                while self.campagne_fight:
                    """The game will stay in a fight loop until you finish fighting"""
                    self.screen.fill('white')
                    self.fight_demo.check_events_fight(self)
                    self.fight_demo.draw_fight_screen(self)
                    pygame.display.flip()
                for event in pygame.event.get():
                    #print('here')
                    
                    if event.type == pygame.QUIT:
                        self.game = False
                        #print('here')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #print('here')
                        mouse_pos = pygame.mouse.get_pos()
                     
                if self.map_1:
                    self.world1.draw_map()
                    self.try1.draw_me()
                    self.world1.draw_grass()
                    self.world2.draw_grass()
                    self.world3.draw_grass()
                    self.world4.draw_grass()
                    self.world1.draw_flowers()
                    self.level_1_boss.draw_me_2()
                    x = len(self.enemy_list)
                    i = 0
                    while i < x:
                        """"""
                        self.enemy_list[i].draw_me()
                        i += 1
                    #self.world1.draw_flowers()
                    self.player1.draw_me(self)
                    self.particle_list_1[1].check_particle(self)  
            pygame.display.flip()

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

    def create_overlay(self):
        """This is an overlay for battle screen. may not be used. """
        overlay_color = self.screen_color
        self.rect1 = pygame.Rect(0,0,150,600)
        self.rect1.midleft = self.screen_rect.midleft
        self.screen.fill(overlay_color,self.rect1)

        self.rect2 =pygame.Rect(0,0,500,150)
        self.rect2.topleft = self.screen_rect.topleft
        self.rect2.y += 50
        self.screen.fill(overlay_color,self.rect2)

        self.rect3 = pygame.Rect(0,0,150,600)
        self.rect3.midleft = self.screen_rect.midleft
        self.rect3.x += 350
        self.screen.fill(overlay_color,self.rect3)

        self.rect4 = pygame.Rect(0,0,500,60)
        self.rect4.bottomleft = self.screen_rect.bottomleft
        self.screen.fill(overlay_color,self.rect4)

    def create_overlay_2(self):
        """lverlay for player 2 in battle screen. may not be used. """
        overlay_color = self.screen_color
        self.rect1 = pygame.Rect(0,0,150,600)
        self.rect1.midright = self.screen_rect.midright
        self.rect1.x -= 350
        self.screen.fill(overlay_color,self.rect1)

        self.rect2 =pygame.Rect(0,0,500,150)
        self.rect2.topright = self.screen_rect.topright
        self.rect2.y += 50
        
        self.screen.fill(overlay_color,self.rect2)

        self.rect3 = pygame.Rect(0,0,150,600)
        self.rect3.midright = self.screen_rect.midright
        
        self.screen.fill(overlay_color,self.rect3)

        self.rect4 = pygame.Rect(0,0,500,300)
        self.rect4.bottomright = self.screen_rect.bottomright
        self.screen.fill(overlay_color,self.rect4)

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