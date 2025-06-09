from destiny_movements import Destiny_movements
from text_for_cut_scene import Text_for_cutscene
from player import Player
from boss import Boss
from particles import Particle
from button import Button
import pygame

class Cut_scene():
    """This will allow a cut scene type event to happen.
    This will take an initial condition, do the cut scene, then
    return to the initial condition. """

    def __init__(self,rpg,**kwargs):
        """Initialize"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.cut_scene_active = False
        self.cut_scene_part_1 = True # this is used to determine which part of the cut scene we are in.
        self.cut_scene_part_2 = False
        self.cut_scene_part_3 = False
        movements_temp = kwargs['movements']
        timing_temp = kwargs['timing']
        text_temp = kwargs['text'] 
        directions_temp = kwargs['directions']
        
        self.destiny = Destiny_movements(movements=movements_temp,timing=timing_temp,directions=directions_temp)

        self.text_destiny = Text_for_cutscene(text_temp)

        """game_over_words = 'Game Over!'
        self.game_over = self.font.render(game_over_words,True,self.text_color,'red')
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.screen.blit(self.game_over,self.game_over_rect)"""
        self.lines = text_temp[0].splitlines()

        self.font_cut_scene = pygame.font.SysFont('vinerhanditc',28)
        self.text_1 = self.font_cut_scene.render(self.lines[0],True,(128,70,27),(229,228,226))
        self.text_1_rect = self.text_1.get_rect()
        self.text_2 = self.font_cut_scene.render(self.lines[1],True,(128,70,27),(229,228,226))
        self.text_2_rect = self.text_2.get_rect()
        self.text_3 = self.font_cut_scene.render(self.lines[2],True,(128,70,27),(229,228,226))
        self.text_3_rect = self.text_3.get_rect()
        self.text_4 = self.font_cut_scene.render(self.lines[3],True,(128,70,27),(229,228,226))
        self.text_4_rect = self.text_4.get_rect()
        self.text_5 = self.font_cut_scene.render(self.lines[4],True,(128,70,27),(229,228,226))
        self.text_5_rect = self.text_5.get_rect()
        self.text_6 = self.font_cut_scene.render(self.lines[5],True,(128,70,27),(229,228,226))
        self.text_6_rect = self.text_6.get_rect()
        self.text_7 = self.font_cut_scene.render(self.lines[6],True,(128,70,27),(229,228,226))
        self.text_7_rect = self.text_7.get_rect()
        self.text_8 = self.font_cut_scene.render(self.lines[7],True,(128,70,27),(229,228,226))
        self.text_8_rect = self.text_8.get_rect()
        self.text_1_rect.center = self.screen_rect.center 
        self.text_1_rect.centery -= 300
        self.text_2_rect.topleft = self.text_1_rect.bottomleft
        self.text_3_rect.topleft = self.text_2_rect.bottomleft
        self.text_4_rect.topleft = self.text_3_rect.bottomleft
        self.text_5_rect.topleft = self.text_4_rect.bottomleft
        self.text_6_rect.topleft = self.text_5_rect.bottomleft
        self.text_7_rect.topleft = self.text_6_rect.bottomleft
        self.text_8_rect.topleft = self.text_7_rect.bottomleft

        


        self.next_button = Button(self,'Next',1)
        self.next_button.rect.midbottom = self.screen_rect.midbottom
        self.next_button.prep_msg('Next')

        self.end_scene_button = Button(self,'End Cut Scene',1)
        self.end_scene_button.rect.midbottom = self.screen_rect.midbottom
        self.end_scene_button.prep_msg('End cut scene')

        self.added_x = 0
        self.added_y = 0

        self.change_x = 0
        self.change_y = 0

        self.camera_change = False
        self.camera_change_delay = 5
        self.camera_change_delay_old = self.camera_change_delay


        self.cut_scene_player = Player(rpg)
        self.cut_scene_spot = 0

        self.cut_scene_boss = Boss(self,200,300,200,300,True,'none','regular')

        #self.particle_for_cut_scene = Particle(self)
        self.particle_cut_scene_list = []
        w = 0
        x = 5
        while w <= x:
            y = Particle(self,cut_scene=True,total=x)
            #y.particle_color = (255,100,w*5)
            self.particle_cut_scene_list.append(y)
            
            w += 1

        self.particle_needed = False
     
        
    def update_location(self,rpg,movement_id):
        """This updates the location of stuff"""
        if self.camera_change == False:
            #print(self.added_x, self.cut_scene_player.rect_2.x)
            if self.destiny.directions[movement_id] == 'right':
                self.cut_scene_player.cut_scene_animation_counter = 99 
            if self.destiny.directions[movement_id] == 'left':
                self.cut_scene_player.cut_scene_animation_counter = 81
            if self.destiny.directions[movement_id] == 'up':
                self.cut_scene_player.cut_scene_animation_counter = 72
            if self.destiny.directions[movement_id] == 'down':
                self.cut_scene_player.cut_scene_animation_counter = 90
            
            
            if self.cut_scene_spot >= len(self.destiny.destiny_movements_list) - 1:
                self.cut_scene_active = False
            self.cut_scene_player.rect_2.x += self.destiny.destiny_movements_list[movement_id][0] * rpg.dt
            self.cut_scene_player.rect_2.y += self.destiny.destiny_movements_list[movement_id][1] * rpg.dt
            self.added_x += self.destiny.destiny_movements_list[movement_id][0] * rpg.dt
            self.added_y += self.destiny.destiny_movements_list[movement_id][1] * rpg.dt
            if abs(self.added_x) >= abs(self.destiny.destiny_movements_list[movement_id][0] * self.destiny.destiny_timing_list[movement_id]):
                
                if self.cut_scene_part_1 == True:
                    self.cut_scene_part_1 = False
                    self.cut_scene_part_2 = True
                    self.cut_scene_spot += 1
                """if self.cut_scene_part_2 == True:
                    self.cut_scene_part_2 = False
                    self.cut_scene_part_3 = True
                    self.cut_scene_spot += 1"""
                
        

    def cycle_cut_scene(self,rpg):
        """This holds the cut scene loop"""
        if self.camera_change == False:
            self.cut_scene_1(rpg)
            """self.update_location(rpg,movement_id=self.cut_scene_spot)
            self.draw_cutscene()# this draws the player.
            self.draw_particles_for_cut_scene(rpg)"""

    def cut_scene_1(self,rpg):
        """This will be the loop for cut scene 1"""
        
        self.draw_cutscene()
        self.draw_particles_for_cut_scene(rpg)
        if self.cut_scene_active and self.cut_scene_part_1:
            """Then part 1 of the cut scene"""
            self.update_location(rpg,movement_id=self.cut_scene_spot)
            #self.draw_cutscene()
        if self.cut_scene_active and self.cut_scene_part_2:
            """Then part 1 of the cut scene"""
            #print(self.text_destiny.text_for_cut_scene[0][0])
            self.screen.blit(self.text_1,self.text_1_rect)
            self.screen.blit(self.text_2,self.text_2_rect)
            self.screen.blit(self.text_3,self.text_3_rect)
            self.screen.blit(self.text_4,self.text_4_rect)
            self.screen.blit(self.text_5,self.text_5_rect)
            self.screen.blit(self.text_6,self.text_6_rect)
            self.screen.blit(self.text_7,self.text_7_rect)
            self.screen.blit(self.text_8,self.text_8_rect)
            self.end_scene_button.draw_button()
            self._check_end_button(rpg)
            
        if self.cut_scene_part_1:
            self._check_next_button()
            self.next_button.draw_button()
       


    def draw_cutscene(self):
        """This draws the cut scene stuff"""

        self.cut_scene_player.draw_for_cut_scene()
        #self.next_button.draw_button()


    def draw_particles_for_cut_scene(self,rpg):
        """This draws particles for the cut scene"""
        if self.camera_change == False:
            w = 0
            x = len(self.particle_cut_scene_list) - 1
            while w <= x:
                self.particle_cut_scene_list[w].draw_particle_for_cut_scene(rpg)
                w += 1
            #self.particle_for_cut_scene.draw_particle_for_cut_scene(rpg)

    def _check_end_button(self,rpg):
        """This checks to see if the player clicks next"""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_clicked = self.end_scene_button.rect.collidepoint(mouse_pos) #
                if button_clicked and self.cut_scene_part_2:
                    """"""
                    self.cut_scene_part_2 = False
                    #self.cut_scene_part_2 = True
                    self.cut_scene_spot += 1
                    #print('button pressed')
                    self.cut_scene_active = False
                    rpg.campagne_mode = True
                    pygame.mixer.Sound.stop(rpg.level_stuff.sound_logic.before_boss_1_dialogue)
                    pygame.mouse.set_visible(False)


    def _check_next_button(self):
        """This checks to see if the player clicks next"""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_clicked = self.next_button.rect.collidepoint(mouse_pos) #
                if button_clicked and self.cut_scene_part_1:
                    """"""

                    self.cut_scene_part_1 = False
                    self.cut_scene_part_2 = True
                    self.cut_scene_spot += 1
                    #print('button pressed')
                """if button_clicked and self.cut_scene_part_2:
                    """"""
                    self.cut_scene_part_2 = False
                    self.cut_scene_part_3 = True
                if button_clicked and self.cut_scene_part_3:
                    """"""
                    self.cut_scene_part_3 = False"""
            #self.cut_scene_part_2 = True
    def change_camera_angle(self,x_change_total,y_change_total):
        """This will change the camera angle.
        This will be done by moving stuff"""
        if self.camera_change == False:
            self.change_x += x_change_total
            self.change_y += y_change_total

            # that is how much the camera moves. then everything moves by that amount.

            self.cut_scene_player.rect_2.x += x_change_total
            self.cut_scene_player.rect_2.y += y_change_total

            self.cut_scene_boss.rect.x += x_change_total
            self.cut_scene_boss.rect.y += y_change_total

            self.camera_change = True
        

    def check_camera_change_ends(self):
        """This checks if the camera change is over
        This is used for a transition."""

        if self.camera_change == True:
            self.screen.fill('black')
            self.camera_change_delay -= 1
            if self.camera_change_delay <= 0:
                self.camera_change_delay = self.camera_change_delay_old
                self.camera_change = False
        


    